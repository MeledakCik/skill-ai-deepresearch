# Trigger tests

Use these to check that the right skill activates (and that none activates when it should not).
Run each prompt in a fresh chat and note which skill loaded. Target: >= 9 of 10 correct per skill.

| Prompt | Expected skill |
|:---|:---|
| deep research: dampak QRIS terhadap UMKM di Jawa Barat 2024-2026 | deep-research-council |
| Tolong cek apakah klaim "ekspor nikel naik 40%" itu benar, kasih sumber | deep-research-council |
| Bandingkan 3 platform toko online untuk UMKM, mana yang paling murah biaya transaksinya | deep-research-council |
| Buatkan landing page aplikasi kasir yang tidak kelihatan seperti template AI | web-ui-design |
| Perbaiki kontras dan aksesibilitas halaman login ini | web-ui-design |
| Buat komponen antrean bengkel sendiri dengan transisi buka-tutup yang bisa dibalik di tengah animasi | ui-component-motion |
| Rancang microinteraction untuk melepas filter dengan keyboard dan mode minim gerak | ui-component-motion |
| Tulis ulang email ini supaya tidak terdengar seperti ChatGPT | natural-writing |
| Rapikan caption Instagram ini biar natural | natural-writing |
| Bantu susun Bab II skripsi tentang sistem rekomendasi | academic-writing |
| Review metodologi tesis saya, cari kelemahannya seperti penguji | academic-writing |
| Buat project baru Next.js + Postgres lengkap dengan CI | project-scaffolding |
| Siapkan Terraform untuk deploy ke GCP region Jakarta | infrastructure-iac |
| Review plan Terraform ini sebelum apply ke production | infrastructure-iac |
| Refactor layar Compose ini ke MVI | android-compose |
| Audit plugin ini, aman tidak untuk diinstal? | skill-security-audit |
| Buat shot list video iklan 15 detik untuk Dreamina | ai-video-production |
| Kenapa sesi Claude Code saya boros token? | token-efficiency |
| Padatkan konteks riset panjang tanpa kehilangan asal data atau bukti yang membantah | token-efficiency |
| Kuota mingguan hampir habis. Simpan bagian yang sudah teruji supaya bisa lanjut besok | usage-limit-recovery |
| Sesi gratis terputus waktu menyimpan. Lanjutkan dari checkpoint, cek dulu apakah penulisannya berhasil | usage-limit-recovery |

## Should NOT trigger any skill

| Prompt | Why |
|:---|:---|
| Ibu kota Prancis apa? | Simple fact |
| Terjemahkan "selamat pagi" ke bahasa Inggris | Translation |
| Fix typo di fungsi ini | Small code edit |
| Tambah pesan validasi bila judul artikel melebihi limit 80 karakter | Ordinary form validation |
| Hai, apa kabar? | Chat |

## Results log

| Date | Version | Tester | Score | Notes |
|:---|:---|:---|:---|:---|
| 2026-11-19 | 17.0.0 | Claude Haiku (routing only, all real skills visible incl. built-ins) | 24/24 | 16 expected skills, 4 "none", 4 extra prompts routed sensibly (investor market report -> deep-research-council; slides -> pptx) |
| 2026-11-19 | 17.0.0 | Claude Sonnet (same) | 24/24 | Same choices as Haiku |

Quality runs (2026-11-19, Sonnet): natural-writing caption rewrite passed (no invented facts, assumption flagged); deep-research-council Quick tier on "tarif PPN per November 2026" passed with 3 opened sources (2 T1), gaps reported. Gaps found in the skill text were fixed in 17.1.0.

## Offline behavior checks

- **Design.** Build a mobile booking list whose vehicle details expand inline. Verify that reservation times remain visible, rows operate independently, rapid reversal settles correctly, keyboard focus survives and the same result is available with reduced motion.
- **Research on a budget.** Give the researcher a pilot report, a press release quoting it and a registry with a different denominator. Ask for a decision in 140 words. Check origin count, locator, comparability and the condition that would change the conclusion after compaction.
- **Quota.** Simulate a weekly cutoff with one verified result and an uncertain write. Preserve both, resume from the saved snapshot and reconcile the receipt before any replay. Check the installed helper with `python -B -m unittest discover -s evals`.

Observed in local trials for 17.2.0 (2026-11-21):

- Workshop bookings in headless Chromium at 320, 390 and 1024 px kept all reservation times in position with two vehicles expanded. Enter/Space, rapid reversal, focus, reduced motion and empty states passed.
- The closed-packet research trial distinguished a 50% drop in the pilot median from a 6.7% drop in the network mean, traced the press bulletin back to the pilot, and identified staffing as a competing explanation. The trial led to an explicit closed-packet rule for recency checks.
- In a simulated weekly cutoff, the queue page reopened and the saved receipt resolved the timed-out notification without replay. The helper now accepts a terminal checkpoint with verified evidence and no remaining action.
