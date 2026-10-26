# glass-widgets

Frosted-glass phone widgets and mini artifacts float around your head; each one pops in when you mention its content.

**Best for:** Showcasing a workflow, a result, a day in the life, a product.  
**Typical length:** 4–12 s

## Fill it from the transcript

- Build every widget from the transcript; never keep the placeholder values.
- stat tile: `title` (source/app), `text` (the biggest number they say), `sub` (2 short lines: what the number means).
- progress bar: `bar` (what is in progress, from their words), `bar_label` (short context).
- chart: `chart_title`, `chart_value` (a number they say), `chart_bars` (relative values if they compare things; otherwise a plausible descending shape and say so in the brief).
- now card: `now_tag` (e.g. NOW TALKING ABOUT), `song` (the topic, 2–3 words), `now_sub`.
- calendar: `day`, `date`, `event` (a deadline, plan or date they mention).
- ring: `ring` (≤4 chars: a %, a count) and `ring_label`.
- profile only if the user gave `name` + `handle`; it is hidden otherwise. `pill` = 'Edited by|Claude' or 'none'.
- `at` = when each widget pops in, on the word it refers to: `stat=2.1|chart=4.0|...` (keys: stat, progress, profile, chart, now, calendar, ring, pill). `hide` = widgets with nothing real to say (e.g. `calendar|ring`). 4–6 widgets beat 8 generic ones.

## Options

| Option | Meaning |
|---|---|
| `title` | stat tile header |
| `text` | big number |
| `sub` | two lines with &#124; |
| `bar` | progress title |
| `bar_label` | progress caption |
| `chart_tag` | chart header |
| `chart_title` | chart title |
| `chart_value` | chart number |
| `chart_bars` | values with &#124; |
| `now_tag` | now-card label |
| `song` | now-card title |
| `now_sub` | now-card caption |
| `day` | e.g. MON |
| `date` | e.g. 26 |
| `event` | calendar event |
| `ring` | ring text |
| `ring_label` | ring caption |
| `name` | profile name |
| `handle` | profile handle |
| `pill` | 'Edited by&#124;Claude' or none |
| `at` | key=video second, joined with &#124; |
| `hide` | keys to hide, joined with &#124; |
| `grade` | warm, none, ... |
| `dark` | glass darkness (0.22) |
| `look` | simple = 3-widget version |

## Example plan entry

```json
{"fx": "glass-widgets", "start": 1.0, "end": 13.0, "title": "Claude Code", "text": "50", "sub": "video effects|one skill", "bar": "Reading transcript", "bar_label": "context", "song": "AI video edits", "now_tag": "NOW TALKING ABOUT", "hide": "calendar|ring", "at": "stat=3.2|progress=4|chart=6|now=7"}
```
