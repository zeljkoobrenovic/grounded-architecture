

# Economic Modeling With ROI and Financial Options: Learning From the Finance Field {#economics}

![](assets/images/istock/iStock-1503371245.jpg)
^image by microstockhub from istock^

**IN THIS SECTION, YOU WILL:** Get two answers to the question of the economic value of architecture: the return on investment metaphor and the selling options metaphor.

{pagebreak}

A> **KEY POINTS:**
A> * Architects are frequently asked about **the economic value of architecture** or technology investments.
A> * Answering this question is **a crucial skill for any senior architect**, especially with a **non-technical audience**.
A> * I sketch **two answers** to this question: **the return on investment metaphor** and **the selling options metaphor**.

Decision-making in organizations is often an **economic risk exercise**. Financial and risk models help leaders evaluate alternatives, compare trade-offs, and make decisions with more discipline. They support forecasts, expose assumptions, and make uncertainty easier to discuss.

These models also improve resource allocation. By estimating future costs, benefits, and risks, they help organizations use limited resources more deliberately and prepare for plausible disruptions rather than reacting too late.

They are equally valuable in strategic planning. Good models help organizations anticipate challenges and opportunities, test scenarios, and identify risks early enough to respond effectively.

Organizations conduct financial and risk modeling exercises, such as ROI calculations, for several key reasons:

* **Decision-Making Support**: Evaluate investments and compare alternatives to allocate resources effectively.
* **Risk Management**: Identify potential risks and perform sensitivity analysis to anticipate and mitigate issues.
* **Budgeting and Planning**: Aid in resource allocation, detailed budgeting, and long-term forecasting.
* **Performance Measurement**: Track progress, measure success, and ensure accountability.
* **Stakeholder Communication**: Build investor confidence and promote transparency with detailed financial projections.
* **Strategic Planning**: Explore different strategic scenarios and support growth-related decisions.
* **Operational Efficiency**: Identify cost reduction opportunities and optimize business processes.
* **Regulatory Compliance**: Ensure accurate financial reporting and assess regulatory risks.

Because financial and risk modeling matters in every organization, architects are often asked about the **economic value of technology investments and architecture**. Answering that question clearly is a crucial skill for any senior architect, especially when speaking to a non-technical audience.

Within this book, that question matters for a broader reason. Grounded Architecture argues that architecture should improve execution, adaptability, and decision-making, not just system elegance. Economic framing helps make that contribution visible in language that business leaders can use.

Good architecture requires investment. That investment may take the form of time and effort spent on architectural patterns, technical debt reduction, or refactoring. We therefore need a credible way to explain the value created by that effort.

In this post, I sketch two answers to the question of the economic value of architecture:
* the return-on-investment (ROI) metaphor
* the financial options metaphor

## The Return-on-Investment Metaphor

In economic terms, **return on investment (ROI)** is a ratio between profits and costs over some period. In other words, ROI shows how much you **get back from your investment**. 

![](assets/images/istock/iStock-1386532266.jpg)
^image by nicoelnino from istock^

A high ROI means the investment's gains compare favorably to its cost. As a performance measure, you can use ROI to evaluate an investment's efficiency or compare the efficiencies of several different investments (Figure 1).

![](assets/images/economics/roi-model.png)
**Figure 1:** *An illustration of the ROI metaphor. Investment leads to lower costs or higher value. It takes some time to reach a break-even point when an additional value has compensated for the investment. After the break-even point, we earn more than without the investment.*

An investment in **good architecture can increase the ROI of IT**. A strong example comes from Martin Fowler’s argument for [investing in internal quality](https://martinfowler.com/articles/is-quality-worth-cost.html). Figure 2 summarizes that logic.

Well-architected systems are typically much easier to understand and change. As our systems continuously evolve, the return on investing in making them easier to understand and change can be significant. The primary value of such investment comes from generating fewer errors and bugs, more straightforward modifications, a short time to market, and improved developer satisfaction.

![](assets/images/economics/roi-internal-quality.png)
**Figure 2:** *Software with high internal quality gets a short initial slowdown but delivers more rapidly and cheaply later (source martinfowler.com/articles/is-quality-worth-cost.html).*

The ROI metaphor is easy for non-technical audiences to understand, but it has limits. **Architecture, quality, and productivity are difficult to measure precisely**, so an excessive focus on ROI can reduce the discussion to cost-cutting. Costs are easier to quantify than benefits such as faster delivery or improved adaptability. In addition, not every architectural investment produces a direct and immediate profit increase. Many decisions are made under significant uncertainty. The following section explains why those investments can still be worthwhile.

## The Financial Options Metaphor

Gregor Hohpe has frequently argued that the best way to explain architecture to non-technical people is by using **a financial option metaphor.** A financial option is **a right, but not an obligation, to buy or sell financial instruments at a future time with some predefined price**. As such, a financial option is **a way to defer a decision**: instead of deciding to buy or sell a stock today, you have the right to make that decision in the future at a known price.

![](assets/images/istock/iStock-1283813790.jpg)
^image by olivier le moal from istock^

Options are not free, and a complex market exists for buying and selling financial options. Fischer Black and Myron Scholes computed the value of an option with the [Black-Scholes Formula](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model). A critical parameter in establishing the option's value is the price at which you can purchase the stock in the future, the so-called strike price. The lower this strike price, the higher the value of the option (Figure 3).

![](assets/images/economics/options-model.png)
**Figure 3:** *An illustration of the financial option metaphor. Options have a price, leading to higher initial costs. However, if an opportunity can generate more value, we gain additional profit (or lose it if we do not invest).*

Applying the financial option metaphor to IT architecture, we can argue that **buying options gives the business and IT a way to defer decisions**. Gregor Hohpe gives an example of the server size you need to purchase for a system. If your application is architected to be horizontally scalable, you can defer this decision: additional (virtual) servers can be ordered later at a known unit cost.

Another example of an IT option is architecting your system to **separate concerns**. For instance, deciding early what authentication mechanism an application should use may be challenging. A system that properly separates concerns allows changes to be localized so that updating one aspect of a system does not require expensive changing of the whole system. Such isolation will enable you to change a decision late in the project or even after go-live, at a nominal cost. For example, if authentication is a well-isolated concern, you must refactor only a minimal part of the system to use another authentication system.

The option's value originates from being able to **defer the decision until you have more information** while fixing the price. In times of uncertainty, the value of the options that architecture sells only increases.

As with any analogy, the financial options analogy has its limits. Again, it **is not easy to quantify** architecture values and have metrics for the value of separation of concerns or horizontal scaling. Second, while the metaphor may be easy to grasp for an economic audience, it may **require explaining** to other stakeholders, who may be less familiar with financial options markets.

## Communication Frameworks

UNESCO's [manual for investigative journalism](https://unesdoc.unesco.org/ark:/48223/pf0000193078) says that *"The facts do not tell the story. The story tells the facts."* The same applies to any financial analysis. Good data and analysis can have zero impact if they are not communicated in a way that people understand and lead to action.

### General Framework For Communicting Value of IT Investments

Here, I share communication frameworks I have used to explain the economic value of architecture and technology investment more holistically (Figure 4).

![](assets/images/economics/economics_framework.png)
**Figure 4:** *A framework for discussing investments and options.*

I separate the value of investments in two buckets:
* Increasing and protecting revenue and
* Reducing costs and risks.

#### Top Line: Increasing and Protecting Revenue

Increasing and protecting revenue investments have three forms.

**Investments that create new revenue streams** by creating new products or adding new features. These investments are typically easier to defend and control, as most stakeholders intuitively understand that new functionality is needed to create new value for customers and generate more revenue. An essential aspect of this type of investment is tracking the product's success. Adding new features will not automatically create value for customers or revenue.

**Investments needed to stay ahead.** This type of investment is a less obvious way to protect and increase revenue. It boils down to the fact that you cannot stop developing your product as the rest of the world moves on. As the saying goes, **"It takes all the running you can do to keep in the same place."** For instance, you must keep essential features in parity with the competition, your system must comply with changes in regulations, and your UX must be modern.

**Investments needed to create future options** refer to being in shape to adapt to changes in the market more quickly and to bring new features to the market more quickly. Investing in keeping your system easy to maintain and extend directly creates more opportunities. Another way to look at this value driver is to frame it as preventing a revenue loss due to the impossibility of quickly adapting to future opportunities.

#### Bottom Line: Reducing Costs and Risks

The second bucket relates to the more invisible part of the value created by investments:

**Investments to reduce maintenance costs** need to ensure that your code is easy to understand, change, and test. Such investments directly reduce your most significant cost, people costs, as code that is easy to maintain requires fewer people. Alternatively, you can look at these investments as a way to spend more effort on innovation and creating new revenue streams rather than merely keeping the systems in the air. Figure 5 illustrates what may happen if you do not invest. As systems grow in size and complexity, more developers are needed to maintain them. If the system is not easy to maintain, people will avoid touching code as they can easily break it. This situation will lead to a workaround (such as copying and pasting code and diverse hacks). These inefficient workarounds further increase the size and complexity of code, requiring even more developers to maintain it. And the vicious, expensive cycle continues.

{pagebreak}
![](assets/images/economics/unsustainable-sw-dev.png)

**Figure 5:** *A downward spiral of poorly maintainable code.*

**Investments in reducing infrastructure costs** reduce spending and, if successful, are more directly visible. Such investments could take the form of redesigning your application to be more elastic, scaling up and down with minimal overhead. They could also create more transparency to have a precise image of all cost drivers and mechanisms to react quickly to any undesirable cost increases.

**Investments in reducing license and vendor costs** ensure that there is no unnecessary diversity of technologies and vendor contracts and that you can leverage economies of scale, as having fewer vendors with more users enables negotiating more favorable contracts. 

**Investments in reducing risk costs**. When your system is down, your business is disrupted, and you lose revenue. According to [diverse studies](https://www.atlassian.com/incident-management/kpis/cost-of-downtime), the average cost of downtime ranges from $2,300 to $9,000 per minute. You must invest in keeping your system reliable and secure to avoid losing revenue and disrupting your business. While the benefits of these types of investments are huge, the challenge with building the business case for this investment is that a reliable system will only create a few incidents, making it less tangible for many stakeholders to understand the importance of continuing such investments. Or, as noted by Repenning and Sterman "[Nobody Ever Gets Credit for Fixing Problems that Never Happened](https://web.mit.edu/nelsonr/www/CMR_Getting_Quality_v1.0.html)".

### The Tech Debt Reduction ROI Framework

In addition to the general framework discussion in this section, I frequently used the following framework to visually communicate how increasing technical debt progressively reduces profit through added operating, delay, and instability costs, emphasizing the importance of managing technical debt to preserve profitability.

![](assets/images/figures/tech_debt_profitability.png)
**Figure 6:** *A framework for discussing ROI of tech debt reduction from a profitability standpoint.*

Figure 6 illustrates a framework for understanding the ROI (Return on Investment) of reducing technical debt, showing the impact on profit and costs across three progressive dimensions:

1. **Extra Operating Costs**: Technical debt can increase operating costs due to inefficiencies (e.g., complexity or lack of automation may require more people and time to make changes), reducing profit by raising expenses.

2. **Costs of Delays**: This dimension represents the loss of profit related to delays. Technical debt can impact the ability to deliver new features or fix issues promptly.

3. **Instability Costs**: Tech debt is a risk that can lead to less stable systems, with more frequent and longer downtimes and errors. Instability and downtime further reduce profit.

This framework shows the compounded effect of technical debt, where extra operating costs increase overall costs, and instability and downtime further reduce profit.

Taken together, the ROI metaphor, the options metaphor, and the communication frameworks in this chapter offer architects a more practical way to discuss value. They do not eliminate uncertainty, but they make trade-offs easier to explain and decisions easier to align around. That is the larger connection to Grounded Architecture: better architecture is not only about making better systems, but also about making better economic choices under real organizational constraints.

## To Probe Further

* [Architecture: Selling Options](https://architectelevator.com/architecture/architecture-options/), by Gregor Hohpe, 2016
* [Is High Quality Software Worth the Cost?](https://martinfowler.com/articles/is-quality-worth-cost.html), by Martin Fowler, 2019
* [Don't get locked up into avoiding lock-in](https://martinfowler.com/articles/oss-lockin.html), by Gregor Hohpe, 2019

## Questions to Consider
Use the following questions to examine how you explain the economic value of architecture and technology choices.

* *How can you effectively communicate the value of architectural investments to non-technical stakeholders in your organization?*
* *How do you weigh the importance of short-term cost reductions against long-term architecture improvements?*
* *How could the return-on-investment metaphor be useful in explaining the benefits of architecture investment to your team or organization?*
* *If you were to use the ROI metaphor to explain architecture's value to non-technical stakeholders, what examples or case studies would you use to illustrate your points?*
* *What are some potential pitfalls of relying too heavily on the ROI metaphor when deciding on architecture investments?*
* *How could you use the financial options metaphor to explain the value of architectural investments? What are the benefits and challenges of using this metaphor in your organization?*
* *How can you better quantify the value of architectural investments, particularly in terms of attributes like time-to-market and developer satisfaction?*
* *How might the financial options metaphor apply to recent decisions facing your organization or team, and how could it influence those decisions?*
