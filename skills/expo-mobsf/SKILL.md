---
name: expo-mobsf
description: Harden Expo Android apps and remediate MobSF static-analysis findings while preserving required permissions and features. Use to prepare a release APK for MobSF, improve a reported score, or apply an Android 10 baseline to a new Expo project.
---

# Expo Android MobSF hardening

Aim for a measured MobSF score of at least 70 unless the user specifies another threshold. A configuration change, successful build, or source review is not a passing scan. Android 10 is a compatibility floor, not a claim that devices still receive security updates.

## Establish the actual app and report

- Read project instructions, `package.json`, effective Expo configuration, lockfile, EAS profiles, and relevant native/config plugins. Preserve unrelated work. Determine whether native projects are generated or maintained before editing them.
- Read the installed Expo major's versioned docs at `https://docs.expo.dev/versions/v<major>.0.0/`. For tooling use `https://docs.expo.dev/llms.txt` and follow its links. Install SDK packages with the project's runner and `expo install`; do not assume remembered options still exist.
- For an existing report, confirm package, APK hash, build variant, baseline score, scanner version, and suppressions. Read the full findings and file locations, not just the scorecard titles. Store app reports locally outside this public skill repository; redact credentials in output.
- For a new project without an APK, apply the baseline below, then explicitly report that its score is unverified.
- Identify required camera/audio/media, authentication, storage, analytics, deep links, and networking. The skill does not authorize removing features, uploading to a hosted scanner, paid builds, deployments, or additional testing contrary to project instructions.

## Apply persistent hardening

Read [Expo configuration and permission guidance](references/expo-android.md). Default to API 29 or the app/framework's higher existing minimum; never lower an existing requirement. Use Expo configuration or config plugins for generated projects.

- Disable app backup unless the user requires a reviewed backup design. Preserve secure-store exclusions; explain that OS/vendor device-transfer behavior can differ.
- Disallow release cleartext traffic. Keep endpoints and certificate validation intact; development access must not relax production configuration.
- Remove demonstrated-unused permissions; preserve required camera access and its denial/settings recovery. Barcode-only camera usage normally needs no microphone, media-library, external-storage, or overlay permission. Check actual app use and SDK plugin options before blocking them.
- Verify release is non-debuggable and not a development client; preserve existing signing, ABI, optimization, environment, and update behavior. Do not trade away required platforms or architecture support for score.
- Review exported components and intent handling individually. Launcher/deep-link activities and signature-protected library components have legitimate uses. Do not blanket-remove components, change authentication/browser task affinity, or override library crypto to silence a finding.

## Remediate actual findings

Read [finding triage and scan workflow](references/mobsf-workflow.md).

Trace each high finding and relevant warning to app code or a specific bundled dependency/version. For obfuscated code, use the matching build's mapping file or decompiled context; mappings from another APK are not evidence. Fix app-owned vulnerabilities and use supported, SDK-compatible dependency fixes. Document unresolved library findings and reasons for retaining them.

Protect secrets, tokens, logs, URLs, WebViews, local files, SQL inputs, and cryptography according to the actual data path. Firebase client configuration and native symbol strings are not automatically private credentials. Static matches are not proof of exploitability; equally, a possible false positive does not authorize suppressing it.

Never modify scanner rules, add suppressions, exclude code from analysis, remove required analytics/security features, or manufacture secure findings to reach the threshold. Keep scan and production security settings equivalent.

## Build, scan, and report evidence

- Respect verification permissions. Lint/typecheck, APK analysis, automated tests, and device/UI QA are separate activities. Do not infer permission for all of them from this skill.
- Prefer an existing production-derived release APK profile with explicit EAS environment, `developmentClient: false` when applicable, and bundled JS. An AAB or debug APK is not interchangeable evidence. Local EAS builds still resolve EAS environments and require a toolchain and signing credentials; shell environment prefixes alone do not pin profile/server variables.
- If authorized, build a newly signed APK, inspect its manifest/permissions/signature, and scan it using an authorized local MobSF instance. Confirm no findings are suppressed. Keep API keys out of arguments, logs, and committed files.
- Save the raw report and scorecard outside the skill repository. Run `python3 scripts/record_evidence.py --help` for the evidence helper. It verifies the scorecard MD5 and report MD5/SHA-256 against the APK before evaluating the threshold; it does not run a scan or establish device behavior.
- Iterate up to three completed build/scan cycles per request unless the user sets another budget. Stop sooner on a concrete blocker or when the threshold is met and reviewed findings are addressed. Do not keep rebuilding an unchanged artifact or promise a guaranteed score.
- Hand off the measured score, APK path/hash, scanner version, applied changes, remaining risks, verification performed/omitted, and device acceptance checklist. If below target or not scanned, say so clearly. Never publish app reports, binaries, signing material, or suspected secrets with the skill.
