

# Operating Model: General Principles {#operating-model-principles}

![](assets/images/istock/iStock-2149699571.jpg)
^image by maria_castellanos from istock^

**IN THIS SECTION, YOU WILL:**  Understand that an effective architecture practice must be tailored to organizational needs, grounded in collaboration and clear rules of engagement, and focused on enabling teams through strategic alignment, distributed decision-making, and supported standards like golden paths.

{pagebreak}

A> **KEY POINTS:**
A> * **No one-size-fits-all architecture practice**: organizations must customize architecture to their specific challenges and most pressing issues.
A> * Successful architectural work depends on **collaboration with teams**, **distributed decision-making**, and clear **rules of engagement**.
A> * **Golden Paths** are essential for **reducing fragmentation** and guiding teams toward efficient, aligned development practices.
A> * Important architecture activities include **decision frameworks**, **legacy modernization**, **technical debt tracking**, and **strategic technology direction**.
A> * Architectural support is most effective when teams meet **baseline criteria**. Clear expectations and boundaries keep architectural work **scalable and high-impact**.

Each organization will have different architectural needs and contexts. When forming an architecture practice, I use as a starting point these [two pieces of advice from Gregor Hohpe](https://architectelevator.com/architecture/organizing-architecture/):

* *"Your architecture team’s job is to **solve your biggest problems**. The best setup is the one that allows it to accomplish that."*
* *"Your organization has to earn its way to an effective architecture practice. **You can't just plug some architects into the current mess** and expect it to solve all your problems."*

Taking Gregor Hohpe's points seriously means accepting that there is no universal operating model for architecture. You need to define the activities and working model that allow architecture to address your organization's most important problems.

In the broader flow of the manuscript, this chapter turns the Operating Model from a high-level concept into day-to-day practice. If the earlier chapters define the three pillars of the framework, this one explains the behavioral rules that make those pillars usable: how architects engage, how decisions are distributed, and how alignment is maintained without excessive control.

Whatever operating model you choose, it is crucial to establish **explicit agreements** and rules of engagement with key stakeholders. Without them, architecture work becomes inconsistent, difficult to scale, and easy to misunderstand.

This section outlines lessons I learned while defining IT architecture operating models. In the Grounded Architecture framework, the Operating Model is the set of **processes and agreements** that enables architects to do the work expected of an architecture practice. It should draw on Lightweight Architectural Analytics and Collaborative Networks to create data-informed impact across the organization.

## Examples of Architecture Activities

An Operating Model enables a structured and strategic approach to an architecture practice within the organization.

![](assets/images/istock/iStock-479875962.jpg)
^image by brauns from istock^

Here are examples of the activities I have been engaged in with architects to provide a clearer understanding of what I mean by an operating model.

* **Designing Mechanisms for Teams to Make Better Decisions**: These mechanisms involved creating global decision-support frameworks such as advisory forums facilitating informed discussions across teams. For compliance-sensitive projects, we establish formal design authorities. Additionally, we develop team-specific mechanisms, like escalation paths, to resolve decision conflicts effectively (e.g., when teams disagree on a common messaging middleware).

* **Supporting Teams in Their Daily Work**: This support entailed integrating into key team activities and aligning architectural work with team rituals to provide timely support. We assisted teams during all critical phases, such as reviewing architecture proposals before the commencement of a project or sprint, ensuring alignment with overall architectural standards.

* **Supporting Planned New Initiatives and Projects**: Ensuring seamless alignment between projects that require multi-team collaboration is crucial. We worked to facilitate communication and coordination, ensuring all teams are on the same page regarding project goals and requirements.

* **Supporting Teams in Dealing with the Legacy Landscape**: We provided data and insights about the legacy landscape, identifying problematic areas such as frequently changed, low-quality, untested legacy code. We helped define scenarios and roadmaps for legacy modernization, ensuring a structured approach to updating and maintaining legacy systems.

* **Tracking Tech Debt and Defining Tech Debt Reduction Programs**: This involves creating a centrally aligned backlog of technical debt and defining programs for its reduction. We integrate these programs into the planning processes to ensure that tech debt is managed proactively and effectively.

* **Performing SWOT and Other Analyses of Platforms and Systems**: Conducting deep dives to understand specific areas of the technology landscape. We performed SWOT (Strengths, Weaknesses, Opportunities, Threats) analyses and other assessments. These analyses helped in creating comprehensive plans and roadmaps for improvement.

* **Standardizing Processes and Documentation**: We defined standard templates for key documents such as Architectural Decision Records (ADRs), Technical Design Reviews (TDRs), and common diagrams. This standardization ensures consistency and clarity across all architectural documentation.

* **Supporting Merger and Acquisition (M&A) Activities with Expertise and Analyses**: We provided analyses, recommendations, and integration planning for mergers and acquisitions. Such support ensures that architectural considerations are well-integrated into M&A activities, facilitating smoother transitions and integrations.

* **Defining Key Technology Strategies**: We contributed to the development of essential technology strategies, including those for Cloud, Data, and Platforms. These strategies provide a clear roadmap for technological development and investment, ensuring alignment with business goals.

* **Defining Vision and Direction of Technology**: In collaboration with Engineering Leaders, we created a sustainable organizational setting that aligns with the overarching technology strategies. This work involved setting a clear vision and direction for the technology landscape within the organization.

## Guiding Principles for Architectural Excellence: Policies, Autonomy, and Engagement

An operating model becomes real only when it shapes daily behavior. In practice, that means deciding how architects engage with teams, where decisions are made, how much autonomy teams have, and what forms of alignment are non-negotiable.

My default stance is that architecture should be **collaborative, supportive, and early**. Architects should help teams make better decisions, not create approval queues. They should move constantly between daily support and long-range direction, using data to ground discussions and lightweight guardrails to prevent fragmentation.

The sections that follow describe the three ideas that matter most in this model:

* A high-level operating framework for how architects engage
* A distributed decision model that combines autonomy with transparency
* Golden Paths as the practical expression of alignment

### High-Level Operating Framework

The exact list of activities will vary by organization and will change over time. What should remain stable is the way the practice behaves. In my own work, I have usually relied on a common operational framework inspired by Gregor Hohpe's strategy-principles-decisions model (Figure 1). 

![](assets/images/arch/architecture-system.png)
**Figure 1:** *A common operating framework I typically use for Grounded Architecture activities.*

The framework has four defining characteristics:

**Engagement mindset**:
  * Architects work with teams in a **collaborative and supportive manner**.
  * The aim is to **strengthen team judgment**, not replace it.

**Contributions of architects**:
  * **Bring relevant data** to inform decisions leveraging [Lightweight Architectural Analytics](#analytics).
  * **Define decision boundaries** to enable minimal compatibility and strategic alignment (e.g., golden paths or tech stack constraints).
  * **Define fundamental principles** to facilitate consistency in decision-making.
  * **Share and generalize** lessons learned via [Collaborative Networks](#people).

**Social dynamics of architects**:
  * Architects spend their time in **constant motion** between team-level support and strategic work, helping the organization stay aligned between strategy and implementation.

**Shift left**:
  * Avoid **late-stage approval processes** in which architects mostly review decisions that are already difficult to change.
  * Bring architects in **early**, during planning and framing, when they can still influence the shape of the solution rather than react to it.

### Distributing Decisions, Autonomy, and Alignment

With any operating model, I try to keep architectural decision-making distributed and embedded in development teams. In most cases, those teams hold the richest local information. As Gregor Hohpe has pointed out, the worst decision systems are those in which the people with the relevant information cannot decide, while the people making the decisions lack context. Grounded Architecture tries to correct that imbalance by making information more visible and by connecting the right people at the right time.
 

But autonomy is not isolation. It does not mean teams can ignore shared constraints, avoid feedback, or optimize purely for themselves. Teams need to pair **autonomy** with **transparency**, **proactive alignment**, and a willingness to expose decisions early enough for others to react.

I have sometimes implemented the concept of a **decision pyramid** (Figure 2) to give the teams **maximal autonomy** while maintaining a **minimal** level of **global alignment** and compatibility.

The **decision pyramid** expresses this balance. Teams should make most decisions, but they do so inside a set of boundaries created by broader strategic and area-level choices. Selecting a public cloud provider, for example, is often a CTO-level decision. Limiting the number of programming languages in a domain may be an engineering leadership decision. Those constraints reduce fragmentation and make hiring, onboarding, maintenance, and cross-team mobility easier.

![](assets/images/arch/decision-pyramid.png)
***Figure 2:** A decision pyramid. The development teams should make most decisions. However, several strategic and area-level decisions may provide decision boundaries for teams (e.g., golden paths or tech stack constraints).*

### General Architecture Decision Policy

Distributed decision-making scales well, but it can lead to chaos if entirely uncoordinated. Some decision policies are needed. Inspired by the famous **[Netflix expense policy](https://hbr.org/2014/01/how-netflix-reinvented-hr)**, *"Act in Netflix’s best interests”*, I frequently argued that architecture decision policy could similarly be summarized in six words: *"Decide in the Organization's Best Interests."*

![](assets/images/arch/decision-policy.png)

What I mean by that is that **anyone can make architecture decisions**, provided that, in addition to their specific requirements, they also think about the **impact of their choices** on:

* **Alignment with company goals**: Trace the decision to current strategy/OKRs, KPIs, and risk appetite. Improves one or more: time-to-value, reliability/SLOs, cost efficiency, security & compliance, sustainability. Avoids local optimizations that conflict with portfolio priorities or product roadmap.
* **Overall organizational complexity**: Technology is more manageable by limiting tech diversity, size, and dependencies. Limiting technology choices reduces the attack surface with fewer third-party dependencies and tool ecosystems (build, testing, etc.).
* **Ease of moving people** between teams (both to get help and help others): Do not unnecessarily create exotic islands with few experts in technologies not supported or widely used in the organization. People cannot get help or move across the organization as their expertise may be useless outside the team.
* **Ease of training and onboarding** of internal and external developers: Using conventional technologies supported by external learning resources (e.g., books, tutorials) significantly helps find and grow experts.
* **Talent density** and the possibility of performing at the world-scale level: Building world-scale technology and scaling requires in-depth knowledge and fine-tuning. You cannot achieve it with only a few in-house experts.
* New **reorganizations**: If the ownership of components changes (e.g., another team is taking it over), would your choices fit with other components from other areas? 
* Reducing global **duplication of effort** and inefficiencies: Are you doing the work others are doing? Can others reuse your work? Can you reuse the work of others?

While it may not always be enough, this simple policy can resonate well with many people and can encourage them to be more thoughtful when making decisions.

### Golden Paths

I have found Golden Paths to be one of the most effective mechanisms for turning abstract alignment into concrete practice. Inspired in part by [Spotify's implementation](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/), Golden Paths are **opinionated and supported** ways of building common classes of systems.

![](assets/images/spotify-golden-paths_infrastructure-and-tooling-700x327.png)
^image by engineering.atspotify.com^

Golden Paths matter because they connect architecture, platform work, and community practice. They give guilds and central teams something practical to build, improve, and support together. Instead of merely discussing best practices, teams can turn those practices into reusable defaults that are easier to adopt than to ignore.

When done well, Golden Paths reduce fragmentation without creating rigidity. They improve **uniformity, efficiency, and reliability** by making the preferred route well-supported, secure, and easy to use. They do not remove choice entirely, but they make the default choice good enough that most teams will take it voluntarily.

## Guided Autonomy and Privileged Autonomy

I believe in team autonomy, but autonomy will not work without proper support. That's why I use two modes: **Guided Autonomy** and **Privileged Autonomy**.

In **Guided Autonomy**, the team still owns decisions, and I stack the deck so they can win. For less-mature teams—or teams operating in a brand-new domain—I'll embed an architect for a time-boxed stretch (think 4–12 weeks), design clinics and office hours, pair on ADRs, and narrow the choice set to our Golden Paths and pre-approved building blocks. The guardrails are clear: use the Golden Path by default, document decisions, consult early on cross-team impacts, and get steward sign-off for one-way doors. Graduation isn't based on seniority; it's earned with a short streak of solid ADRs (e.g., 5–10) that show explicit alignment to company goals/OKRs, sensible trade-offs, and production outcomes that hold (better SLOs, lower cost/lead time, stronger security), plus good feedback from adjacent teams.

**Privileged Autonomy**—a term I first heard on the [Product Thinking podcast with Georgie Smallwood](https://www.produxlabs.com/product-thinking-blog/2021/2/17/how-to-succeed-as-a-senior-product-leader-with-georgie-smallwood)—is the earned fast lane. If you consistently apply the Decision Criteria, deliver outcomes, and stick to standards (or justify exceptions with an exit plan), you can make medium- to high-impact calls without pre-approval. You still work within the policy: tie decisions to goals, prefer Golden Path options, publish ADRs within 48 hours, and notify affected teams. One-way doors (irreversible choices, significant spend, complex data contracts) still need a different process.

Teams move between these modes based on signals, not titles. A strong streak and stable outcomes move you from Guided to Privileged. Repeated misalignment or avoidable churn pauses Privileged and puts us back in Guided until a fresh 3–5 ADR run restores confidence. Example: a team new to event streaming starts in Guided with an embedded architect, ships on the managed messaging Golden Path, and after five solid ADRs graduates to Privileged. A seasoned team choosing a Radar/Golden Path service proceeds under Privileged; proposing a niche database for a core platform triggers an exception review.

## Embracing Diversity

When building architecture guilds and virtual architecture teams, it's crucial to acknowledge that organizational units have diverse structures and sizes. In big organizations, **embracing diversity** is a prerequisite to having a broad impact.

![](assets/images/istock/iStock-1384284589.jpg)
^image by annaspoka from istock^

There is no one-size-fits-all solution for assigning architecture responsibilities within departments. Based on Gregor Hohpe's view of architects and their teams' relationships, I've generally encountered three types of team-architect systems:

1. **Benevolent "dictator"**: An architect or architecture team tells developers what to do or how to do things. The key nuance here is whether the communication is unidirectional or bi-directional.
     
2. **Primus inter pares (first among equals)**: Architects are embedded within teams where each is just another team member, but with a focus on the system structure and trade-offs and taking a longer-term view than other team members.
   
3. **Architecture without architects**: Architecture is done within teams, but the task is a shared responsibility among multiple (or all) team members. This approach is often the preferred model in modern technology organizations.
    
Remember, there is no magic bullet. Different structures work for various organizations; sometimes, the best solution is a mix of these approaches.

## Setting Boundaries: Clear Boundaries + Strong Relationships = Effective Architecture Practice

One of the persistent challenges in setting up an architecture practice is that everyone has a different idea of what "architecture" should cover. Good architects can do many things, but that does not mean they should do everything. We need to **set boundaries** so the practice stays focused on the work that matters most.

![](assets/images/istock/iStock-92285726.jpg)
^image by ingenui from istock^

To be effective, I have found it essential to define and communicate clear "**rules of engagement**" (ROE). In practice, ROE clarify how architects work with teams and stakeholders: how decisions are made, how disagreements are resolved, and what support architecture can reasonably provide.

While you may need to tailor these rules to fit your organization, I found it helpful to set expectations for what the team should be able to do to qualify for the architecture support. Here's a handy list of expectations for teams seeking architecture support. This also helps clarify what an architecture practice isn't supposed to do:

1. **Organizational Awareness and Connections:** Teams should know all relevant stakeholders and actively engage with them. This knowledge should include product, development, and business stakeholders. Planning should be collaborative across all affected teams, with active working relationships with global functions like QA, DevOps, or Security.

2. **Enough Capacity and Skills:** Teams should have adequate development capacity with the right skills and seniority to innovate and maintain their products. 

3. **Strategic Awareness:** Teams should understand the organization’s strategic goals, technologies, and other relevant strategies, and know their role within these frameworks.

4. **Technical Documentation Literacy:** Teams should be capable of creating technical documentation, such as ADRs (Architecture Decision Records) or RFCs (Request for Comments).

5. **Technology Standard Awareness:** Teams should be familiar with the organization’s technology standards, including golden paths and guidelines for planning, documentation, security, DevOps, and QA processes.

6. **Participation and Citizenship:** Teams should actively participate in relevant communities (like architecture guilds) and global events (such as architecture summits).

7. **Tech Debt Management:** Teams must be aware of the technical debt they create and maintain, ideally having a tech debt backlog and a plan for “paying” it back.

Aligning on these rules with teams helps create productive conversations about architectural support. When these conditions are met, an architecture practice can help teams level up. When they are not, architecture support is naturally less effective. That does not mean struggling teams should be ignored. Architecture can help teams meet these expectations, but it cannot fully compensate for their absence. Teams still need to take ownership. For example, it is not scalable to use architects as long-term substitute senior developers for a single team. Architects can coach, unblock, and help people grow, but the teams themselves need to engage and improve.

Clear expectations and clear rules of engagement make the architecture practice more focused, scalable, and effective.

## Final Thoughts

Here are **five key points** to consider when defining an architecture practice and its operating model within your organization:

1. **No One-Size-Fits-All Architecture Practice**:
   Organizations must customize their architecture practices to address specific challenges and contexts. It's ineffective to place architects in disarray and expect positive results—architecture should focus on resolving the organization's most pressing issues.

2. **Collaborative and Distributed Operating Models**:
   Successful architectural work depends on collaboration with teams, distributed decision-making, and clearly defined "rules of engagement." Architects should empower teams, get involved early, avoid bureaucratic delays, and ensure alignment with strategic goals.

3. **Golden Paths and Standardization Promote Alignment**:
   "Golden Paths"—clear, opinionated, and supported solutions—are essential for reducing fragmentation, increasing consistency, and guiding teams toward efficient and aligned development practices.

4. **Architecture Activities Must Be Grounded and Strategic**:
   Important architecture activities include designing decision frameworks, supporting projects and legacy modernization, tracking technical debt, conducting platform analyses, and defining strategic technology directions—all while being integrated into team workflows.

5. **Set Clear Expectations and Boundaries for Effective Support**:
   Architectural support is most effective when teams meet baseline criteria (e.g., stakeholder awareness, skills, documentation literacy). Establishing expectations and defining boundaries ensures that architectural efforts are scalable and focused on areas with the most significant impact.

These principles also reinforce one of the book's core arguments: architecture becomes effective when it helps teams make better decisions in context, not when it tries to centralize every important choice. The Operating Model works best when it creates clarity, support, and practical defaults rather than bureaucracy.

## To Probe Further

* [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html), by Andrew Harmel-Law, 2021
* [Scaling Engineering Teams via RFCs: Writing Things Down](https://blog.pragmaticengineer.com/scaling-engineering-teams-via-writing-things-down-rfcs/), by Gergely Orosz, 2022
* [Transformation Agents: An Engagement Model](https://architectelevator.com/transformation/transformation-engagement-model/), by Gregor Hohpe, 2022
* [Would you like architects with your architecture?](https://architectelevator.com/architecture/organizing-architecture/), by Gregor Hohpe, 2021

## Questions to Consider
Use the following questions to examine whether your principles are clear, usable, and strong enough to guide everyday choices.

* *How can you identify the most critical problems that your architects need to solve in your organization?*
* *What activities and operating models can you think of that will best enable architecture in your organization to work on these critical problems?*
* *What does the Operating Model look like in your organization, and how could it be improved?*
* *Which of the provided examples of architectural activities are you currently performing in your organization?*
* *How does the proposed common operating model align with your current operational practices in your organization? What changes might be necessary to adopt this model?*
* *In your experience, how early are architects involved in projects and activities? Do you agree with the goal of 'shifting left' the architecture work?*
* *How are architectural decisions distributed across your organization currently? How could this process be improved to ensure the people with the most relevant information make the decisions?*
* *How could you better implement a mechanism to give teams autonomy while maintaining alignment and compatibility with global strategy?*
* *How does the concept of a decision pyramid resonate with you?*
* *Which strategic and area-level decisions provide team decision boundaries in your organization? Are there areas where you need more or less limitations to optimize performance?*
