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
| Susun tiga wireframe untuk reservasi klinik di HP, pilih salah satu, lalu uji saat slot pilihan sudah terisi | web-ui-design |
| Rancang workspace desktop untuk mencocokkan pembayaran rupiah dan meninjau selisih | web-ui-design |
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

- **Advanced design research.** Given a 390 px viewport and a dense paragraph, compare a fixed desktop margin with an adaptive grid; verify ordinary text before rounding its contrast and distinguish text-spacing overrides from author defaults. For a revenue dashboard with ties, zero and a missing branch, derive the recorded subtotal, choose an encoding for a named task and trace failure and recovery. Record source-backed claims separately from proposed user tests.
- **Visual direction and flow.** With one supplied timetable and no testimonials, compare three grayscale booking directions. Look for a real difference in the user's first decision and a revision prompted by an unavailable slot. The landing page must use evidence from the brief, the phone must retain the user's work after a conflict, and the desktop must support comparison when a row is selected. Verify sample labels, keyboard recovery and long names.
- **Design.** Build a mobile booking list whose vehicle details expand inline. Verify that reservation times remain visible, rows operate independently, rapid reversal settles correctly, keyboard focus survives and the same result is available with reduced motion.
- **Research on a budget.** Give the researcher a pilot report, a press release quoting it and a registry with a different denominator. Ask for a decision in 140 words. Check origin count, locator, comparability and the condition that would change the conclusion after compaction.
- **Quota.** Simulate a weekly cutoff with one verified result and an uncertain write. Preserve both, resume from the saved snapshot and reconcile the receipt before any replay. Check the installed helper with `python -B -m unittest discover -s evals`.

In 17.3.0, two independent offline concept walkthroughs exercised Part F. A mobile booking conflict left both supplied slots full and the revised design retained the entered name. A printmaking landing page distinguished class capacity from remaining seats and proposed mobile crops from the photo descriptions. Neither walkthrough rendered an interface or inspected the actual photos.

In 17.4.0, two offline forward tests used previously unseen briefs. The dashboard handoff reported Rp 1.195.000 from four reporting branches, preserved a zero and a tie, identified the missing branch, and withheld the day-over-day change because coverage differed. The refund-flow handoff treated the cashier's complaint as an observation, proposed a placement comparison and left gaze and task outcomes unmeasured.

The U1 CSS example was rendered in Chromium at 320, 390, 1024 and 1440 CSS px. The 390 px grid had four 77.5 px tracks. The 1440 px grid had twelve 78 px tracks. The sample heading, paragraph and button remained visible with the text-spacing overrides applied. All four documented contrast ratios were independently recalculated from the specified sRGB values.

Observed in local trials for 17.2.0 (2026-11-21):

- Workshop bookings in headless Chromium at 320, 390 and 1024 px kept all reservation times in position with two vehicles expanded. Enter/Space, rapid reversal, focus, reduced motion and empty states passed.
- The closed-packet research trial distinguished a 50% drop in the pilot median from a 6.7% drop in the network mean, traced the press bulletin back to the pilot, and identified staffing as a competing explanation. The trial led to an explicit closed-packet rule for recency checks.
- In a simulated weekly cutoff, the queue page reopened and the saved receipt resolved the timed-out notification without replay. The helper now accepts a terminal checkpoint with verified evidence and no remaining action.
