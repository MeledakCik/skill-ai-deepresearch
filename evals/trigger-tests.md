# Trigger tests

Use these to check that the right skill activates (and that none activates when it should not).
Run each prompt in a fresh chat and note which skill loaded. Target: >= 9 of 10 correct per skill.

| Prompt | Expected skill |
|:---|:---|
| deep research: dampak QRIS terhadap UMKM di Jawa Barat 2024-2026 | deep-research-council |
| Susun protokol systematic review untuk intervensi X dan catat query serta alur screening | deep-research-council |
| Buat paket evaluasi deep research yang bilingual, pisahkan closed-packet dari live search, dan definisikan acceptance rule sebelum menilai | deep-research-council |
| Audit laporan riset multi-file ini: cek locator PDF/tabel, dokumen pengalih, asal sumber duplikat, dan sitasi untuk setiap klaim material | deep-research-council |
| Jalankan CP-ID-01 dari evals/deep-research; jangan baca rubrik tersembunyinya sebelum jawaban selesai | deep-research-council |
| Bandingkan hasil tiga studi ini, cek beda populasi dan heterogenitas sebelum pooling | research-data-analysis |
| Analisis CSV berikut. Periksa missing value, duplikasi dan conversion per cohort dengan interval kepercayaan | research-data-analysis |
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
| Threat-model API penyewaan ini dan review akses objek lintas tenant dalam kode lokal | application-security |
| Periksa implementasi autentikasi dan sesi web ini dengan kontrol OWASP yang sesuai | application-security |
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
- **Formal review gate.** Give the researcher a narrowly scoped web search, a broad database protocol request and an inaccessible full-text study. It must label the first as a scoped search, form a dated protocol for the second and disclose the third as unavailable. It must not claim a completed systematic review from the partial search.
- **Research quality evaluation.** Provide a report where a real source is cited but does not support a pivotal number. Grade citation entailment separately from report style and coverage. The unsupported pivotal claim blocks a passing result even if the prose is strong.
- **Deep-research regression protocol.** Provide a dated bilingual task pack with a closed multi-file corpus containing relevant evidence, a duplicate-origin article, a distractor table and one inaccessible source, plus a separate live-search task. Ask for a small before/after evaluation plan. It must record model/tool/skill versions and date, use exact page/table locators, state metric denominators, keep critical citation failures separate from presentation, and label live-search source discovery as task-level rather than global recall. Human review must be blind to version on the sampled reports; no universal score threshold or significance claim is invented.
- **Research data analysis.** Provide a small table with a duplicate row, a missing feed, a true zero, uneven denominators and a before/after association. The analysis must reconcile totals, distinguish missing from zero, report the comparison units and limitations, and avoid a causal claim without an identifying design.
- **Application security.** Provide local web/API code with a cross-tenant object-authorization flaw and a nearby clean path. The review must trace the reachable server-side check, show a safe local regression test and avoid probing external endpoints or printing credentials.

In 17.3.0, two independent offline concept walkthroughs exercised Part F. A mobile booking conflict left both supplied slots full and the revised design retained the entered name. A printmaking landing page distinguished class capacity from remaining seats and proposed mobile crops from the photo descriptions. Neither walkthrough rendered an interface or inspected the actual photos.

In 17.4.0, two offline forward tests used previously unseen briefs. The dashboard handoff reported Rp 1.195.000 from four reporting branches, preserved a zero and a tie, identified the missing branch, and withheld the day-over-day change because coverage differed. The refund-flow handoff treated the cashier's complaint as an observation, proposed a placement comparison and left gaze and task outcomes unmeasured.

The U1 CSS example was rendered in Chromium at 320, 390, 1024 and 1440 CSS px. The 390 px grid had four 77.5 px tracks. The 1440 px grid had twelve 78 px tracks. The sample heading, paragraph and button remained visible with the text-spacing overrides applied. All four documented contrast ratios were independently recalculated from the specified sRGB values.

### 17.5.0 design trials in Chromium (2026-11-21)

- **Checkout Patch.** A local checkout with a long Indonesian shipping label, Rp 1.250.000.000 total, missing product image and invisible focus produced 671 px of document width at a 390 px viewport. After repair, screenshots at 390 × 844 and 1440 × 900 in both themes showed the full amount and payment action with zero page overflow. Tab, Shift+Tab, Space and Enter exercised details, payment and focus restoration. Aborting the repaired image request displayed a fallback and checkout still worked.
- **Gradient and glass.** The two F2.5 palettes used the same 115-degree axis and stops at 0%, 58% and 100%. At 390 and 1440 px the lowest sampled contrast under three label rectangles was 6.75:1 cool and 7.91:1 warm. White text over a white middle between dark ends reached 1.00:1. Over black and white backdrops, the lowest text contrasts on the frosted panel were 11.85:1 light and 10.75:1 dark. Emulating reduced transparency activated the solid panel (14.19:1 light, 13.70:1 dark). Measurements used background pixels from a second render with the text hidden and layout preserved. Other crops and imagery require fresh checks.
- **Canvas.** Five actual tab round trips produced ten visibility transitions, zero frames scheduled while hidden and at most one on return. A manual pause and emulated reduced motion survived the switch. Startup with WebGL disabled kept the poster and HTML controls usable. Two extension-induced context losses and restores rebuilt the software WebGL scene and retained the selection changed through the fallback. These fixtures did not measure physical GPU performance or test a screen reader.

Observed in local trials for 17.2.0 (2026-11-21):

- Workshop bookings in headless Chromium at 320, 390 and 1024 px kept all reservation times in position with two vehicles expanded. Enter/Space, rapid reversal, focus, reduced motion and empty states passed.
- The closed-packet research trial distinguished a 50% drop in the pilot median from a 6.7% drop in the network mean, traced the press bulletin back to the pilot, and identified staffing as a competing explanation. The trial led to an explicit closed-packet rule for recency checks.
- In a simulated weekly cutoff, the queue page reopened and the saved receipt resolved the timed-out notification without replay. The helper now accepts a terminal checkpoint with verified evidence and no remaining action.
