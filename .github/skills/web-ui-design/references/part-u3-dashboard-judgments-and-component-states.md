## U3. Dashboard judgments and component states

### Choose an encoding from the decision

| User question | Starting representation | What to verify |
|:---|:---|:---|
| “Berapa omzet hari ini?” | Prominent currency amount with date, scope, coverage and last refresh | Check aggregation, refunds, missing feeds and timezone before calling it a total. |
| “Cabang mana paling tinggi?” | Sorted horizontal bars with a shared zero baseline and direct values | Preserve units and ties. Use one neutral series with one meaningful highlight. |
| “Kapan omzet mulai turun?” | A time-ordered line with units and an explicit gap for missing periods | Compare like periods. Distinguish zero sales from a missing observation. |
| “Berapa bagian tiap kanal?” | A labeled part-to-whole chart for a few positive, exhaustive shares with the same denominator | For more than four categories or close shares, try sorted bars. A signed amount or incomplete denominator changes the question. |
| “Transaksi mana yang harus saya cek?” | A table with a useful initial sort and row detail | Align text to the reading start and comparable amounts to the right. Use tabular numerals, header units and subtle row separation. Test whether striping helps track a wide row. |

Heer and Bostock asked people to estimate proportions using different encodings. In Experiment 1A, judgments using position on a common scale were more accurate than angle judgments. This supports aligned bars for close comparisons. The experiment tested perceptual judgments, so whether a dashboard helps a clerk resolve a discrepancy still needs a task check. For exact currency values, provide labels or a table that also works by keyboard. [Heer & Bostock, Experiment 1A](https://vis.stanford.edu/files/2010-MTurk-CHI.pdf) · [GOV.UK table guidance](https://design-system.service.gov.uk/components/table/)

**Worked fixture.** Five branches should report today's revenue in rupiah. A reports 180,000, B 160,000, C 160,000, D 0, and E has yet to report. Display “Omzet tercatat Rp 500.000 · 4 dari 5 cabang”. Keep D visible as zero and E as “Belum masuk”. Highlight the missing feed if the operator's job is to chase it. A comparison of B and C must show a tie. A previous complete day is an unsuitable baseline for a headline percent change until coverage and cutoffs match. If the operator asks for the full network total, state that it is pending.

### Define variants, transitions and recovery

Specify the emphasis and action state independently so a destructive button can be busy and a secondary button can receive keyboard focus. Exercise a representative instance of each relevant state in the component and again in the real flow.

| Element | State and visible treatment | Behavioral check |
|:---|:---|:---|
| Button | Primary commits, secondary offers an alternative, ghost keeps a routine action quiet, danger names the consequence. Cover default, hover, pressed, focus-visible, disabled and loading. | Trigger by keyboard, try repeated activation while busy and check one submission. Keep dimensions stable. Explain blocked actions next to the control. |
| Input | Persistent label with an optional placeholder, empty, filled, focused, invalid, confirmed when useful, and disabled. Error needs a message as well as color. | Associate the message with the field. On failed submission retain the value and move focus where the person can correct it. Confirmed state must reflect the actual validation performed. |
| Result or collection | First load, refresh with prior data, first-use empty, no filter matches, success, recoverable failure. | During a known layout's first load, reserve its shape with a skeleton. For a pending save use inline status; for measurable progress use a progress indicator. On refresh keep the previous result and its timestamp until replaced. |

Once a request settles, end the busy state. “Belum ada transaksi” follows a successful empty response. “Tidak ada yang cocok” can offer “Hapus filter”. A network error can offer “Muat ulang” with the filters intact. Show progress without flashing and honor reduced motion. Expose changing status in the accessibility tree when focus stays put. Test a fast response, a delayed response, failure and retry. A compact spinner with a meaningful label can suit an indeterminate operation whose final shape is unknown. [Carbon loading pattern](https://www.carbondesignsystem.com/building-blocks/core/patterns/loading) · [W3C status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
