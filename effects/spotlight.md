# spotlight

Kills the lights, keeps you lit, optional glowing word behind you.

**Best for:** Dramatic turns: 'but here's the thing', a confession, the big reveal.  
**Typical length:** 2–4 s

## Fill it from the transcript

- Start on the turn ("but", "here's the secret").
- `text` = the key word of the reveal, if there is one.
- `look=sparkle` (alias glitter-spotlight) for celebratory moments (wins, launches).

## Options

| Option | Meaning |
|---|---|
| `text` | glowing word |
| `color` | hex |
| `push` | slow zoom (1.1) |
| `look` | sparkle for the golden version |

## Example plan entry

```json
{"fx": "spotlight", "start": 1.0, "end": 5.0, "text": "SECRET"}
```
