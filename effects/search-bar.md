# search-bar

A search bar above your head types what you are talking about, then results drop down.

**Best for:** Questions people ask, 'everyone googles X'.  
**Typical length:** 2.5–4 s

## Fill it from the transcript

- `text` = the question/topic phrased as a lowercase search query.
- `results` = up to 3 related things they mention or answer.

## Options

| Option | Meaning |
|---|---|
| `text` | query |
| `results` | up to 3 with &#124; |
| `y` | 0–1 |

## Example plan entry

```json
{"fx": "search-bar", "start": 1.0, "end": 5.0, "text": "how to edit reels with ai", "results": "claude video effects|auto captions|b-roll ideas"}
```
