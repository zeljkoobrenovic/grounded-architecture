---
layout: post
section: "Grounded Architecture Framework"
title: "Operating Model: Nudge, Taxation, Mandates"
position: 3011
podcast: governance.mp3
spotify: https://open.spotify.com/episode/2UTAYFVJoWRmvX5CvJsJST?si=83969e560b6c4886
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
icon: govern.png
permalink: governance
timetoread: 15 min
excerpt: "Architecture practice should support governance models that are adaptable to organizations' complex and diverse needs. I see a technology governance model as a well-balanced hybrid of three different styles of governing: nudging, taxes, and mandates and bans."

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/greece-1594689_1920.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/nl/users/nonbirinonko-3101900/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1594689">nonbirinonko</a> from <a href="https://pixabay.com/nl//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1594689">Pixabay</a>
</div>
> **IN THIS SECTION, YOU WILL:** Understand that a technology governance model should be a well-balanced hybrid of three different styles of governing: mandates and bans, taxes, and nudging.
>
> **KEY POINTS:**
>
> * Architecture practice should support governance models adaptable to organizations' complex and diverse needs. A technology governance model should be a well-balanced hybrid of three different styles of governing: mandates and bans, taxes, and nudging.
> * Nudging is a form of governing where you create subtle or indirect suggestions influencing someone's behavior or decision-making without forcing them or limiting their freedom of choice.
> * Governing with taxes (economic incentives) is a form of guiding in which people are not forbidden to make some decisions but need to "pay" some form of taxes on used resources.
> * With mandates and bans, you guide people by explicitly defining what they should or should not do.
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
</style>

**Governance** is the **framework of rules and processes** by which an organization is **directed and controlled**, focusing on **accountability**, **fairness**, and **transparency**. It applies to **corporate**, **IT**, **project**, and **data governance**.

**IT architecture serves as a form of governance** by **establishing structured frameworks** for managing **technology resources** and ensuring **alignment with business objectives**. It promotes **standardization**, manages **risks**, **optimizes resources**, and supports **decision-making**, **innovation**, and **performance measurement**.

Governance faces challenges due to **diverse interests**, **rapidly changing conditions**, and **multifaceted issues**. A successful governance framework requires **adaptability**, **collaboration**, and a **commitment to addressing both immediate and long-term challenges**. Effective governance **balances stakeholder interests** and **evolves to meet organizational objectives**.


Architecture practice should support governance models that are aligned and adaptable to organizations' complex and diverse needs. Consequently, I see an architecture governance model as a well-balanced hybrid of three different styles of governing:
* **nudging**,
* **taxes** (economic incentives), and
* **mandates and bans**.

<div class="quote">
Architecture practice should support governance models <b>adaptable to organizations' complex and diverse needs</b>.
</div>
<br>
## Nudging

In behavioral economics and psychology, a **nudge is a subtle or indirect suggestion** influencing someone's behavior or decision-making **without forcing them or limiting their freedom of choice**. Nudges can be applied in various settings, such as policy-making, marketing, and personal interactions, to encourage people to make better choices, improve their well-being, or achieve specific goals.

<br>
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/istock/iStock-1390608248.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/Chernetskaya">Liudmila Chernetska</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

A nudge can take many forms, such as a slight change in the environment, a gentle reminder, positive reinforcement, or a default option. For example, placing healthy food options at eye level in a cafeteria can nudge people to choose healthier meals. Setting a default option for organ donation can increase the number of donors.

<div class="quote">
A nudge is a subtle or indirect suggestion influencing someone's behavior or decision-making without forcing them or limiting their freedom of choice.
</div>

The concept of a nudge was popularized by the book **"Nudge: Improving Decisions About Health, Wealth, and Happiness"** by Richard Thaler and Cass Sunstein, which argues that various cognitive biases and heuristics often influence people's decisions, and that nudges can help people overcome these biases and **make better choices**.

Richard Thaler and Cass Sunstein also introduced the concept of choice architecture as a critical component of nudging. Choice architecture refers to how options are presented to individuals, which can significantly influence their choices. It is the design of the decision-making environment, which includes the layout, structure, and organization of available options.

In IT architecture, examples of nudging include:
* Architectural **principles** as informal decision guidelines. Such principles do not prescribe a solution but can subtly guide alignment.
* Recommendations for **best practices** to stimulate introduction and alignment around such practices, 
* Default options for technology choices via 
[**golden paths**](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/)
* **Highlighting** bad quality software on a [Lightweight Architectural Analytics](analytics) dashboard to create subtle pressure for people to improve it,
* Tracking of **tech debt** to create awareness about its size and lead action to reduce it,
* **Visualizing cost trends** of cloud services per team to stimulate teams to improve the performance efficiency of their software.

Nudges can frequently lead to better alignment and more harmonization without the negative consequences of mandates, bans, or taxation.

Grounded Architecture is well aligned with ideas of nudging. I designed many [Lightweight Architectural Analytics](analytics) tools to **highlight areas and issues** we wanted (nudged) people to improve. The [Collaborative Networks](people) can create mechanisms for sharing experiences, promoting **positive examples**, and capturing lessons learned to help people make better, more informed decisions. In the [Operating Model](operating-model), I use the operating model that stimulates people to make decisions autonomously but **nudges them to stay well-aligned** and connected to the organizational strategic direction.


<br>
## Taxation (Economic Incentives)

**Governing with taxes** is a strategic approach that allows individuals or departments to make choices and decisions without prohibition. Instead, they must *"pay"* a **tax on the resources they use**. This system creates a **feedback loop** that encourages **responsible resource consumption** and **optimizes overall system efficiency**. A practical application of this approach can be seen in **managing public cloud costs** within an organization. By **cross-charging** these expenses across various departments or projects, each unit receives a **clear signal regarding its resource consumption**. This practice not only enables **accurate cost allocation** but also raises awareness, motivating efforts to **minimize unnecessary usage**. It effectively prevents the *"tragedy of the commons,"* where unrestricted access to shared resources leads to overconsumption and depletion.


<div class="quote">
Governing with taxes is a form of guiding in which people are not forbidden to make some decisions but need to "pay" some form of taxes on used resources.
</div>

<br>
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/credit-squeeze-g61ddead85_1920.png">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/stevepb-282134/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=522549">Steve Buissinne</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=522549">Pixabay</a>
</div>

In contrast to **nudging**, which subtly influences behavior by providing information or setting default choices without imposing direct consequences, **taxes introduce clear and tangible consequences**. For instance, projects that exceed budgeted IT costs due to excessive resource use might be **canceled**. The **architecture practice** plays a crucial role in this governance model, ensuring that taxation policies are grounded in **accurate and comprehensive data**, such as public cloud cost reports. **Transparency is essential**; all stakeholders should understand **how and why taxes are levied**, along with clear reports detailing the basis of taxation and its effect on resource consumption.

Developing **efficient feedback loops** is another critical aspect. These loops provide **timely and actionable feedback** on key metrics related to taxes, allowing for continual refinement and optimization of the taxation system.[ Lightweight Architectural Analytics](analytics) is key to this approach, as it aggregates and analyzes all data related to resource consumption and taxation, generating insights from public cloud cost reports that **guide decision-making**. [Collaborative Networks](people) foster alignment of organizational processes, goals, and working methods with the taxation system, promoting a **culture of responsible resource usage** and continuous improvement.

In conclusion, governing with taxes is an effective approach to resource management that **balances autonomy with accountability**. By implementing a data-driven and **transparent taxation system**, organizations can optimize resource usage, prevent overconsumption, and **drive meaningful change**. An architecture practice, supported by robust Lightweight Architectural Analytics and Collaborative Networks, is essential for achieving these goals and ensuring the **sustainability of shared resources**.


<br>
## Mandates and Bans

Governing through mandates and bans involves clearly outlining what people **should or should not do**. In various workplaces, these tools play a **limited yet crucial role** in defining the **broader strategic boundaries** of available choices. For instance, restricting the use of public cloud providers to specific vendors or enforcing strict **privacy and security protocols** must be clearly defined and controlled.

It is essential to use **bans carefully and as a last resort** to avoid unnecessarily hindering development and innovation. However, mandates and bans can effectively clarify important issues where nudging or taxation alone would be insufficient. For example, establishing clear rules and control mechanisms to prevent violations of **privacy or financial laws** can help avert incidents and damage. Well-defined mandates and bans ensure **compliance with critical regulations** and help **protect the organization’s integrity and reputation**.


<div class="quote">
By governing with mandates and bans, I mean guiding people by explicitly defining what they should or should not do.
</div>
<br>

<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/ethics-g277df4183_1920.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/tumisu-148124/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2991600">Tumisu</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2991600">Pixabay</a>
</div>

The role of architecture in this form of governance should be to act as **a stakeholder but not the sole owner in defining mandates and bans**. These mandates and bans should often be determined collaboratively with other functions, such as security and legal departments. The an architecture practice can contribute by **creating clarity and providing transparency**.

[Lightweight Architectural Analytics](analytics) is crucial for creating **clarity and transparency**. For example, it can provide insights through security reports or maps of areas in the source code or infrastructure that need monitoring and controlling based on privacy or security requirements. This foundation helps in identifying and mitigating risks, ensuring that the organization's technology landscape aligns with its governance frameworks.

The [Collaborative Networks](people) can help propagate the decision and ensure its **positive impact and acceptance**. Mandates and bans should not be issued routinely without sufficient explanation. It is crucial to spend time with all stakeholders to explain the **reasons and motivations** behind introducing certain limitations. A strong Collaborative Networks fosters strong connections with key stakeholders, leveraging these relationships to implement changes smoothly. This foundation ensures that governance measures are understood, accepted, and integrated into the organization's culture and practices, enhancing overall effectiveness.

In summary, governing with mandates and bans involves setting clear, explicit guidelines for acceptable behavior and practices. It requires a balanced approach to ensure it does not stifle innovation while maintaining necessary controls. Effective implementation relies on collaboration, transparency, and communication to ensure that all stakeholders understand and accept the governance measures.

<br>
## Questions to Consider

* *What are the key components of the governance model in your organization, and how do mandates, taxes, and nudging influence them?*
* *How does your organization currently handle mandates and bans? Are they explicit and aligned with the overall technology strategy?*
* *How effective is the enforcement of these mandates and bans in your organization? Could improvements be made to create clarity and provide transparency?*
* *How does your organization approach taxation as a form of governance? Is it transparent, data-driven, and efficient?*
* *Can you identify any examples of 'nudging' in your current architectural environment? How effective are these subtle suggestions in influencing behavior or decision-making?*
* *How does your organization promote best practices and align around them? Are there any 'golden paths' for technology choices?*
* *How are your organization's tech debt and the cost trends of cloud services tracked and visualized? Do these methods create enough awareness to stimulate improvement?*
* *How could you better utilize nudging to improve organizational decision-making? What biases or barriers to effective decision-making could you target with this approach?*
