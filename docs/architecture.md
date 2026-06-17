# Architecture

## System Overview

The framework combines Deep Double Q-Networks (DDQN) with A* path planning for autonomous vehicle navigation in CARLA.

### Pipeline

CARLA Simulator
→ Sensors (Camera, Collision, Lane Detection)
→ State Encoder
→ DDQN Agent
→ Arbitration Layer
→ A* Planner (Fallback)
→ Vehicle Control
→ Reward Engine
→ Replay Buffer
→ DDQN Training

## Core Modules

### environment.py
CARLA environment wrapper.

### ddqn_agent.py
Implements DDQN learning and target network updates.

### astar.py
Global path planning using A* search.

### arbitrator.py
Selects between DDQN actions and A* actions based on confidence.

### reward.py
Computes rewards for navigation performance.

### benchmark.py
Evaluates navigation metrics and exports results.

## Training Flow

1. Collect state from CARLA.
2. Select action using DDQN.
3. Check confidence score.
4. Use DDQN action or A* fallback.
5. Execute action.
6. Store experience.
7. Train DDQN.
