---
layout: post
section: "Doing Architecture"
title: "Architecture Governance: Nudge, Taxation, Mandates"
position: 7012
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
icon: pragmatics.png
permalink: governance
timetoread: 15 min
excerpt: "Grounded Architecture supports governance models adaptable to organizations' complex and diverse needs. I see a technology governance model as a well-balanced hybrid of three different styles of governing: nudging, taxes, and mandates and bans."

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
> * Grounded Architecture supports governance models adaptable to organizations' complex and diverse needs. A technology governance model should be a well-balanced hybrid of three different styles of governing: mandates and bans, taxes, and nudging.
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

Grounded Architecture supports governance models adaptable to organizations' complex and diverse needs. By governing, I mean guiding technology **choices in the organization in a particular direction** aligned with the strategy. I see a technology governance model as a well-balanced hybrid of three different styles of governing:
* **nudging**,
* **taxes** (economic incentives), and
* **mandates and bans**.

Grounded Architecture supports governance models **adaptable to organizations' complex and diverse needs**.

<br>
## Nudging

In behavioral economics and psychology, a nudge is a **subtle or indirect suggestion** influencing someone's behavior or decision-making **without forcing them or limiting their freedom of choice**. Nudges can be applied in various settings, such as policy-making, marketing, and personal interactions, to encourage people to make better choices, improve their well-being, or achieve specific goals.

<br>
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/iStock-1390608248.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

A nudge can take many forms, such as a **slight change in the environment**, a **gentle reminder**, a **positive reinforcement**, or a **default option**. For example, placing healthy food options at eye level in a cafeteria can nudge people to choose healthier meals. Or setting a default option for organ donation can increase the number of donors.

<div class="quote">
A nudge is a subtle or indirect suggestion influencing someone's behavior or decision-making without forcing them or limiting their freedom of choice.
</div>

The concept of a nudge was popularized by the book **"Nudge: Improving Decisions About Health, Wealth, and Happiness"** by Richard Thaler and Cass Sunstein, which argues that various **cognitive biases and heuristics** often influence people's decisions, and that nudges can help people overcome these biases and make better choices.

Richard Thaler and Cass Sunstein also introduced the concept of **choice architecture** as a critical component of nudging. It refers to how the options are presented to individuals, which can significantly influence their choices. Choice architecture is **the design of the decision-making environment**, which includes the layout, structure, and organization of available options.

In architecture, nudges could include:
* architectural **principles** as informal decision guidelines,
* recommendations for **best practices** to stimulate introduction and alignment around such practices, 
* default options for technology choices via 
[**golden paths**](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/)
* **highlighting** bad quality software on a [Data Foundation](data) dashboards to create subtle pressure for people to improve it,
* tracking of **tech debt** to create awareness about its size and lead action to reduce it,
* **visualizing cost trends** of cloud services per team to stimulate teams to improve the performance efficiency of their software.

Nudges can frequently lead to better alignment and more harmonization without the negative consequences of mandates, bans, or taxation.

Grounded Architecture is well aligned with ideas of nudging. I frequently designed many [Data Foundation](data) tools to **highlight areas and issues** we wanted people to improve. And the [People Foundation](people) can create mechanisms for sharing experiences, promoting **positive examples**, and capturing lessons learned to help people to make better, more informed decisions. And in the [Architecture Activities Platform](activities-platform), I use the operating model that stimulates people to make decisions autonomously but **nudges them to stay well-aligned** and connected to the organizational strategic direction.


<br>
## Taxation (Economic Incentives)

Governing with taxes is a form of guidance in which we do not forbid people to make choices or decisions but **need to "pay" some form of taxes on used resources**. For instance, costs of public cloud usage could be **cross-charged across the organization**, providing a helpful feedback loop to optimize our systems and avoid unnecessary resource consumption, avoiding the "tragedy of commons" which frequently happens when there are no limits on shared resource consumption (e.g., public cloud budget). 

<div class="quote">
Governing with taxes is a form of guiding in which people are not forbidden to make some decisions but need to "pay" some form of taxes on used resources.
</div>

<br>
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/credit-squeeze-g61ddead85_1920.png">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/stevepb-282134/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=522549">Steve Buissinne</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=522549">Pixabay</a>
</div>

The role of Grounded Architecture in this form of governance should be to ensure that "taxation" is **data-driven and transparent** and to create efficient feedback loops on critical metrics related to "taxes."

The [Data Foundation](data) can include and provide all **data regarding "taxes,"** for instance, via insights based on public cloud cost reports. The People Foundation can facilitate **aligning processes**, goals, and working methods to ensure that taxation leads to desired and **meaningful change**.

<br>
## Mandates and Bans

By governing with mandates and bans, I mean guiding people by **explicitly defining what they should or should not do**. In places I worked in, such mandates and bans have had a limited by important place to **define broader strategic boundaries of choices** people can make. For instance, restricting the usage of public cloud providers to specific vendors or following **strict privacy and security procedures** needs to be explicitly defined and controlled.

You should **use bans with care** and as a last resort to avoid unnecessary blocking or slowing down development and innovation. Nevertheless, they could help clarify critical topics where nudging or taxation would not be sufficient. For instance, having clear rules and control mechanisms to avoid breaking privacy or financial laws can prevent unnecessary incidents and damage. 

<div class="quote">
By governing with mandates and bans, I mean guiding people by explicitly defining what they should or should not do.
</div>
<br>

<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/ethics-g277df4183_1920.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/tumisu-148124/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2991600">Tumisu</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2991600">Pixabay</a>
</div>

The role of architecture in this form of governing should be to be **a stakeholder but not a sole owner in defining mandates and bans**. Mandates and bans frequently need to be defined in collaboration with others, such as security and legal functions. The Grounded Architecture can help by **creating clarity and providing transparency**.

The [Data Foundation](data) is crucial in creating **clarity and transparency**, for instance, via insights security reports or maps of areas in source code or infrastructure that needed monitoring and controlling based on privacy or security requirements.

The [People Foundation](people) can help propagate the decision and ensure its **positive impact and acceptance**. You should never order or forbid people to do some things routinely. Spending enough time with all stakeholders to explain the **reasons and motivations** behind introducing some limitations is crucial to ensure the effective working of mandates and bans. A strong People Foundation provides strong connections with key stakeholders and can leverage them to change ways of working more smoothly.

## Questions to Consider

* *What are the key components of the governance model in your organization, and how do mandates, taxes, and nudging influence them?*
* *How does your organization currently handle mandates and bans? Are they explicit and aligned with the overall technology strategy?*
* *How effective is the enforcement of these mandates and bans in your organization? Could improvements be made in creating clarity and providing transparency?*
* *How does your organization approach taxation as a form of governance? Is it transparent, data-driven, and efficient?*
* *Can you identify any examples of 'nudging' in your current architectural environment? How effective are these subtle suggestions in influencing behavior or decision-making?*
* *How does your organization promote best practices and align around them? Are there any 'golden paths' for technology choices?*
* *How are your organization's tech debt and the cost trends of cloud services tracked and visualized? Do these methods create enough awareness to stimulate improvement?*
* *How could you better utilize nudging to improve organizational decision-making? What biases or barriers to effective decision-making could you target with this approach?*
