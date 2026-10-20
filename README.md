# Uzski Corp Agent Skills

Reusable skills for design engineering and application development, maintained by [Uzski Corp](https://github.com/Uzski-Corp).

## React to LiveView

Port React pages and components to Phoenix LiveView and HEEx while preserving layout, styling, responsive behavior, and interactions. The skill discovers the source and destination projects' conventions rather than assuming a framework, component library, or design system.

### Install

```sh
npx skills add Uzski-Corp/agent-skills --skill react-to-liveview-port
```

### Use

Ask your coding agent to use `react-to-liveview-port`, specifying the React source and Phoenix destination. For example:

> Use react-to-liveview-port to port the React profile page in ./frontend to the Phoenix app in ./backend. Preserve its responsive layout and existing interactions, and follow the destination repository's conventions.

The skill inspects effective styles and behavior, maps components and data actions to the destination, then implements and reviews the port within your requested scope and verification permissions. An analysis-only request produces findings without implementing the port.

### Contents

- [Skill instructions](skills/react-to-liveview-port/SKILL.md)
- [React interface inspection](skills/react-to-liveview-port/css-extraction.md)
- [LiveView integration guidance](skills/react-to-liveview-port/liveview-conventions.md)

Supply access to both codebases and any required design assets. Missing backend integrations and deliberate deviations should be reported explicitly. Source review alone does not establish runtime or visual parity.

## License

[MIT](LICENSE) © 2026 Uzski Corp.
