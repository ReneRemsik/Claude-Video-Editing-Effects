# the-bill

Prints your instructions like a receipt into the wall above your head.

**Best for:** Recipes, steps, prompts, 'what you need', a cost breakdown.  
**Typical length:** 3–5 s

## Fill it from the transcript

- `text` = an order line, then each step/ingredient they say (short), then a TOTAL line summarising the outcome or price they mention.

## Options

| Option | Meaning |
|---|---|
| `text` | receipt lines joined with &#124; |

## Example plan entry

```json
{"fx": "the-bill", "start": 1.0, "end": 6.0, "text": "ORDER #1|1x transcript|1x face track|3x widgets|TOTAL: 1 prompt"}
```
