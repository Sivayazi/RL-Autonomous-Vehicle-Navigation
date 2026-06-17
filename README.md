# RL Autonomous Vehicle Navigation

## Overview

This repository contains a Reinforcement Learning framework for autonomous vehicle navigation and dynamic obstacle avoidance using the CARLA simulator.

### Features

- CARLA Simulator Integration
- Deep Double Q-Network (DDQN) framework
- A* Path Planning module
- Hybrid DDQN + A* decision architecture
- CNN-based feature extraction
- Dynamic obstacle avoidance
- Benchmarking and evaluation utilities
- TensorBoard-ready training workflow

## Project Structure

```text
RL-Autonomous-Vehicle-Navigation/
├── README.md
├── requirements.txt
├── LICENSE
├── src/
├── scripts/
├── configs/
├── docs/
├── models/
├── notebooks/
└── results/
```

## Requirements

- Python 3.8+
- CARLA 0.9.13
- PyTorch
- TensorFlow
- Stable-Baselines3

Install dependencies:

```bash
pip install -r requirements.txt
```

## Training

Start CARLA and run:

```bash
python scripts/train_ddqn.py
```

## Evaluation

```bash
python scripts/evaluate.py
```

## Benchmarking

```bash
python scripts/run_benchmark.py
```

## Research Areas

- Reinforcement Learning
- Autonomous Driving
- Path Planning
- Obstacle Avoidance
- Deep Learning
- Robotics

## License

MIT License
