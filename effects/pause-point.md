# pause-point

Freezes the frame and points at you with a hand-drawn arrow.

**Best for:** Self-deprecating callouts: 'this guy', 'me, three years ago'.  
**Typical length:** 1.5–3 s

## Fill it from the transcript

- `text` = 1–3 words labelling the speaker as they describe themselves ("me!", "broke me").

## Options

| Option | Meaning |
|---|---|
| `text` | label |
| `color` | hex |
| `label_x` | label position |

## Example plan entry

```json
{"fx": "pause-point", "start": 1.0, "end": 4.0, "text": "me, 2023"}
```
