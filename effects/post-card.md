# post-card

Your own words appear as a social post card under your chin, word by word.

**Best for:** Quotable lines, hot takes, advice.  
**Typical length:** 2.5–5 s

## Fill it from the transcript

- `text` = the single most quotable sentence, verbatim (lightly trimmed).
- Start when they begin that sentence; `name`/`handle` from the user.

## Options

| Option | Meaning |
|---|---|
| `text` | the quote |
| `name` |  |
| `handle` |  |
| `stats` | footer text |
| `type` | off = no typing |
| `y` | 0–1 |

## Example plan entry

```json
{"fx": "post-card", "start": 1.0, "end": 6.0, "text": "Stop editing. Start describing.", "name": "Your Name", "handle": "@yourhandle"}
```
