# apple-toggles

An iPhone settings card flips its switches on, one line at a time.

**Best for:** Settings, habits, 'turn on X'.  
**Typical length:** 3–5 s

## Fill it from the transcript

- `text` = the things they turn on/enable; `ticks` = when each is said.

## Options

| Option | Meaning |
|---|---|
| `text` | rows with &#124; |
| `ticks` | seconds with &#124; |
| `color` |  |
| `pos` | below |
| `overlap` |  |
| `zoom` |  |

## Example plan entry

```json
{"fx": "apple-toggles", "start": 1.0, "end": 6.0, "text": "One clip|Type /effects|Zero editing apps"}
```
