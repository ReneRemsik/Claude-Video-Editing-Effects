# chat-bubbles

Chat bubbles pop in beside you as a conversation plays out.

**Best for:** Retelling conversations: 'my friend asked… I said…'.  
**Typical length:** 3–6 s

## Fill it from the transcript

- One bubble per line of the conversation they retell: `them::msg` or `me::msg`.
- `ticks` = when each line is said.

## Options

| Option | Meaning |
|---|---|
| `text` | who::message joined with &#124; |
| `ticks` | seconds with &#124; |
| `max` | visible (4) |
| `y` | 0–1 bottom |

## Example plan entry

```json
{"fx": "chat-bubbles", "start": 1.0, "end": 7.0, "text": "them::did you edit this?|me::nope, Claude did", "ticks": "2.0|3.2"}
```
