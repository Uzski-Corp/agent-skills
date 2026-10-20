# Inspecting a React interface for a faithful port

Capture enough evidence to rebuild the requested interface without guessing. Scale the report to the component; a button needs less analysis than a responsive feed with overlays.

## Trace the rendering path

Follow the requested page's imports, wrappers, layouts, providers, relevant children, conditional rendering, and data-dependent variants. Read children deeply when they determine the visible surface or behavior; summarize unrelated internals.

Identify the actual styling implementation: plain CSS, CSS Modules, utility classes, CSS-in-JS, library themes, inline styles, or a combination. Do not assume Next.js, Tailwind, or shadcn/ui.

## Resolve effective styles

For significant regions, record:

- Container width, alignment, grid/flex structure, gaps, padding, overflow, positioning, stacking, and sticky behavior.
- Font family and loaded files, weight, size, line height, tracking, wrapping, truncation, and icon metrics.
- Colors, borders, radii, shadows, gradients, backgrounds, opacity, and image crop/fit.
- Responsive breakpoints and changes in layout, visibility, order, density, and navigation.

Trace tokens through actual configuration, variable scopes, inherited defaults, fallbacks, and theme overrides. A variable absent from one theme block can still inherit a valid value. Flag missing tokens only after tracing the applicable cascade.

Keep original color expressions and alpha values. Provide resolved values when useful; do not replace wide-gamut or dynamic colors with lossy hex approximations. Label values that depend on unavailable generated CSS, viewport settings, or runtime styles as unresolved rather than presenting guesses as computed output.

For library primitives, inspect the implementation or installed source: base styles, selected variants/sizes, state selectors, slot styles, and page-level overrides. Resolve class merging and CSS precedence; concatenation order alone does not determine the winning declaration. Record effective rules rather than dumping every utility class.

Preserve intentional one-off values when no equivalent destination token exists. Reuse matching tokens; do not approximate spacing, colors, or shadows merely to fit the destination palette.

## Map interactions and data

Trace handlers, effects, hooks, forms, links, requests, and subscriptions. Record each relevant action's trigger, state owner, visible result, and failure behavior.

Cover applicable loading, empty, populated, validation, pending, success, error/retry, disabled, permission, and interrupted-work states. Check optimistic updates/rollback, pagination ordering, URL state, persistence, and reconnection where present. Do not invent unrelated product behavior.

For overlays and composite controls, inspect keyboard behavior, focus entry/return, dismissal, accessible names, and scroll locking. Identify behaviors supplied by portals or injected library wrappers that will disappear in HEEx.

## Record assets and motion

Locate original imagery, icons, fonts, and known availability or reuse constraints. Record dimensions, aspect ratios, responsive sources, crops, loading behavior, and alternative text. Framework image components may supply optimization or sizing that ordinary image tags need explicitly.

Identify the actual motion implementation: CSS transitions/keyframes, library props, springs, gestures, or browser APIs. Record triggers, properties, easing, duration/delay, exits, interruption, and reduced-motion handling. Read installed configuration rather than assuming library defaults.

## Produce a migration brief

Use the smallest useful set of notes:

1. Layout and responsive structure.
2. Typography, token/theme mapping, assets, and significant literal values.
3. Component defaults and effective overrides.
4. Interaction/state map, data dependencies, and motion.
5. Destination mappings, unresolved evidence, and material deviations.

Distinguish source bugs from deliberate design choices. Surface bugs affecting migration; apply authorized fixes without silently redesigning the interface. Continue an authorized implementation unless a material ambiguity needs the user's answer.
