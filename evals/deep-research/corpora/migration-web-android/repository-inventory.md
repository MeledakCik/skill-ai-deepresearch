# Repository inventory (fictional)

## §1 Components

The supplied inventory describes a React single-page web client, a Node API service, and PostgreSQL. The client has nine route-level screens. The `receiving` route owns form state in the browser component. No Android project, mobile build pipeline, device-management package, or shared client-domain module appears in the supplied inventory. The inventory does not establish that none exists outside the reviewed repository.

## §2 Identity and release

The web client uses a same-site secure session cookie and a CSRF token. The only documented sign-in flow is for the browser client. No mobile token flow, device enrollment flow, or Android release automation is documented. Managed Play distribution is a sponsor requirement; current account and review details are not in the packet.

## §3 Verification limits

The inventory lists source directories and package manifests but contains no dependency graph, runtime trace, test report, supported-browser matrix, or measured migration estimate. The nine-screen count is not a work breakdown.
