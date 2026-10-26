# notification-stack

Phone notifications about what you are saying drop in and stack above your head.

**Best for:** Results, news, 'then I got a message…', listing outcomes.  
**Typical length:** 2–5 s

## Fill it from the transcript

- One notification per fact they mention: `App::Title::Message`. The app is whatever fits the fact (Messages, Calendar, Bank, YouTube Studio, Claude).
- `ticks` = when each fact is said.

## Options

| Option | Meaning |
|---|---|
| `text` | App::Title::Message joined with &#124; |
| `ticks` | seconds with &#124; |
| `max` | visible at once (3) |
| `y` | 0–1 top |

## Example plan entry

```json
{"fx": "notification-stack", "start": 1.0, "end": 6.0, "text": "Claude::Edit finished::Your reel is ready|Studio::New record::12,400 views today", "ticks": "3.1|4.6"}
```
