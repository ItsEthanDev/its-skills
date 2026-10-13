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

The directory contains every skill. To select individual skills, use their complete directory paths instead, such as `"${inputs.its-skills}/skills/writing"`. Keep each selected skill's references, templates, scripts, `PROVENANCE.md`, `LICENSE`, and any `licenses/` directory with it; selecting a `SKILL.md` alone does not preserve its bundle or notices.

### Installation notes

- The CLI commands leave target-agent selection to the CLI prompts and use project-local installation by default. Add `--global` for user-wide installation or `--agent <agent>` to select a target explicitly.
- Invocation metadata support depends on the consuming agent.

## Project principles

The [project constitution](CONSTITUTION.md) governs skill composition, context use, and attribution. [Agent instructions](AGENTS.md) point contributors using agents to the applicable guidance.

## Acknowledgments

ItsSkills draws on ideas and adapted guidance from:

- [Matt Pocock's skills](https://github.com/mattpocock/skills), published under the [MIT license](https://github.com/mattpocock/skills/blob/24fe0ef7737efae15c87225755e9f6f5965e4888/LICENSE). Copyright (c) 2026 Matt Pocock.
- [Lauren Tan (Poteto)'s Pstack](https://github.com/cursor/plugins/tree/main/pstack), published under the [MIT license](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/LICENSE). Copyright (c) 2026 Lauren Tan.
- [Anthropic's frontend design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design), published under the [Apache License 2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/LICENSE.txt).

## License

ItsSkills' original material uses [MIT](LICENSE). Copied and adapted material retains its applicable upstream notices. The [skill inventory](THIRD-PARTY-NOTICES.md#skill-inventory) classifies all 28 skills and links to file-level evidence. Each skill directory includes `PROVENANCE.md`, `LICENSE`, and any additional upstream licenses under `licenses/`; retain them with individual skill distributions. Inspiration credits do not change the license of original local text.
