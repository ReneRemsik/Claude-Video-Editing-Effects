# split-headline

A headline card slides down and pushes you to the bottom half.

**Best for:** News-style hooks: 'X just launched'.  
**Typical length:** 2–4 s

## Fill it from the transcript

- `text` = their hook as a 2–3 line headline (their wording, tightened); `hl` = the key word to highlight; `pill` = source/category.

## Options

| Option | Meaning |
|---|---|
| `text` | lines with &#124; |
| `hl` | highlighted word |
| `pill` | label |
| `color` | hex |
| `push` |  |
| `height` |  |

## Example plan entry

```json
{"fx": "split-headline", "start": 1.0, "end": 5.0, "text": "Claude|edits my|reels.", "hl": "edits"}
```
