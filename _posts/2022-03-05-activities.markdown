---
layout: post
section: "Grounded Architecture Framework"
title: "Architecture Activities Platform"
position: 3006
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: activities
icon: activities.png
timetoread: 15 min
excerpt: "The Architecture Activities Platform is where, by leveraging data and People Foundations, we perform activities that help an organization reach its goals. Examples include supporting teams in their daily work, tracking tech debt, performing technical due diligence, standardizing processes and documentation, and defining cloud, data, and platform strategies."

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/parliament-366199_1920.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/cocoparisienne-127419/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=366199">Anja</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=366199">Pixabay</a>
</div>
> **IN THIS SECTION, YOU WILL:**  Understand what activities you can do as a part of architecture practice and get tips on creating pragmatic operating models for an architecture practice.
>
> **KEY POINTS:**
>
> * The Architecture Activities Platform is a system of processes and agreements enabling architects to do everything architecture typically does, leveraging Data and People Foundations to create a data-informed, organization-wide impact.
> * Examples of activities include: supporting teams in their daily work; tracking tech debt, defining tech debt reduction programs; performing technical due diligence; standardizing processes and documentation; defining cloud, data, and platform strategies.
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
        [class="quote"] {
            display: none;
        }
    }
    h3 {
      margin-top: 30px;    
    }
</style>

<br>
Each organization will have different architectural needs and contexts. When forming architecture functions, I use as a starting point these [two pieces of advice from Gregor Hohpe](https://architectelevator.com/architecture/organizing-architecture/):

* *"Your architecture team’s job is to **solve your biggest problems**. The best setup is the one that allows it to accomplish that."*
* *"Your organization has to earn its way to an effective architecture function. **You can't just plug some architects into the current mess** and expect it to solve all your problems."*

Considering Gregor Hohpe's previous two points, I approach defining an architecture practice with the mindset that there is no one-size-fits-all method. You must find your own activities and operating models to enable architecture to solve the most critical problems.

<div class="quote">
There is no one-size-fits-all approach: each organization must find activities and operating models that enable architecture to solve the most critical problems.
</div>

No matter which operating models you select, it's crucial to develop **explicit agreements** and "rules of engagement" with key stakeholders. This collaborative approach is essential to create a sustainable and practical architectural function.

![](assets/images/model-strategy.png)
***Figure 1:** The structure of Grounded Architecture: Architecture Activities Platform.*

The Architecture Activities Platform (Figure 1) is a set of processes and agreements that allows architects to do everything architecture practice typically does. It leverages Data and People Foundations to develop a data-informed, organization-wide impact. Data and People Foundations provide a basis for data-informed decision-making well embedded in the organization. It's about instilling confidence and trust in your decision-making process.


<br>
## Examples of Architecture Activities

To provide a clearer understanding of what I mean by an Architecture Activities Platform, here are detailed examples of the activities I have been engaged in with architects.

* **Designing Mechanisms for Teams to Make Better Decisions**: This involves creating global decision-support frameworks such as advisory forums, which facilitate informed discussions across teams. For compliance-sensitive projects, we establish formal design authorities. Additionally, we develop team-specific mechanisms, like escalation paths, to resolve decision conflicts effectively (e.g., when teams disagree on a common messaging middleware).

* **Supporting Teams in Their Daily Work**: This entails integrating into key team activities, aligning architectural work with team rituals to provide timely support. We assist teams during all critical phases, such as reviewing architecture proposals before the commencement of a project or sprint, ensuring alignment with overall architectural standards.

* **Supporting Planned New Initiatives and Projects**: Ensuring seamless alignment between projects that require multi-team collaboration is crucial. We work to facilitate communication and coordination, ensuring all teams are on the same page regarding project goals and requirements.

* **Supporting Teams in Dealing with the Legacy Landscape**: We provide data and insights about the legacy landscape, identifying problematic areas such as frequently changed, low-quality, untested legacy code. We help define scenarios and roadmaps for legacy modernization, ensuring a structured approach to updating and maintaining legacy systems.

* **Tracking Tech Debt and Defining Tech Debt Reduction Programs**: This involves creating a centrally aligned backlog of technical debt and defining programs for its reduction. We integrate these programs into the planning processes to ensure that tech debt is managed proactively and effectively.

* **Performing SWOT and Other Analyses of Platforms and Systems**: Conducting deep dives to understand specific areas of the technology landscape, We perform SWOT (Strengths, Weaknesses, Opportunities, Threats) analyses and other assessments. These analyses help in creating comprehensive plans and roadmaps for improvement.

* **Standardizing Processes and Documentation**: We define standard templates for key documents such as Architectural Decision Records (ADRs), Technical Design Reviews (TDRs), and common diagrams. This standardization ensures consistency and clarity across all architectural documentation.

* **Supporting Merger and Acquisition (M&A) Activities with Expertise and Analyses**: We provide analyses, recommendations, and integration planning for mergers and acquisitions. My support ensures that architectural considerations are well-integrated into M&A activities, facilitating smoother transitions and integrations.

* **Defining Key Technology Strategies**: We contribute to the development of essential technology strategies, including those for Cloud, Data, and Platforms. These strategies provide a clear roadmap for technological development and investment, ensuring alignment with business goals.

* **Defining Vision and Direction of Technology**: In collaboration with Engineering Leaders, We work on creating a sustainable organizational setting that aligns with the overarching technology strategies. This involves setting a clear vision and direction for the technology landscape within the organization.

These activities collectively form an Architecture Activities Platform, enabling a structured and strategic approach to architectural practices within the organization.


<br>
## Guiding Principles for Architectural Excellence: Policies, Autonomy, and Engagement

In this section, I address different guiding principles of architectural work. The **operating model** emphasizes a **collaborative** and **supportive** approach. Architects empower development teams to make most decisions while ensuring strategic alignment and minimal compatibility. Architects engage early in processes to **avoid bureaucratic delays,** focus on constant motion between daily support and strategic tasks, and use data to inform decisions. The **distributed decision-making** model promotes team autonomy complemented by high transparency and alignment, guided by principles that balance autonomy with global consistency. The "Golden Paths" concept enhances uniformity and efficiency.

### High-Level Operating Model

While exact activities and their scope will depend on an organization setting and will change over time, I usually followed a common operational model in daily work inspired by Gregor Hohpe's strategy-principles-decisions model (Figure 2). 

<div>
<a href="assets/images/arch/architecture-system.png" target="_blank">
    <img src="assets/images/arch/architecture-system.png">
</a>
</div>
**Figure 2:** *A common operating model I typically use for Grounded Architecture activities.*

<br>

Here are the key characteristics of this operating model. 

**Engagement mindset**: 
  * Architects engage with stakeholders and product and project teams in a **collaborative and supportive manner**. 
  * Architects aim to **empower the teams** so that they make most of the decisions.

**Contributions of architects**: 
  * **Bring relevant data** to inform decisions leveraging a [Data Foundation](data).
  * **Define decision boundaries** to enable minimal compatibility and strategic alignment (e.g., public cloud provider, golden paths, or tech stack constraints).
  * **Define fundamental principles** to facilitate consistency in decision-making.
  * **Share and generalize** lessons learned via a [People Foundation](people).

**Social dynamics of architects**:
  * Architects spend their time in **constant motion** between supporting teams' **daily work** and working on **strategic topics**, helping the organization achieve alignment between strategy and implementation.

**Shift left**:  
  * Avoid **formal bureaucratic approval** processes, where architects appear too late and are frequently busy approving trivial decisions. 
  * Have architects **involved early** in any of the processes, such as during the planning and preparation stages, where it is possible to make more significant changes. Think of it as having the architects as early birds catching the architectural worms, making big changes before the day officially starts.

<br>
### Distributing Decisions, Autonomy, and Alignment

With any operating model, I aim to keep architectural decision-making distributed across the organization and embedded in the development teams. Development **teams traditionally have the best insights and most information** relevant for making decisions. As noted by Gregor Hohpe, the worst case of organizational decision-making happens when people with relevant information are not allowed to make decisions, while people who lack sufficient information make all decisions. Grounded Architecture aims to make relevant information more readily available to a broader audience and better connect people when making decisions.
 

<div class="quote">
Grounded Architecture aims to make relevant information more readily available to a broader audience and better connect people when making decisions.
</div>

While I aim to create a mechanism to give teams autonomy, autonomy does not mean that teams are alone and do not align with anyone, do not get feedback from anyone, and do whatever they want. Teams must complement autonomy with high transparency and proactivity in alignment with other groups. 

To give maximal autonomy to the teams while maintaining a **minimal** level of global **alignment and compatibility**, I have sometimes implemented the concept of a **decision pyramid**  (Figure 3).

The **decision pyramid** highlights that development teams should make most decisions. However, several strategic and area-level choices may provide team decision boundaries. For example, selecting the public cloud provider is typically a CTO-level strategic decision. Similarly, engineering leaders in some areas may want to limit some choices, such as the number of programming languages, to more easily train new people, maintain code, and support moves between teams.

![](assets/images/arch/decision-pyramid.png)
***Figure 3:** A decision pyramid. The development teams should make most decisions. However, several strategic and area-level decisions may provide decision boundaries for teams (e.g., a public cloud provider).*

### General Architecture Decision Policy

Distributed decision-making scales well, but it can lead to chaos if entirely uncoordinated. Some decision policies are needed. Inspired by the famous **[Netflix expense policy](https://hbr.org/2014/01/how-netflix-reinvented-hr)**, *"Act in Netflix’s best interests”*, I frequently argued that architecture decision policy could similarly be summarized in six words:

![](assets/images/arch/decision-policy.png)

What I mean by that is that **anyone can make architecture decisions**, provided that, in addition to their specific requirements, they also think about the **impact of their choices** on:

* **Overall organizational complexity**: Technology is more manageable by limiting tech diversity, size, and dependencies. Limiting technology choices reduces the attack surface with fewer third-party dependencies and tool ecosystems (build, testing, etc.).
* **Ease of moving people** between teams (both to get help and help others, get promoted): Do not unnecessarily create exotic islands with few experts in technologies not supported or widely used in the organization. People cannot get help or move across the organization as their expertise may be useless outside the team.
* **Ease of training and onboarding** of internal and external developers: Using conventional technologies, supported with external learning resources (books, tutorials, StackOverflow) significantly helps find and grow experts.
* **Talent density** and the possibility of performing at the world-scale level: Building world-scale technology and scaling requires in-depth knowledge and fine-tuning. It cannot be achieved with only a few in-house experts.
* New **reorganizations**: If the ownership of components changes (e.g., another team is taking it over), would your choices fit with other components from other areas? 
* Reducing global **duplication of effort** and inefficiencies: Are you doing the work others are doing? Can others reuse your work? Can you reuse the work of others?

While it may not always be enough, this simple policy resonates well. It encourages people to be more thoughtful when making decisions.


<br>
### Golden Paths

I have found that the concept of Golden Paths provides an excellent ground to **drive alignment and collaboration** in architecture activities. Golden Paths is an approach utilized to streamline and unify the development process within a software ecosystem, aiming to tackle fragmentation and foster consistency, inspired by [Spotify's implementation](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/). Golden Paths can be described as "**opinionated and supported**" routes developers can follow to build systems efficiently and effectively. 

<img style="" 
     src="assets/images/spotify-golden-paths_infrastructure-and-tooling-700x327.png">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by engineering.atspotify.com
</div>

Golden paths provide a solid **foundation for aligning** architecture activities, serving as a common target of work for Guilds and central architectural teams. Rather than being solely knowledge-sharing entities, guilds can be empowered to develop golden paths, serving as an excellent catalyst for more effective community engagement. This approach not only enhances the role of guilds but also increases the adoption of golden paths as they are created collaboratively.

Golden Paths can be crucial to an organization's IT development landscape as a deliberate and strategic effort to promote uniformity, efficiency, and reliability. By advocating for a set of preferred technologies and practices that are well-supported, secure, and aligned with the organization's broader objectives, Golden Paths can guide developers to build less fragmented, and faster-to-develop software. Ultimately, this leads to higher-quality and more maintainable IT systems.


<br>
## Setting Boundaries

One of the amusing challenges with setting up an architecture function in an organization is that everyone seems to have a different idea of what "architecture" should entail. It's like asking people to describe a unicorn: some imagine a mythical, majestic creature, while others picture a sparkly horse with a horn that grants wishes. Good architects can do many things, but this versatility might not always be the most effective way to support the organization. We need to **set boundaries** so that we can focus on what's important rather than becoming frazzled by what's not.

<br>
![](assets/images/iStock-92285726.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>
<br>

To be effective, I've found it crucial to establish and clearly communicate some "**rules of engagement**" (ROE). Think of ROE as the office playbook for how architects should operate. In a corporate setting, ROE are the principles that guide how employees and departments interact with each other, clients, and stakeholders. This includes communication protocols, decision-making processes, and conflict-resolution mechanisms. Essentially, ROE sets the stage for what's expected and what's not, ensuring everyone plays nicely and fairly.

While you may need to tailor these rules to fit your organization, I found it helpful to set expectations for what the team should be able to do to qualify for the architecture support. Here's a handy list of expectations for teams seeking architecture support. This also helps clarify what architecture practice isn't supposed to do:

1. **Organizational Awareness and Connections:** Teams should know all relevant stakeholders and actively engage with them. This includes product, development, and business stakeholders. Planning should be collaborative across all affected teams, with active working relationships with global functions like QA, DevOps, or Security.

2. **Enough Capacity and Skills:** Teams should have adequate development capacity with the right skills and seniority to innovate and maintain their products. 

3. **Strategic Awareness:** Teams should understand the organization’s strategic goals, technologies, and other relevant strategies, and know their role within these frameworks.

4. **Technical Documentation Literacy:** Teams should be capable of creating technical documentation, such as ADRs (Architecture Decision Records) or RFCs (Request for Comments).

5. **Technology Standard Awareness:** Teams should be familiar with the organization’s technology standards, including golden paths and guidelines for planning, documentation, security, DevOps, and QA processes.

6. **Participation and Citizenship:** Teams should actively participate in relevant communities (like architecture guilds) and global events (such as architecture summits).

7. **Tech Debt Management:** Teams must be aware of the technical debt they create and maintain, ideally having a tech debt backlog and a plan for “paying” it back.

Aligning on these rules with the teams helps ensure productive conversations about architectural support. When these conditions are met, architecture practice can help teams level up. When they’re not, architecture support can’t be as effective. However, that doesn’t mean struggling teams are left in the lurch. Architecture can help teams meet these expectations but can’t compensate for their total lack. Teams need to take the initiative and lead. For instance, it’s impractical to have architects working full-time for months with one team as their senior developer. However, architects can coach and help developers grow. Similarly, architects can assist in building relationships with other teams, but the teams themselves need to be active and engaged.

So, set those expectations, establish your rules of engagement, and watch as your architecture function goes from a sparkly unicorn to a well-oiled machine!

<br>
## To Probe Further

* [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html) <br>by Andrew Harmel-Law, December 2021
* [Scaling Engineering Teams via RFCs: Writing Things Down](https://blog.pragmaticengineer.com/scaling-engineering-teams-via-writing-things-down-rfcs/) <br>by Gergely Orosz, September 2022

<br>
## Questions to Consider

Your architecture practice job is to solve the biggest problems in your organization. Ask yourself the following questions:

* *How can you identify the most critical problems that your architects need to solve in your organization?*
* *What activities and operating models can you think of that will best enable architecture in your organization to work on these critical problems?*
* *What does the Architecture Activities Platform look like in your organization, and how could it be improved?*
* *Which of the provided examples of architectural activities are you currently performing in your organization?*
* *How does the proposed common operating model align with your current operational practices in your organization? What changes might be necessary to adopt this model?*
* *In your experience, how early are architects involved in projects and activities? Do you agree with the goal of 'shifting left' the architecture work?*
* *How are architectural decisions distributed across your organization currently? How could this process be improved to ensure the people with the most relevant information make the decisions?*
* *Reflect on the balance of autonomy and alignment in your organization. How could you better implement a mechanism to give teams autonomy while maintaining alignment and compatibility with global strategy?*
* *How does the concept of a decision pyramid resonate with you? How is it reflected in your current organization, and how could it be better implemented?*
* *Which strategic and area-level decisions provide team decision boundaries in your organization? Are there areas where you need more or less limitations to optimize performance?*

