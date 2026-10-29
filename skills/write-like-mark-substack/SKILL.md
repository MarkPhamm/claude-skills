---
name: write-like-mark-substack
description: Write a Substack post, intro, outro, title or LinkedIn blurb in Mark (Minh) Pham's voice, matched to his posts at https://markphammm.substack.com/. Use when asked to draft, rewrite or "make it sound like me / like my Substack" for any data, analytics engineering, or tooling write-up.
---

# Write like Mark's Substack

Mark (Minh) Pham is an Analytics Engineer at Infinite Lambda (AI and Data consulting, London), previously at Insurify (startup, Redshift, ~1500 dbt models), TCU class of 2025. His Substack is about data engineering, analytics engineering, and the tools he builds or re-learns.

Match the voice of his **posts from June 2026 onward**. In "I tell people I'm an AE, but wtf does that mean?" (2026-06-20) he said he was done writing "the polite way": more personal, more hot takes, more swearing, still data. His 2025 posts are more polished, use emoji, and read like generic blog copy; do not imitate those.

## Before writing

1. Read [references/excerpts.md](references/excerpts.md): real lines from his posts, grouped by job (hook, intro, punchline, ending).
2. If the topic overlaps something he already wrote, or the excerpts feel thin, pull his latest posts and read the closest one or two:

   ```sh
   python3 -I ~/.claude/skills/write-like-mark-substack/scripts/fetch_posts.py /tmp/mark_substack
   ```

   It writes one plain-text file per post (title, subtitle, date, body). Reference his earlier posts by name when the new one builds on them ("same thing I complained about in my resume article").
3. Decide the post type, because it sets how loud the voice is:
   - **Opinion / explainer** ("Power BI or Tableau? Wrong question.", the AE post): short punchy paragraphs, hot takes, swearing allowed (a few per post, never every paragraph), the kitchen analogy.
   - **Build log** ("I just wanted to send someone an ERD, so I built a CLI..."): pain point first, then what he built, commands, real numbers, a self-aware "is this over-engineering?" section.
   - **Tutorial / series** (the zero-infrastructure pipeline parts): calmer, step by step, no swearing, still first person and honest about trade-offs.

## Voice

- **First person, talking to one reader.** "I", "you", contractions. Sounds like explaining something to a colleague over Slack, not a conference talk.
- **Short sentences.** Recent posts average 12-18 words. Punchlines get their own one-line paragraph: "The tool changes. The principles don't." / "Technically correct, practically useless." / "It's a new role. The person who only cooks."
- **Hot take, then the reason.** State the opinion flat ("I honestly don't think it matters that much."), then back it with experience. Concede the other side in a line ("If your project has 8 tables, open QuickDBD and you're done.").
- **Self-deprecating and hyperbolic humour.** "I've dashboarded in Streamlit like a psychopath", "stitch them together like it's 2009", "some vendor API still returning XML in the year of our lord 2026", "I have zero chill about this project".
- **Text emoticons, sparingly:** `¯\_(ツ)_/¯`, `=))))`, `:")`. At most one or two per post. No emoji.
- **Casual markers he actually uses:** "honestly", "actually", "pretty", "basically", "idk", "wtf", "TLDR", "Quick detour on...", "Fair warning,", "So yeah,". Do not stack them.
- **Concrete over abstract.** Real file names, real commands in code blocks, real numbers (145 tables, 235 relationships, 1,500 lines of Python), named tools and people he credits (Vu Trinh, Matt David's book).
- **Honest about trade-offs.** "The work does not disappear, it relocates." Say what got harder, not only what got easier.
- **British spelling** in recent posts: favourite, colour, neighbours.
- Keep his casual grammar, but do not add typos on purpose.

## Recurring ideas he returns to

Use them when they fit the topic; do not force all of them in.

- **If something gets edited, reviewed and shared over and over, it should be text, in git, with a history.** Resume, laptop setup, ERD. "The picture is just a build artifact. The text is the source of truth."
- **The kitchen analogy:** warehouse = kitchen, dataset = dish, dashboard = the plate that hits the table. DE hunts and drives the truck (extract, load), AE cooks (transform), DA/DS run the dining room.
- **Garbage in, garbage out**, usually as "just garbage with a nicer font".
- **Fundamentals over tools:** "The tool is just where the buttons are."
- **Decisions, not dashboards:** "Can someone make a better decision because of what you built?"
- **"Is this over-engineering?"**, asked of his own project, answered with "Probably, idk, you decide" and when it is worth it.

## Shape of a post

- **Title:** a first-person story or a contrarian claim. "I just wanted to X, so I built Y", "People version control everything except the file that gets them a job", "<Common question>? Wrong question."
- **Subtitle:** one punchy aside or joke. "And no it's not Account Executive for god sake", "You tell me if this is over-engineering or not".
- **Hook first:** a relatable pain, often shown as a code block or list of the mess (`resume_final_v2.pdf`, `erd_v2.png (someone's screenshot, half cropped)`), then a one-line verdict ("Surprisingly “un”professional ¯\_(ツ)_/¯").
- **Intro line** (build logs and tutorials): "Hi everyone, I'm Minh, an Analytics Engineer at Infinite Lambda, an AI and Data consulting company headquartered in London." Then "Today I want to talk about..." or "This post is about why, and how...". Use "Mark" instead of "Minh" only if asked.
- **TLDR or Takeaway near the top** of long posts: 3-5 bullets of what the reader gets.
- **Numbered headers** for build logs (`## 1. Intro`, `### 2.1 ...`), with headers that are claims, not labels ("Then you hit table 11", "Screenshots go stale the moment you send them").
- **Thoughts section near the end:** the self-aware question, then "The bigger idea" tying it back to a recurring idea.
- **Series:** "This is part 1 of three", tease the next part's twist, "Part 3 - CDC (you are here)".
- **Ending:** a one-line callback punchline ("None of us are calling you about your car insurance."), then his sign-off, picked to fit:
  - "If you enjoyed this, please react or share so I know to keep going. Thanks for reading this far."
  - "Feel free to dm me to learn more about it" / "Feel free to connect with me and ask any question"

## Avoid

- Corporate or generic blog phrasing: "In today's fast-paced data landscape", "leverage", "unlock", "Let's dive in!", "In conclusion".
- Emoji, and closing on a moral ("Use exposures to make your dbt project not just a data pipeline but a documented, traceable system of insights." is the old style he moved away from).
- Long, balanced, hedged paragraphs. Pick a side.
- Swearing in tutorials, or swearing in every paragraph of an opinion post.
- Inventing facts about his jobs, projects or numbers. If a detail is not in the request or his posts, leave a `[TODO: ...]` for him to fill.

## Output

Write in Markdown that pastes into Substack: `##`/`###` headers, `-` bullets, fenced code blocks, `[image: what the screenshot should show]` where he would drop a screenshot. Hand over the draft, then list any `[TODO]`s in one short line.
