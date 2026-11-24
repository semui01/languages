# Must vs. have to vs. müssen

26 s vertical explainer (1080×1920, 30 fps, with music, no voiceover).

- Video: [`must-vs-have-to.mp4`](must-vs-have-to.mp4) · poster: [`must-vs-have-to-poster.png`](must-vs-have-to-poster.png)
- Storyboard, sources and check results: [`NOTES.md`](NOTES.md)

## Rebuild

Needs Node 18+, Playwright with Chromium, ffmpeg with libx264/AAC, Python 3 with numpy.

```bash
./build.sh /tmp/frames must-vs-have-to.mp4
```

`film.html` is the animation (open it in a browser to preview and scrub), `score.py` the soundtrack.
Fonts in `fonts/`: Gelasio and Inter (SIL OFL), DejaVu Sans Mono (Bitstream Vera licence).
