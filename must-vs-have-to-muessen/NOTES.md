# Must vs. have to vs. müssen: vertical explainer

26 s · 1080×1920 · 30 fps · H.264 + AAC · −14 LUFS (phone profile). No voiceover; synthesized score.
Rebuild: `./build.sh /tmp/frames must-vs-have-to.mp4` (fonts are local files in `fonts/`).

## Storyboard as built
| # | Time | Visual | On-screen text |
|---|------|--------|----------------|
| 1 | 0–3.0 | Three-strand ribbon divides EN \| DE; blue/red washes left, gold right | ENGLISH · DEUTSCH / "Must" vs. / "have to" |
| 2 | 3.0–6.6 | Figure; 8 blue arrows press in from clocks, §, offices, rule books | HAVE TO / Pressure from outside. / "I have to wear a uniform." |
| 3 | 6.6–9.9 | Arrows reverse; heart lights; red arrows radiate to hearts and bulbs | MUST / Drive from within. / "I must call my dad." |
| 4 | 9.9–13.4 | Slide to a dusk porthole; a window lights up | MUST · LOGIC / Also a conclusion. / Lights on? She must be home. |
| 5 | 13.4–17.9 | Porthole collapses into the window light; blue and red streams merge into a müssen banner | DEUTSCH / One word, both senses. / ich muss = I must · I have to |
| 6 | 17.9–22.2 | Banner rises; two cards | CAREFUL / The negative trap. / du musst nicht = you don't have to / du darfst nicht = you must not |
| 7 | 22.6–26 | End card (complete by ~24.4 s) | IN SHORT / must ≈ inside / have to ≈ outside / müssen = both / A tendency, with lots of overlap. |

## Facts and sources
- have to = obligation from outside the speaker; must = often obligation from the speaker (or the authority writing the rule). British Council LearnEnglish, "Modals: permission and obligation" (learnenglish.britishcouncil.org). The same page's moderators note "a lot of overlap" in real usage, hence the hedged end-card line.
- must for logical deduction ("She must be home"): standard epistemic use; also on the British Council pages.
- Example sentences adapted from British Council examples ("We have to wear a uniform…", "I must phone my dad…").
- du musst nicht = you don't have to; du darfst nicht = you must not: UT Austin Grimm Grammar (coerll.utexas.edu/gg/pr/vm_01.html); Boise State "Deutsch im Blick" grammar chapter on Modalverben.

## Simplifications
- The internal/external split is a tendency (strongest in British English). In American English, "have to" is more common in both senses. Shown with ≈ rather than =.
- müssen also covers "need to", and "brauchen nicht zu" is a common alternative to "nicht müssen". Neither is shown.

## Fonts
Network was off, so Google fonts couldn't be fetched. Local OFL/free fonts were used instead: Gelasio (display), Inter (body), DejaVu Sans Mono Bold (kickers). All glyphs (ü ≈ “ ” ’ ·) are covered.

## Final checks (tools/check.py)
- 0 high findings. 1 medium: the banner word measures 29 px for a few frames while it scales in (it is 77–140 px once settled).
- Picture median luma 0.78. Loudness −14.0 LUFS, TP −3.3 dBTP, LRA 4.1 LU. Energy below 120 Hz 5%.
- Sync: arrow pops −0.3 ms / +1.0 ms median, cards −0.3 ms.
- 34 text elements, 84 words (3.2 words/s).
- Not checked: listening. The mix was measured only.
