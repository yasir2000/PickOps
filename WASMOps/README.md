# WASMOps - WebAssembly Operations

WebAssembly runtime management, compilation, and edge computing.

## 🎯 Overview

- WASM runtimes (Wasmtime, Wasmer, WasmEdge)
- WASM compilation (Emscripten, wasm-pack)
- Edge computing with WASM
- Serverless WASM functions
- WASM-based microservices
- Performance profiling

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Wasmtime | 8080 | WASM runtime |
| WasmEdge | 8081 | Edge WASM runtime |
| Wasmer | 8082 | Universal WASM runtime |
| Spin | 3000 | Serverless WASM |
| Krustlet | 3001 | K8s WASM runtime |
| WAPM Registry | 8000 | Package registry |

## 🚀 Quick Start

```bash
cd WASMOps
cp .env.example .env
./scripts/start.sh
```
