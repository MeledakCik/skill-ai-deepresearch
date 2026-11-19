## M2. Dreamina (CapCut / ByteDance) — AI Video Research & Production Mode

**What is public:** Dreamina offers text-to-video, image-to-video, AI image generation and avatar tools, using its Seedance video models (⚠ model names/versions change), with multimodal references and controls for style, motion and scenes, plus a path into CapCut for editing.

The same workflow applies to any video generator (Dreamina/Seedance, Veo, Sora, Kling, Runway). **The research happens before the first generation.**

### M2.1 Pre-Production Research

1. **Brief:** goal (ad, explainer, short drama, social clip), platform (TikTok/Reels 9:16, YouTube 16:9), length, audience, call to action.
2. **Reference board:** collect 5-10 *references you have rights to use or that are only for analysis* (lighting, framing, pacing). Write down what you take from each: "warm rim light", "handheld, slight sway", "2-second cuts".
3. **Shot list (the script of the video):**

| # | Duration | Shot type | Subject & action | Camera | Light / mood | Audio | Purpose |
|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 3 s | Wide establishing | Night market street, steam from carts | Slow push-in, eye level | Warm tungsten, neon accents | Ambient crowd | Set place |
| 2 | 2 s | Close-up | Hands folding martabak | Static macro | Warm, shallow depth | Sizzle | Hook detail |

4. **Platform research:** current aspect ratios, max lengths, safe zones for captions/UI, and disclosure rules for AI-generated content on the target platform (⚠ verify current rules).

### M2.2 Prompt Anatomy for Video

```
[Subject + appearance] + [Action, one main verb] + [Setting + time of day]
+ [Camera: shot size, angle, movement, lens feel] + [Lighting + color palette]
+ [Style / medium] + [Pacing / duration] + [Constraints: what must NOT change]
```

Example: "Elderly street vendor in a batik shirt flips a martabak on an iron griddle, Jakarta night market, steam rising; medium close-up, slow dolly-in at eye level, 35mm feel, shallow depth of field; warm tungsten light with teal neon background; natural documentary style; 5 seconds; keep the vendor's face and shirt consistent with the reference image."

### M2.3 Production Discipline

- **One idea per clip.** Short clips with one action each, then edit them together. Long clips with many actions drift.
- **Consistency:** reuse the same reference image/character sheet and the same descriptive phrases across shots; change one variable per iteration.
- **Iteration budget:** decide max generations per shot (e.g., 4) before starting; credits and time are the token cost of video.
- **Log what works:** keep `prompt_log.md` (shot, prompt, seed/settings if exposed, result, keep/reject, why).
- **Edit in an NLE** (CapCut, Premiere, DaVinci): pacing, captions, color match, sound design. Audio quality matters more for perceived quality than most visual tweaks.
- **Anti-slop for video:** avoid default "epic cinematic" looks, oversaturated gradients, morphing hands and faces left in frame, random slow-motion. Cut any shot that has artifacts instead of hoping viewers miss them.

### M2.4 Rights, Ethics, Safety (Blocking)

- No real person's likeness or voice without their consent; no impersonating public figures; no deceptive "real footage" of events that never happened.
- No copyrighted characters, logos or brand mascots unless you hold rights.
- Label AI-generated content where platforms or law require it.
- Check the tool's terms for commercial use of outputs (⚠ varies by plan).
