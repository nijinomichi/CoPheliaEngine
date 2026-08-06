# CoPhelia³ Engine

**失敗のゆらぎを φ に変える、人間とAIの共創エンジン**  
Failure-Loving Human-AI Co-Creation Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Stars](https://img.shields.io/github/stars/nijinomichi/CoPheliaEngine?style=social)](https://github.com/nijinomichi/CoPheliaEngine)

> わたしたちは「成功の平均」ではなく「失敗のゆらぎ」を観察し、  
> 消去せず、変換し、次の創造へ渡します。

CoPhelia³ Engine is an experimental framework for transforming anonymized failure narratives into inspectable creative signals. Mathematical language such as φ-scaling and PT symmetry is used as a computational and aesthetic model, not as proof of psychological or physical effects.

## Four-Layer Architecture

The engine separates intake, transformation, trust, and downstream expression so that poetic interpretation does not impersonate measurement.

### Layer 1 — Failure Intake

Human or machine-generated failure text enters through a minimal, anonymized schema.

- Remove names, contact details, credentials, and identifying context
- Preserve the creative friction: what resisted, broke, or changed direction
- Mark shared examples with `"anonymous": true`
- Keep the original observation distinguishable from later interpretation

Example input:

```json
{
  "anonymous": true,
  "failure_text": "The first prototype collapsed under its own complexity.",
  "creative_friction": "Removing features revealed the central interaction.",
  "language": "en"
}
```

### Layer 2 — φ Transformation

The core engine converts the failure text and prior context into a reproducible transformation result.

- Text vectorization or embeddings
- Similarity and tension calculations
- Optional φ-based scaling
- Experimental PT-symmetric transformations
- Deterministic parameters where reproducibility matters

This layer produces computational outputs. It does not diagnose people, predict personal outcomes, or establish physical claims about consciousness.

### Layer 3 — RadicanTrust™ Review

Before reuse, the transformed material passes through a trust boundary.

- Provenance: where the input and transformation came from
- Consent: whether the material may be shared or remixed
- Privacy: whether anonymization is sufficient
- Claim type: computational, empirical, metaphorical, aesthetic, or speculative
- Failure visibility: limitations and unsuccessful attempts remain inspectable

RadicanTrust™ is a project protocol for responsible reuse. It is not a standardized clinical, legal, or scientific trust score.

### Layer 4 — Creative Output

Reviewed signals can become downstream artifacts without erasing their origin.

- Golden-spiral and phase-portrait visualizations
- Notebooks and HCI experiment scripts
- VRChat worlds
- Stable Diffusion or ComfyUI nodes
- Poems, installations, interfaces, and research prototypes

The output should retain a link to its provenance and clearly distinguish generated interpretation from observed data.

```text
anonymized failure
        ↓
computational transformation
        ↓
RadicanTrust™ review
        ↓
inspectable creative output
```

## Quick Start

```bash
pip install -r requirements.txt
python CoPheliaEngine.py
```

Python example:

```python
from CoPheliaEngine import CoPheliaEngine

engine = CoPheliaEngine()
result = engine.process_failure(
    "私の失敗作",
    ["過去1", "過去2"],
)
print(result)
```

## Core Principles

- **Failure is not deleted:** unsuccessful attempts remain part of the provenance chain
- **Poetry is not measurement:** aesthetic language and scientific claims remain separated
- **Minimal dependencies:** the target baseline is `numpy + scipy`
- **Human review matters:** consent, context, and downstream risk cannot be delegated entirely to a model
- **Non-destructive evolution:** prefer focused branches, reviewable diffs, and reversible changes

## Repository Files

| File | Purpose |
|---|---|
| `CoPheliaEngine.py` | Minimal runnable core |
| `requirements.txt` | Minimal Python dependencies |
| `failure_log_sample.json` | RadicanTrust™ anonymous schema example |
| `CONTRIBUTING.md` | Contribution, privacy, and PR guidance |

## Roadmap

- [x] Minimal engine and sample failure log
- [x] Four-layer architecture documentation
- [ ] Golden-Spiral visual demo notebook
- [ ] Results Brief with reproducible observations and limitations
- [ ] Colab one-click workflow
- [ ] HCI and creative-coding experiment templates

Each roadmap item should normally be introduced through a focused branch and Draft PR.

## Intended Audiences

- **AI and complexity researchers:** transformation assumptions, reproducibility, and limitations
- **HCI and creativity researchers:** experiment scripts, observations, and participant safeguards
- **Artists and curators:** inspectable provenance for generated visual and spatial works
- **Builders:** small modules that can be reused without importing the entire conceptual framework

## Contributing

Contributions are welcome in Japanese, English, and other languages. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting failure logs, engine changes, visualizations, translations, or downstream modules.

Prefer one focused change per PR and explain how it supports the **failure → φ → reviewed output** loop.

## License

MIT. Reuse freely, preserve provenance, and treat shared failures with care.

---

*RadicanTrust™ / CoPhelia³ — built with φ by Banana Conference.*  
Star ★ · Fork · Share an anonymized `failure_log.json`
