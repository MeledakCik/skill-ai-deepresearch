# Android repository inventory (fictional)

## §1 Client and user roles

The Android client uses Kotlin, Jetpack Compose, and Room. It is installed on managed Android 11+ devices. The field workflow includes opening an assigned job, completing an inspection, attaching photos, and submitting the result. The app has no dispatcher scheduling interface in the supplied route inventory.

## §2 Offline state

Room holds cached jobs and a queue of unsent inspections. WorkManager retries synchronization. Technicians may work offline for up to 48 hours. Once the server accepts an inspection, the server is authoritative. The local database is encrypted using device-bound Android Keystore material; the packet provides no export or cross-device restore flow for this database.

## §3 Evidence limits

The inventory has no browser or macOS client, no browser-auth configuration, no macOS-specific integration, and no usability or performance baseline for dispatchers. Absence from this inventory is not proof a capability is impossible.
