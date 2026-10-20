---
name: react-to-liveview-port
description: Port React pages or components to Phoenix LiveView and HEEx with faithful styling, responsive behavior, and interactions. Use for React-to-LiveView migrations, JSX-to-HEEx conversions, or inspecting a React interface before rebuilding it in Phoenix.
---

# React to Phoenix LiveView

Reproduce the requested React interface while integrating with the destination application's architecture. Treat the source as the visual and behavioral reference; follow explicit destination requirements where they differ. Discover conventions from code rather than assuming a React framework, CSS system, component library, or Phoenix version.

## Establish scope and conventions

- Read applicable repository instructions and relevant documentation in both projects. Locate the React entry point, destination application, and requested route or component. Projects may be separate repositories or share a workspace.
- Inspect manifests and existing implementations to identify styling, components, fonts, themes, assets, routing, authentication, data access, and JavaScript integration. Check for an existing route, partial port, component, or hook before creating one.
- Keep scope to the assigned interface and required behavior. A static mockup does not require new backend features; a functional migration requires real integrations or explicitly disclosed gaps.
- Respect the user's testing and tool permissions. Source inspection, reference inspection, preview preparation, automated tests, and browser QA are distinct activities; do not assume all are authorized.

## 1. Inspect the source

Read [css-extraction.md](css-extraction.md). Trace the page, visually significant children, styles, component variants, assets, and state logic. Establish:

- Layout, responsive rules, typography, themes, imagery, and motion.
- Effective styles after library defaults, local overrides, conditional props, and the CSS cascade.
- Navigation, forms, overlays, loading, permissions, mutations, persistence, and recovery paths relevant to scope.

Record a compact migration map: source component → destination component, source data/action → destination context/event, source token → destination equivalent. Separate observed behavior from assumptions and unresolved runtime values.

For an analysis request, deliver findings and stop. For an authorized implementation, surface material gaps or deviations briefly and continue. Ask only when an unresolved choice materially changes scope, behavior, or fidelity; do not require a separate confirmation for routine translation decisions.

## 2. Implement in Phoenix

Read [liveview-conventions.md](liveview-conventions.md). Reuse destination components, layouts, contexts, authorization, tokens, assets, and hooks where they reproduce the required result.

- Translate rendered output and behavior rather than React syntax or component names mechanically.
- Preserve visual values, responsive rules, states, and semantics. Do not substitute a vaguely similar font, icon, component, or animation without justification.
- Apply explicit destination requirements consistently and explain visible deviations. Never carry another project's font restrictions, storage provider, route structure, or naming into the port.
- Keep server-owned state in LiveView and contexts; use CSS or existing client mechanisms for local visual behavior. Add hooks only for browser capabilities that need them.
- Complete applicable loading, empty, validation, pending, success, failure, retry, permission, and recovery states. Preserve user input on failure and prevent repeated actions from corrupting data.

## 3. Review and hand off

Review changes against the migration map, including responsive/theme variants, authorization, event handling, accessibility, and lifecycle cleanup. Check that required assets and referenced components exist.

Use project verification commands and runtime tools only when permitted. Prepare a live preview when allowed. Never claim runtime, visual, or test verification from source inspection alone.

Hand off briefly: what was ported, material deviations, mocks or missing integrations, verification performed or omitted, and states the user should exercise. If a dependency blocks completion, identify it concretely and finish independent work within scope.
