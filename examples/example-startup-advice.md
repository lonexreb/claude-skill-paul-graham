# Example: Startup Advice

Sample Claude Code session showing how the `paul-graham` skill routes a
typical founder question.

---

**User:**
> I have a stable senior eng job at a big company. I keep thinking about
> starting something but I have no idea, no co-founder, and I don't think
> I'm "the type." Should I just stay where I am?

**Claude (with `paul-graham` skill active):**

You're describing three things PG has written about specifically, so let me
take them one at a time.

**"I have no idea."** Paul Graham, in *["How to Get Startup Ideas"](https://www.paulgraham.com/startupideas.html)* (2012),
argues that the best ideas are *noticed*, not generated. You don't sit down
and think them up. They come from living in the future — being deep in some
domain or community where you naturally notice things that should exist.

You already have one: a big-company senior eng role. What annoys you every
day at work that wouldn't exist if someone had built the right tool? That's
the start of an idea, and it has a built-in user (you) and a built-in
market (people like you).

**"I don't think I'm the type."** PG covers this directly in
*["Why to Not Not Start a Startup"](https://www.paulgraham.com/notnot.html)* (2007) — the "I'm not the type"
objection is one of the classic rationalizations. The real founder traits,
he writes in *["Relentlessly Resourceful"](https://www.paulgraham.com/relres.html)* (2009), aren't credentials
or personality — they're the willingness to figure things out under
pressure. If you have shipped a hard project at work, you probably have
that.

**"No co-founder."** This is the genuinely hard one. Solo is harder than
co-founded, but it's not disqualifying. PG would say: don't pick a random
co-founder to fix the loneliness — that's worse than going solo. The right
order is **find the itch first, build the smallest version, then look for
a co-founder among people who care about the same problem**.

A concrete next step: spend two weekends on the most annoying part of your
current job. Build the dumbest tool that fixes it. See if anyone you work
with would use it. That's a much better signal than another month of
thinking.

---

## Why this works

- The skill auto-triggered on "starting something," "founder type," and
  "should I stay" — all in the trigger set.
- Claude pulled from three reference files (`startup-ideas.md`,
  `founders.md`) and cited the specific essays + URLs.
- The response applies PG's frames to the user's specific situation
  rather than reciting the essay.
- Every quote/citation links to paulgraham.com so the user can read the
  full essay.
