# Finding triage and release scanning

## Read evidence before changing dependencies

Use the full static report, decompiled source, manifest, and (when available) the exact build's R8 mapping. Keep a compact ledger: finding/rule, source location, owning package/version, actual data flow, remediation, and remaining limitation.

- **CBC/weak hashes/random:** distinguish application encryption or security tokens from platform capability probes, image/cache identifiers, and non-security randomness. AndroidX Biometric can include an AES/CBC capability probe; inspect context before calling it an app data-encryption vulnerability. Do not patch vendor crypto or remove secure storage just to silence it.
- **WebViews:** identify whether the app uses an embedded browser or Expo DOM component and whether untrusted URLs, JavaScript, bridges, or file URLs reach it. Fix app-owned unsafe settings; do not change unrelated external-browser auth behavior. A bundled module can produce a static warning even without an app call site.
- **Exported components:** verify intent purpose and the protection level where the permission is actually defined. Android framework permissions such as `DUMP` can be privileged. Do not disable launch/deep-link, Google services, or AndroidX components solely because MobSF cannot resolve an external permission.
- **Possible secrets:** inspect privately. Distinguish genuine private credentials from Firebase public client identifiers, native C++ symbol names, protocol constants, and sample/test literals. Rotate exposed real credentials through the owner's normal process; removing a source literal does not revoke it. Never print secret values in terminal output or PRs.
- **Storage/SQL/temp/logging:** trace actual sensitive data and input. Keep secrets out of unencrypted preferences, logs, public storage, and transient files. Parameterize user input in SQL. An API match in dependency code does not establish an app-owned injection path.
- **Trackers:** preserve requested analytics and document collection/disclosure. Disable unused advertising permissions/identifiers with supported settings. A retained analytics SDK may remain a scoring penalty.
- **Secure findings:** pinning/root-detection API matches in a library are not proof the app's network path uses pinning or enforces root policy. Do not claim those behaviors without evidence.

## Local scan sequence

Use the authorized instance's `/api_docs` and installed version as the source of truth. Common MobSF REST endpoints are:

1. `POST /api/v1/upload` with multipart `file`; save its returned `hash`.
2. `POST /api/v1/scan` with `hash`; handle asynchronous scanning according to that instance's documented task/status API.
3. `POST /api/v1/report_json` and `POST /api/v1/scorecard` with `hash`; save both JSON responses verbatim to a private local directory.
4. Check `/api/v1/list_suppressions` where supported, including package-wide suppression state. Report a suppressed baseline separately; never count it as an unmodified passing scan.

Use the `Authorization` header per the local docs. Load its API key from a protected environment or secret store; never put it in a command argument, committed file, URL, evidence summary, or logs. Do not send an app to `mobsf.live`, VirusTotal, or another hosted service without explicit authorization for that destination. Review optional scanner integrations before uploading sensitive binaries.

Record the scanner version and image digest/commit where practical. Save raw JSON even when below target, then use:

```sh
python3 /path/to/expo-mobsf/scripts/record_evidence.py \
  --apk /private/path/app.apk \
  --report /private/path/report.json \
  --scorecard /private/path/scorecard.json \
  --mobsf-version 'version-from-local-instance' \
  --changes-file /private/path/changes.txt \
  --output /private/path/evidence.json
```

The helper exits 0 at/above the threshold, 1 below it, and 2 for invalid/mismatched inputs. It hashes the APK, requires matching identifiers in both JSON artifacts, records findings, and copies the raw inputs into the new evidence bundle. It refuses to overwrite an existing bundle. Review suppression state separately; the helper does not attest to scanner integrity, scan freshness, signing, or device behavior. Its MD5 is only MobSF's artifact identifier; SHA-256 is also recorded.

MobSF scores depend on the installed scanner's rule set and bundled libraries. Do not extrapolate a new score from removed warnings; measure the rebuilt artifact. A score above 70 is a threshold result, not a security certification. If the threshold remains unmet after the agreed iteration budget, report the actual score and the concrete unresolved findings.

Source: [MobSF official repository and API implementation](https://github.com/MobSF/Mobile-Security-Framework-MobSF).
