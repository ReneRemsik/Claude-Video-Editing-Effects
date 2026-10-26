# lean-in

A fast punch-in on one word.

**Best for:** Emphasis: the single most important word in a sentence.  
**Typical length:** 0.6–1.5 s

## Fill it from the transcript

- Pick the stressed word (a number, a 'never', 'secret', 'free', the punchline) and start exactly on its timestamp.
- Use at most once every ~5 s or it stops landing.

## Options

| Option | Meaning |
|---|---|
| `zoom` | punch-in amount (1.45, max 2) |
| `speed` | seconds to reach it (0.18) |

## Example plan entry

```json
{"fx": "lean-in", "start": 1.0, "end": 2.5}
```
