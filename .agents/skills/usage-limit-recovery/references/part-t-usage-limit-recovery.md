# PART T — USAGE LIMIT RECOVERY

Use host-provided signals when available. Context capacity, short-lived request throttling and a session or weekly allowance describe different constraints. A free plan alone gives no evidence of remaining calls. Save milestones early enough that an abrupt cutoff leaves the previous useful result intact.

| Situation | Response while execution is available |
|:---|:---|
| Early warning, long task, or unknown remaining budget | Pick one user-visible slice and its acceptance check. Leave time for that check. Save a concise handoff before starting the next costly unit. |
| Context too large | Compact the task to the handoff and the exact code or evidence locators. Resume in the available context. |
| Explicit temporary rate limit | If a safe retry fits the available time, respect the provider delay, back off and try once. Inspect the actual state of any interrupted write before deciding to replay it. Stop if throttling persists. |
| Exhausted allowance, unaffordable wait or ambiguous limit response | Stop using the affected service. Deliver the saved work and any available offline checks. Quote a reset time only if supplied. |

A 429 response may include a retry delay. Its status code alone does not identify the user's quota window. [RFC 6585 §4](https://www.rfc-editor.org/rfc/rfc6585#section-4)

**Leave a runnable slice.** Before a multi-file change, check the existing entry point if feasible. Integrate coupled edits together, such as a component and the route that imports it. Check that route and the user action before recording the milestone. If the remaining work would expose an unfinished control, keep the last functioning flow available. If the check fails, record the failure and the last known working artifact. A checkpoint records progress and evidence; the runnable files themselves must also be saved.

**File-capable host.** Keep the snapshot with the task's working notes. The optional helper uses Python 3.8+ and the standard library. The example runs from the plugin repository root. In another project use the helper's installed path and a dedicated checkpoint in the working project. Give one writer ownership of that path. Save the complete current snapshot on each call, repeating an option for multiple entries. Keep secrets and raw transcripts out of the note.

```text
python skills/usage-limit-recovery/scripts/checkpoint.py save ./task-notes/repair-queue.json --goal "Repair queue UI" --verified "Queue opens and the selected row expands by keyboard in the preview" --pending "Add retry for a failed notes request" --unverified "Offline behavior on mobile" --next "Simulate one notes request failure on the preview route"
python skills/usage-limit-recovery/scripts/checkpoint.py read ./task-notes/repair-queue.json
```

The example illustrates a check that has already passed. Record the actual check and artifact path or source locator from the run. When all requested outcomes have passed, save the verified evidence with `--complete` in place of `--next`. This requires verified work and empty pending and unverified lists. The helper replaces a complete snapshot in one filesystem operation. If saving fails, keep the last readable snapshot and include the current handoff in the response. In a chat-only host, deliver those fields as text in the same message as each usable milestone. Once a host blocks execution, recovery starts with the last successfully saved file or delivered message.

**Resume.** Compare the note with the current artifact. For an uncertain side effect, inspect the destination or receipt first. For code, rerun the entry point affected by intervening edits. For research, reopen the source behind any decisive claim that may have changed. Continue with the first pending check. Show exactly what works, what remains untested and the next action.
