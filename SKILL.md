---
name: effects
description: Add any of 50 transcript-aware video effects to a talking-head video (glass widgets, keyword pop, notification stack, post card, big number, chapter bar, search bar, chat bubbles, lower third, orbit, spotlight, checklist, liquid glass graph, LED sign and more). Claude reads what the speaker says first, then fills each effect with that content and times it to the words. Use when the user types /effects, names one of the effects, or asks to add an effect, zoom, grade, sticker, caption pop or animation to their video.
---

# Claude Video Editing Effects

50 video effects that are written from what the speaker actually says. The user is usually not technical: keep replies short and friendly, do the work for them, never ask them to run commands.

All paths are relative to this skill's folder (the folder this SKILL.md is in). Use its absolute path in commands. `PY` below means `.venv/bin/python` (Windows: `.venv\Scripts\python.exe`).

## How the command is read
`/effects <effect> [when] [extra wishes]` plus a video (dragged in or a path).
- `<effect>` is a name from the list below (aliases work too). No name → show the list and suggest 3 that fit the video once you know what it is about.
- Several effects are fine: "/effects keyword-pop on the hook, then big-number when I say the views".
- No timing → you choose it from the transcript (that is the point of this skill).

## 1. Set up (first run only)
Run `bash scripts/setup.sh`. It prints `READY` when done (1–3 minutes the first time).
- `NEED_FFMPEG`: install it (Mac `brew install ffmpeg`, Windows `winget install ffmpeg`, Linux `apt-get install ffmpeg`).
- `NEED_PYTHON`: install Python 3.12, then run setup again.
- Linux error `libEGL.so.1` / `libGLES`: `apt-get install -y libegl1 libgles2 libgl1`.

## 2. Understand the video (always, before designing anything)
1. Transcript: `PY scripts/words.py <video>` → word-level timestamps, saved as `<video>.words.json`. Read it fully. If the transcription model can't be downloaded, tell the user and ask them to paste what they say (or the key lines with rough times).
2. Look: `PY scripts/frames.py <video> <workdir>/frames --every 2` and view the frames: setting, room colours, where the head sits, what they hold or point at.
3. Write a short brief (show it to the user in 4–6 lines):
   - topic in one sentence and the hook;
   - the concrete facts they say: numbers, names, tools, dates, steps, results;
   - the beats: the moments where an effect would reinforce what is being said, with timestamps.

## 3. Load the effect's instructions
For each requested effect, read `effects/<name>.md`. It says what the effect is for, how to fill every option from the transcript, the ideal length, and gives an example plan entry. Follow it.

Rules that apply to every effect:
- Content comes from the transcript. Never ship placeholder text, numbers or names. If an option needs something the video doesn't contain (the user's name, handle, a number), ask the user or hide that part.
- Time things to the words: an item appears on the timestamp of the word it refers to (`ticks`, `at`, `word@sec`).
- Use the speaker's own wording, tightened. Short beats long: 1–4 words per label.
- Match colours to the room when an effect takes `color`.

## 4. Plan, check, render
1. Write the plan next to the video as `<video-name>_effects.json`:
   ```json
   {"effects": [
     {"fx": "keyword-pop", "start": 0.4, "end": 2.6, "text": "STOP@0.5|*EDITING@0.9|MANUALLY@1.5"},
     {"fx": "big-number", "start": 6.1, "end": 8.6, "to": "12,400", "label": "views in 24h"}
   ]}
   ```
2. Check stills first (fast): `PY scripts/fx.py --plan <plan.json> <video> <workdir>/check.png --still 1.2,7.4` at the middle of each effect (and at each pop-in for timed items). Look at the PNGs yourself. Fix anything that covers the face, is cut off, unreadable, or doesn't match what is being said at that moment.
3. Show the user the brief and a couple of stills, then render: `PY scripts/fx.py --plan <plan.json> <video> <video-name>_effects.mp4` (add `--width 2160` for 4K). Audio is kept.
4. Tell them where the file is and list each effect with its time and the line it is tied to, so they can ask for changes one by one. Remind them in one line to watch it before posting.

A message like "Exception ignored in ... ImageSegmenter.__del__" after a run is harmless shutdown noise.

## The 50 effects
| `fx` | What it does |
|---|---|
| `noise` | reels pile up behind your head, one every quarter second |
| `lineup` | numbered tiles fan out in an arc above your head |
| `locked-on` | corner brackets snap onto your face and the camera follows you |
| `orbit` | your reels circle your head: in front at the bottom, behind you at the top |
| `lean-in` | a fast punch-in on one word |
| `backdrop-word` | a giant word drops in behind you |
| `spotlight` | kill the lights, keep you lit |
| `the-bill` | prints every instruction like a ticket, into the wall above your head |
| `moody` | a moody colour grade: darker, softer, teal shadows |
| `swipe` | a before and after slider that sweeps across you |
| `todo` | a checklist card beside your head that ticks off as you talk |
| `tap` | a Follow button pops up and flips to Following |
| `pause-point` | freeze the frame and point at something with a hand-drawn arrow |
| `uninstall` | a glitchy uninstall bar that breaks the frame apart |
| `reel-frame` | your video shrinks into an Instagram reel card |
| `shortcut-rain` | keyboard keys rain down behind you |
| `reject-stamp` | a big red stamp slams onto the screen |
| `countdown-flip` | a 3, 2, 1 flip clock above your head |
| `rabbit-hole` | the frame tunnels into itself, spinning |
| `cover-star` | you become a magazine cover, with the title behind your head |
| `scribble` | marker doodles draw themselves around you |
| `red-collage` | black and white you, a giant red word behind, kinetic type stacked beside you |
| `split-headline` | a clean headline card slides down and pushes you into the bottom of the frame |
| `pastel-word` | a soft lavender backdrop, a giant word behind you and a profile card that gets followed |
| `check-pills` | grid-paper room, your reels pinned behind you and blue pills that get clicked |
| `headline-box` | a punch-in with a clean two-line headline, the second line in a white box |
| `profile-wall` | your profile grid fills the wall behind you while a counter ticks up |
| `tier-list` | a tier list drops in front of you and Claude flies into S tier |
| `broll-split` | split screen: b-roll on top with a price-tag sticker, you on the bottom |
| `phone-fan` | your reels fan out like a hand of phones in front of you, under a two-line headline |
| `dot-reveal` | your shot builds itself out of glowing dots, then snaps into the full picture |
| `headline-wall` | a wall of your own reel headlines piles up behind your head, then your total views pop in front |
| `checklist` | a Claude task list builds under your chin: each step spins, then ticks green |
| `glass-widgets` | frosted glass phone widgets and mini artifacts float around your head, with an Edited by Claude pill |
| `timeline` | a dark red cinematic grade with an editing timeline, a REC timecode and a glowing playhead |
| `comment-box` | an Instagram comments sheet above your head types your word, posts it, gets a heart and your reply |
| `liquid-glass-graph` | a liquid glass card floats under your chin while a graph climbs and the number counts up |
| `carousel-spin` | your reels spin around you in a 3D carousel, then slow to a stop |
| `match-cut` | news pages cut on one word, locked in place behind your head |
| `apple-toggles` | an iPhone settings card under your chin flips its switches on, one line at a time |
| `led-sign` | the lights drop and a glowing LED sign types itself out behind you |
| `slow-push` | a slow cinematic push-in from the wide shot to your face, the room melting out of focus |
| `keyword-pop` | the key words you say pop up big under your chin, one at a time, right when you say them |
| `notification-stack` | phone notifications about what you are saying drop in and stack up above your head |
| `post-card` | your own words appear as a social post card under your chin, word by word |
| `chapter-bar` | a glass progress bar at the top shows the chapters of your video and which one you are in |
| `search-bar` | a search bar above your head types what you are talking about, then results drop down |
| `big-number` | a giant number counts up behind your head while you say it, with a label underneath |
| `chat-bubbles` | chat bubbles pop in beside you as a conversation you describe plays out |
| `lower-third` | a glass name tag slides in at the bottom: who you are and why it matters |

Named looks: `glitter-spotlight` (= `spotlight` with `look=sparkle`), `cover-star` with `look=editorial`, `liquid-glass-graph` with `look=bento`, `glass-widgets` with `look=simple`, `comment-box` with `look=bar`.

Aliases: `bill`, `to-do`, `follow`, `stamp`, `countdown`, `cover`, `rain`, `pause`, `glass`, `widgets`, `keywords`, `kinetic`, `notifications`, `post`, `quote`, `chapters`, `search`, `number`, `counter`, `chat`, `messages`, `name-tag` and more (see `ALIASES` in `scripts/fx.py`).

## Rules
- Never cover the face. Effects go behind the person or avoid the face themselves; if a still shows otherwise, move it (`x`, `y`) or shorten the text.
- Effects run in plan order. Put camera effects (`locked-on`, `lean-in`, `spotlight`, `slow-push`) first when they overlap others.
- Zoom never goes past 2x.
- Visuals only: sound effects and full captions are up to the user.
- Be honest that these are starter versions if the user compares them to a reel they saw.
