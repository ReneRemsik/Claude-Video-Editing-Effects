# comment-box

An Instagram comments sheet types a word, posts it, gets a heart and your reply.

**Best for:** Calls to action: 'comment X and I'll send it'.  
**Typical length:** 3–5 s

## Fill it from the transcript

- `text` = the exact keyword they ask viewers to comment.
- `reply` = what they promise to send, `handle` = their handle if known. `look=bar` for the simpler comment bar.

## Options

| Option | Meaning |
|---|---|
| `text` | the word typed |
| `reply` | your reply |
| `handle` | your handle |
| `chip` | first chip |
| `look` | bar for the simple version |

## Example plan entry

```json
{"fx": "comment-box", "start": 1.0, "end": 6.0, "text": "EFFECTS"}
```
