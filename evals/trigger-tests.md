# Trigger tests

Use these to check that the right skill activates (and that none activates when it should not).
Run each prompt in a fresh chat and note which skill loaded. Target: >= 9 of 10 correct per skill.

| Prompt | Expected skill |
|:---|:---|
| deep research: dampak QRIS terhadap UMKM di Jawa Barat 2024-2026 | deep-research-council |
| Susun protokol systematic review untuk intervensi X dan catat query serta alur screening | deep-research-council |
| Audit paket systematic review ini: cek query log, duplikasi, full text yang hilang, alasan eksklusi dan apakah hasilnya boleh dipool | deep-research-council |
| Buat paket evaluasi deep research yang bilingual, pisahkan closed-packet dari live search, dan definisikan acceptance rule sebelum menilai | deep-research-council |
| Lanjutkan riset dari checkpoint, jangan ulangi sumber yang sudah tuntas, dan verifikasi satu bukti baru yang dapat mengubah keputusan | deep-research-council |
| Sumber resmi mengembalikan 403; cari fallback resmi, pisahkan fakta yang terverifikasi dari yang belum, dan jangan mengutip snippet sebagai isi sumber | deep-research-council |
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
| Rancang unit dan integration test untuk perhitungan ongkir ini tanpa menguji implementasi internal | software-testing |
| Playwright test ini kadang lolos setelah retry; diagnosis trace dan cari sumber flakiness tanpa menyamarkan failure | software-testing |
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

### 17.33.1 cross-host duplicate reads (2026-11-28)

Claude Code 2.1.332 loaded the user-installed plugin in a fresh CLI session. Two sequential Bash calls ran the same simple read of the repository's research skill. The first tool reply contained the complete Markdown. The second contained the 115-character reuse notice, which the model identified in its answer. No provider cache or quota saving was measured.

`python -B -m unittest evals.test_host_cache_guard` exercises separately extracted Claude, Gemini, Copilot and OpenCode packages. The tests check native response shapes, first and repeated reads, and context resets. Gemini and Copilot events are fixtures. OpenCode's registered callbacks run with Node and a local fixture. These checks do not establish live execution in those three clients.

### 17.31.0 screenshot transformation (2026-11-28)

Give an image-capable agent the [mobile reference](design/studio-mobile.png), the generated design skill and U5. Ask in Indonesian for a standalone responsive HTML file that preserves the phone appearance, supports a narrow panel inside a desktop window, and keeps the selection and draft during resize. Withhold the reference HTML, color values and expected desktop composition.

In one Codex CLI trial, Chrome reproduced the visible labels, both sessions, selected Studio Barat, the existing note and one save action. The source and reconstruction measured 390 × 795 px. Both used a navy header, warm canvas and green selected/action roles. The rendered action fill was RGB (23, 94, 85) against (26, 98, 87) in the reference. The button started 8 px lower. Light and dark browser preferences produced identical renders of this single supplied theme.

The [desktop render](design/studio-desktop-trial.png) paired the session list with its summary and editor. The same live form changed from one column at 639 CSS px of content width to two at 640 and 641 px. In a 1440 px viewport it returned to one column in a 360 px panel. After selecting Studio Timur and changing the note, the value, selection, keyboard focus and single reachable save action survived widening and narrowing. Neither the document nor the inspected form regions overflowed horizontally, including at a 320 px viewport. This trial covered Chromium web layout. Native platform behavior and a user-specified desktop design would need their own checks.

### 17.30.0 context and answer scope (2026-11-28)

Four separate Codex CLI sessions received the generated research skill and an Indonesian prompt. Web search was disabled. Results below describe those runs.

| Prompt condition | Observed output |
|:---|:---|
| Budget corrected from Rp900.000 to Rp700.000. Choose between A at Rp575.000 with CSV and B at Rp825.000 with offline sync. Give the choice, remainder, offline risk and a test in three points. | Chose A, calculated Rp125.000 remaining, identified offline support as unknown and described an offline edit/reconnect check. Three points. |
| “Riset yang terbaik buat proyek ini, ya. Hasil risetnya akan menentukan pembelian.” No project or purchase identified. | Asked what the user wanted to buy and for which project in a single sentence. |
| Require 90-day retention and a Rp500.000 ceiling. N offers 30 days at Rp450.000 and P offers 90 days at Rp640.000. Give verdict, price gap and the decision needed in two sentences. | Identified the conflict, calculated the Rp140.000 gap and named which constraint each option would require relaxing. Two sentences. |
| “Perdalam yang tadi.” The preceding note compared moving the Pay button with changing the logo color. Twelve of twenty customers waited while cashiers searched for the button. Ask for one priority and a way to evaluate it in two points. | Prioritized moving the button and proposed comparing the number delayed with the 12/20 baseline. Two points. |

### 17.29.0 adaptive shipment row and map panel (2026-11-28)

Headless Chrome 152 rendered the HTML and CSS from U4 at slot widths of 288, 320, 390, 527, 528, 529 and 640 CSS px, each with a root size of 16 and 32 px. The same focused link remained active across all 14 resizes. The row stayed inside its slot and its column count matched the 33rem rule in every case. At a 16 px root, the switch occurred at 528 px.

In a separate panel swatch on a uniform black backdrop, an 8 px backdrop blur with a 35% white fill produced RGB (89, 89, 89) at its center. A 60% fill produced (153, 153, 153). For opaque #202020 text these sampled backgrounds give 2.33:1 and 5.72:1 respectively. The fixture measures layout and composite color. User task performance, real map crops and device frame times require their own observations.

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
- **Software testing.** Provide a deterministic calculation with boundary cases and a browser flow with an intermittent failure. The skill should choose distinct test levels, reuse the existing runner, inspect first-failure evidence, report a retry-pass as flaky, and not run the suite unless the user or repo instructions authorize it.

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
