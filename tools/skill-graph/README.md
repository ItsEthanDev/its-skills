# Skill Graph Tool

Generate `DEPENDENCIES.md` and `dependencies.json` from runtime sources under `skills/<role>/<skill-name>/`. Source paths remain relative to the repository root. These are repository maintenance commands, not installation tools.

## Run

Nix with flakes enabled is required. The adjacent pinned environment supplies Python and the Markdown parser. Missing Nix is an error, not a request to install it. Dependency acquisition uses the Nix store, not a user profile.

From the repository root:

```sh
sh tools/skill-graph/graph.sh generate
sh tools/skill-graph/graph.sh check
sh tools/skill-graph/graph.sh test
```

Use `--help` for the executable interface. Commands resolve the repository from the tool location, not the current working directory; `--root PATH` selects another source repository for fixtures or relocated checkouts. Generation updates only the two derived output files. Check mode validates sources and compares both outputs without rewriting them. Test mode exercises the public generator/check interface with disposable source fixtures.

## Interpret

An arrow A to B means that A contains an inline-code reference to B's exact frontmatter name, directly or in its supporting Markdown. Conditional and explanatory references count equally. Plain prose, frontmatter, fenced examples, comments, unknown identifiers, and self-references do not create edges. Skill resources are attributed to their owner; they are not separate graph nodes.

For a conservative subset, include each selected skill and all nodes reachable through its outgoing edges. For potential impact, follow incoming edges transitively; a changed resource first maps to its owning skill. Neither calculation proves that a dependency will be invoked or a caller will break. Same-skill resources must travel with their owner under whatever installation mechanism a consumer chooses.

The generated JSON is the consumer data interface. Its structure is described in the generated graph document alongside the direct dependency table and evidence links. Consumers may implement their own traversal or installation tooling; this repository does not install or resolve dependencies for them.

## Maintain

Regenerate after changing references, skill identifiers, resource locations, or the generator. Commit both outputs with their source changes. CI runs tests and the freshness check. A stale graph, cross-skill link, invalid identifier, duplicate name, forbidden role direction, or cycle must fail rather than produce a successful partial graph.

The feature contract is [Skill Dependency Graph](../../specs/skill-dependency-graph/spec.md).
