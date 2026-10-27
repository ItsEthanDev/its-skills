# Implementation triage

Use this feature when the project uses implementation tickets. It requires an agreed issue tracker or local ticket convention. It is not required merely because the project tracks decisions or learning activities.

Recommend the default roles from the triage-label seed: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix`. Ask whether to keep those strings; preserve any existing mapping or collect the user's overrides.

Record the agreed mapping in the project's triage guidance. Local implementation tickets use those strings in `Status:`; Wayfinder decision tickets instead use the tracker-specific lifecycle convention. Keep the two distinct.

Record required remote labels without creating them. Setup writes the mapping; label creation is a separate remote action requiring authorization. Don't prescribe implementation triage to a writing or learning project that doesn't use it.
