# Provenance: prototype

**Classification: Adapted.** Shared process generalized for non-code artifacts; engineering rules extracted and capture boundaries clarified.

## License scope

`LICENSE` contains the collection's MIT notice for original local material and modifications. Copied or adapted upstream material retains the applicable notice below; the local license does not replace it.

- [`licenses/Matt-Pocock-MIT.txt`](licenses/Matt-Pocock-MIT.txt): unmodified Matt Pocock MIT notice, relocated from this bundle's former `LICENSE`. Applies to the copied or adapted material identified below.

Retain this file and the applicable license files when distributing this directory. Attribution does not imply endorsement or authorship of unrelated local material.

## File evidence

| Local file | Classification | Pinned source | Evidence and changes |
| --- | --- | --- | --- |
| `SKILL.md` | Adapted | [Matt Pocock: `skills/engineering/prototype/SKILL.md`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/prototype/SKILL.md) | Question-driven branch selection and common rule wording retained where applicable; only code-specific details are extracted. Non-code artifacts broaden the method beyond software; explicit software routing avoids forcing non-code state models into HTML demos. State visibility applies to non-code workflows too. Lightweight issue context preserves the question across handoffs; obvious answers permit agent judgment while caller-required human confirmation remains binding. Version control is a blocking prerequisite so the primary source has a retrievable revision. Capture retains upstream throwaway-branch wording for code and non-code alike, allowing explicit project conventions with equivalent isolation and a durable revision pointer; preservation requires no ongoing upkeep, and implementation and publication remain separately scoped. |
| `ENGINEERING.md` | Adapted | [Matt Pocock: `skills/engineering/prototype/SKILL.md`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/prototype/SKILL.md) | Execution, persistence, code-polish, and state-rendering instructions retain upstream wording apart from numbering and removal of the shared rationale for skipping polish. Shared principles and the implementation-scope boundary remain in SKILL.md instead of being copied here. UI-specific routing conventions remain in UI.md. |
| `LOGIC.md` | Copied | [Matt Pocock: `skills/engineering/prototype/LOGIC.md`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/prototype/LOGIC.md) | Byte-identical to the pinned upstream file. Shared SKILL.md guidance governs decision authority, capture conventions, and when integration is in scope. |
| `UI.md` | Copied | [Matt Pocock: `skills/engineering/prototype/UI.md`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/prototype/UI.md) | Byte-identical to the pinned upstream file. Shared SKILL.md guidance governs decision authority, capture conventions, and when integration is in scope. |

The source revisions pin this comparison, not necessarily the original import. "Original" means no identifiable borrowing from the three audited projects, not proof of independent creation. Local history includes imports from earlier Nix-configuration adaptations whose exact upstream import revisions are not recorded.
