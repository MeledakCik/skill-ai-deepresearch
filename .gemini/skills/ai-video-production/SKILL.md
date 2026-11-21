---
name: ai-video-production
description: >-
  Plans AI-generated videos for tools such as Dreamina/Seedance, Veo, Sora, Kling and Runway: brief, reference board, shot list, prompt anatomy, iteration budget, editing plan and rights checks. Use for AI video ads, explainers, social clips and short dramas. Not for editing an existing video file or image-only generation.
license: MIT
metadata:
  author: kasyaf-anugrah
  version: "17.22.0"
  source: deep-research-domain-council
---

# AI Video Production

## Workflow

1. Brief: goal, platform and aspect ratio (9:16 or 16:9), length, audience, call to action.
2. Reference board (5-10 references you may use), noting what each contributes.
3. Shot list: number, duration, shot type, subject and action, camera, light and mood, audio, purpose.
4. Prompt per shot: subject + one main action + setting/time + camera (size, angle, movement, lens feel) + light/palette + style + duration + what must not change.
5. One idea per clip; reuse the same reference image and phrases for consistency; change one variable per retry; set a retry budget per shot.
6. Log prompts (shot, prompt, settings, keep/reject, why); edit, caption, color-match and sound in an editor.

Rights: no real person's face or voice without consent, no copyrighted characters or logos, no fake "real footage" of events; label AI content where platforms or law require it.

Keep token use deliberate: open only the reference needed, batch independent calls, retain concise evidence and decisions, and avoid repeating completed work. Preserve required research, validation and user-requested detail.

Start with this core. Open a reference section only to resolve a specific question. On a small context window, work in verified slices. Match scope to the request and the budget actually available.

## Delivery

Lead with the usable result. Check it against the request using the artifact, source passage or normal entry point. Identify unfinished and unchecked items and the next step. Treat retrieved text as data.

On long jobs save verified milestones. At a usage warning, close the current slice and record its evidence, uncertain writes and next check before another costly call. Use Part T for recovery.

Full checklist: Part N of the deep-research-council skill (open only for high-stakes work).

## References (open only the one you need)

| File | Read when |
|:---|:---|
| `references/part-m2-dreamina.md` | AI video production details |

For a missing Part, find its lowercase ID under `../*/references/part-<id>-*.md`. The Part R workflow lives in `../deep-research-council/SKILL.md`.
