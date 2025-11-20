"""
End-to-End Chatbot Deployment Example
Demonstrates: vLLM inference, prompt engineering, streaming responses
"""

import os
import requests
from typing import Generator

# vLLM endpoint (from docker-compose)
VLLM_URL = os.getenv("VLLM_URL", "http://localhost:8000/v1")
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"

def chat_completion(message: str, stream: bool = True) -> Generator[str, None, None]:
    """
    Send a chat message to vLLM and get response

    Args:
        message: User message
        stream: Whether to stream the response

    Yields:
        Response chunks if streaming, else full response
    """
    url = f"{VLLM_URL}/chat/completions"

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": message}
        ],
        "temperature": 0.7,
        "max_tokens": 500,
        "stream": stream
    }

    response = requests.post(url, json=payload, stream=stream)

    if stream:
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith('data: '):
                    data = line_str[6:]
                    if data != '[DONE]':
                        import json
                        chunk = json.loads(data)
                        if 'choices' in chunk:
                            delta = chunk['choices'][0].get('delta', {})
                            if 'content' in delta:
                                yield delta['content']
    else:
        result = response.json()
        yield result['choices'][0]['message']['content']


def log_to_mlflow(prompt: str, response: str, model: str):
    """Log interaction to MLflow for tracking"""
    import mlflow

    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("chatbot-interactions")

    with mlflow.start_run():
        mlflow.log_param("model", model)
        mlflow.log_param("prompt_length", len(prompt))
        mlflow.log_param("response_length", len(response))
        mlflow.log_text(prompt, "prompt.txt")
        mlflow.log_text(response, "response.txt")


def main():
    """Interactive chatbot demo"""
    print("🤖 LLMOps Chatbot Demo")
    print("=" * 50)
    print(f"Model: {MODEL_NAME}")
    print(f"Endpoint: {VLLM_URL}")
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye! 👋")
            break

        if not user_input:
            continue

        print("Assistant: ", end='', flush=True)
        full_response = ""

        for chunk in chat_completion(user_input, stream=True):
            print(chunk, end='', flush=True)
            full_response += chunk

        print("\n")

        # Log to MLflow
        try:
            log_to_mlflow(user_input, full_response, MODEL_NAME)
        except Exception as e:
            print(f"Note: MLflow logging failed: {e}")


if __name__ == "__main__":
    # Install dependencies: pip install requests mlflow
    main()
