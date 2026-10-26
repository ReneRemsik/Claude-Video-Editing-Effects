# keyword-pop

The key words you say pop up big under your chin, one at a time, right when you say them.

**Best for:** Hooks and punchlines: kinetic captions for 2–5 words.  
**Typical length:** 1.5–4 s

## Fill it from the transcript

- Pick 2–5 consecutive key words from the line (drop filler).
- Write each as `word@second` using its transcript start time; prefix `*` to highlight one word.
- Don't use it as full captions; it is for emphasis.

## Options

| Option | Meaning |
|---|---|
| `text` | word@sec joined with &#124; (prefix * to highlight) |
| `ticks` | alternative timing list |
| `color` | highlight hex |
| `font` | anton, bold, uib |
| `y` | 0–1 vertical position |

## Example plan entry

```json
{"fx": "keyword-pop", "start": 1.0, "end": 5.0, "text": "STOP@1.2|*EDITING@1.6|MANUALLY@2.1"}
```
