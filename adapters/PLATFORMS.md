# Panduan per Platform

Skill ini mengikuti **Agent Skills open standard** (folder berisi `SKILL.md` dengan frontmatter YAML). Platform yang mendukung standar ini membaca file aslinya langsung. Platform lain memakai adapter ringkas (`CORE_PROMPT.md`, ±4,8 KB) ditambah `SKILL.md` lengkap sebagai file pengetahuan.

| Platform | Dukungan | Cara pasang |
|:---|:---|:---|
| Claude Code | Native | Repo: `.claude/skills/deep-research-domain-council/` (sudah ada). Global: `scripts/install.*` → `~/.claude/skills/` |
| Claude.ai (web/desktop) | Native | Settings → Capabilities → Skills → upload `adapters/claude-ai/deep-research-domain-council.zip` ⚠ letak menu bisa berubah |
| OpenAI Codex (CLI / IDE) | Native | Repo: `.agents/skills/` (sudah ada). Global: `~/.agents/skills/` (versi lama: `~/.codex/skills/`). Cek dengan `/skills` atau panggil `$deep-research-domain-council` |
| ChatGPT | Adapter | **Custom GPT:** tempel `adapters/chatgpt/INSTRUCTIONS.md` ke kolom Instructions (di bawah batas 8.000 karakter), lalu upload `deep-research-domain-council/SKILL.md` sebagai Knowledge. **Projects:** tempel ke Project instructions dan tambahkan SKILL.md sebagai file |
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

## Kenapa ada dua ukuran

- **`SKILL.md` lengkap (±99 KB, ±25 ribu token):** platform native memuatnya bertahap. Saat idle hanya `name` + `description` yang dibaca, jadi aman.
- **`CORE_PROMPT.md` (±4,8 KB, ±1.200 token):** inti aturan untuk platform yang menyuntikkan instruksi ke **setiap** percakapan (Custom GPT, Gem, rules Cursor, system prompt API). Memasukkan 99 KB ke sana akan boros token dan bisa melewati batas karakter.

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

Edit hanya `deep-research-domain-council/SKILL.md`, lalu jalankan:

```bash
python scripts/sync.py
```

Skrip ini menyalin SKILL.md ke semua folder adapter dan membangun ulang zip Claude.ai.
