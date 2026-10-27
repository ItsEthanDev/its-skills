# Quickstart

ItsSkills is a source collection; there is no application server to start.

## Prerequisites

- Git.
- Python 3; the repository check needs no additional packages.
- GitHub CLI (`gh`) and GitHub authentication only when using the issue tracker.

Consumer installation prerequisites depend on the chosen [installation method](../README.md#installation).

## Get the checkout

```sh
git clone https://github.com/ItsEthanDev/its-skills.git
cd its-skills
```

No environment file, secrets, or service configuration is required for local checks.

## Verify a change

From the repository root:

```sh
python3 scripts/check_repo.py
```

Success prints `Repository consistency checks passed.`

The check validates catalog coverage, required bundle notices, and existing attribution inventory entries. It does not establish instruction quality, provenance accuracy, license adequacy, or installation behavior.

Review changed instructions against the principles and applicable writing guidance. For documentation changes, check local links and exercise changed commands where safe.

The repository check also runs on pushes and pull requests through [GitHub Actions](../.github/workflows/check-repo.yml).
