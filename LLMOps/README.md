# LLMOps - Large Language Model Operations

Production-grade stack for training, serving, and monitoring Large Language Models.

## 🎯 Overview

This stack provides a complete LLMOps platform with:
- Model training and fine-tuning (Axolotl, DeepSpeed)
- Model serving and inference (vLLM, Text Generation Inference)
- Vector database for embeddings (Qdrant)
- Experiment tracking (MLflow)
- Model registry and versioning
- Monitoring and observability (Prometheus, Grafana)

## 🏗️ Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Nginx     │────▶│     vLLM     │────▶│   Qdrant    │
│  (Gateway)  │     │  (Inference) │     │  (Vectors)  │
└─────────────┘     └──────────────┘     └─────────────┘
       │                    │                     │
       │            ┌───────────────┐             │
       └───────────▶│    MLflow     │◀────────────┘
                    │  (Tracking)   │
                    └───────────────┘
                            │
                    ┌───────────────┐
                    │  Prometheus   │
                    │   Grafana     │
                    └───────────────┘
```

## 📦 Components

| Service | Version | Port | Description |
|---------|---------|------|-------------|
| vLLM | latest | 8000 | High-throughput LLM inference |
| Text-Generation-Inference | 2.0 | 8001 | HuggingFace model serving |
| Ollama | latest | 11434 | Local LLM runtime |
| MLflow | 2.10 | 5000 | Experiment tracking |
| Qdrant | latest | 6333 | Vector database |
| Prometheus | latest | 9090 | Metrics collection |
| Grafana | latest | 3000 | Visualization |
| Nginx | latest | 80 | API Gateway |

## 🚀 Quick Start

1. **Clone and configure:**
   ```bash
   cd LLMOps
   cp .env.example .env
   # Edit .env with your settings
   ```

2. **Start the stack:**
   ```bash
   ./scripts/start.sh
   ```

3. **Verify services:**
   ```bash
   ./scripts/health-check.sh
   ```

## ⚙️ Configuration

### Environment Variables

```bash
# Model Configuration
MODEL_NAME=meta-llama/Llama-2-7b-chat-hf
MODEL_REVISION=main
HUGGINGFACE_TOKEN=your_token_here

# Resource Limits
GPU_DEVICES=0,1
MAX_MODEL_LEN=4096
TENSOR_PARALLEL_SIZE=2

# MLflow
MLFLOW_TRACKING_URI=http://mlflow:5000
MLFLOW_BACKEND_STORE_URI=sqlite:///mlflow.db
MLFLOW_ARTIFACT_ROOT=/mlflow/artifacts

# Qdrant
QDRANT_API_KEY=your_qdrant_key
QDRANT_COLLECTION=embeddings
```

## 📊 Usage Examples

### Inference with vLLM

```bash
curl http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-2-7b-chat-hf",
    "prompt": "Explain quantum computing",
    "max_tokens": 100
  }'
```

### Using Ollama

```bash
# Pull a model
docker exec -it llmops-ollama ollama pull llama2

# Run inference
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Why is the sky blue?"
}'
```

### Track Experiments with MLflow

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("llm-fine-tuning")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 2e-5)
    mlflow.log_metric("loss", 0.45)
```

### Vector Search with Qdrant

```python
from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")
results = client.search(
    collection_name="embeddings",
    query_vector=[0.1, 0.2, ...],
    limit=5
)
```

## 🔧 Operations

### Fine-tune a Model

```bash
./scripts/finetune.sh \
  --model meta-llama/Llama-2-7b-hf \
  --dataset timdettmers/openassistant-guanaco \
  --output ./models/llama2-finetuned
```

### Deploy a New Model

```bash
./scripts/deploy-model.sh meta-llama/Llama-2-13b-chat-hf
```

### Backup Models and Data

```bash
./scripts/backup.sh
```

## 📈 Monitoring

Access monitoring dashboards:

- **Grafana:** http://localhost:3000 (admin/admin)
- **Prometheus:** http://localhost:9090
- **MLflow:** http://localhost:5000

### Key Metrics

- Request latency (p50, p95, p99)
- Tokens per second
- GPU utilization
- Model memory usage
- Queue depth

## 🐛 Troubleshooting

### GPU Not Detected

```bash
# Check GPU availability
docker run --rm --gpus all nvidia/cuda:12.1.0-base-ubuntu22.04 nvidia-smi
```

### Out of Memory

Reduce batch size or model size:
```bash
# Edit .env
MAX_MODEL_LEN=2048
TENSOR_PARALLEL_SIZE=1
```

### Slow Inference

Enable quantization:
```bash
QUANTIZATION=awq  # or gptq, bitsandbytes
```

## 📚 Documentation

- [vLLM Documentation](https://docs.vllm.ai/)
- [MLflow Guide](https://mlflow.org/docs/latest/index.html)
- [Qdrant Docs](https://qdrant.tech/documentation/)
- [Configuration Guide](./docs/configuration.md)
- [Architecture Details](./docs/architecture.md)

## 🔐 Security

- Set strong API keys in `.env`
- Enable authentication for all services
- Use TLS in production
- Rotate credentials regularly

## 📝 License

See main [LICENSE](../LICENSE)
