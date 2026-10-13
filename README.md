# ItsSkills

ItsSkills is an experimental collection of agent skills for human-directed, agent-executed software engineering.

## Installation

The repository follows Vercel's skills CLI source layout and can be consumed as a source-only Nix flake input. Both methods use the same skill directories. End-to-end installation verification against the published repository is pending publication.

### Individual skills

Choose any skill or combination by identifier:

```sh
npx skills add ItsEthanDev/its-skills --skill writing codebase-design
```

### Project setup

Install `setup` to establish a project's documentation baseline, issue-tracker configuration, and domain-doc layout:

```sh
npx skills add ItsEthanDev/its-skills --skill setup
```

Invoke `setup` explicitly in your agent. It explores the repo and asks you to approve the proposed documentation before writing.

### Nix

Add a source-only input to your configuration flake:

```nix
inputs.its-skills = {
  url = "github:ItsEthanDev/its-skills";
  flake = false;
};
```

Your consumer's `flake.lock` pins the source revision. ItsSkills does not require a provider flake, package build, or separate copy of the skills.

For Pi through Home Manager, pass your flake `inputs` through `extraSpecialArgs` and point its skill discovery at the source directory:

```nix
{ inputs, ... }: {
  programs.pi-coding-agent = {
    enable = true;
    settings.skills = [ "${inputs.its-skills}/skills" ];
  };
}
```

The directory contains every skill. To select individual skills, use their complete directory paths instead, such as `"${inputs.its-skills}/skills/writing"`. Keep each selected skill's references, templates, and scripts with it; selecting a `SKILL.md` alone does not preserve its bundle.

### Installation notes

- The CLI commands leave target-agent selection to the CLI prompts and use project-local installation by default. Add `--global` for user-wide installation or `--agent <agent>` to select a target explicitly.
- Invocation metadata support depends on the consuming agent.

## Project principles

The [project constitution](CONSTITUTION.md) governs skill composition, context use, and attribution. [Agent instructions](AGENTS.md) point contributors using agents to the applicable guidance.

## Acknowledgments

ItsSkills draws on ideas and adapted guidance from:

- [Matt Pocock's skills](https://github.com/mattpocock/skills), published under the [MIT license](https://github.com/mattpocock/skills/blob/24fe0ef7737efae15c87225755e9f6f5965e4888/LICENSE). Copyright (c) 2026 Matt Pocock.
- [Lauren Tan (Poteto)'s Pstack](https://github.com/cursor/plugins/tree/main/pstack), published under the [MIT license](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/LICENSE). Copyright (c) 2026 Lauren Tan.

[Anthropic's Frontend Design skill](https://www.skills.sh/anthropics/skills/frontend-design) informed Frontend Design's emphasis on intentional visual structure, user-centered copy, restraint, and screenshot inspection. The collection's skill uses original instructions rather than importing Anthropic's skill or its distinctive-identity premise.

The collection developed through earlier local adaptations in the maintainer's Nix configuration. Attribution is currently collection-level; exact file-by-file upstream lineage has not been fully reconstructed. These license references identify the versions checked, not necessarily the original import revisions. Credit does not imply endorsement or upstream authorship of every skill.

## License

ItsSkills uses [MIT](LICENSE). Collection-level [third-party notices](THIRD-PARTY-NOTICES.md) preserve the upstream copyright and permission notices, which apply to their respective material. Distributions of copied or adapted material must retain the applicable notices. Individual-directory installations may omit these root files; notice preservation for those installations remains unresolved.
