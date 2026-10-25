# Uzski Corp Agent Skills

Reusable skills for design engineering, application development and product communication, maintained by [Uzski Corp](https://github.com/Uzski-Corp).

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

## Programming Best Practices

Apply production Go and Rust practices while writing or reviewing services: project layout, errors, concurrency, HTTP and GraphQL APIs, PostgreSQL, Redis, authentication, security, observability, testing, payments, and background jobs. The skill reads the reference that matches the task.

### Install

```sh
npx skills add Uzski-Corp/agent-skills --skill programming-best-practices
```

### Use

Ask your coding agent to use `programming-best-practices` and name the language and the change. For example:

> Use programming-best-practices to add an idempotent payment endpoint in this Go service. Follow the existing project layout.

The skill applies the patterns in the matching reference and checks its production checklist before finishing. Security references are for prevention and review.

### Contents

- [Skill instructions](skills/programming-best-practices/SKILL.md)
- [Go](skills/programming-best-practices/references/golang-best-practices.md) and [advanced Go](skills/programming-best-practices/references/go-advanced-patterns.md)
- [Rust](skills/programming-best-practices/references/rust-best-practices.md) and [advanced Rust](skills/programming-best-practices/references/rust-advanced-patterns.md)
- [Web applications](skills/programming-best-practices/references/web-application-patterns.md), [API design](skills/programming-best-practices/references/api-design-patterns.md), and [databases](skills/programming-best-practices/references/database-engineering-patterns.md)
- [Caching](skills/programming-best-practices/references/caching-performance-patterns.md), [API security](skills/programming-best-practices/references/api-security-patterns.md), and [web vulnerability prevention](skills/programming-best-practices/references/web-security-attacks-guide.md)
- [Observability](skills/programming-best-practices/references/observability-patterns.md), [testing](skills/programming-best-practices/references/testing-patterns.md), and [payments, orders, and jobs](skills/programming-best-practices/references/real-world-project-patterns.md)
- [Quick reference](skills/programming-best-practices/references/QUICK_REFERENCE.md)
- [Go example config](skills/programming-best-practices/examples/go-api-example) and [Rust example config](skills/programming-best-practices/examples/rust-api-example)

Source notes: [nutcas3/best-practices](https://github.com/nutcas3/best-practices), compiled from 100 Go Mistakes, Effective Go, the Rust API Guidelines, and OWASP.

## Expo MobSF

Harden Expo Android release builds and remediate MobSF findings while preserving camera permissions, authentication, analytics, and other required features. Applies an Android 10 / API 29 baseline (or preserves a higher minimum), reviews full findings, and verifies the score against the actual release APK. The default target is 70; a passing score requires a fresh scan and is not guaranteed by configuration alone.

### Install

```sh
npx skills add Uzski-Corp/agent-skills --skill expo-mobsf
```

### Use

> Use expo-mobsf to harden this Expo Android app and verify a release APK against a MobSF score target of 70. Preserve required camera scanning and its permission recovery.

For a new app, ask the skill to apply the baseline after project creation. The skill uses version-matched Expo docs and respects the project's build and testing permissions. APKs and scan reports stay outside this repository.

### Contents

- [Skill instructions](skills/expo-mobsf/SKILL.md)
- [Expo Android configuration](skills/expo-mobsf/references/expo-android.md)
- [Finding triage and scanning](skills/expo-mobsf/references/mobsf-workflow.md)
- [Saved-report evidence helper](skills/expo-mobsf/scripts/record_evidence.py)

## Sean Product Copy

Write clear product marketing copy for websites, ads, social carousels, app store screenshots, listings and promotional graphics. Uses English by default, with occasional conversational Swahili for suitable Kenyan audiences. Includes approved Bread and Corral examples and guidance for grounding claims in the actual product.

### Install

```sh
npx skills add Uzski-Corp/agent-skills --skill sean-product-copy
```

### Use

> Use sean-product-copy to write a six-slide Instagram carousel introducing this product. Read the product brief first, make each slide specific and end with the appropriate next action.

### Contents

- [Skill instructions](skills/sean-product-copy/SKILL.md)
- [Voice examples and approved marketing directions](skills/sean-product-copy/references/voice-examples.md)

## Sean Communication

Draft concise, warm professional emails, proposals, outreach, client updates and scope discussions in Sean Motanya's voice. Builds confidence through clear scope and supportable facts, with courteous ways to negotiate changes.

### Install

```sh
npx skills add Uzski-Corp/agent-skills --skill sean-communication
```

### Use

> Use sean-communication to draft a brief email accompanying this proposal. Refer to the client's launch goals and use the scope and timeline in the proposal.

### Contents

- [Skill instructions](skills/sean-communication/SKILL.md)

Both writing skills are self-contained and can be installed separately. Supply the relevant brief and product or client context. Drafting does not authorise sending messages, publishing content or changing agreements.

## License

[MIT](LICENSE) © 2026 Uzski Corp.
