---
layout: post
section: "Expanding the Architect's Toolkit"
title: "Decision Intelligence in IT Architecture: Learning From Data, Social, and Managerial Fields"
position: 9026
podcast: decision-intelligence.mp3
spotify: https://open.spotify.com/episode/5yz8glpHVNYA4qJXH8tFh1?si=968-czNVQiC_lvPIGGaR6w
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
icon: decision.png
permalink: decision-intelligence
timetoread: 11 min
excerpt: "Decision intelligence is the discipline of turning information into better actions. It includes strategies for
improving decision-making, reliable data-driven decisions, and avoiding biases."

---

<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover"
src="assets/images/istock/iStock-1365878406.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/sasunbughdaryan">sasun bughdaryan</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>
<style>
 .quote {
     border-left: 8px solid #d9ead3;
     padding-left: 36px;
     margin-top: 30px;
     margin-bottom: 40px;
     font-size: 140%;
     font-style: normal;
     color:#888;
 }
    @media only screen and (max-width: 768px) {
        [class= "quote"] {
            display: none;
        }
    }
    h3 {
        margin-top: 32px;
    }
    h4 {
        margin-top: 32px;
    }
</style>

> **IN THIS SECTION, YOU WILL:**  Learn the basics of decision intelligence, the discipline of turning information into
> better actions, and its relevance for an IT architecture practice.
>
> **KEY POINTS:**
> * Decision intelligence is the discipline of turning information into better actions.
> * A decision involves more than just selecting from available options; it represents a commitment of resources you
    cannot take back.
> * Many factors make the decision-making process more or less complex, such as the number of options, costs, cognitive
    load, emotions, and access to information.
> * Data can significantly improve decision-making, but data do not guarantee objectivity and can even lead to more
    subjectivity.
> * Group decision-making offers significant advantages but increases complexity as it requires higher decision-making skills from each member.

<br>
**Decision intelligence** is the discipline of turning information into better decisions. It combines **applied data science**, **social science**, and **managerial science** to help people make better choices under real-world constraints. **[Cassie Kozyrkov](https://en.wikipedia.org/wiki/Cassie_Kozyrkov)** has done a great deal to popularize the field, and I regularly recommend her [posts](https://www.linkedin.com/pulse/introduction-decision-intelligence-cassie-kozyrkov/) and [online lessons](https://www.linkedin.com/learning/decision-intelligence/) to architects.

<div class="quote">
"Excessive complexity is nature's punishment for organizations that are unable to make decisions." -Gregor Hohpe
</div>

In this chapter, I want to share a few useful lessons from her work and how they apply in IT architecture. Architects exercise decision intelligence every day:

* By **making decisions** (e.g., deciding which cloud provider and services to use when moving applications from a
  private data center to a public cloud).
* By **creating mechanisms** for teams to make better decisions (
  e.g., [advisory forums](https://martinfowler.com/articles/scaling-architecture-conversationally.html)).
* By **creating [options](https://architectelevator.com/architecture/architecture-options/)** for teams to make
  decisions later.

Decision intelligence is therefore central to architectural work.

Within the broader arc of this book, this chapter extends the earlier discussion of bias and judgment into a more operational discipline. If Grounded Architecture is about connecting data, people, and operating models to real outcomes, decision intelligence explains how those ingredients actually become better choices.

![](assets/images/istock/iStock-1194231226.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/francescoch">francescoch</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

<br>
## Basics of Decision-Making

It helps to start with a few basics: decisions, outcomes, and goals.

### Decision Is More Than Selecting Among Options

Kozyrkov defines a decision as more than just selecting from available options. A decision represents **an irrevocable
allocation of resources**, which could be monetary, physical actions, time, or options. Whatever you decide to do, you
will spend some time and other resources on it and will not get that time and resources back. The only way to reverse
the consequences of some decisions is to invest more resources in that reversal.

<div class="quote">
"If you ever drop your keys into a river of molten lava, let 'em go... because man, they're gone!" -Jack Handy
</div>

Less obviously, optionality is also a resource. Choosing between two options may seem cost-free. However, the
possibility of selecting some options is frequently lost once you decide. This loss of opportunity is considered an
irrevocable allocation of resources. For instance, before starting a project in IT, you can select from many programming
languages and frameworks to implement your system. However, after that, it is very costly to change that decision as you
need to rewrite your system entirely in another language.

Having or losing options is directly related to a frequent topic in IT: vendor lock-in, which is one of the main drivers
behind [creating or avoiding lock-in](https://martinfowler.com/articles/oss-lockin.html). Lock-in in IT refers to a
situation where a customer becomes dependent on a specific vendor for products and services, making switching to an
alternative solution difficult, costly, or time-consuming. This dependency can result from proprietary technologies,
high switching costs, contractual obligations, or the significant effort required to migrate data and systems.

From an IT architecture perspective, another important lesson of this view on decisions is that if there is no
irreversible allocation of resources, we cannot talk about decisions. Ivory tower architects who make "principal
decisions" that no one follows are technically not making any decisions.

### Outcome = Decision x Luck

An outcome is **a result of a decision**. Two factors influence it:

* **the quality of the decision-making process** and
* an **element of randomness**, or **luck**.

We can control the decision-making process, but not luck. If we judge decisions only by outcomes, we can easily mistake good luck for good judgment, and bad luck for bad judgment.

To fairly judge a decision, we need to look at the context and the information available when the decision was made.
Consider a simple example: you choose the route that appears 30 minutes faster, but an accident causes a traffic jam after you start driving. The outcome is bad, but that does not automatically mean the decision was poor. At the time, the available information supported it.

The COVID-19 pandemic is a strong recent example. It reshaped the global economy abruptly. Some industries, like travel and tourism, took a severe hit (e.g., Uber, Booking.com,
and [Airbnb](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9998299/)). On the flip side, however, COVID-19 boosted online
tools' rocket boost. It birthed a new era of virtual collaboration (think Zoom, Microsoft Teams, Slack, Miro).

We cannot control the dice roll, but we can improve the quality of the decision process.

### Economics of Decision-Making

Not all decisions deserve the same level of effort. The concept of "[value of clairvoyance](https://en.wikipedia.org/wiki/Value_of_information)" helps estimate how much time, information, and analysis a decision is worth.

For low-stakes decisions, perfectionism is wasteful. High-stakes decisions, by contrast, deserve much more care. Kozyrkov suggests the following approach:

1. **Visualize the Best and Worst Outcomes**: Start by picturing your decision's potential paradise and disaster
   scenarios. This helps you grasp the stakes involved.
2. **Apply the "Value of Clairvoyance" Technique**: Imagine you could know the correct answer in advance. How much
   would you reasonably spend in money, time, or effort for that level of certainty?
3. **Balance Investment with Importance**: This little exercise helps you determine the value of achieving perfect
   clarity and making the best choice.

If perfect information would not be worth much, the decision probably does not justify heavy analysis. This framing helps balance decision effort against decision importance.

Choosing a public cloud provider is a high-impact decision and deserves serious analysis. Approving a developer license that can be canceled at any time is not. Yet many organizations apply similar ceremony to both.

The practical lesson is simple: reserve heavy decision processes for decisions that actually justify them.

<br>
## Preparing for Making Decisions

Decisions are the steering wheel for reaching our goals. Consequently, it is crucial to understand and define goals
properly and to understand whether a decision needs to be made at all.


### Setting Goals

Practical goal setting requires clarity about priorities and opportunities. Without that clarity, decision-making becomes noisy and reactive.


![](assets/images/istock/iStock-1301200404.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/DilokKlaisataporn">Dilok Klaisataporn</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

Common goal-setting failures include goals that are too vague to guide action or too rigid to survive reality. A better approach uses **layered goals** with different purposes: outcome, performance, and process goals.

* **Outcome Goals**: These are the grand finales, the ultimate wins, but they can be as vague as a politician's promise
  and influenced by things beyond your control. It's like "creating value for customers" and "being profitable." Nice,
  right? But how do you measure "value" and "profit" when you're busy fighting off existential crises?

* **Performance Goals**: These goals are measurable and, if you're not aiming for the moon, primarily within your
  control. In business, it's all about increasing website visits, slashing infrastructure costs, and boosting revenue.
  They're aspirational and tricky to manage, but hey, no pain, no gain.

* **Process Goals**: They're measurable and entirely within your control. In business, this translates to rolling out
  new features on time or launching a targeted marketing campaign. These goals keep you on track but should always serve
  your higher aspirations.

You need all three types of goals neatly connected like a well-oiled machine. For example, running a flashy marketing
campaign (a process goal) should attract more visitors to your site and boost revenue (performance goals), ultimately
delivering more value to customers and fattening your bottom line (outcome goals). Consolidating IT infrastructure (a
process goal) should trim overall costs (a performance goal), making your business more profitable (an outcome goal).

But beware! Don't let process goals hog the spotlight and distract you from the big picture. Wise goal setting is all
about layering your goals, aligning them with your priorities, setting ambitious targets, and establishing manageable
processes, all while staying flexible and responsive to life's curveballs.

### Aligning Goals: The Principal-Agent Problem

One of the classic challenges in complex organizations is the **principal-agent problem**: the interests of the decision-maker (the agent) differ from those of the owner or sponsor (the principal). If unmanaged, that divergence leads to poor decisions and poor incentives.

![](assets/images/istock/iStock-1446703605.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/MariaStavreva">Maria Stavreva</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>


In IT, **technology selection** is a common example. Individual teams may prefer the newest tools or the technologies they personally enjoy. But if every team optimizes locally, the overall landscape becomes harder to train for, support, and evolve.

The usual response is to create **rules or constraints** that align local decisions with broader organizational interests.

This principle also applies to personal decision-making, especially when juggling **short-term temptations** and **long-term
goals.** By setting up **pre-emptive constraints,** you can steer your choices toward those long-term dreams and avoid
decisions that may look attractive in the short term but create avoidable regret later.

For instance, in technology selection, one strategy I often use is to
create "[golden paths](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/)"
—supporting a limited set of technologies and making it harder to create unnecessary fragmentation.

This is not about restricting teams for its own sake. It is about preserving alignment and avoiding unnecessary fragmentation.

### Is There A Decision To Be Made?

In many situations, especially when you are not the formal decision-maker, it is important to determine whether there is actually a decision to be made. Sometimes the outcome has already been fixed and the process is only being staged.

![](assets/images/istock/iStock-1303761470.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/PheelingsMedia">Pheelings Media</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

Before investing effort, clarify whether there is genuine room for choice. According to Cassie Kozyrkov, this starts with two simple steps.

1. **Check the Default Direction**: Determine what the primary decision-maker would do if you were not involved.
2. **Ask the Critical Question**: Ask, “**What would it take to change your mind?**" If the honest answer is "Nothing,"
   then there is no real decision under discussion.

This question is useful for several reasons:

1. **Starts Insightful Conversations**: It reveals how the decision-maker is thinking about the problem.
2. **Identifies the Decision-Maker**: It helps you figure out if the person you're talking to is the real decision-maker
   or just a messenger.
3. **Detects Real Decisions**: If no information can change their mind, then there is no real decision to be made.

This question helps you map the decision-making landscape, gauge openness to new information, and determine whether there is genuine room to influence the outcome. If not, you can conserve energy for decisions that are still open.

<br>
## Decision-Making Complexity

Some decisions are easier to make than others. Kozyrkov identifies 14 factors that can make decision-making more or less
complex:


![](assets/images/istock/iStock-1043738948.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/chaiyapruek2520">chaiyapruek2520</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>


### Number of options

Decision-making becomes simpler with **fewer options.** When choosing between a limited number of options, it's
straightforward. However, as more options, especially combined choices, are introduced, the process becomes more
complex, involving **compound decision-making** (several dependent decisions you must make together). The simplest
scenario is a straightforward yes or no decision.

### Clarity of options' boundaries

Some decisions are straightforward when the choice is **clear-cut,** like choosing your meal between a rock and an
apple, where the preferable option is obvious. Deciding between two varieties of apples is slightly more challenging.
Still, it remains easy if the decision **isn't significant or high-stakes**. In IT, having a preferred public cloud
provider provides a clear-cut decision about public cloud hosting. Once inside a public cloud, selecting an appropriate
service is much more challenging as hundreds of options are available.

### Clarity of objectives

Having **clear objectives** is another factor that simplifies decision-making. It involves considering the most
effective approach to the decision and quickly determining the criteria for making that choice.

### Cost of making a decision

**Low-cost** of decision-making simplifies decision-making. These costs include the effort required to **evaluate**
information, the ease of **implementing** the decision, and the potential **consequences of any mistakes**. Decisions
are easier when these associated costs are low.

### Costs of reversing a decision

While decisions typically involve a commitment of resources you can't undo, some are considered reversible. If you can **change your decision quickly and with little cost**, the consequences of a wrong choice are less severe, making the decision easier.

### Cognitive load

If a decision requires **significant mental effort**, such as remembering **many details** or making choices while **distracted,** it becomes more challenging. On the other hand, if you can make the decision easily and consistently, even amidst other tasks or distractions, then it's a simpler decision.

A lot of IT architects' work involves creating visualizations and abstractions that can reduce cognitive load and help
others make better decisions about complex systems.

### Emotional impact

If a decision doesn't **evoke strong emotions** or significantly affect you emotionally, it tends to be easier.
Conversely, decisions that stir up intense emotions or leave you highly agitated are more difficult.

For instance, the company's decision to use only one frontend programming language significantly affects people
unfamiliar with the choice, as they cannot perform at a senior level in new technology for a long time and need to learn
many new things. Many people negatively affected by this choice may decide to leave and find a job where they can work
with technologies in which they are experts. So, a simple technological decision quickly becomes a personal
career-making choice and an HR issue.

### Pressure and stress

Decisions made under conditions of **low pressure and stress** are generally easier. In contrast, those made in
high-pressure, stressful situations are more challenging.

### Access to information

Decisions are easier when you **have complete and reliable information readily available**. In contrast, making
decisions with only partial information and uncertain probabilities is more challenging. As discussed in the context of
statistics, having limited information complicates the decision process as you need to guess missing pieces of
information.

### Risks and ambiguity

Decisions become simpler when there is no **risk or ambiguity involved.** Risk and ambiguity, though different, both
complicate decision-making. Ambiguity arises when the probabilities of outcomes are unknown,
making choices uncertain. On the other hand, risk involves taking a known gamble, where you understand the potential
consequences and likelihoods.

### Timing

Difficulties arise when the **decision's timing
conflicts with other simultaneous decisions** or when there's **insufficient time** to consider the choice thoroughly.
Situations requiring a rapid response can add significant pressure, making the decision process more challenging.

### Impact on others

Making decisions alone is generally easier. The process is simpler when you're the sole decision-maker, without
involving others, and the decision's outcome impacts only you. In contrast, making decisions in a social context is more
complex. Factors like **social scrutiny**, considering the **impact on others**, balancing **different preferences and
opinions**, and the potential
**effect on your reputation** all add to the difficulty.

### Internal conflicts

Decisions are more problematic when there are internal conflicts, as opposed to situations where all **motivations and
incentives align** with the decision. For instance, deciding to make shortcuts in your systems design and skipping steps
in a process to get some features quicker to the market vs. spending more time tidying and testing your code is a
typical dilemma many software engineers and IT architects face.

### Adversarial dynamics

Finally, adversarial dynamics impact decision-making. When you face **competition or opposition from others,** these
decisions become more challenging compared to those made cooperatively or independently. For example, when you merge two
companies with different technology stacks (e.g., one using React and Java in AWS, and another Angular and C# in Azure)
and want to consolidate on one stack, you may end up in competition and opposition with people from each company wanting
a consolidated stack to be as close as possible to their previous one.

<br>
## Decision is a Step in the Process

The Radical Candor book introduces a [productivity-focused strategy](https://www.radicalcandor.com/wp-content/uploads/2022/09/How-To-Get-Shit-Done-With-Radical-Candor.pdf) to improve decision-making processes, reduce time
spent in unproductive meetings, and enhance overall efficiency. The central premise of this methodology is that you
cannot just make a decision. To have any impact, you need to go through several steps: Listen, Clarify, Debate, Decide,
Persuade, Implement, and Learn.

![](assets/images/istock/iStock-1262959028.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/t_kimura">t_kimura</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

### Listen

The first step is to **Listen**. Gathering relevant data, feedback, and insights from various sources is crucial.
Understanding different perspectives from stakeholders, team members, and experts helps form a comprehensive view of the
situation. This step ensures a thorough **understanding of the situation** by gathering relevant data and insights from
various sources. It also ensures consideration of **diverse perspectives,** which helps form a well-rounded view of the
issue.

### Clarify

Next, you need to **Clarify**. Clearly articulate the issue or decision to ensure **everyone understands the context.**
Establishing clear, specific goals and desired outcomes for the decision is essential. This sets the stage for focused
discussions and aligned efforts. Clarifying the problem or decision you need to make ensures clear articulation and
alignment on objectives and desired outcomes. This step **eliminates misunderstandings** and ambiguities, solidifying the
foundation for focused discussions.

### Debate

Following clarification, the step is to **Debate**. Engage in discussing potential solutions and alternatives, weighing
the **pros and cons** of each option. Encourage an **open discussion** where team members can freely share their ideas and
constructively challenge each other's viewpoints. This collaborative approach helps in exploring various aspects of the
decision. Debating potential solutions ensures a thorough evaluation of all possible options. It promotes an open
exchange of ideas and constructive challenges, allowing for exploring various aspects and implications of the decision.

### Decide

Once the debate has provided a thorough evaluation of options, it's time to **Decide**. Choose the best course of action
based on the gathered information and discussions. Depending on your organizational culture, you may reach a consensus
among the team or have the decision made by a designated leader. The key is to make an **explicit and informed choice.** The
decision-making step ensures an informed and thoughtful choice based on the available information and discussions. It
provides a clear resolution and direction for moving forward, ensuring the best action is selected.

### Persuade

After making the decision, the next step is to **Persuade**. Clearly **communicate** the decision and the rationale behind
it to all stakeholders. It's essential to **gain buy-in** from team members and stakeholders by addressing their concerns
and objections, convincing them of the decision's validity and importance. Persuading stakeholders and team members
ensures effective communication of the decision and its rationale. This step secures buy-in and support, addressing and
mitigating any concerns or objections that may arise.

### Implement

With buy-in secured, you move to **Implement**. Execute the plan by **assigning tasks and responsibilities** to the
appropriate individuals. Ensure everyone understands their role in the overall plan, providing the **necessary resources**
and support to facilitate effective implementation. Alignment and clear communication are vital during this phase.
Implementing the decision ensures the execution of the plan through the assignment of tasks and responsibilities. It
ensures alignment and understanding of roles and the provision of necessary resources and support for successful
implementation.

### Learn

Finally, it's crucial to **Learn**. Monitor the implementation process and measure the outcomes against the set
objectives. **Collect feedback** from stakeholders and team members to assess the effectiveness of the decision. **Analyze the
results** to identify lessons learned and make necessary adjustments to improve future decision-making processes. This
continuous improvement approach helps **refine strategies** and **enhance productivity** over time. Learning from the process
ensures continuous improvement. Monitoring and measuring the implementation and outcomes, collecting and analyzing
stakeholder feedback, and identifying lessons learned all refine future decision-making processes.



<br>
## Decision-Making With Data and Tools

Decision-making has evolved beyond pen and paper, with data playing a crucial role in modern methods. Data, like the one
I use in [Lightweight Architectural Analytics](analytics), while visually appealing and powerful when used correctly, 
is **only a tool to assist** in making informed decisions. It's a means to an impactful end, but **without purposeful application, data is ineffective**.

![](assets/images/istock/iStock-1316937637.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/Blue Planet Studio">Blue Planet Studio</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

### Remember that data has limitations

Just as not everything written in a book is true, data can be **misleading or incomplete**. It's a collection of
information recorded by humans, subject to errors and omissions.

For instance, in artificial intelligence (AI), **AI biases stem from the data** it's fed, reflecting the choices and
prejudices of those who compile the data. The issues with AI bias are often due to poor decisions regarding data
selection. **Data isn't inherently objective**; it carries the **implicit values of its creators**.

Data's value lies in its ability to **enhance memory, not ensure objectivity**. Embracing data means embracing a
significant advancement in human potential. It's about transforming information into action, extending beyond the limits
of personal memory to make better, more informed decisions.

### Chose the right tool for the job

Cassie Kozyrkov groups data-analysis techniques into three [categories](https://kozyrkov.medium.com/what-on-earth-is-data-science-eb1237d8cb37):

1. **Analytics**: This is like using data as a telescope that can give you a clear view of the available data landscape.
   It's like having a magic map highlighting viable options, reasonable assumptions, and thought-provoking questions.
   Data and Analytics can spark those "Aha!" moments by revealing insights that were previously hiding in plain sight.
   For those "What's the weather like?" kinds of questions. Or "What is that service in our public cloud costing as $1M
   per year?"
2. **Statistics**: This is a core tool for decision-making under incomplete
   information and uncertainty. For example, "How likely am I to get struck by lightning?" or "What is the probability
   of downtime or our IT services (famous three, four, five-nines of uptime)?"
3. **Machine Learning (ML)/AI**: This is your army of data minions, ready to tackle a gazillion decisions and mountains
   of data without breaking a sweat. For the "Can I build a weather-predicting robot?" level of inquiries. Or "What will
   our IT costs be next year based on detailed traffic estimates?"

Used well, these techniques help you ask better questions and reach better-informed answers.

### Prefer complete information to partial information

No matter how you plan to use data, full information is always preferable to partial information. If you only have
partial information, you're dealing with uncertainty, and that's where statistical methods come in.

Statistics is used when you don't have all the facts and must manage uncertainty. They can help you balance the
likelihood of a wrong decision against your data budget, considering your risk preferences.

### Be in the driving seat

Just staring at data and crunching numbers isn't decision-making. As the decision maker, your job is to set the stage,
choose the relevant topics, frame the right questions, and guide the analysis like a maestro conducting an orchestra.

As a decision-maker, it's crucial to **ask the right questions**, and figure out **which decisions are worth your
brainpower**. Once you've identified those critical decisions, then—and only then—should you whip out the advanced
statistical or other methods to get more accurate answers in the murky waters of uncertainty. Diving into data without
asking the right questions is like wandering into a labyrinth with a blindfold on.

For architects, the practical lesson is that better decisions require more than more data. They require deliberate framing, thoughtful trade-offs, and the discipline to connect evidence to action. That is one of the clearest ways architecture creates leverage: by helping organizations decide better, not just document better.


<br>
## To Probe Further
* [Introduction to Decision Intelligence](https://www.linkedin.com/pulse/introduction-decision-intelligence-cassie-kozyrkov/), by Cassie Kozyrkov, 2020
* [Decision Intelligence: The steering wheel for your life](https://www.linkedin.com/learning/decision-intelligence/), by Cassie Kozyrkov, 2024
* [Making decisions right, even if they’re not always the right decision](https://architectelevator.com/strategy/always-be-right/), by Gregor Hohpe, 2021
* [Are IT's biggest decisions its worst?](https://architectelevator.com/transformation/it-decisions/), by Gregor Hohpe, 2019
* [Your most important architecture decisions might be the ones you didn't know you made](https://architectelevator.com/architecture/important-decisions/), by Gregor Hohpe, 2020


<br>
## Questions to Consider
Use the following questions to think about how decisions are framed, informed, and improved in your environment.

* *How do you typically approach decision-making in your professional role, and in what ways could you incorporate the
  principles of decision intelligence to enhance your decision-making process?*
* *Have you observed instances where excessive organizational complexity resulted from poor decision-making? How can IT
  architects address this, and what role can they play in simplifying decision-making processes?*
* *Reflect on a recent significant decision you made. Were you aware of the resources you were committing and the
  opportunities you were preceding? How could you have evaluated these factors more effectively?*
* *Think of a situation where the outcome of a decision didn't align with your expectations. How did you judge the
  quality of the decision-making process in hindsight, and did you consider the role of luck or randomness?*
* *Consider a recent decision you faced. What would have been the value of perfect information in that scenario? How
  does this concept help you balance the effort and resources you allocate to different decisions?*
* *How do you set and align your goals, and what challenges have you faced? Are there instances where misalignment has
  led to ineffective decision-making?*
* *What factors have you found to increase the complexity of decision-making in your experience? How do you manage these
  complexities effectively?*
* *How do you use data in your decision-making process? Are there instances where data has misled your decisions, and
  how can you safeguard against this in the future?*
