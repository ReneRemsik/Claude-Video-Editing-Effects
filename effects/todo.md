# todo

A checklist card beside your head ticks off as you talk.

**Best for:** Step-by-step explanations, routines, requirements.  
**Typical length:** 3–8 s

## Fill it from the transcript

- `text` = each step in the speaker's words, 2–4 words each.
- `ticks` = the second each step is said (from the transcript), so it ticks exactly then.
- `title` = what the list is for.

## Options

| Option | Meaning |
|---|---|
| `text` | items joined with &#124; |
| `ticks` | video seconds joined with &#124; |
| `title` | card title |

## Example plan entry

```json
{"fx": "todo", "start": 1.0, "end": 9.0, "title": "To post a reel", "text": "Film it|Drop it in Claude|Type /effects", "ticks": "2.1|3.4|4.8"}
```
