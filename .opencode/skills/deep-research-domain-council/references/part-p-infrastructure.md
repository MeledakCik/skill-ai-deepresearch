# PART P — INFRASTRUCTURE (Claude Opus 5.5 max + Claude Fable 5.2 max)

Infrastructure mistakes are the most expensive kind: outages, data loss, security holes, surprise bills. So infra work uses two strong models in **author/reviewer** roles, and nothing touches production without a plan, a review and a human approval.

## P1. Model Roles

| Role | Model | Effort | Why |
|:---|:---|:---|:---|
| **Author** (IaC, pipelines, configs, runbooks) | Claude Opus 5.5 | max for architecture, migrations, incident analysis; xhigh/high for routine changes | Anthropic's recommended default for long-running agentic coding; strong agentic-coding scores at lower cost than Fable |
| **Reviewer / red team** | Claude Fable 5.2 | max for production designs, migrations, DR plans, security-sensitive changes | For demanding reasoning and long-horizon work; an independent model catches what the author normalized |
| **Routine edits** (one resource, a version bump) | Opus 5.5 at medium | medium | Max here is cost without benefit |

**Cost discipline:** Fable 5.2 at max costs several times more per task than at high, and its *high* setting already matches Opus 5.5 *max* on Anthropic's coding sweep. Use max on both only where a mistake would cost more than the tokens: production architecture, data migrations, DR, security boundaries, incidents. Log the effort used in the change record.

**Safety note (⚠ verify):** Anthropic applies extra safeguards to some cyber-security requests on its frontier models. Defensive infra hardening is normal work; if a request is refused, rephrase it to its defensive purpose rather than looking for workarounds.

## P2. Infrastructure Principles

1. **Everything as code:** Terraform/OpenTofu, Pulumi, CloudFormation/Bicep; Kubernetes manifests via Helm/Kustomize; pipelines in repo. No click-ops in prod.
2. **Plan before apply:** every change has a reviewed plan/diff; state is remote, locked, versioned, encrypted.
3. **Least privilege:** scoped IAM roles, short-lived credentials (OIDC from CI), no long-lived keys, no wildcard permissions without justification.
4. **Secrets in a secret manager** (Vault, AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, SOPS); never in code, images, or logs.
5. **Environments parity:** dev/staging/prod from the same modules with different variables.
6. **Immutable deploys:** build once, promote the same artifact (image digest), roll back by redeploying the previous digest.
7. **Observability first:** logs, metrics, traces; golden signals (latency, traffic, errors, saturation); SLOs with alerting on burn rate.
8. **Backups are only real if restore is tested:** scheduled restore drills; documented RPO/RTO.
9. **Blast-radius control:** separate accounts/projects per environment; resource limits; feature flags; canary/blue-green.
10. **Cost is a requirement:** budgets and alerts, tagging, right-sizing, autoscaling bounds, lifecycle rules for storage.

## P3. Infra Workflow (Author ↔ Reviewer)

```
Requirements & SLOs → Capacity estimate → Architecture + threat model (Opus)
→ Design review (Fable) → IaC + pipeline (Opus) → plan/diff
→ Plan review (Fable) → Human approval → Apply to dev → staging
→ Verify (tests, SLO checks) → Human approval → Prod (canary) → Verify → Runbook + postmortem notes
```

**Capacity estimate (always with numbers):** peak RPS (λ), target latency (W), concurrency $L = \lambda W$; storage growth per month; egress; then instance counts with headroom (utilization target 50-70%).

**Threat model (STRIDE per component):** entry points, trust boundaries, data classification, secrets flow, who can change what.

## P4. Reviewer Checklist (Fable 5.2)

| Area | Questions |
|:---|:---|
| Correctness | Does the plan diff match the intent? Any unexpected destroy/replace? |
| Security | Public exposure (0.0.0.0/0, public buckets)? Encryption at rest/in transit? IAM wildcards? Secrets handling? |
| Reliability | Single points of failure? Health checks, readiness/liveness, PodDisruptionBudgets, multi-AZ? Timeouts/retries/circuit breakers? |
| Data | Backups, retention, migration reversibility, point-in-time recovery? |
| Rollback | Exact rollback steps and time to roll back? |
| Observability | Will we know within minutes if this breaks? Which alert fires? |
| Cost | Monthly estimate and the biggest line item; any unbounded autoscaling or egress? |
| Compliance | Data residency (e.g., Indonesian PDP Law requirements ⚠ verify), audit logs, retention rules |

Output format: findings with severity (blocker/major/minor), evidence (file/line or plan resource), and fix.

## P5. Hard Safety Rules for Agents Doing Infra

- **No `apply`, `destroy`, `delete`, `drop`, `kubectl delete`, `helm uninstall`, force-push, or DNS change on staging/prod without explicit human approval in the conversation.** Dry-run/plan is always allowed.
- Never disable state locking, deletion protection, backups, or audit logging to "make it work".
- Never print secrets; redact in logs and outputs.
- Use the least-privileged credentials available for each step; never escalate on your own.
- Change windows and freeze periods set by the team are respected.

## P6. Infra Error Handling (Extends Part N)

| Situation | Response |
|:---|:---|
| Plan shows unexpected replace/destroy | Stop. Explain which attribute forces replacement; propose `lifecycle`/`moved` blocks or a migration plan |
| Apply failed midway (partial state) | Do not re-run blindly. Refresh state, read what was created, decide fix-forward vs rollback, document |
| State lock held | Find the holder (CI run, teammate). Never force-unlock without confirming nothing is running |
| Drift detected | Report the diff; decide whether code or reality is correct; never overwrite manual hotfixes silently |
| Deploy unhealthy | Automatic rollback to last good digest; then investigate with logs/traces |
| Quota/permission errors | Report the exact missing permission or quota; do not widen IAM broadly to get past it |

## P7. Deliverables for Any Infra Change

1. Design note (problem, architecture diagram description, capacity numbers, threat model summary).
2. IaC + pipeline code with README.
3. Plan output summary (resources added/changed/destroyed).
4. Reviewer findings and how each was resolved.
5. Rollback plan with commands.
6. Runbook: how to operate, alerts and what to do when each fires.
7. Cost estimate with assumptions.
