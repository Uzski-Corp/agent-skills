# Persistent Expo Android baseline

Read the project's installed SDK documentation, not the `latest` reference by default. The following example is verified against Expo SDK 58; retain unrelated configuration and adapt to the installed SDK.

```json
{
  "expo": {
    "android": {
      "allowBackup": false,
      "blockedPermissions": [
        "android.permission.RECORD_AUDIO",
        "android.permission.READ_EXTERNAL_STORAGE",
        "android.permission.WRITE_EXTERNAL_STORAGE",
        "android.permission.SYSTEM_ALERT_WINDOW"
      ]
    },
    "plugins": [
      ["expo-build-properties", {
        "android": {"minSdkVersion": 29, "usesCleartextTraffic": false}
      }],
      ["expo-camera", {
        "cameraPermission": "Allow this app to scan product barcodes.",
        "recordAudioAndroid": false
      }]
    ]
  }
}
```

This example assumes barcode scanning only. Add/configure `expo-camera` only when the app uses it. Preserve existing plugin options and deduplicate entries. Retain any higher app, SDK, or library minimum. Do not block audio, media, or overlay permissions when required by actual app features. Check inherited EAS environment and dynamic `app.config` branches; a JSON edit does not establish effective build configuration.

`create-expo-app` has no documented minimum-Android flag as of the SDK 58 documentation. Keep starter aliases intact and apply the baseline after creation. Do not invent a CLI argument or change the template/SDK unnecessarily.

## Permission and native boundaries

- Keep `android.permission.CAMERA` for scanning. The camera plugin's iOS explanation does not replace Android manifest permission or a runtime request.
- Review first grant, retryable denial, permanent denial with Open Settings, foreground permission refresh, camera mount failure, and manual-entry fallback. Preserve scan drafts across recovery.
- `recordAudioAndroid: false` prevents the camera plugin from adding microphone permission. Other packages may add it; inspect the final merged manifest. Use `blockedPermissions` for proven-unused transitive permissions.
- Native permission, SDK, manifest, plugin, and library changes need a fresh native build. Expo Go, OTA delivery, and browser preview cannot validate them.
- Never hand-edit generated `android/` or `ios/`. Apply persistent config, regenerate via Expo tooling, and inspect the resulting release manifest/APK. Do not run destructive clean prebuild over maintained native changes.
- `allowBackup: false` disables Android backup participation but may not prevent all manufacturer device-to-device transfers. Review extraction rules when sensitive data warrants it; retain SecureStore exclusions.
- Keep production HTTPS and system certificate validation. If development needs HTTP, isolate it in an explicit development profile and inspect release output for leaks. Do not add trust-all certificates.

## Release evidence

Use the existing production-derived EAS APK profile, explicit EAS environment, and proper signing credentials. Preserve platform/ABI support. Local EAS builds can retrieve remote environments and credentials; they are not offline builds. Never expose keystore passwords or mislabel a debug-key Gradle release as production-signed.

Inspect the APK with installed Android tools (`apkanalyzer`, `aapt`/`aapt2`, `apksigner`), confirming application ID, min/target SDK, `debuggable`, `allowBackup`, cleartext settings including any network security XML, permissions, exported components, ABIs, and signature. Verify secure-storage and camera plugins remain present.

Sources:
- [Expo documentation index](https://docs.expo.dev/llms.txt)
- [SDK 58 BuildProperties](https://docs.expo.dev/versions/v58.0.0/sdk/build-properties/)
- [SDK 58 app configuration](https://docs.expo.dev/versions/v58.0.0/config/app/)
- [SDK 58 Camera](https://docs.expo.dev/versions/v58.0.0/sdk/camera/)
- [Expo Android permissions](https://docs.expo.dev/guides/permissions/)
- [create-expo-app options](https://docs.expo.dev/more/create-expo/)
- [Android backup behavior](https://developer.android.com/identity/data/autobackup)
