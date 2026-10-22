# Provenance: verifying-work

**Classification: Adapted.** Poteto verification protocols and Matt feedback-loop guidance combined; HITL script copied.

## License scope

`LICENSE` contains the collection's MIT notice for original local material and modifications. Copied or adapted upstream material retains the applicable notices below; the local license does not replace them.

- [`licenses/Lauren-Tan-MIT.txt`](licenses/Lauren-Tan-MIT.txt): unmodified [Lauren Tan (Poteto) license](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/LICENSE). Applies to the copied or adapted material identified below.

- [`licenses/Matt-Pocock-MIT.txt`](licenses/Matt-Pocock-MIT.txt): unmodified [Matt Pocock license](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/LICENSE). Applies to the copied or adapted material identified below.

Retain this file and the applicable license files when distributing this directory. Attribution does not imply endorsement or authorship of unrelated local material.

## File evidence

| Local file                      | Classification | Pinned source                                                                                                                                                                                                                          | Evidence and changes                                                                                                                                                          |
| ------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SKILL.md`                      | Adapted        | [Lauren Tan (Poteto): `pstack/skills/principle-prove-it-works/SKILL.md`](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/skills/principle-prove-it-works/SKILL.md)                              | Real-artifact evidence, build-vs-behavior distinction, and observation-method checks reworked into a bounded verification workflow.                                           |
| `SKILL.md`                      | Adapted        | [Lauren Tan (Poteto): `pstack/skills/create-verification-skill/SKILL.md`](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/skills/create-verification-skill/SKILL.md)                            | Existing harnesses, readiness, isolation, evidence, and cleanup guidance synthesized; see local design history f515e0e and restoration c6ca664.                               |
| `FEEDBACK-LOOPS.md`             | Adapted        | [Matt Pocock: `skills/engineering/diagnosing-bugs/SKILL.md`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/diagnosing-bugs/SKILL.md)                                           | Phase 1 method taxonomy, sharpening/repeatability/speed, intermittent reproduction, and blocker reporting extracted and rewritten in c6ca664.                                 |
| `PROJECT-VERIFICATION.md`       | Adapted        | [Lauren Tan (Poteto): `pstack/skills/create-verification-skill/SKILL.md`](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/skills/create-verification-skill/SKILL.md)                            | Repo interview, launch/readiness/drive/evidence/cleanup, discovery metadata, and end-to-end proof adapted without Cursor-specific paths or mandatory feature map.             |
| `PROJECT-VERIFICATION.md`       | Adapted        | [Lauren Tan (Poteto): `pstack/skills/maintain-verification-skill/SKILL.md`](https://github.com/cursor/plugins/blob/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack/skills/maintain-verification-skill/SKILL.md)                        | Protocol drift, harness gaps, product regressions, re-driving corrections, and evidence-preserving cleanup adapted without its required parallel feature wave or PR workflow. |
| `scripts/hitl-loop.template.sh` | Copied         | [Matt Pocock: `skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/diagnosing-bugs/scripts/hitl-loop.template.sh) | Byte-identical human-assisted loop template, moved into this bundle in c6ca664.                                                                                               |

The source revisions pin this comparison, not necessarily the original import. "Original" means no identifiable borrowing from the three audited projects, not proof of independent creation. Local history includes imports from earlier Nix-configuration adaptations whose exact upstream import revisions are not recorded.
