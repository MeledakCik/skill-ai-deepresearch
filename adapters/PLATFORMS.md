# Panduan per Platform

Skill ini mengikuti **Agent Skills open standard** (folder berisi `SKILL.md` dengan frontmatter YAML). Platform yang mendukung standar ini membaca skill yang relevan. Untuk aplikasi chat, gunakan adapter lengkap atau lite sesuai anggaran konteks.

| Platform | Dukungan | Cara pasang |
|:---|:---|:---|
| Claude Code | Native | Repo: `.claude/skills/<nama-skill>/` (sudah ada). Global: `scripts/install.*` → `~/.claude/skills/` |
| Claude.ai (web/desktop) | Plugin | Buat arsip plugin dari repo dengan `python scripts/sync.py --zip`, lalu gunakan arsip di direktori induk |
| OpenAI Codex (CLI / IDE) | Native | Skill proyek berada di `.agents/skills/`. Contoh panggilan langsung `$ui-component-motion` dan `$usage-limit-recovery` |
| ChatGPT | Adapter | **Custom GPT:** tempel `adapters/chatgpt/INSTRUCTIONS.md` ke kolom Instructions (di bawah batas 8.000 karakter), lalu upload `SKILL.md` dari skill yang relevan di `skills/` (plus file `references/`-nya) sebagai Knowledge. **Projects:** tempel ke Project instructions dan tambahkan SKILL.md sebagai file |
| Gemini CLI | Native | Repo: `.gemini/skills/` atau `.agents/skills/` (sudah ada). Global: `~/.gemini/skills/`. Cek dengan `/skills list`, muat ulang dengan `/skills reload`. ⚠ Di sebagian versi, fitur skills harus diaktifkan dulu di settings |
| Gemini app (Gems) | Adapter | Buat Gem baru → tempel `adapters/gemini-gem/INSTRUCTIONS.md` → tambahkan `SKILL.md` sebagai file pengetahuan |
| GitHub Copilot | Native + instruksi | Skill dibaca dari `.github/skills/` atau `.claude/skills/`; `.github/copilot-instructions.md` mengarahkan ke skill |
| OpenCode | Native | `.opencode/skills/` (sudah ada). Global: `~/.config/opencode/skills/` |
| Cursor | Rule | `.cursor/rules/deep-research-domain-council.mdc` (agent-requested; berisi core + rujukan ke SKILL.md) |
| Windsurf | Rule | `.windsurf/rules/deep-research-domain-council.md` |
| Cline | Rule | `.clinerules/deep-research-domain-council.md` |
| Roo Code | Rule | `.roo/rules/deep-research-domain-council.md` |
| Agen umum (AGENTS.md) | Pointer | `AGENTS.md` di root mengarahkan agen ke skill |
| DeepSeek / API LLM apa pun | System prompt | Pakai `adapters/api/system-prompt.md` sebagai system prompt; lampirkan bagian SKILL.md yang relevan bila perlu detail |

## Pilihan ukuran

Untuk agen native, setiap skill memiliki panduan inti dan referensi terpisah. Untuk aplikasi chat, adapter lengkap memuat prosedur lintas bidang. Versi lite memprioritaskan klaim utama, pemeriksaan singkat, dan catatan untuk melanjutkan saat kuota terbatas.

## Contoh pemakaian API (DeepSeek, OpenAI, Gemini, dll. — format OpenAI-compatible)

```python
from openai import OpenAI
system = open("adapters/api/system-prompt.md", encoding="utf-8").read()
client = OpenAI(base_url="https://api.deepseek.com", api_key="YOUR_KEY")  # ganti base_url sesuai provider
resp = client.chat.completions.create(
    model="deepseek-chat",  # ⚠ cek nama model terbaru di dokumentasi provider
    messages=[{"role": "system", "content": system},
              {"role": "user", "content": "Deep research: ..."}],
)
print(resp.choices[0].message.content)
```

Riset mendalam butuh akses web. Lewat API mentah, aktifkan tool pencarian dari provider (misalnya web search tool) atau sambungkan MCP pencarian. Tanpa itu, model hanya bisa menjawab dari pengetahuannya sendiri.

## Setelah mengedit skill

Ubah referensi di `deep-research-domain-council/SKILL.md`, inti skill di `scripts/sync.py`, atau prompt chat di `adapters/CORE_PROMPT.md` dan `adapters/CORE_LITE.md`. Bangun ulang dengan perintah berikut.

```bash
python scripts/sync.py
```

Skrip memperbarui salinan native dan adapter. Tambahkan `--zip` untuk membuat arsip plugin.
