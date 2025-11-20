# IoTOps - IoT Operations

IoT device management, data collection, and edge computing platform.

## 🎯 Overview

- Device management (ThingsBoard, Eclipse Ditto)
- MQTT broker (Mosquitto, EMQX)
- Time-series database (InfluxDB, TimescaleDB)
- Edge computing (EdgeX Foundry)
- Protocol gateways (Modbus, OPC-UA)
- IoT data analytics

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| ThingsBoard | 8080 | IoT platform |
| EMQX | 1883 | MQTT broker |
| InfluxDB | 8086 | Time-series DB |
| Grafana | 3000 | Visualization |
| Node-RED | 1880 | Flow programming |
| EdgeX | 59880 | Edge framework |

## 🚀 Quick Start

```bash
cd IoTOps
cp .env.example .env
./scripts/start.sh
```
