"""
CoPhelia³ Engine
Failure-Loving Human-AI Co-Creation Framework

失敗のゆらぎをφ（黄金比）に変える最小実装。
MIT License
"""

import numpy as np
from scipy.linalg import eig
from typing import List, Optional, Dict, Any
import json
from pathlib import Path


class CoPheliaEngine:
    """Core engine that turns failure fluctuations into φ-boosted creative output."""

    def __init__(self, phi: float = 1.618033988749895, failure_log: Optional[List[Dict]] = None):
        self.phi = phi
        self.failure_log = failure_log or []

    def phi_perturbation(self, input_vector: np.ndarray) -> np.ndarray:
        """Apply non-Hermitian PT-symmetric matrix scaled by φ to inject and stabilize failure noise."""
        # Golden-ratio PT-symmetric core matrix
        pt_matrix = np.array([[0.0, 1.0], [self.phi, 0.0]])
        noise = np.random.normal(0, 0.08, input_vector.shape)
        perturbed = input_vector.astype(float) + noise
        # Project into 2D if needed
        if perturbed.ndim > 1:
            perturbed = perturbed.flatten()[:2]
        if len(perturbed) < 2:
            perturbed = np.pad(perturbed, (0, 2 - len(perturbed)))
        eigenvalues, _ = eig(pt_matrix @ perturbed.reshape(2, 1))
        return np.real(eigenvalues) * self.phi

    def process_failure(self, user_input: str, failure_history: Optional[List[str]] = None) -> str:
        """RadicanTrust™ style anonymous failure sharing → φ-boosted remix."""
        history = failure_history or []
        # Simple deterministic vectorization from content
        vec = np.array([
            abs(hash(user_input)) % 100 / 100.0,
            len(history) / 10.0,
            len(user_input) / 50.0
        ])
        boosted = self.phi_perturbation(vec[:2])
        phi_score = float(np.abs(boosted[0]))

        remix = (
            f"φ-boosted remix: 「{user_input}」 + failure fluctuation "
            f"→ creative spark {phi_score:.4f} "
            f"(history depth {len(history)})"
        )

        entry = {
            "input": user_input,
            "phi_score": phi_score,
            "history_len": len(history),
            "timestamp": None  # caller can fill
        }
        self.failure_log.append(entry)
        return remix

    def save_log(self, path: str = "failure_log.json") -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.failure_log, f, ensure_ascii=False, indent=2)

    def load_log(self, path: str = "failure_log.json") -> None:
        p = Path(path)
        if p.exists():
            with open(p, encoding="utf-8") as f:
                self.failure_log = json.load(f)


if __name__ == "__main__":
    engine = CoPheliaEngine()
    print(engine.process_failure("私の失敗作", ["過去失敗1", "過去失敗2"]))
    print("\n--- φ core ready. Star the repo & share your failure_log ---")
