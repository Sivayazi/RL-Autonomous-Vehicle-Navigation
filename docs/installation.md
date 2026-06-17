# Installation

## Requirements

- Python 3.8 or newer
- CARLA 0.9.13
- NVIDIA GPU (recommended)

## Clone Repository

```bash
git clone https://github.com/<username>/RL-Autonomous-Vehicle-Navigation.git
cd RL-Autonomous-Vehicle-Navigation
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## CARLA Setup

1. Download CARLA 0.9.13.
2. Extract CARLA.
3. Start simulator:

```bash
CarlaUE4.exe
```

or on Linux:

```bash
./CarlaUE4.sh
```

## Verify Installation

```bash
python scripts/train_ddqn.py
```
