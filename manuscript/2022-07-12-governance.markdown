

# Architecture Governance: Nudge, Taxation, Mandates {#governance}

![](assets/images/arch/greece-1594689_1920.jpg)
^image by nonbirinonko from pixabay^

**IN THIS SECTION, YOU WILL:** Understand that a technology governance model should be a well-balanced hybrid of three different styles of governing: mandates and bans, taxes, and nudging.

{pagebreak}

A> **KEY POINTS:**
A> * Architecture practice should support governance models adaptable to organizations' complex and diverse needs. A technology governance model should be a well-balanced hybrid of three different styles of governing: mandates and bans, taxes, and nudging.
A> * Nudging is a form of governing where you create subtle or indirect suggestions influencing someone's behavior or decision-making without forcing them or limiting their freedom of choice.
A> * Governing with taxes (economic incentives) is a form of guiding in which people are not forbidden to make some decisions but need to "pay" some form of taxes on used resources.
A> * With mandates and bans, you guide people by explicitly defining what they should or should not do.

Architecture practice should support governance models adaptable to organizations' complex and diverse needs. By governing, I mean guiding technology **choices in the organization in a particular direction** aligned with the strategy. I see a technology governance model as a well-balanced hybrid of three different styles of governing:
* **nudging**,
* **taxes** (economic incentives), and
* **mandates and bans**.

## Nudging

In behavioral economics and psychology, a nudge is a **subtle or indirect suggestion** influencing someone's behavior or decision-making **without forcing them or limiting their freedom of choice**. Nudges can be applied in various settings, such as policy-making, marketing, and personal interactions, to encourage people to make better choices, improve their well-being, or achieve specific goals.

![](assets/images/arch/iStock-1390608248.jpg)
^image by istock^

A nudge can take many forms, such as a **slight change in the environment**, a **gentle reminder**, a **positive reinforcement**, or a **default option**. For example, placing healthy food options at eye level in a cafeteria can nudge people to choose healthier meals. Or setting a default option for organ donation can increase the number of donors.

The concept of a nudge was popularized by the book **"Nudge: Improving Decisions About Health, Wealth, and Happiness"** by Richard Thaler and Cass Sunstein, which argues that various **cognitive biases and heuristics** often influence people's decisions, and that nudges can help people overcome these biases and make better choices.

Richard Thaler and Cass Sunstein also introduced the concept of **choice architecture** as a critical component of nudging. It refers to how the options are presented to individuals, which can significantly influence their choices. Choice architecture is **the design of the decision-making environment**, which includes the layout, structure, and organization of available options.

In architecture, nudges could include:
* architectural **principles** as informal decision guidelines,
* recommendations for **best practices** to stimulate introduction and alignment around such practices, 
* default options for technology choices via 
[**golden paths**](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/)
* **highlighting** bad quality software on a [Data Foundation](#data) dashboards to create subtle pressure for people to improve it,
* tracking of **tech debt** to create awareness about its size and lead action to reduce it,
* **visualizing cost trends** of cloud services per team to stimulate teams to improve the performance efficiency of their software.

Nudges can frequently lead to better alignment and more harmonization without the negative consequences of mandates, bans, or taxation.

Grounded Architecture is well aligned with ideas of nudging. I designed many [Data Foundation](#data) tools to **highlight areas and issues** we wanted (nudged) people to improve. And the [People Foundation](#people) can create mechanisms for sharing experiences, promoting **positive examples**, and capturing lessons learned to help people to make better, more informed decisions. And in the [Architecture Activities Platform](#activities-platform), I use the operating model that stimulates people to make decisions autonomously but **nudges them to stay well-aligned** and connected to the organizational strategic direction.

## Taxation (Economic Incentives)

Governing with taxes is a form of guidance in which we do not forbid people to make choices or decisions but **need to "pay" some form of taxes on used resources**. For instance, costs of public cloud usage could be **cross-charged across the organization**, providing a helpful feedback loop to optimize our systems and avoid unnecessary resource consumption, avoiding the "tragedy of commons" which frequently happens when there are no limits on shared resource consumption (e.g., public cloud budget). 

![](assets/images/arch/credit-squeeze-g61ddead85_1920.png)
^image by steve buissinne from pixabay^

The role of architecture practice in this form of governance should be to ensure that "taxation" is **data-driven and transparent** and to create efficient feedback loops on critical metrics related to "taxes."

The [Data Foundation](#data) can include and provide all **data regarding "taxes,"** for instance, via insights based on public cloud cost reports. The People Foundation can facilitate **aligning processes**, goals, and working methods to ensure that taxation leads to desired and **meaningful change**.

## Mandates and Bans

By governing with mandates and bans, I mean guiding people by **explicitly defining what they should or should not do**. In places I worked in, such mandates and bans have had a limited by important place to **define broader strategic boundaries of choices** people can make. For instance, restricting the usage of public cloud providers to specific vendors or following **strict privacy and security procedures** needs to be explicitly defined and controlled.

You should **use bans with care** and as a last resort to avoid unnecessary blocking or slowing down development and innovation. Nevertheless, they could help clarify critical topics where nudging or taxation would not be sufficient. For instance, having clear rules and control mechanisms to avoid breaking privacy or financial laws can prevent unnecessary incidents and damage. 

![](assets/images/arch/ethics-g277df4183_1920.jpg)
^image by tumisu from pixabay^

The role of architecture in this form of governing should be to be **a stakeholder but not a sole owner in defining mandates and bans**. Mandates and bans frequently need to be defined in collaboration with others, such as security and legal functions. The architecture practice can help by **creating clarity and providing transparency**.

The [Data Foundation](#data) is crucial in creating **clarity and transparency**, for instance, via insights security reports or maps of areas in source code or infrastructure that needed monitoring and controlling based on privacy or security requirements.

The [People Foundation](#people) can help propagate the decision and ensure its **positive impact and acceptance**. You should never order or forbid people to do some things routinely. Spending enough time with all stakeholders to explain the **reasons and motivations** behind introducing some limitations is crucial to ensure the effective working of mandates and bans. A strong People Foundation provides strong connections with key stakeholders and can leverage them to change ways of working more smoothly.

## Questions to Consider

* *What are the key components of the governance model in your organization, and how do mandates, taxes, and nudging influence them?*
* *How does your organization currently handle mandates and bans? Are they explicit and aligned with the overall technology strategy?*
* *How effective is the enforcement of these mandates and bans in your organization? Could improvements be made in creating clarity and providing transparency?*
* *How does your organization approach taxation as a form of governance? Is it transparent, data-driven, and efficient?*
* *Can you identify any examples of 'nudging' in your current architectural environment? How effective are these subtle suggestions in influencing behavior or decision-making?*
* *How does your organization promote best practices and align around them? Are there any 'golden paths' for technology choices?*
* *How are your organization's tech debt and the cost trends of cloud services tracked and visualized? Do these methods create enough awareness to stimulate improvement?*
* *How could you better utilize nudging to improve organizational decision-making? What biases or barriers to effective decision-making could you target with this approach?*
