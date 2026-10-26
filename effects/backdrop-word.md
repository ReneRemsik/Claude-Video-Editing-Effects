# backdrop-word

A giant word drops in behind you.

**Best for:** The topic word or the one-word thesis.  
**Typical length:** 1.5–3 s

## Fill it from the transcript

- `text` = ONE word from the transcript that sums up the line (the noun they repeat, the product, the verdict). Max ~8 letters reads best.
- Start on that word; match `color` to the room.

## Options

| Option | Meaning |
|---|---|
| `text` | the word |
| `color` | hex |
| `font` | bold or serif |

## Example plan entry

```json
{"fx": "backdrop-word", "start": 1.0, "end": 4.0, "text": "FOCUS"}
```
