# big-number

A giant number counts up behind your head while you say it, with a label.

**Best for:** Any single impressive number.  
**Typical length:** 1.5–3 s

## Fill it from the transcript

- Start ~0.3 s before they say the number; `to` = the number exactly as said with units ($12K, 3.5M, 59%, 12,400); `label` = what it counts.

## Options

| Option | Meaning |
|---|---|
| `to` | final number |
| `from` | start (0) |
| `label` | caption |
| `color` | hex |
| `font` |  |
| `y` | 0–1 |

## Example plan entry

```json
{"fx": "big-number", "start": 1.0, "end": 4.0, "to": "12,400", "label": "views in 24h"}
```
