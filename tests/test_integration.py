import numpy as np
from neuron7x import NeuroConfig, BioQuantumEngine, QuantumEncoder

def test_decision_logic():
    config = NeuroConfig()
    engine = BioQuantumEngine(config)

    embeddings = {"opportunity": np.random.rand(config.DIM)}
    encoder = QuantumEncoder(embeddings, config)

    engine.memory.store("buy", encoder.encode("opportunity"), reward=0.8)

    context = {"risk": 0.9, "novelty": 0.8}
    decision, report = engine.decide(context, "opportunity")

    assert decision in ["buy", "hold"]
    assert 0.0 <= report["score"] <= 2.0
