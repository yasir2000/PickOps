"""
Complete ML Training Pipeline
Demonstrates: Model training, experiment tracking, model registry, serving
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow
import mlflow.sklearn
import joblib
import requests

# MLflow setup
MLFLOW_TRACKING_URI = "http://localhost:5000"
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment("iris-classification")

def load_data():
    """Load and prepare iris dataset"""
    from sklearn.datasets import load_iris

    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name='target')

    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train, params):
    """Train Random Forest model"""
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model and return metrics"""
    y_pred = model.predict(X_test)

    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1': f1_score(y_test, y_pred, average='weighted')
    }

    return metrics, y_pred

def register_model(model_name, run_id):
    """Register model in MLflow Model Registry"""
    model_uri = f"runs:/{run_id}/model"

    # Register model
    model_details = mlflow.register_model(model_uri, model_name)

    # Transition to staging
    client = mlflow.tracking.MlflowClient()
    client.transition_model_version_stage(
        name=model_name,
        version=model_details.version,
        stage="Staging"
    )

    return model_details

def deploy_to_serving(model_name, version):
    """Deploy model to TensorFlow Serving"""
    # Download model from MLflow
    client = mlflow.tracking.MlflowClient()
    model_uri = f"models:/{model_name}/{version}"

    # Export for serving (simplified)
    print(f"Model ready for serving: {model_uri}")
    print(f"Access via: http://localhost:8501/v1/models/{model_name}")

def main():
    """Complete training pipeline"""
    print("🚀 MLOps Training Pipeline")
    print("=" * 60)

    # Load data
    print("📊 Loading data...")
    X_train, X_test, y_train, y_test = load_data()
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")

    # Hyperparameter tuning
    param_grid = [
        {'n_estimators': 50, 'max_depth': 5, 'random_state': 42},
        {'n_estimators': 100, 'max_depth': 10, 'random_state': 42},
        {'n_estimators': 200, 'max_depth': 15, 'random_state': 42},
    ]

    best_run_id = None
    best_f1 = 0

    for idx, params in enumerate(param_grid):
        print(f"\n🔬 Experiment {idx + 1}/{len(param_grid)}")
        print(f"Parameters: {params}")

        with mlflow.start_run(run_name=f"rf_experiment_{idx + 1}") as run:
            # Log parameters
            mlflow.log_params(params)

            # Train model
            print("  Training...")
            model = train_model(X_train, y_train, params)

            # Evaluate
            print("  Evaluating...")
            metrics, y_pred = evaluate_model(model, X_test, y_test)

            # Log metrics
            mlflow.log_metrics(metrics)

            # Log model
            mlflow.sklearn.log_model(model, "model")

            # Log feature importance
            feature_importance = pd.DataFrame({
                'feature': X_train.columns,
                'importance': model.feature_importances_
            }).sort_values('importance', ascending=False)

            mlflow.log_text(
                feature_importance.to_string(),
                "feature_importance.txt"
            )

            print(f"  Metrics: {metrics}")

            # Track best model
            if metrics['f1'] > best_f1:
                best_f1 = metrics['f1']
                best_run_id = run.info.run_id

    print(f"\n✅ Best model F1: {best_f1:.4f}")
    print(f"Run ID: {best_run_id}")

    # Register best model
    print("\n📦 Registering model...")
    model_name = "iris-classifier"
    model_details = register_model(model_name, best_run_id)

    print(f"Model registered: {model_name} v{model_details.version}")

    # Deploy
    print("\n🚀 Deploying to serving...")
    deploy_to_serving(model_name, model_details.version)

    print("\n" + "=" * 60)
    print("✨ Pipeline complete!")
    print(f"View in MLflow UI: {MLFLOW_TRACKING_URI}")
    print("=" * 60)

if __name__ == "__main__":
    # Install: pip install mlflow scikit-learn pandas numpy
    main()
