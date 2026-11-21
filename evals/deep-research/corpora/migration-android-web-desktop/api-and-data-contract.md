# API and data contract (fictional)

## §1 Job updates

`GET /v2/jobs` returns the server's job version. `PATCH /v2/jobs/{id}` requires `If-Match`; an older version receives `409 Conflict`. The Android client then refreshes before the user retries. Browser-origin configuration and a browser authentication/session flow are not documented.

## §2 Inspection submission

`POST /v2/inspections` accepts a `submissionId` that makes retries idempotent for the same inspection. An accepted inspection becomes server-authoritative. Client-side validation rules and any web-specific validation behavior are not supplied.

## §3 Attachments

Inspection photos are uploaded through signed URLs valid for 20 minutes. If a URL expires, the client requests a new URL; a local image is retained until the server acknowledges the upload. The packet does not specify browser file permissions, Safari support, or macOS file-system integration.
