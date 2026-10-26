# Claude Video Editing Effects

50 video effects for Claude Code that are **written from what you actually say**.

Drop a talking-head video into Claude, type `/effects` and an effect name. Claude transcribes your video, works out the topic, the numbers and the key moments, fills the effect with *your* content, times every element to the word it belongs to, checks preview frames so nothing covers your face, and renders the video with your original audio.

## Install

Paste this into a terminal (or ask Claude Code to run it for you):

```bash
git clone https://github.com/ReneRemsik/Claude-Video-Editing-Effects ~/.claude/skills/effects
```

On Windows (PowerShell) use `$HOME\.claude\skills\effects` as the destination. Restart Claude Code afterwards.

The first time you use it, Claude sets itself up (about 2 minutes). It needs `ffmpeg` and Python 3.10+ and installs what is missing.

## Use it

```
/effects glass-widgets
/effects keyword-pop on my hook
/effects big-number when I say the views, then lower-third at the start
/effects chapter-bar
```

What happens:

1. **Understand**: a word-level transcript plus sample frames of your video, so Claude knows the topic, the facts you mention and the colours of your room.
2. **Brief**: Claude shows you a short brief: the topic, the hook, the facts and the beats where effects should land.
3. **Fill**: each effect has its own instruction file in `effects/<name>.md`, which says how to turn your words into that effect's content and timing.
4. **Check and render**: preview stills first, then the full video as `yourvideo_effects.mp4`.

## The 50 effects

| Effect | What happens |
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


## Add your own effect

1. Write a function in `scripts/fx.py` decorated with `@effect('my-effect', 'one-line description')`. Read options from `e.o`, the local time from `c.lt`, and the face position from `c.fx`, `c.fy` and `c.fw`. Draw with `place(..., behind=True)` to sit behind the speaker.
2. Add `effects/my-effect.md` explaining how to fill its options from a transcript (copy any existing file as a template).
3. Test it: `python scripts/fx.py my-effect in.mp4 check.png --still 2 --start 1 --end 4`.

## Honest notes

- These are starter versions. They look best on vertical phone videos with one person facing the camera.
- Visuals only: add sound effects and full captions in your editor.
- Always watch the result before posting. Claude drafts, you approve.

## Licence

MIT, see `LICENSE`. The fonts in `fonts/` and the models in `models/` keep their own licences (see `fonts/*.txt` and `models/NOTICE.md`).
