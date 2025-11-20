# Chatbot Deployment Example

End-to-end example of deploying and using a chatbot with vLLM.

## What You'll Learn

- Deploy LLM with vLLM for inference
- Implement streaming chat completions
- Track conversations with MLflow
- Monitor performance metrics

## Prerequisites

```bash
# Start the LLMOps stack
cd ../../
docker-compose up -d vllm mlflow

# Wait for services to be ready (~2 minutes for model loading)
docker-compose logs -f vllm
```

## Install Dependencies

```bash
pip install requests mlflow
```

## Run the Example

```bash
python app.py
```

## Example Interaction

```
🤖 LLMOps Chatbot Demo
==================================================
Model: meta-llama/Llama-2-7b-chat-hf
Endpoint: http://localhost:8000/v1
Type 'quit' to exit

You: What is the capital of France?
Assistant: The capital of France is Paris.

You: Tell me an interesting fact about it
Assistant: Paris is known as the "City of Light" (La Ville Lumière) 
because it was one of the first European cities to use gas street 
lighting extensively in the 19th century...
```

## View Metrics

1. **MLflow UI**: http://localhost:5000
   - View all chat interactions
   - Compare response times
   - Track prompt/response lengths

2. **Prometheus Metrics**: http://localhost:9090
   - Query: `vllm_request_duration_seconds`
   - Query: `vllm_queue_size`

3. **Grafana Dashboard**: http://localhost:3000
   - Username: admin / Password: admin
   - Pre-configured LLM metrics dashboard

## Advanced Usage

### Batch Processing

```python
questions = [
    "What is machine learning?",
    "Explain neural networks",
    "What is deep learning?"
]

for q in questions:
    response = list(chat_completion(q, stream=False))[0]
    print(f"Q: {q}\nA: {response}\n")
```

### Custom System Prompt

```python
# Modify the system message in app.py
"system": "You are a Python expert. Provide concise code examples."
```

## Troubleshooting

**vLLM not responding:**
```bash
# Check if model is loaded
docker-compose logs vllm | grep "Uvicorn running"
```

**Out of memory:**
```bash
# Use smaller model (edit .env)
VLLM_MODEL=meta-llama/Llama-2-7b-chat-hf  # instead of 13b
```

## Next Steps

- Try [rag-pipeline](../rag-pipeline/) example
- Implement [ab-testing](../ab-testing/) for model comparison
- Set up [monitoring-alerts](../monitoring-alerts/)
