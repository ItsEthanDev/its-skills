# Third-party notices

The skills listed in the inventory below and their supporting files have been compared against Matt Pocock's skills, Lauren Tan (Poteto)'s Pstack, and Anthropic's skills. New skills outside that audit record their creation history in their own provenance files. Each skill directory contains `PROVENANCE.md`, a `LICENSE`, and any additional upstream licenses under `licenses/`, so its notices travel with individual-directory distributions.

ItsSkills' original material uses the MIT license. Copied and adapted material retains its upstream notices. An inspiration credit does not relicense original local text. Attribution does not imply endorsement or upstream authorship of unrelated material. Retain each directory's provenance and applicable license files when redistributing it.

## Audit scope and classifications

The comparison uses these pinned source trees:

- [Matt Pocock: 49dd158d1076134a641b33efb035946536778336](https://github.com/mattpocock/skills/tree/49dd158d1076134a641b33efb035946536778336)
- [Pstack: 1dcc2bacde73ddd284803b7af28164d0436198fc](https://github.com/cursor/plugins/tree/1dcc2bacde73ddd284803b7af28164d0436198fc/pstack)
- [Anthropic: dbd4588f9e1033efb41dad4bef2f7947c8993d44](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44)

The review combines full local-file inspection, exact diffs, distinctive passage matching across the three source collections, and local Git history. Matt's and Pstack's license files at these revisions are byte-identical to the earlier license pins below. These pins identify comparison revisions, not necessarily original imports; some material arrived through earlier Nix-configuration adaptations.

- **Copied:** substantive instructions are verbatim, including bundles that only rename metadata or add a heading. File-level evidence identifies those packaging changes.
- **Adapted:** upstream text or a distinctive procedure is retained with changed instructions, extraction, reorganization, or synthesis. A bundle with both original and borrowed files is classified as adapted.
- **Inspired:** evidence establishes idea-level influence, without identifiable copied passages or an adapted procedure.
- **Original:** no identifiable borrowing from these three projects. This is a bounded audit finding, not proof of independent creation; generic similarities and calls to another skill do not establish derivation.

## Skill inventory

| Skill                                                                                             | Classification | Evidence                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`alignment`](skills/general/alignment/PROVENANCE.md)                                             | Copied         | Renamed copy of grilling; the interview procedure is verbatim.                                                                                               |
| [`code-review`](skills/engineering/code-review/PROVENANCE.md)                                     | Adapted        | Near-verbatim code-review with the setup reference retargeted.                                                                                               |
| [`codebase-design`](skills/engineering/codebase-design/PROVENANCE.md)                             | Copied         | All three instruction files are byte-identical.                                                                                                              |
| [`diagnosing-bugs`](skills/engineering/diagnosing-bugs/PROVENANCE.md)                             | Adapted        | Diagnosis workflow retained; feedback-loop construction extracted and reproduction gate changed.                                                             |
| [`dry-run`](skills/general/dry-run/PROVENANCE.md)                                                 | Original       | Local diff-preview and approval procedure.                                                                                                                   |
| [`frontend-design`](skills/engineering/frontend-design/PROVENANCE.md)                             | Inspired       | Original task-centered instructions informed by Anthropic frontend-design.                                                                                   |
| [`implement`](skills/engineering/implement/PROVENANCE.md)                                         | Adapted        | Implementation workflow extended with verification gates.                                                                                                    |
| [`improve-codebase-architecture`](skills/engineering/improve-codebase-architecture/PROVENANCE.md) | Adapted        | Architecture review retargeted to local skills; report guidance copied verbatim.                                                                             |
| [`ingest-document`](skills/general/ingest-document/PROVENANCE.md)                                 | Original       | Local document-intake and adoption procedure.                                                                                                                |
| [`pause-work`](skills/general/pause-work/PROVENANCE.md)                                           | Adapted        | Matt handoff text combined with Poteto safe-pause guidance.                                                                                                  |
| [`pr`](skills/general/pr/PROVENANCE.md)                                                           | Adapted        | PR guidance retained; evidence guidance generalized for executable behavior, prose, and research. Upstream credit preserved.                                 |
| [`propose-first`](skills/general/propose-first/PROVENANCE.md)                                     | Original       | Local investigation, recommendation, and approval procedure.                                                                                                 |
| [`prototype`](skills/general/prototype/PROVENANCE.md)                                             | Adapted        | Shared process generalized for non-code artifacts; engineering rules extracted and capture boundaries clarified.                                             |
| [`repitch`](skills/general/repitch/PROVENANCE.md)                                                 | Adapted        | wait-what expanded with scope and conversational-state rules.                                                                                                |
| [`research`](skills/general/research/PROVENANCE.md)                                               | Copied         | Byte-identical research skill.                                                                                                                               |
| [`retro`](skills/general/retro/PROVENANCE.md)                                                     | Adapted        | Retrospective procedure retained; engineering guidance extracted into a conditional reference.                                                               |
| [`setup`](skills/general/setup/PROVENANCE.md)                                                     | Adapted        | Matt setup and domain-modeling guidance adapted into selectable features and project-owned terminology/decision-record methods; file-level sources retained. |
| [`to-spec`](skills/engineering/to-spec/PROVENANCE.md)                                             | Adapted        | to-spec adapted to configured triage roles.                                                                                                                  |
| [`tdd`](skills/engineering/tdd/PROVENANCE.md)                                                     | Copied         | Skill and both test-quality references are byte-identical.                                                                                                   |
| [`teach`](skills/learning/teach/PROVENANCE.md)                                                    | Copied         | Skill and all three format references are byte-identical to Matt's teach skill.                                                                              |
| [`to-implementation-tickets`](skills/engineering/to-implementation-tickets/PROVENANCE.md)         | Adapted        | to-tickets renamed and adapted to configured tracker conventions.                                                                                            |
| [`to-questionnaire`](skills/general/to-questionnaire/PROVENANCE.md)                               | Adapted        | Matt's questionnaire skill with "Grill the send" changed to "Align on the send".                                                                             |
| [`verifying-work`](skills/general/verifying-work/PROVENANCE.md)                                   | Adapted        | Poteto verification protocols and Matt feedback-loop guidance combined; HITL script copied.                                                                  |
| [`wayfinder`](skills/general/wayfinder/PROVENANCE.md)                                             | Adapted        | Wayfinding procedure adapted to local skills and tracker conventions.                                                                                        |
| [`wizard`](skills/general/wizard/PROVENANCE.md)                                                   | Copied         | Skill and bash template are byte-identical.                                                                                                                  |
| [`writing`](skills/general/writing/PROVENANCE.md)                                                 | Adapted        | Matt agent-writing and Poteto technical-writing guidance behind an original audience router.                                                                 |

### Retained upstream credit and audit limits

Matt's `pr` skill credits Dex Horthy / Humanlayer's `show-me`; that metadata is preserved in the local file. Humanlayer was not independently audited because this review is limited to the three requested projects. This is an upstream credit, not a claim that its separate licensing has been verified.

Anthropic's frontend-design license is colocated as a source reference, not as the license of the original local skill. Its repository's third-party dependency notices concern components not included in this skill bundle; none of those components is distributed here. No frontend-design-specific `NOTICE` file was found in the pinned source tree.

## Project guidance

The terminology and decision-record methods in setup and project guidance adapt
Matt Pocock's domain-modeling skill. Their applicable MIT notice is included in
`skills/general/setup/licenses/Matt-Pocock-MIT.txt` and in this collection-level notice.

- [Domain guidance](docs/agents/domain.md) adapts the active terminology practice from
  [domain-modeling/SKILL.md](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md)
  and definition rules from
  [GLOSSARY-FORMAT.md](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/GLOSSARY-FORMAT.md).
- [Decision-record guidance](docs/agents/decision-records.md) adapts the offer criteria from
  [domain-modeling/SKILL.md](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md)
  and the short record format, examples, and optional sections from
  [ADR-FORMAT.md](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/ADR-FORMAT.md).

Local additions define project approval, discovery, and maintenance. The setup
bundle's provenance identifies the corresponding adapted templates; upstream
authorship is not claimed for unrelated local policy.

## Matt Pocock's skills

Source: [mattpocock/skills](https://github.com/mattpocock/skills).

License verified at [24fe0ef7737efae15c87225755e9f6f5965e4888](https://github.com/mattpocock/skills/blob/24fe0ef7737efae15c87225755e9f6f5965e4888/LICENSE).

```text
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Lauren Tan (Poteto)'s Pstack

Source: [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack).

License verified at [e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/LICENSE).

```text
MIT License

Copyright (c) 2026 Lauren Tan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## Anthropic's frontend design skill

Source: [anthropics/skills/frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design).

License verified at [dbd4588f9e1033efb41dad4bef2f7947c8993d44](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/LICENSE.txt).

```text

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS
```
