# Excerpts from Mark's Substack

Verbatim lines from https://markphammm.substack.com/, grouped by the job they do in a post. Use them to calibrate rhythm and tone; do not copy them into new posts.

## Titles and subtitles

- "I just wanted to send someone an ERD, so I built a CLI and a VS Code extension" / "Quickdbd has ten tables for free, then everything turns into "Table 11". So I made my own."
- "People version control everything except the file that gets them a job" / "You tell me if this is over-engineering or not"
- "Power BI or Tableau? Wrong question." / "The dashboard principles that survive every tool migration"
- "I tell people I'm an AE, but wtf does that mean?" / "And no it's not Account Executive for god sake"
- "I re-learn Spark (Again) - Part 1" / "This time it finally clicks"

## Hooks

> Every data project I have worked on has the same moment. Someone new joins, or a stakeholder asks "wait, how does `orders` connect to `customers` again?", and I go looking for the ERD.
>
> And the ERD is always one of these:
>
> ```
> erd.png                  (from 6 months ago, 3 tables missing)
> erd_v2.png               (someone's screenshot, half cropped)
> schema_FINAL.drawio      (nobody has edit access)
> ```
>
> Surprisingly "un"professional ¯\_(ツ)_/¯

> People keep asking me the same thing: should I learn Power BI or Tableau?
>
> And I honestly don't think it matters that much.

> `SQL` lives in Git. `dbt` lives in Git. `Terraform` lives in Git. [...] But there is one file I have probably edited dozens of times without ever thinking seriously about version control: my resume.

## Intros

> Hi everyone, I'm Minh, an Analytics Engineer at Infinite Lambda, an AI and Data consulting company headquartered in London. Today I want to talk about a slightly controversial, and probably slightly over-engineered topic: version controlling your resume with Git.

> So this project asks the opposite question: how much of that can I delete if I let a managed vendor do the extract and the load?
>
> The answer turned out to be "almost all of it, and the interesting problems move somewhere else."

## Opinion voice

> I've used Tableau. I've used Power BI. I've dashboarded in Streamlit like a psychopath. I've used Mode and Hex, and those two are my favorites. And tomorrow my company could decide to migrate everything to Sigma for all I know.
>
> The tool changes. The principles don't.

> If yes, good dashboard. If no, you made expensive wall art.

> The dataset is the product. If the dataset is garbage, every chart, every model, every "data driven" decision on top of it is also garbage, just garbage with a nicer font.

> Then the company grows. Now it's not five sources, it's fifty. Salesforce, Stripe, Google Ads, Meta, and some vendor API still returning XML in the year of our lord 2026.

> So somebody flipped two letters and the entire industry changed. ETL became ELT.

## Build-log voice

> 10 tables. My `bronze` layer alone is more than 10 tables. Insurify's dbt project was reaching 1500 models when I left.

> That PNG is frozen. Add a column next week and the picture is already lying.

> Python 3.11+, and that's it. No Node, no Graphviz, no browser needed. I was pretty stubborn about this one, because "just install these 4 system dependencies first" is how a tool dies on a teammate's laptop.

> That last one is honestly my favourite. "How do I get from `order_items` to `customers`?" Click, click, here's the join.

## Tutorial voice

> The work does not disappear, it relocates. I did not write a line of extract-load logic, and in exchange I had to actually learn what a replication slot is and how Snowflake's role hierarchy works. I think that is a good trade.

> Those three columns are the most interesting thing in this entire project, and part 3 is essentially one long argument about them. For now, just notice they are there.

## Thoughts sections

> Probably, idk, you decide - If your project has 8 tables, open QuickDBD and you're done. You don't need any of this.

> It's the same thing I keep writing about. If something gets edited, reviewed and shared over and over, it should be text, in git, with a history. The resume, the laptop setup, and now the ERD.
>
> The picture is just a build artifact. The text is the source of truth.

> I am still not at the point where I open a pull request and self-approve my own resume.

## Endings

> None of us are calling you about your car insurance.

> If you try it on your own dbt project and something looks weird, open an issue. Fair warning, I will probably ship the fix the same day, because I have zero chill about this project :")
>
> Feel free to dm me to learn more about it

> If you enjoyed this, please react or share so I know to keep going. Thanks for reading this far.
>
> Feel free to connect with me and ask any question
