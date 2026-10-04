# Repository Tools

This directory owns tools for maintaining ItsSkills sources and committed derived artifacts. Runtime skills and their bundled execution resources belong in their role directories instead.

Keep each tool's entry point, dependency declarations, tests, and usage documentation together. Tool commands must not install prerequisites into a user profile or depend on the maintainer's machine configuration.

- [Skill graph](skill-graph/README.md): generate and check the committed skill dependency graph.
