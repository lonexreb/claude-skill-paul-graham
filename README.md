<p align="center">
  <img src="./assets/banner.svg" alt="Paul Graham — a Claude Code skill on startups and high agency" width="100%" />
</p>

# claude-skill-paul-graham

> A Claude Code skill that puts Paul Graham's frameworks into every
> brainstorming session — so when your brain hasn't reached for the
> right essay, Claude does.

The point isn't to look up PG when you remember to. It's that when you're
thinking out loud with Claude about an idea — *"I'm thinking about
building X," "should I quit my job for this," "is this even worth doing"* —
the right PG frame (schlep blindness, do things that don't scale, default
alive, top idea in your mind, make something people want) shows up in the
conversation *before* you'd have reached for it on your own.

It's PG sitting next to you while you brainstorm, instead of PG on a
shelf you'd have to remember to open.

## What this is

Paul Graham has written ~230 essays at [paulgraham.com](https://www.paulgraham.com/articles.html).
They are some of the most useful writing on startups, founders, and high
agency that exists — and they are completely unsearchable by what you
actually need.

This repo distills ~40 of them, organized by theme, with **proactive
trigger rules** so Claude surfaces the relevant frame the moment you
start reasoning through a startup decision — even if you don't ask, and
even if you've never read the essay.

## What's inside

```
skills/paul-graham/
├── SKILL.md
└── references/
    ├── INDEX.md           # master list of all curated essays
    ├── high-agency.md     # ambition, agency, doing things that don't scale
    ├── startup-ideas.md   # finding, validating, schlep blindness
    ├── founders.md        # what makes a great founder
    ├── growth.md          # startup = growth; doing things that don't scale
    ├── fundraising.md     # raising money without losing your mind
    ├── product.md         # make something people want
    ├── mental-models.md   # top idea in your mind, taste, life is short
    └── SOURCES.md
```

Each essay entry has:
- **Canonical URL** at paulgraham.com
- **One-line thesis** (our synthesis)
- **Key excerpt** (≤90 words, fair-use)
- **When this applies** — concrete situations the skill should surface it

## Install

### As a user-level skill (available everywhere)

```bash
git clone https://github.com/lonexreb/claude-skill-paul-graham.git
mkdir -p ~/.claude/skills
cp -r claude-skill-paul-graham/skills/paul-graham ~/.claude/skills/
```

### As a project-level skill (just this repo)

```bash
cd your-project
git clone https://github.com/lonexreb/claude-skill-paul-graham.git .pg-skill
mkdir -p .claude/skills
cp -r .pg-skill/skills/paul-graham .claude/skills/
```

That's it. Open Claude Code, ask a startup or founder question, and the skill
auto-activates.

## How it shows up in a brainstorm

See [`examples/`](./examples/) for full transcripts. Quick taste:

| You say (mid-brainstorm) | Claude surfaces |
|---|---|
| "Thinking about a tool for vendor invoice reconciliation. Sounds boring." | Schlep Blindness — boring is a moat |
| "I want to be more ambitious but I can't focus." | The Top Idea in Your Mind — what's actually occupying the slot? |
| "Not sure if this idea is too small." | Frighteningly Ambitious Startup Ideas — find the wedge into the big version |
| "I should probably set up a funnel." | Do Things That Don't Scale — not yet; go meet the user |
| "How do I know if a co-founder is right?" | What We Look for in Founders + Mean People Fail |

## What's NOT in here

This skill is for **timeless principles**. It does not cover:

- Current YC application logistics or deadlines
- Specific legal, tax, or incorporation advice
- Market timing or recent startup news
- Anything that requires fresh data — use WebFetch for that

## Attribution

Essays © Paul Graham, all rights reserved.
This is an unofficial fan project. See [ATTRIBUTION.md](./ATTRIBUTION.md).

## Contributing

Want to add an essay, fix a thesis, or extend a theme? PRs welcome.
Two rules:

1. Excerpts stay ≤ 90 words.
2. Every entry links to paulgraham.com.

## License

MIT for our code and structure. PG's essays remain his copyright.
See [LICENSE](./LICENSE) and [ATTRIBUTION.md](./ATTRIBUTION.md).
