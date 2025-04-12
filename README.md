```markdown
# neuron7x-core

**BioQuantumEngine** – A neuro-inspired cognitive engine integrating harmonic memory encoding, neurotransmitter modulation, and personality-influenced decision logic. Part of the modular architecture behind **Neuron7X: Cognitive Engine**.

## Overview

`neuron7x-core` provides a biologically plausible decision-making system using quantum-inspired vector encoding, neurochemical state tracking, and harmonic evaluation. This repository is the foundation for simulating adaptive cognitive behavior under complex states including psychedelic influence, risk evaluation, and personalized strategy shaping.

## Features

- BioQuantumEngine: Cognitive decision core with neurotransmitter-driven behavior
- QuantumEncoder: OOV-resilient vector hashing and semantic encoding
- Shu Harmonic Engine: Harmonic matrix optimization for signal coherence
- NeurochemicalState: Dynamic tracking of neurotransmitter and receptor states
- PersonalityProfile: Modular personalities for behavioral modulation
- Psychedelic Simulation: Effects of serotonergic compounds on cognitive plasticity
- Integrated testing included

## Directory Structure

```
neuron7x_hub/
├── neuron7x/
│   ├── config.py
│   ├── quantum_encoder.py
│   ├── harmonic_engine.py
│   ├── neurochemistry.py
│   ├── bioprocessor.py
│   ├── personality.py
│   └── utils/
│       ├── logger.py
│       └── validator.py
├── tests/
│   ├── test_encoder.py
│   ├── test_harmonics.py
│   └── test_integration.py
├── examples/
│   ├── basic_usage.py
│   └── psychedelic_sim.py
```

## Installation

```bash
pip install neuron7x-hub
```

## Example Usage

```python
from neuron7x import NeuroConfig, BioQuantumEngine, QuantumEncoder

config = NeuroConfig()
engine = BioQuantumEngine(config)
encoder = QuantumEncoder({"opportunity": np.random.rand(config.DIM)}, config)

engine.memory.store("buy", encoder.encode("opportunity"), reward=0.9)
simulate_psychedelic(engine, dose_mg=25.0)

decision, report = engine.decide({"risk": 0.7, "novelty": 0.6}, "opportunity")
print(report)
```

## Run Tests

```bash
pytest tests/
```

Or:

```bash
python neuron7x/bioquantum_engine.py
```

## Documentation

```bash
pdoc --html neuron7x -o docs/
```

## Applications

- Cognitive modeling
- Neural adaptation engines
- Psychedelic cognition simulations
- Neuro-symbolic reasoning
- Experimental AI agents

## License

MIT License © 2025 Neuro Labs Collective
```
