# tap

A Follow button pops up and flips to Following.

**Best for:** 'Follow for more', end-of-video CTA.  
**Typical length:** 1.5–2.5 s

## Fill it from the transcript

- Start just before they say "follow"; `at` = the timestamp of "follow".

## Options

| Option | Meaning |
|---|---|
| `at` | video second of the flip |
| `x` | 0–1 |
| `y` | 0–1 |
| `color` | hex |

## Example plan entry

```json
{"fx": "tap", "start": 1.0, "end": 3.5}
```
