"""
Stable Diffusion Image Generation API
Demonstrates: Text-to-image, img2img, inpainting, model management
"""

import requests
import base64
import json
from pathlib import Path
from typing import Optional, Dict, List
import time

# Stable Diffusion WebUI endpoint
SD_URL = "http://localhost:7860"

class StableDiffusionAPI:
    def __init__(self, base_url: str = SD_URL):
        self.base_url = base_url

    def text_to_image(
        self,
        prompt: str,
        negative_prompt: str = "",
        steps: int = 30,
        cfg_scale: float = 7.5,
        width: int = 512,
        height: int = 512,
        seed: int = -1,
        sampler: str = "Euler a"
    ) -> Dict:
        """Generate image from text prompt"""

        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "steps": steps,
            "cfg_scale": cfg_scale,
            "width": width,
            "height": height,
            "seed": seed,
            "sampler_name": sampler,
        }

        response = requests.post(
            f"{self.base_url}/sdapi/v1/txt2img",
            json=payload
        )

        return response.json()

    def img_to_img(
        self,
        init_image_path: str,
        prompt: str,
        denoising_strength: float = 0.75,
        **kwargs
    ) -> Dict:
        """Transform existing image based on prompt"""

        # Read and encode image
        with open(init_image_path, 'rb') as f:
            init_image = base64.b64encode(f.read()).decode()

        payload = {
            "init_images": [init_image],
            "prompt": prompt,
            "denoising_strength": denoising_strength,
            **kwargs
        }

        response = requests.post(
            f"{self.base_url}/sdapi/v1/img2img",
            json=payload
        )

        return response.json()

    def get_models(self) -> List[str]:
        """List available models"""
        response = requests.get(f"{self.base_url}/sdapi/v1/sd-models")
        return [model['model_name'] for model in response.json()]

    def switch_model(self, model_name: str):
        """Switch to different model"""
        payload = {"sd_model_checkpoint": model_name}
        requests.post(f"{self.base_url}/sdapi/v1/options", json=payload)

    def save_image(self, image_data: str, output_path: str):
        """Save base64 image to file"""
        image_bytes = base64.b64decode(image_data)
        Path(output_path).write_bytes(image_bytes)

def generate_variations(api: StableDiffusionAPI, base_prompt: str):
    """Generate multiple variations of same prompt"""

    print("🎨 Generating variations...")

    variations = [
        ("photorealistic", "cartoon, anime, painting"),
        ("oil painting", "photo, realistic"),
        ("anime style", "realistic, photo"),
        ("digital art", "traditional art"),
    ]

    results = []

    for idx, (style, negative) in enumerate(variations):
        full_prompt = f"{base_prompt}, {style}"

        print(f"\n  Variation {idx + 1}: {style}")

        result = api.text_to_image(
            prompt=full_prompt,
            negative_prompt=negative,
            steps=30,
            cfg_scale=7.5,
            seed=42  # Same seed for consistency
        )

        # Save image
        output_path = f"output/variation_{idx + 1}_{style.replace(' ', '_')}.png"
        Path("output").mkdir(exist_ok=True)
        api.save_image(result['images'][0], output_path)

        print(f"    Saved: {output_path}")
        results.append(output_path)

    return results

def batch_generation(api: StableDiffusionAPI, prompts: List[str]):
    """Generate images for multiple prompts"""

    print(f"\n🔄 Batch generation ({len(prompts)} prompts)...")

    results = []

    for idx, prompt in enumerate(prompts):
        print(f"\n  [{idx + 1}/{len(prompts)}] {prompt[:50]}...")

        start_time = time.time()

        result = api.text_to_image(
            prompt=prompt,
            steps=20,  # Fewer steps for batch
            width=512,
            height=512
        )

        duration = time.time() - start_time

        output_path = f"output/batch_{idx + 1}.png"
        api.save_image(result['images'][0], output_path)

        print(f"    Generated in {duration:.2f}s")
        results.append(output_path)

    return results

def main():
    """Demo various generation techniques"""

    print("🚀 Stable Diffusion API Demo")
    print("=" * 60)

    api = StableDiffusionAPI()

    # Check available models
    print("\n📦 Available models:")
    models = api.get_models()
    for model in models[:5]:  # Show first 5
        print(f"  - {model}")

    # Example 1: Simple text-to-image
    print("\n" + "=" * 60)
    print("Example 1: Basic Text-to-Image")
    print("=" * 60)

    prompt = "a serene mountain landscape at sunset, highly detailed, 4k"
    negative = "blurry, low quality, watermark"

    print(f"\nPrompt: {prompt}")
    print("Generating...")

    result = api.text_to_image(
        prompt=prompt,
        negative_prompt=negative,
        steps=30,
        cfg_scale=7.5,
        width=768,
        height=512
    )

    Path("output").mkdir(exist_ok=True)
    api.save_image(result['images'][0], "output/landscape.png")
    print("✅ Saved: output/landscape.png")

    # Example 2: Style variations
    print("\n" + "=" * 60)
    print("Example 2: Style Variations")
    print("=" * 60)

    base_prompt = "a cat sitting on a windowsill"
    variations = generate_variations(api, base_prompt)
    print(f"\n✅ Generated {len(variations)} variations")

    # Example 3: Batch generation
    print("\n" + "=" * 60)
    print("Example 3: Batch Generation")
    print("=" * 60)

    batch_prompts = [
        "futuristic cityscape with flying cars",
        "medieval castle on a hilltop",
        "tropical beach with palm trees",
        "cozy library with fireplace",
    ]

    batch_results = batch_generation(api, batch_prompts)
    print(f"\n✅ Generated {len(batch_results)} images")

    # Example 4: High-resolution generation
    print("\n" + "=" * 60)
    print("Example 4: High-Resolution")
    print("=" * 60)

    print("\nGenerating 1024x1024 image...")

    hires_result = api.text_to_image(
        prompt="epic fantasy dragon, intricate scales, dramatic lighting",
        negative_prompt="blurry, low quality",
        steps=40,
        cfg_scale=8.0,
        width=1024,
        height=1024
    )

    api.save_image(hires_result['images'][0], "output/dragon_hires.png")
    print("✅ Saved: output/dragon_hires.png")

    print("\n" + "=" * 60)
    print("✨ All examples complete!")
    print("Check the 'output/' directory for generated images")
    print("=" * 60)

if __name__ == "__main__":
    # Install: pip install requests
    main()
