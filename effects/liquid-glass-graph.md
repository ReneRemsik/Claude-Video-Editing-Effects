# liquid-glass-graph

A liquid-glass card under your chin: a green graph climbs while the number counts up.

**Best for:** Growth, results, metrics.  
**Typical length:** 2–4 s

## Fill it from the transcript

- `from`/`to` = the before/after numbers they say (keep units: 197K, 59%); `text` = what the metric is.
- `look=bento` adds donut/KPI/bars tiles: fill `donut`, `kpi`, `bars` only from numbers they say.

## Options

| Option | Meaning |
|---|---|
| `text` | label |
| `from` |  |
| `to` |  |
| `color` | hex |
| `look` | bento |
| `donut` | 29%::label |
| `kpi` | 672K::label |
| `bars` | a&#124;b&#124;c::label |

## Example plan entry

```json
{"fx": "liquid-glass-graph", "start": 1.0, "end": 5.0, "text": "followers", "from": "2K", "to": "48K"}
```
