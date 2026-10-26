# chapter-bar

A glass progress bar at the top shows the chapters of your video and which one you are in.

**Best for:** Tutorials and longer explanations with clear sections.  
**Typical length:** whole video s

## Fill it from the transcript

- Split the transcript into 3–5 sections; `text` = a 1–3 word name for each; `ticks` = when each section starts.
- Run it from the first section start to the end.

## Options

| Option | Meaning |
|---|---|
| `text` | chapter names with &#124; |
| `ticks` | start seconds with &#124; |
| `color` | hex |
| `y` | 0–1 |

## Example plan entry

```json
{"fx": "chapter-bar", "start": 0.0, "end": 15.0, "text": "The problem|The fix|The result", "ticks": "0|5.2|10.4"}
```
