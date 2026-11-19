## C6. Skill Security Auditor (`dabit3/skill-audit`) & Cryptographic Vault

**Part A, audit scoring (security starts at 100):**
- CRITICAL (−40): RCE (`eval`, `curl…|sh`, `wget…|bash`), reads of `/etc/passwd`, `~/.ssh`, `.env`; fork bombs.
- HIGH (−25): unsanitized `child_process.exec`/`spawn`, `sudo`, hardcoded keys, remote shell exec.
- MEDIUM (−15): path-traversal writes, unverified downloads (no SHA-256), `chmod 777`.
- LOW (−5): sensitive stdout, missing `set -euo pipefail`.
- Quality (0-100): frontmatter, examples, links, pinned deps, input validation.
- Overall $=0.6\cdot\text{Security}+0.4\cdot\text{Quality}$; grades A-F. Ship ≥80 (B) with 0 CRITICAL/HIGH.

**Part B, vault + exposure scanner:**

```typescript
import crypto from "node:crypto";

// why: salt must be random per deployment and stored alongside config; a constant salt is only safe for high-entropy secrets.
export function deriveKeyHKDF(masterSecret: Buffer, salt: Buffer, context: string): Buffer {
  return Buffer.from(crypto.hkdfSync("sha256", masterSecret, salt, Buffer.from(context), 32));
}

export function encryptVaultGCM(plaintext: string, key: Buffer, aadContext: string) {
  const iv = crypto.randomBytes(12); // why: 96-bit random IV; never reuse an IV with the same key
  const cipher = crypto.createCipheriv("aes-256-gcm", key, iv);
  cipher.setAAD(Buffer.from(aadContext, "utf8"));
  const ciphertext = Buffer.concat([cipher.update(plaintext, "utf8"), cipher.final()]).toString("hex");
  return { iv: iv.toString("hex"), authTag: cipher.getAuthTag().toString("hex"), ciphertext, aadContext };
}

export function decryptVaultGCM(rec: { iv: string; authTag: string; ciphertext: string; aadContext: string }, key: Buffer): string {
  const decipher = crypto.createDecipheriv("aes-256-gcm", key, Buffer.from(rec.iv, "hex"));
  decipher.setAAD(Buffer.from(rec.aadContext, "utf8"));
  decipher.setAuthTag(Buffer.from(rec.authTag, "hex"));
  return Buffer.concat([decipher.update(Buffer.from(rec.ciphertext, "hex")), decipher.final()]).toString("utf8");
}

export function shannonEntropy(str: string): number {
  if (!str) return 0;
  const freq = new Map<string, number>();
  for (const c of str) freq.set(c, (freq.get(c) ?? 0) + 1);
  let h = 0;
  for (const n of freq.values()) { const p = n / str.length; h -= p * Math.log2(p); }
  return Number(h.toFixed(3));
}
```

**Scanner signatures (defensive use on your own assets only):** `/.env`, `/.git/HEAD`, high-entropy strings $H(X) > 4.5$ bits/char, known webshell filenames (`wp2shell`, `php2shell`, `node2shell`, `go2shell`, `py2shell`, `tinyfilemanager.php`, `node-oob`).
