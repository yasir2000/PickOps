# MLOps - Machine Learning Operations

Production ML pipeline with training, deployment, and monitoring.

## 🎯 Overview

- Model training (Kubeflow, MLflow)
- Model serving (TensorFlow Serving, Seldon)
- Feature store (Feast)
- Experiment tracking
- Model monitoring
- Data versioning (DVC)

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| MLflow | 5000 | Experiment tracking |
| Jupyter | 8888 | Notebooks |
| TF Serving | 8501 | Model serving |
| Feast | 6566 | Feature store |
| MinIO | 9001 | Object storage |
| PostgreSQL | 5432 | Metadata store |

## 🚀 Quick Start

```bash
cd MLOps
cp .env.example .env
./scripts/start.sh
```

## Access Points

- MLflow: http://localhost:5000
- Jupyter: http://localhost:8888 (token in logs)
- TF Serving: http://localhost:8501
- MinIO: http://localhost:9001 (minioadmin/minioadmin)
