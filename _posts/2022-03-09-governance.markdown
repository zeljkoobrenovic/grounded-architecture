---
layout: post
section: "Grounded Architecture Framework"
title: "Operating Model: Nudge, Taxation, Mandates"
position: 3009
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

Governance refers to the framework of rules, practices, and processes by which an organization is directed and controlled. It encompasses the mechanisms by which an organization's goals are set, pursued, and monitored, ensuring accountability, fairness, and transparency. Governance can be applied to various domains, including corporate, IT, project, and data governance.

**IT architecture is a form of governance** because it **establishes structured frameworks** for managing and controlling an organization's technology resources and processes. It ensures alignment with business objectives, promotes standardization, manages risks, optimizes resources, facilitates change management, supports decision-making, measures performance, and fosters innovation. IT architecture governance involves defining the technological infrastructure, setting standards for technology use, and ensuring that all technology-related activities align with the organization's overall goals. This form of governance provides a comprehensive approach to managing technology, ensuring that it supports the organization's strategic direction and operational needs.

The difficulty of governance stems from the need to navigate a complex web of diverse interests, rapidly changing conditions, and multifaceted challenges. There is no one-size-fits-all form of governance, as each organization has unique needs, goals, and environments. Effective governance requires adaptability, collaboration, and a commitment to addressing immediate and long-term issues. It involves balancing various stakeholder interests, anticipating and responding to external changes, and continually refining governance practices to meet evolving demands. This complexity demands a strategic approach, robust communication, and a willingness to innovate and adapt to ensure that governance frameworks remain relevant and effective in achieving organizational objectives.

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
* **Highlighting** bad quality software on a [Architectural Analytics](analytics) dashboard to create subtle pressure for people to improve it,
* Tracking of **tech debt** to create awareness about its size and lead action to reduce it,
* **Visualizing cost trends** of cloud services per team to stimulate teams to improve the performance efficiency of their software.

Nudges can frequently lead to better alignment and more harmonization without the negative consequences of mandates, bans, or taxation.

Grounded Architecture is well aligned with ideas of nudging. I designed many [Architectural Analytics](analytics) tools to **highlight areas and issues** we wanted (nudged) people to improve. The [Collaborative Networks](people) can create mechanisms for sharing experiences, promoting **positive examples**, and capturing lessons learned to help people make better, more informed decisions. In the [Operating Model](operating-model), I use the operating model that stimulates people to make decisions autonomously but **nudges them to stay well-aligned** and connected to the organizational strategic direction.


<br>
## Taxation (Economic Incentives)

Governing with taxes is a strategic approach where individuals or departments are not prohibited from making choices or decisions. Instead, they are required to "pay" some form of tax on the resources they use. This system creates a feedback loop that encourages responsible resource consumption and helps optimize overall system efficiency. One practical application of this approach is in managing the costs of public cloud usage within an organization. By cross-charging these costs across various departments or projects, each unit receives a clear signal about their resource consumption. This not only helps in allocating costs accurately but also promotes awareness and encourages efforts to minimize unnecessary usage, effectively preventing the "tragedy of the commons," where unrestricted access to shared resources can lead to overconsumption and depletion.

<div class="quote">
Governing with taxes is a form of guiding in which people are not forbidden to make some decisions but need to "pay" some form of taxes on used resources.
</div>

<br>
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/credit-squeeze-g61ddead85_1920.png">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/stevepb-282134/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=522549">Steve Buissinne</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=522549">Pixabay</a>
</div>

Compared to nudging, which influences behavior subtly by providing information or setting default choices without imposing direct consequences, taxes introduce tangible consequences. For example, projects that exceed budgeted IT costs due to excessive resource consumption might be canceled. The role of an architecture practice in this form of governance is crucial. It involves ensuring that taxation policies are based on accurate and comprehensive data, using public cloud cost reports and other relevant information to inform tax rates and policies. Transparency is essential, allowing all stakeholders to understand how and why taxes are levied and providing clear insights and reports detailing the basis of taxation and its impact on resource consumption.

Developing efficient feedback loops is another critical aspect, providing timely and actionable feedback on critical metrics related to taxes and continually refining and optimizing the taxation system. [Architectural Analytics](analytics) plays a key role in this approach by aggregating and analyzing all data related to resource consumption and taxation, generating insights from public cloud cost reports, and guiding decision-making. Collaborative Networks ensures alignment of organizational processes, goals, and working methods with the taxation syst[2022-06-03-skills.markdown](2022-06-03-skills.markdown)em, fostering a culture of responsible resource usage and continuous improvement.

In conclusion, governing with taxes is a robust approach to resource management that balances autonomy with accountability. By implementing a data-driven and transparent taxation system, organizations can optimize resource usage, prevent overconsumption, and drive meaningful change. An an architecture practice, supported by strong Architectural Analytics and Collaborative Networks, is essential in achieving these goals and ensuring the sustainability of shared resources.

<br>
## Mandates and Bans

Governing with mandates and bans involves guiding people by explicitly defining what they should or should not do. In various workplaces, such mandates and bans have played a limited yet important role in defining the broader strategic boundaries of choices available to people. For instance, restricting the use of public cloud providers to specific vendors or adhering to strict privacy and security procedures needs to be explicitly defined and controlled.

Using bans with care and as a last resort is essential to avoid unnecessary blocking or slowing down development and innovation. However, mandates and bans can help clarify critical topics where nudging or taxation would not be sufficient. For example, having clear rules and control mechanisms to avoid breaking privacy or financial laws can prevent unnecessary incidents and damage. Explicitly defined mandates and bans can ensure compliance with important regulations and safeguard the organization's integrity and reputation.

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

[Architectural Analytics](analytics) is crucial for creating **clarity and transparency**. For example, it can provide insights through security reports or maps of areas in the source code or infrastructure that need monitoring and controlling based on privacy or security requirements. This foundation helps in identifying and mitigating risks, ensuring that the organization's technology landscape aligns with its governance frameworks.

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
