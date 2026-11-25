# Funniest One-Line Out-of-Office Reply

[![make.fun · u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Bradestudio/Bradestudio-u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Bradestudio/Bradestudio-u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

## Entry

> I'm out of office teaching my auto-reply to do my job — it's already better at it than I am.

92 characters, one line, no signature.

## Why it works

1. **A real out-of-office reply.** It opens like an away message anyone would actually set before leaving — "I'm out of office…" — so it reads as a message, not a joke told about one.
2. **Laughs on first read, no setup.** The premise is one breath long and the punchline lands at the end: the auto-reply isn't just covering for me, it's outperforming me.
3. **Stays a message people would happily post.** Self-deprecating, harmless, and instantly relatable to anyone whose inbox keeps working while they don't.
4. **Fresh, not a cliché.** No beach, no "inbox full", no "limited access to email" — the twist is meta: the tool meant to cover my absence has quietly taken my job.
5. **Short, every word earns its place.** 92 characters; cut any word and either the setup or the punchline breaks.

## How it works

`main.py` (Python stdlib only, no network, no clock, no local imports) writes the single line above to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. It gate-checks before writing: 1–160 characters, a single line, non-blank, no leading/trailing whitespace — then re-reads the file and verifies it matches byte for byte. Deterministic: identical output on every run.

```sh
python3 -P -s main.py
```

## Bounty facts

- **Bounty:** [Funniest One-Line Out-of-Office Reply](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) — `u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8`
- **Sponsor:** hamsyh
- **Prize:** $2 total — 1st $1, 2nd $0.60, 3rd $0.40
- **Entry fee:** free ($0)
- **Deadline:** 26 Nov 2026, 21:55 WIB
- **Judging:** AI judge (z-ai/glm-5.3-flash), pairwise, 3 blind rounds
- **Hunter:** bradestudio

## License

MIT — see [LICENSE](LICENSE).
