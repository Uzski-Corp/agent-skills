# Integrating a port into Phoenix LiveView

Use installed Phoenix/LiveView versions and destination code as the starting point. Discover actual modules, paths, hooks, themes, and context APIs; none are universal. Consult version-matched official documentation when an API or lifecycle detail is uncertain.

## Components, layouts, and styles

- Inspect routes, layouts, LiveViews, components, assets, and related contexts. Extend existing partial ports instead of adding competing implementations.
- Use function components for rendering and LiveComponents when independent state/event lifecycles warrant them. Keep page-specific pieces local unless reuse or complexity justifies extraction. Follow local attribute and slot conventions.
- Translate conditions and collections with supported HEEx constructs. Use structured conditional class lists where suitable; ensure dynamic classes work with destination CSS generation.
- Verify source utilities exist in the destination. Tailwind versions, plugins, resets, themes, and content scanning differ; matching class names do not guarantee matching output.
- Map typography and tokens against the source. Preserve values unless explicit destination rules require a difference. Do not assume fonts, weights, or themes have already been ported.
- Reuse the actual theme strategy: class, attribute, media query, or server-driven. Account for initial selection and persistence without adding a competing mechanism.
- Follow the existing asset pipeline or CDN integration. Preserve image sizing, crops, icons, and fonts; do not hardcode another application's host or assume a React image loader exists.

## State ownership

| Source responsibility | Destination choice |
| --- | --- |
| Hover/focus styling and simple visual effects | CSS where sufficient |
| Local disclosure, visibility, or focus | Existing components or Phoenix JS commands where sufficient |
| Browser APIs, widgets, gestures | Existing integration or scoped hook |
| Data loading, forms, permissions, mutations | LiveView events and domain contexts |
| Shareable filters, tabs, pagination | URL parameters where appropriate |
| Realtime domain changes | Existing subscriptions or scoped PubSub when required |

Avoid server events for purely visual interactions. Client-visible state and disabled controls do not establish authorization or enforce domain invariants.

Reuse context functions and data contracts rather than copying browser fetches into a disconnected backend path. For external API clients, follow destination authentication and error handling; keep secrets server-side.

Account for disconnected rendering and connected mount. Avoid duplicate side effects/subscriptions and subscribe in the appropriate connected lifecycle. Follow established async-loading patterns for slow operations and guard against stale results after parameter changes.

## Forms and mutations

- Reuse changesets, validation rules, and supported form APIs rather than manually reconstructing input state.
- Preserve entered values and actionable errors on failure. Distinguish validation, service, and permission failures.
- Prevent repeated submissions in the UI and enforce idempotency or uniqueness at the domain boundary when duplicate execution matters. Preserve optimistic behavior only with reconciliation and rollback.
- Integrate uploads through supported destination mechanisms, including relevant limits, progress, cancellation, and errors.
- Enforce authorization in handlers and contexts, including ownership checks using server-resolved identities. Do not trust client-supplied IDs or hide-only controls.

## Lists and realtime

Inspect list conventions before choosing assigns, streams, or pagination. Streams suit growing or frequently updated collections, but are not mandatory for every list. Preserve stable DOM IDs, required stream containers, ordering, and reset/update behavior supported by the installed version.

For infinite loading, guard concurrent requests and repeated observer triggers. Expose end/error states and preserve cursors on failure. Reuse suitable viewport mechanisms or hooks; an animation observer is not automatically a pagination integration.

Inspect subscriptions and broadcasts before adding realtime behavior. Scope topics and access appropriately. Reconcile inserts, updates, deletes, and duplicates without discarding local work. Do not assume realtime exists or is absent based on another project.

## Hooks and DOM ownership

Follow installed hook registration conventions. Give hooked elements stable IDs; implement needed mount, update, disconnect/reconnect, and cleanup behavior. Disconnect observers, remove listeners, and destroy external instances when elements disappear.

Keep LiveView patching compatible with third-party DOM mutation. Use ignored regions only where necessary, with explicit data synchronization because normal patches will not update them as ordinary elements.

Port motion by behavior rather than React library API. Prefer existing CSS/JS integrations for simple motion; add hooks or dependencies only when fidelity requires them. Preserve interruption and reduced-motion behavior.

## Navigation, overlays, and safe rendering

Follow router scopes, layouts, authentication hooks, and navigation APIs. Distinguish parameter changes within a LiveView, navigation between LiveViews, and external/full-page navigation. Keep dynamic routes from shadowing more specific routes.

Choose local or server-owned overlay visibility according to whether server logic needs to react. Preserve keyboard support, focus trapping/return, escape dismissal, labels, and scroll behavior through existing accessible components or equivalent implementation.

Keep untrusted content escaped. Do not translate React text rendering into raw HTML. Prefer structured rendering for links/mentions; rich HTML needs an established sanitization path and safe URL handling, not a generic escape-then-regex recipe.

## Review boundary

Review routes, dependencies, data/event mappings, responsive/theme states, assets, and lifecycle cleanup. Use only permitted verification actions. Report source review, compilation, tests, and browser/device checks separately; preparing a preview does not establish behavior or visual parity.
