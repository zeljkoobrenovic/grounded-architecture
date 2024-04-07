

# Decision Intelligence in IT Architecture {#decision-intelligence}

![](assets/images/arch/iStock-1365878406.jpg)
^image by istock^

**IN THIS SECTION, YOU WILL:**  Learn the basics of decision intelligence, the discipline of turning information into better actions, and its relevance for IT architecture practice.

{pagebreak}

A> **KEY POINTS:**
A> * Decision intelligence is the discipline of turning information into better actions.
A> * A decision involves more than just selecting from available options; it represents a commitment of resources you cannot take back.
A> * Many factors make the decision-making process more or less complex, such as the number of options, costs, cognitive load, emotions, and access to information. 
A> * Data can significantly improve decision-making, but data do not guarantee objectivity and can even lead to more subjectivity.

**Decision intelligence** is a discipline concerned with selecting between options. It combines the best of **applied data science**, **social science**, and **managerial science** into a unified field that helps people use data to improve their lives, businesses, and the world around them. **[Cassie Kozyrkov](https://en.wikipedia.org/wiki/Cassie_Kozyrkov)** has popularized the field of decision intelligence and created several valuable resources to understand the decision-making process. I recommended her [posts](https://www.linkedin.com/pulse/introduction-decision-intelligence-cassie-kozyrkov/) and [online lessons](https://www.linkedin.com/learning/decision-intelligence/) to all architects because decision-making is an essential part of IT architects' job. 

In this and next chapter, I summarized some of the critical lessons I learned from Cassie Kozyrkov's resources and used them in practice. In their daily work, IT architects are involved in decision-making in several ways: 
* By **making decisions** (e.g., moving applications from a private data center to a public cloud). 
* By **creating mechanisms** for teams to make better decisions (e.g., [advisory forums](https://martinfowler.com/articles/scaling-architecture-conversationally.html)).
* By **creating [options](https://architectelevator.com/architecture/architecture-options/)** for teams to make decisions later.

In all these situations, decision intelligence is a crucial skill for architects. 

![](assets/images/arch/iStock-1194231226.jpg)
^image by istock^

## Basics of Decision-Making

Let's starts wit some basics: definition of decisions, outcomes, and goals.

### Decision Is More Than Selecting Among Options

Kozyrkov defines a decision as more than just selecting from available options. A decision represents **an irrevocable allocation of resources**, which could be monetary, physical actions, time, or options. Whatever you decide to do, you will spend some time and other resources on it and will not get that time and resources back. The only way to reverse the consequences of some decisions is to invest more resources in that reversal.

Less obviously, optionality is also a resource. Choosing between two options may seem cost-free. However, the possibility of selecting some options is frequently lost once you decide. This loss of opportunity is considered an irrevocable allocation of resources. For instance, before starting a project in IT, you can select from many programming languages and frameworks to implement your system. However, after that, it is very costly to change that decision as you need to rewrite your system entirely in another language. Having or losing options is directly related to a frequent topic of IT, a vendor lock-in, and it is one of the main drivers behind [creating or avoiding lock-in](https://martinfowler.com/articles/oss-lockin.html).

From an IT architecture perspective, another important lesson of this view on decisions is that if there is no irreversible allocation of resources, we cannot talk about decisions. Ivory tower architects who make "principal decisions" that no one follows are technically not making any decisions.

### Outcome = Decision x Luck

An outcome is **a result of a decision**. Two factors influence it: 
* **the quality of the decision-making process** and 
* an **element of randomness**, or **luck**. 

We can only control our decision-making process. **Luck is beyond our control** but often plays a role in complex situations. If we only consider the outcome, we can mistakenly attribute good chance to good decision-making skills and bad luck to bad decision-making skills.

We can only control our decision process. Luck is beyond our control and often plays a role in complex situations. Consequently, if we only consider the outcome, we can mistakenly **attribute good luck to good decision-making skills**, and bad luck to bad decision-making skills. 
 

To judge a decision, we should not look at the outcome only, but we need to **understand the context and information available at the time of the decision**. For instance, imagine you are driving a car on the road, and your navigation system gives you two routes you could follow, one 30 minutes shorter. You decide to follow the shortest route. But 10 minutes after you choose to follow that route, the accident happens on your route, which creates a traffic jam, where you spend an hour more than if you were following another route. Does that mean your decision was wrong and you should follow longer routes next time? No. All information known at the time of the decision pointed out that following the first route would save time and energy. But traffic and all realistic real-world situations have randomness, such incidents beyond your control. So you've made a wise decision, but the outcome was terrible.

The most prominent recent example is, of course, the COVID-19 epidemic. The COVID‐19 epidemic has pushed the global economy and humanity into a disaster. Some industries, like travel and tourism, were heavily negatively affected (e.g., Uber, Booking.com, [Airbnb](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9998299/)). But COVID-19 has also positively impacted online tools, accelerated the development of existing tools, and created a new wave of online collaboration tools & software (e.g., Zoom, Microsoft Teams, Slack, Miro).

### Economics of Decision-Making

I've frequently been part of trivial decisions that wasted many people's time and energy. But not all decisions are worthwhile the effort invested to make them. The "[**value of clairvoyance**](https://en.wikipedia.org/wiki/Value_of_information)" concept (also called the value of **perfect information**) in decision analysis can help you gauge the appropriate amount of effort, information, and resources to **invest in a decision**. 

For low-value decisions, perfectionism is unnecessary. Conversely, high-value decisions warrant a substantial investment of resources. To approach decision-making effectively, Kozyrkov recommends to:
* Start by visualizing your decision's **potential best and worst outcomes** to understand the stakes involved.
* Next, apply the "value of clairvoyance" technique. Imagine having access to a psychic who can predict the future, **offering the perfect answer** to your decision. Consider the maximum amount of resources – money, time, or effort – you would be willing to expend for this ideal insight.

This exercise helps determine **the actual value of achieving perfect clarity** and making the best possible choice. 

If you realize the **value of perfect information is low** for a particular decision, it's more efficient to **rely on intuition**. This approach helps balance the investment in decision-making with the importance of the decision itself.

For instance, a decision on a preferred public cloud provider is a high-impact decision requiring in-depth analysis. Approval of costs for an individual developer license that can be canceled at any month is a low-value decision. Nevertheless, it is not uncommon for companies to have procurement processes that require equal time and energy for approval of a multi-year multi-million investment and less than 100 EUR library license.

## Preparing for Making Decisions

Decisions are **steering wheels for reaching our goals**. Consequently, it is crucial to understand and define goals properly. But also to understand if there is a decision to be made at all.

![](assets/images/arch/iStock-1301200404.jpg)
^image by istock^

### Setting Goals

Practical goal setting involves **understanding your priorities and opportunities**. Setting goals misaligned with your opportunities and priorities is pointless. By identifying **what matters most** to you and **discarding others' non-priorities**, you can focus on what's truly important.

Common **mistakes in goal setting** include creating goals that are either **too vague**, leading to deprioritization, or **too concrete**. The solution lies in the clarity that layered goals bring, each serving different purposes. In managerial sciences, goals are classified into three types: outcome, performance, and process goals:

* **Outcome goals** represent the ultimate win but might be vague and influenced by external factors. An example is aiming to be as healthy
as possible. In business, such high-level goals outcome goals include creating value for customers and being profitable. However, these goals are challenging to directly measure and control.

* **Performance goals** are measurable and, if realistic, mostly within your control, like running five miles in under 45
minutes. In business, increasing the number of visits to a website, reducing infrastructure costs, and growing revenue are typical measurable performance goals. However, they might be aspirational and challenging to manage in detail. 

* **Process goals** are measurable and entirely within your control, such as running for 45 minutes every other day, regardless of speed or distance. In business, such goals could be releasing new product features promptly or a targeted marketing campaign. They provide a trackable process but should always align with and serve the outcome goal.

You need to define all three types of goals with a clear relationship among them. For instance, running a targeted marketing campaign (a process goal) is expected to bring more visitors to the site and increase revenue (performance goals), ultimately bringing more value to our customers and making our business more profitable (outcome goals). Consolidating IT infrastructure and IT (a process goal) is expected to reduce overall costs (a performance goal), making our business more profitable (an outcome goal).

Be cautious not to let **process goals overshadow your ultimate objectives**. Wise goal setting involves **a layered approach**, aligning your goals with your priorities, setting aspirational targets, and establishing manageable processes while remaining flexible and responsive to your needs and circumstances.

### Aligning Goals: The Principal-Agent Problem

One of the common problems with goal setting in complex organizations is the **principal-agent problem**. This concept from economics highlights a common issue in business and personal decision-making: **the interests of the decision-maker (agent) differ from those of the owner or principal**. For example, the owners (principals) may prioritize growth in a business, while the managers (agents) might seek personal benefits like increased leisure time or higher salaries. This conflict of interest can lead to mismanagement if addressed. In IT, one typical issue is software technology selections. Individual teams may prefer to use different technologies based on their knowledge and personal preferences. However, allowing each team total freedom may increase the complexity and diversity of the technology landscape. However, it is usually better for an IT organization to keep the number of technologies we use to a minimum to efficiently train new people, maintain our code, and support moves between teams.

The principal **must establish rules or constraints** to **align the agent's decisions with their interests**. This concept can also apply to personal decision-making, particularly in balancing short-term desires and long-term goals.

By **pre-emptively setting constraints**, you can help **steer your choices towards long-term goals** and avoid decisions that may seem appealing in the short term but are detrimental in the long run. For instance, in our example of technology selection, one approach I often used to define constraints in the form of [golden paths](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/), supporting limited technology sets only, and making it difficult to use other.

### Is There A Decision To Be Made?

In decision-making, mainly when you're not the primary decision-maker, it's crucial to determine how you can contribute effectively as a decision expert. The first step is to determine whether a decision needs to be made. Sometimes, the primary decision maker has already decided, and they may need your input only to confirm their decision or tick the boxes in the process. 

Before you invest your time and energy in pretending you are making a decision, you need to clarify whether there is a possibility of making a decision. According to Cassie, the key to answering this question lies in two steps. 
* First, determine what the primary decision maker would **do without your involvement**. 
* Then, ask them a strategic question: "**What would it take to change your mind?**" If the answer to this question is "Nothing!", then you cannot make any new decisions.

This question is powerful for several reasons:
* **Initiates Insightful Conversations**: It opens up a dialogue revealing necessary information about the decision-making process and the decision-maker's mindset.
* **Identifies the Decision-Maker**: The response helps you understand if the person you're speaking with holds the decision-making authority, addressing the issue highlighted in the previous video.
* **Determines the Presence of a Real Decision**: Understanding if any information could alter the decision-maker's stance is crucial. If their mind is already made up and no information could change them, then there isn't an actual decision to be made; any data provided would be for persuasion rather than for aiding in decision-making.

In essence, this question helps assess the decision-making landscape, the decision-maker's openness to new information, and whether there's genuine room for making or influencing a decision. 

![](assets/images/arch/iStock-1043738948.jpg)
^image by istock^

## Factors Influencing Decision-Making

Here, we explore key factors influencing decision-making complexity and decisiveness.

### Decision-Making Complexity

Some decisions are easier to make than others. Kozyrkov identifies 14 factors that can make decision-making more or less complex:

#### Number of options 

Decision-making becomes simpler with **fewer options.** When choosing between a limited number of options, it's straightforward. However, as more options, especially combined choices, are introduced, the process becomes more complex, involving **compound decision-making** (several dependent decisions you must make together). The simplest scenario is a straightforward yes or no decision.

#### Clarity of options' boundaries

Some decisions are straightforward when the choice is **clear-cut,** like choosing your meal between a rock and an apple, where the preferable option is obvious. Deciding between two varieties of apples is slightly more challenging but remains easy if the decision **isn't significant or high-stakes**. In IT, having a preferred public cloud provider provides a clear-cut decision about public cloud hosting. Once inside a public cloud, selecting an appropriate service is much more challenging as hundreds of options are available. 

#### Clarity of objectives

Having **clear objectives** is another factor that simplifies decision-making. It involves considering the most effective approach to the decision and quickly determining the criteria for making that choice.

#### Cost of making a decision

**Low-cost** of decision-making simplifies decision-making. These costs include the effort required to **evaluate** information, the ease of **implementing** the decision, and the potential **consequences of any mistakes**. Decisions are easier when these associated costs are low.

#### Costs of reversing a decision

While decisions typically involve a commitment of resources you can't undo, some decisions are considered reversible. If you can **change your decision quickly and with little cost**, the consequences of a wrong choice are less severe, making the decision easier.

#### Cognitive load

If a decision requires **significant mental effort**, such as remembering **many details** or making choices while **distracted,** it becomes more challenging. On the other hand, if you can make the decision easily and consistently, even amidst other tasks or distractions, then it's a simpler decision.

A lot of the work of IT architects involves creating visualizations and abstractions that can reduce cognitive load and make it easier to understand complex systems so that others can make better decisions about them.

#### Emotional impact

If a decision doesn't **evoke strong emotions** or significantly affect you emotionally, it tends to be easier. Conversely, decisions that stir up intense emotions or leave you highly agitated are more difficult.

For instance, the company's decision to use only one frontend programming language significantly affects people unfamiliar with the choice, as they cannot perform at a senior level in new technology for a long time and need to learn many new things. Many people negatively affected by this choice may decide to leave and find a job where they can work with technologies in which they are experts. So, a simple technological decision quickly becomes a personal career-making choice and an HR issue.

#### Pressure and stress

Decisions made under conditions of **low pressure and stress** are generally easier, whereas those made in high-pressure, stressful situations are more challenging.

#### Access to information

Decisions are easier when you **have complete and reliable information readily available**. In contrast, making decisions with only partial information and uncertain probabilities is more challenging. As discussed in the context of statistics, having limited information complicates the decision process as you need to guess missing pieces of information.

#### Risks and ambiguity

Decisions become simpler when there is no **risk or ambiguity involved.** Risk and ambiguity, though different, both complicate decision-making. Ambiguity arises when the probabilities of outcomes are unknown,
making choices uncertain. Risk, on the other hand, involves taking a known gamble, where you understand the potential consequences and likelihoods.

#### Timing

Difficulties arise when the **decision's timing
conflicts with other simultaneous decisions** or when there's **insufficient time** to consider the choice thoroughly. Situations requiring a rapid response can add significant pressure, making the decision process more challenging.

#### Impact on others

Making decisions alone is generally easier. When you're the sole decision-maker, without involving others, and the decision's outcome impacts only you, the process is simpler. In contrast, making decisions in a social context is more complex. Factors like **social scrutiny**, considering the **impact on others**, balancing **different preferences and opinions**, and the potential
**effect on your reputation** all add to the difficulty.

#### Internal conflicts

Decisions are more problematic when there are internal conflicts, as opposed to situations where all **motivations and incentives align** with the decision. For instance, deciding to make shortcuts in your systems design and skipping steps in a process to get some features quicker to the market vs. spending more time tidying and testing your code is a typical dilemma many software engineers and IT architects face.

#### Adversarial dynamics

Finally, adversarial dynamics impact decision-making. When you face **competition or opposition from others,** these decisions become more challenging compared to those made cooperatively or independently. For example, when you merge two companies with different technology stacks (e.g., one using React and Java in AWS, and another Angular and C# in Azure) and want to consolidate on one stack, you may end up in competition and opposition with people from each company wanting a consolidated stack to be as close as possible to their previous one.

### Factor Influencing Decisiveness

Even when decisions can be made quickly, we may still be indecisive. People can be indecisive for various reasons. 

#### Bad habits

One common cause of indecisiveness is bad habits. Many don't recognize that avoiding a decision is, in itself, a decision. Delaying, postponing, or deprioritizing the decision-making process is a resulting implicit choice, but it doesn't have to be your default mode. But you have the power to change this habit.

For instance, if a company cannot decide on using one consolidated tech stack for its systems, it leads to an **implicit decision** to keep diverse technology stacks with all associated costs and complexity.

#### Overwhelmed by numerous decisions

Indecisiveness can stem from being **overwhelmed by numerous decisions**, especially those of lower priority. **Our cognitive capacity is limited**; we can't focus intensely on everything simultaneously. If **too much attention is devoted to trivial choices**, it leaves less mental bandwidth for more significant decisions. In essence, indecisiveness may indicate a need for recognizing and prioritizing what truly matters. It highlights the need for intentional effort to allocate time and thought to key decisions aligned with one's priorities. This intentionality is crucial for effective decision-making.

For instance, sometimes people see IT architects as the ultimate authority, asking them to approve every trivial change (like upgrading a minor library version). This situation can significantly limit the possibility of architects to work on essential and strategic problems.

#### Emotions and grief

Indecisiveness can also arise from emotional responses, mainly **when all options are undesirable**. In such cases, the most practical approach is to choose the least bad option. After thoroughly evaluating the choices and identifying the least detrimental ones, proceeding with that decision is essential.

However, people often become overwhelmed by emotions like **grief or frustration** when faced with **only unfavorable choices**. This emotional response can lead to a futile search for better options, hoping for new information that realistically won't appear. Once it's clear that no better options will emerge, it **takes courage to move** forward and execute the chosen path.

It's okay to experience and process these emotions, but you should do it concurrently with taking action. On the other hand, when faced with multiple equally appealing options, and the differences between them are minor, it might not be worth the effort to optimize further. In these cases, recognizing that fine-tuning small differences isn't a priority can help make a decision.

If you need help to choose between equally good options, Cassie recommends using a simple method like flipping a coin. If the result of the coin flip leaves you feeling particularly disappointed, it might indicate that the options were more different than you initially thought. This reaction can provide insight and help you make your decision. However, if the differences between the options are minor, it's not worth spending excessive time trying to make the perfect choice. Instead, conserve your energy for more significant decisions.

## Improving Decision Making With Data and Tools

Decision-making has evolved beyond pen and paper, with data playing a crucial role in modern methods. Data, like the one I use in [Data Foundation](#data), while visually appealing and powerful when used correctly, is **only a tool to assist** in making informed decisions. It's a means to an impactful end, but **without purposeful application, data is ineffective**.

![](assets/images/arch/iStock-1316937637.jpg)
^image by istock^

### Data has limitations

Just as not everything written in a book is true, data can be **misleading or incomplete**. It's a collection of information recorded by humans, subject to errors and omissions.

For instance, in the field of artificial intelligence (AI), **AI biases stem from the data it's fed**, reflecting the choices and prejudices of those who compile the data. The issues with AI bias are often due to poor decisions regarding data selection. **Data isn't inherently objective; it carries the implicit values of its creators**.

### Data enhances memory rather than ensuring objectivity

It is crucial to understand that **data's value lies in its ability to enhance memory, not ensure objectivity**. Embracing data means embracing a significant advancement in human potential. It's about transforming information into action, extending beyond the limits of personal memory to make better, more informed decisions.

### Chose the right tool for the job

Cassie Kozyrkov classifies [techniques for the use of data into three groups](https://kozyrkov.medium.com/what-on-earth-is-data-science-eb1237d8cb37):
* **Analytics**: which you can use to get inspired by looking at data,
* **Statistics**: which you can use to make decisions when you need to deal with incomplete information and uncertainty,
* **Machine Learning (ML)/AI**: which you can use to deal with a huge number of decisions and vast volumes of data.

When used correctly, data and the techniques mentioned can enable us to ask better questions and give better answers.

**Good questions** often stem from **being well-informed**, much like gaining insight from looking out of a window in a dark room. Analytics is a discipline that uses data in this fashion, providing a view of the available information. It helps identify viable options, reasonable assumptions, and meaningful questions. Data and Analytics can inspire better questioning by revealing insights that were previously unseen.

However, looking at data and doing **analytics itself isn't decision-making**. As a decision maker, your role is to **set priorities**, choose **relevant topics**, frame the **right questions**, and guide the analysis focus. If the analysis finds nothing intriguing, it's not a failure; it's an opportunity to explore new areas. Analytics is a vital sensory upgrade for modern decision-making, enabling a broader and deeper understanding of the information landscape.

Once when we have better questions, we can also use data to **give better answers**. Depending on the important and type of questions you need to answer, you can get your answers via simple analytics, more complex statistical methods, or even advanced machine-learning and AI techniques.

### Full information is always preferable to partial information

No matter which how you plan to use data, **full information is always preferable to partial information**. If you only have **partial information**, you're **dealing with uncertainty**, and that's where **statistical methods** come in. 

Statistics is used when you don't have all the facts and need to manage uncertainty. They can help you balance the likelihood of a wrong decision against your data budget, considering your risk preferences. 

As a decision maker, it's important to **ask the right questions** and determine **which decisions are worth pursuing**. Only then should you apply advanced methods where necessary to gain more accurate answers under conditions of uncertainty.

## Questions to Consider

* *How do you typically approach decision-making in your professional role, and in what ways could you incorporate the principles of decision intelligence to enhance your decision-making process?*
* *Have you observed instances where excessive complexity in your organization resulted from poor decision-making? How can IT architects address this, and what role can they play in simplifying decision-making processes?*
* *Reflect on a recent significant decision you made. Were you aware of the resources you were committing and the opportunities you were preceding? How could you have evaluated these factors more effectively?*
* *Think of a situation where the outcome of a decision didn't align with your expectations. How did you judge the quality of the decision-making process in hindsight, and did you consider the role of luck or randomness?*
* *Consider a recent decision you faced. What would have been the value of perfect information in that scenario? How does this concept help you balance the effort and resources you allocate to different decisions?*
* *How do you set and align your goals, and what challenges have you faced in this process? Are there instances where misalignment has led to ineffective decision-making?*
* *What factors have you found to increase the complexity of decision-making in your experience? How do you manage these complexities effectively?*
* *Can you identify any habits or emotional factors contributing to your indecisiveness? What strategies can you employ to overcome these challenges?*
* *How do you use data in your decision-making process? Are there instances where data has misled your decisions, and how can you safeguard against this in the future?*
