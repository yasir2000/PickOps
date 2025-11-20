# GenAIOps - Generative AI Operations

Production GenAI deployment and management platform.

## 🎯 Overview

- Multi-modal model serving (Text, Image, Audio)
- Stable Diffusion, DALL-E integration
- Text-to-Speech/Speech-to-Text
- Model management and versioning
- API gateway and load balancing
- Usage tracking and billing

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Stable Diffusion | 7860 | Image generation |
| Whisper | 8001 | Speech-to-text |
| Coqui TTS | 5002 | Text-to-speech |
| ComfyUI | 8188 | Image workflow |
| LiteLLM | 4000 | Multi-LLM proxy |

## 🚀 Quick Start

```bash
cd GenAIOps
cp .env.example .env
./scripts/start.sh
```
