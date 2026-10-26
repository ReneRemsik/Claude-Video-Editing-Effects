# led-sign

The lights drop and a glowing LED sign types itself out behind you.

**Best for:** Mottos, names, the closing line.  
**Typical length:** 2–4 s

## Fill it from the transcript

- `text` = a 1–3 word phrase they say, split on | for two lines.

## Options

| Option | Meaning |
|---|---|
| `text` | lines with &#124; |
| `color` | hex |
| `push` |  |

## Example plan entry

```json
{"fx": "led-sign", "start": 1.0, "end": 5.0, "text": "STAY|CURIOUS"}
```
