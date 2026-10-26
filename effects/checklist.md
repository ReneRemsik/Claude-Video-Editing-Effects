# checklist

A Claude task list under your chin: each step spins, then ticks green.

**Best for:** Processes being automated, 'Claude does X then Y'.  
**Typical length:** 3–6 s

## Fill it from the transcript

- `text` = each step they describe as `step::detail`; `title` = the task.

## Options

| Option | Meaning |
|---|---|
| `text` | step::meta with &#124; |
| `title` |  |

## Example plan entry

```json
{"fx": "checklist", "start": 1.0, "end": 7.0, "title": "Editing your reel", "text": "Read the transcript::context|Tracked your face::every frame|Added widgets::on cue"}
```
