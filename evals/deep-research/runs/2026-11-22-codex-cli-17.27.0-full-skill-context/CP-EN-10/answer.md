Give dispatchers an online browser console for scheduling, assignment and review of synchronized inspections. Keep technicians’ 48-hour offline inspections, photo capture, Room queues and WorkManager retries on managed Android 11+. **Reject the Room copy.** Its encryption keys are device-bound and no export is documented. Let Android sync pending work when connectivity returns. Accepted server records remain authoritative. [MIG-AW-APP §§1–2, MIG-AW-API §2, MIG-AW-OPS §1]

- **Web readiness is unconfirmed.** The release lead should verify supported Chrome and Safari versions, build tools, CI host access and deployment rights. [MIG-AW-OPS §§1–2]
- **Defer native macOS.** No macOS-only need is documented. Minimum OS, SDK, build host and CI access, signing, distribution and release ownership are unconfirmed. [MIG-AW-APP §3, MIG-AW-OPS §1]

**Production feasibility: unresolved. Schedule: conditional.** The six-week, 11-screen proposal is unverified. [MIG-AW-BRIEF §1]

On one staging job, verify sign-in, session renewal and CORS from the intended origin in both browsers. Force a stale `If-Match` PATCH, require `409`, refresh and reapply the assignment without losing the competing edit. Retry one Android inspection with the same `submissionId`. Require exactly one accepted inspection visible in both browsers. Renew an expired 20-minute signed photo URL and verify local retention until upload acknowledgement. Browser file selection and upload renewal remain unverified. [MIG-AW-API §§1–3, MIG-AW-OPS §2]

Pilot with one dispatcher after both browsers pass. Compare completion time with the existing workflow. On any lost edit, duplicate inspection or missing photo, disable the console, resume prior dispatch and reconcile accepted server writes.
