import numpy as np
import json
from neuron7x import NeuroConfig, BioQuantumEngine, QuantumEncoder, PersonalityProfile, simulate_psychedelic

# Initialize configuration
config = NeuroConfig()
engine = BioQuantumEngine(config)

# Prepare embeddings
embeddings = {"opportunity": np.random.rand(config.DIM)}
encoder = QuantumEncoder(embeddings, config)

# Store memory pattern
engine.memory.store("buy", encoder.encode("opportunity"), reward=0.7)

# Add personalities
engine.add_personality(
    PersonalityProfile("trader", {"risk": 0.9, "speed": 0.8})
)
engine.add_personality(
    PersonalityProfile("analyst", {"precision": 0.9, "risk": -0.5})
)

# Simulate psychedelic effect
simulate_psychedelic(engine, dose_mg=20.0)

# Make decision
context = {"risk": 0.7, "novelty": 0.6}
decision, report = engine.decide(context, "opportunity")

# Output
print(f"Decision: {decision}")
print(json.dumps(report, indent=2))
