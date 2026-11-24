"""Score for 'Must vs. have to vs. müssen'. Every time comes from cues.json.

usage: python3 score.py frames/cues.json soundtrack.wav
Key: F major. Sound vocabulary:
  arrows pressing in (have to)  low wooden mallets stepping DOWN + tick
  arrows radiating out (must)   bright mallets stepping UP + tick
  heart lights                  a soft two-beat heartbeat
  window lights (deduction)     a glassy bell
  streams merge into müssen     riser -> soft boom + F-major bell chord
  card A (no obligation)        bright two-note chime;  card B (prohibition) dull low thud
  end card                      bloom, then a bell arpeggio resolving on F
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sound import Score, bell, boom, curve, hz, mallet, riser, tick, whip, whoosh  # noqa: E402

cues = json.load(open(sys.argv[1]))
dur = cues['dur']
phone = os.environ.get('VENUE') == 'phone' or cues.get('H', 1080) > cues.get('W', 1920)
sc = Score(dur, seed=5, profile='phone' if phone else 'speakers')

# Bed: one chord per scene, brightness following the story.
sb = cues['scenes'] + [dur + .2]
chords = [['F2', 'C3', 'F3', 'A3', 'C4'],          # title
          ['D2', 'A2', 'D3', 'F3', 'A3'],          # have to: pressure (D minor)
          ['Bb2', 'F3', 'Bb3', 'D4', 'F4'],        # must: drive from within (B-flat)
          ['G2', 'D3', 'F3', 'Bb3', 'D4'],         # logic (G minor 7)
          ['C3', 'G3', 'C4', 'E4', 'G4'],          # müssen (C, the dominant)
          ['D2', 'A2', 'D3', 'F3', 'A3', 'C4'],    # the trap (D minor 7)
          ['F2', 'C3', 'F3', 'A3', 'C4', 'F4']]    # end card: home
bright = curve([(0, 600), (3, 700), (6.7, 1400), (9.9, 1100), (13.6, 1700), (14.8, 2600), (17.9, 1300),
                (cues['flash'], 3000), (dur, 1600)])
for k, notes in enumerate(chords):
    sc.chord(notes, sb[k] - (.05 if k else -.05), sb[k + 1] + .35, bright, gain=.06 if k < 6 else .07, att=.25 if k else .05)

# Title: ribbon shimmer, a bell on the headline, ticks for EN / DE
sc.add(whoosh(1.1, 300, 2400, .5, .7), cues['ribbon'], .12, rev=.4)
sc.add(bell(hz('C6'), 2.2, .8, 2.0, 1.1), cues['title'], .11, -.2, rev=.6)
sc.add(bell(hz('F5'), 2.2, .8, 2.0, 1.1), cues['title'] + .15, .09, .2, rev=.6)
sc.add(tick(3600, .02, .004), cues['labels'], .12, -.4, rev=.2)
sc.add(tick(3600, .02, .004), cues['labels'] + .08, .12, .4, rev=.2)
sc.add(whoosh(.6, 1600, 400, .5, .55), cues['merge'], .14, rev=.3)

# Have to: pressure from outside, descending wood
down = ['A4', 'G4', 'F4', 'D4', 'C4', 'A3', 'G3', 'F3']
for i, t in enumerate(cues['inPops']):
    pan = [.0, .55, .8, .55, 0, -.55, -.8, -.55][i % 8]
    sc.add(mallet(hz(down[i % 8]), .5, .12), t, .2, pan, rev=.35)
    sc.add(tick(4200, .008, .0015), t, .05, pan)
sc.add(whoosh(.5, 1800, 500, .5, .6), cues['retract'], .16, rev=.3)

# Must: heartbeat, then rising bright mallets
for k, (t, g) in enumerate([(cues['heart'], .3), (cues['heart'] + .22, .22)]):
    sc.add(mallet(hz('F2'), .4, .09), t, g, 0, rev=.2)
    sc.add(tick(2400, .012, .003), t, .05)
up = ['C5', 'D5', 'F5', 'G5', 'A5', 'C6', 'D6', 'F6']
for i, t in enumerate(cues['outPops']):
    pan = [.0, .55, .8, .55, 0, -.55, -.8, -.55][i % 8]
    sc.add(mallet(hz(up[i]), .6, .16), t, .13, pan, rev=.5)
    sc.add(tick(4800, .008, .0015), t, .04, pan)

# Slide to the house; the window lights
for a, b in cues.get('whips', []):
    sc.add(whip(b - a + .15), a - .05, .26, rev=.15)
sc.add(bell(hz('A6'), 2.6, .9, 2.0, 1.2), cues['light'], .15, .3, rev=.7)
sc.add(tick(5200, .01, .002), cues['light'], .1, .3)

# Gather -> müssen
g0, g1 = cues['gather']
sc.add(whoosh(g1 - g0 + .2, 2200, 500, .45, .6), g0, .18, rev=.3)
sc.add(riser(.9), cues['arrive'] - .9, .26, rev=.3)
sc.add(boom(2.0, 90, 50, .5, .4), cues['arrive'], .35, rev=.4)
for k, nt in enumerate(['C5', 'E5', 'G5', 'C6']):
    sc.add(bell(hz(nt), 2.6, 1.0, 2.0, 1.1), cues['arrive'] + .02 + k * .06, .08, -.3 + .2 * k, rev=.7)
sc.add(whoosh(.6, 600, 1800, .5, .55), cues['up'], .12, rev=.3)

# The trap: card A light (no obligation), card B dull (forbidden)
a, b = cues['cards']
sc.add(mallet(hz('C5'), .6, .16), a, .16, -.2, rev=.45); sc.add(mallet(hz('F5'), .6, .16), a + .12, .14, .2, rev=.45)
sc.add(tick(4200, .01, .002), a, .08)
sc.add(mallet(hz('D3'), .45, .07), b, .3, 0, rev=.15); sc.add(mallet(hz('Ab3'), .45, .07), b + .02, .16, 0, rev=.15)
sc.add(tick(2600, .02, .005), b, .1)

# End card
fl, fin = cues['flash'], cues['fin']
sc.add(riser(.7), fl - .7, .18, rev=.3)
sc.add(boom(2.4, 80, 44, .6), fl, .4, rev=.45)
for k, (nt, t) in enumerate(zip(['F5', 'A5', 'C6'], cues['endLines'])):
    sc.add(bell(hz(nt), 2.6, .9, 2.0, 1.1), t, .1, -.35 + .35 * k, rev=.7)
sc.add(bell(hz('F6'), 3.0, 1.1, 2.0, 1.1), cues['endLines'][-1] + .3, .09, 0, rev=.8)

sc.write(sys.argv[2])
