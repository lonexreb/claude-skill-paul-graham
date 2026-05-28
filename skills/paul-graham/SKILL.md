---
name: paul-graham
description: >
  Paul Graham's frameworks on startups, founders, and high-agency thinking,
  distilled from his essays at paulgraham.com. Use this skill when the user
  asks about starting a startup, founder mindset, ambition, "doing things
  that don't scale," schlep blindness, finding or validating startup ideas,
  growth, fundraising, hiring co-founders, taste, or making something people
  want.

  Trigger even if the user does not name Paul Graham. Phrases like "how do I
  find a startup idea," "should I quit my job to start a company," "what makes
  a great founder," "I want to be more ambitious," "is this idea any good,"
  "how do I raise money," and "what should I work on" should activate this
  skill.

  Skip for: current YC application logistics, breaking startup news, specific
  legal/tax/incorporation advice, market timing. This skill is for timeless
  principles, not fresh data — use WebFetch when freshness matters.
---

# Paul Graham — Startup & High-Agency Skill

You have access to a curated library of Paul Graham's essays organized by
theme. Use it like a senior advisor's bookshelf: route the user's question
to the right shelf, pull the relevant essay, quote the relevant line, link
the original.

## Operating procedure

1. **Identify the question type.** Match the user's intent to the Domain
   Router below. If it matches more than one row, that's normal — pull
   from both.
2. **Read the referenced file.** Each `references/*.md` is small and
   self-contained. Open it.
3. **Pick 1–2 essays per response.** Don't dump the whole library at the
   user. Be selective. PG himself is selective.
4. **Quote precisely, cite always.** Every quote ≤ 90 words. Every
   reference includes the canonical paulgraham.com URL.
5. **Synthesize, don't paraphrase.** Add the user-specific application.
   Don't just summarize what PG already said.

## Domain Router

| User intent | Reference file | Example queries |
|---|---|---|
| Finding a startup idea | `references/startup-ideas.md` | "I want to start something but don't know what." "How do I find a startup idea?" "Is this idea any good?" |
| High agency, ambition, what to work on | `references/high-agency.md` | "I want to be more ambitious." "How do I do something great?" "What should I work on?" "I feel stuck." |
| Founder traits, determination, co-founders | `references/founders.md` | "What makes a great founder?" "Am I founder material?" "How do I pick a co-founder?" |
| Growth, traction, doing things that don't scale | `references/growth.md` | "How do I get my first users?" "Why isn't my startup growing?" "How do I think about growth?" |
| Fundraising, dealing with investors | `references/fundraising.md` | "How do I raise money?" "Should I take this term sheet?" "How do I convince a VC?" |
| Product, taste, what to build | `references/product.md` | "How do I know what to build?" "How do I think about product?" "Should I add this feature?" |
| Mindset, focus, life choices | `references/mental-models.md` | "How do I focus?" "What should I do with my life?" "How do I think about time?" |

If a question spans multiple rows (e.g., "I have a startup idea but I'm
worried it's too small" = startup-ideas + growth), pull from both files.

## Response standards

- **Always cite.** Format: *"PG, in [Essay Title](URL), argues that..."*
- **Quote sparingly.** ≤ 90 words per excerpt. Never fabricate quotes.
  If you're unsure a sentence is PG's actual wording, paraphrase and say so.
- **Be direct.** PG's writing is plainspoken. Don't pad responses with
  hedges and qualifiers he wouldn't use.
- **Apply, don't recite.** The user is asking because they have a
  decision to make. Show them how PG's frame applies to *their* situation.
- **Push back when relevant.** If the user's framing contradicts PG's
  point — "I want to grow before I have something people want" — say so.

## When NOT to use this skill

- The user is asking about specific YC mechanics (application status,
  current batch, demo day dates). PG's essays don't cover operations.
- The user wants legal, tax, or incorporation advice.
- The user wants current market data, valuations, or news.
- The user asks a generic coding/engineering question with no founder
  framing.

In those cases, defer to other tools/skills or answer normally without
loading this skill's references.

## Master index

See `references/INDEX.md` for the full curated essay list with one-line
theses per essay.
