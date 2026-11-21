# API and data contract (fictional)

## §1 Receipt endpoint

`POST /api/v1/receipts` creates a receipt only while the API is reachable. The supplied contract documents no idempotency key or client-generated submission ID. Retry behavior after a request commits but its response is lost has not been tested.

## §2 Data authority

PostgreSQL is the canonical source for stock quantity and accepted receipts. Stock changes only after the server accepts a receipt. The packet describes no local database, pending-write queue, synchronization worker, merge rule, or conflict-resolution policy.

## §3 User state

Receipt form values currently live in the browser component until submission. The packet does not say whether values survive a reload or process restart, how barcode scans are normalized, or how concurrent receipts for one SKU are reconciled. Do not infer those behaviors from the schema name.
