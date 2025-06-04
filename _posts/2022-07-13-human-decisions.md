---
layout: post
section: "On Human Complexity"
title: "The Human Side of Decision-Making"
position: 7013
podcast: human-decisions.mp3
spotify: https://open.spotify.com/episode/0wPe0d2uCDGOwjLdFvfLpG?si=k9P84u3oRtC5tA0WjcvPtQ
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
icon: human-side.png
permalink: human-decisions
timetoread: 11 min
excerpt: "Decision-making is a human activity subject to human biases and limitations. Fundamental biases influencing decision-making include outcome, hindsight, and confirmation biases."

---

<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover"
src="assets/images/istock/iStock-1286627625.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/metamorworks">metamorworks</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
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

> **IN THIS SECTION, YOU WILL:**  Learn the basic human factors influencing decision-making.
>
> **KEY POINTS:**
> * Decision-making is a human activity subject to human biases and limitations. 
> * Fundamental biases influencing decision-making include outcome, hindsight, and confirmation biases.
> * Human intuition plays a vital role in decision-making.

<br>
[Cassie Kozyrkov](https://en.wikipedia.org/wiki/Cassie_Kozyrkov), in her [LinkedIn posts](https://www.linkedin.com/pulse/introduction-decision-intelligence-cassie-kozyrkov/) and [online courses](https://www.linkedin.com/learning/decision-intelligence/), emphasizes that **decision-making** is a uniquely human endeavor—a complex blend of brilliance, bias, and occasional mistakes. This insight is particularly important for IT architects to remember. Regardless of how structured our frameworks are or how robust our data may be, **every architectural decision is ultimately shaped by human judgment**, which carries both strengths and imperfections.

We make decisions every day, from choosing what to have for breakfast to selecting the best technology stack for a new project. Despite our best intentions, even the most thoughtful individuals and experienced teams are susceptible to **biases and human limitations** that can unintentionally lead to poor decisions. Biases such as **outcome bias**, **hindsight bias**, and **confirmation bias** can mislead us into thinking we are making rational choices when we are not. Additionally, factors like **indecisiveness**, **emotional influences**, and **intuition**—both helpful and harmful—play significant roles in our decision-making processes. In the fast-paced world of IT, it is crucial to understand these biases and limitations, how they manifest, and how we can manage them. This chapter examines common biases and human limitations in IT decision-making, offers real-world scenarios, and provides practical advice to enhance decision-making effectiveness.

Architects must navigate not only technical trade-offs but also the **psychological quirks**, **cognitive biases**, and **organizational politics** that influence decision-making. Designing effective systems means considering human nature in both the design process and the end user experience.


<br>
## Understanding Human Biases and Limitations

Fundamental biases influencing decision-making include outcome, hindsight, and confirmation biases.

### Outcome Bias

The big trap in decision-making is falling into the **outcome bias** pit, where you **obsess over the results** rather than focusing on how you decided in the first place. Results matter, but if you trip over an unlucky result and think you picked the wrong option, you're learning to fail with flair. This faulty thinking could make you make even wackier choices in the future.

![](assets/images/istock/iStock-1400056155.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/meshcube">mesh cube</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

A decision and its outcome are like two different TV show episodes. The outcome is just what happens after the decision's cliffhanger. You can make a totally solid decision and still end up with a plot twist no one saw coming. Outcomes are a cocktail mixed with decision-making, randomness, and a **splash of luck**. And luck, as we all know, is that elusive ingredient we can't control, often playing a starring role in our most complex dramas.

Suppose we only focus on the outcome, neglecting the rich backstory and the information available at the time of the decision. In that case, we're akin to a film critic who only watches the ending. This can lead to **misjudging people's abilities**, rewarding or penalizing them based on a volatile mix of luck and skill. Therefore, it's crucial to discern whether someone's success stems from their astute decision-making or sheer chance. When evaluating decisions, it's essential not to be overly dazzled by the outcome.

In IT, outcome bias can come in many different forms, typically leading to the reinforcement of poor practices and processes based on the perceived successful outcome of projects.

**Example 1: Ignoring Best Practices Due to Success**

* Due to time constraints, a software team decided to release a critical update without performing adequate regression testing. The update has been released, and fortunately, no major issues have been found by the users.
* Because the update did not cause any immediate problems, the team and management might conclude that regression testing is not always necessary, reinforcing a risky behavior based on a lucky outcome rather than sound engineering practices.

**Example 2: Overlooking Security Flaws**

* A development team delivers a new web application feature without conducting a thorough security review. The feature has gained popularity and has not encountered any immediate security incidents.
* The absence of immediate security breaches leads the team to believe that their approach to security is adequate, even though the feature might have significant vulnerabilities that have not yet been exploited. This can result in a continued lax attitude towards security best practices.

**Example 3: Rewarding Speed Over Quality**
* A software project is completed and delivered significantly ahead of schedule but with known technical debt and suboptimal code quality. The project is well-received by the client due to its timely delivery.
* Management praises the team for their speed, ignoring the long-term consequences of the technical debt. This could lead to future projects prioritizing speed over quality, increasing the risk of long-term maintenance issues and potential project failures.

**Example 4: Skipping Code Reviews**
* A development team decides to skip code reviews to save time, and the software is delivered without any major bugs or issues.
* The team concludes that code reviews are not essential, leading to the institutionalization of skipping this critical quality control step. Future projects might suffer from hidden bugs and poor code quality, which could have been caught during code reviews.

**Example 5: Misinterpreting Customer Feedback**
* A feature is implemented based on limited customer feedback and is launched successfully. The positive reception leads the team to assume their approach to gathering and acting on feedback is effective.
* The team might conclude that extensive user research is unnecessary, believing that limited feedback is sufficient to guide development. This could result in future features missing critical insights from a broader user base, potentially leading to less successful outcomes.

It's essential for teams to critically evaluate their methodologies and ensure that success is attributed to sound practices rather than favorable outcomes alone.

### Hindsight Bias

**Looking back** at decisions can be as tricky as explaining a magic trick once you know the secret, thanks to **hindsight bias**. Everything seems obvious in hindsight, even though it was as clear as mud at the time. The real way to judge a decision is to dig into the info and context available when it was made—like a detective piecing together clues.


![](assets/images/istock/iStock-1394993248.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/designer491">designer491</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

Think about what the decision-maker considered, how they played detective gathering info, and where they got their facts. Also, check if they collected enough intel for the decision's importance or were winging it.

If you don't **write down this process,** it's like trying to remember a dream—you'll miss many details and be left only with a vague feeling. This makes it tough to judge the quality of your decisions or anyone else's, stalling your growth as a decision-making wizard. Write down your decision-making process. This helps you determine if luck was messing with you or if your skills were on point. 

Hindsight bias in IT can lead to an **oversimplified understanding** of past events and decisions, creating an **illusion of predictability.** It is crucial to recognize the context and constraints under which decisions were made to learn accurately from past experiences and improve future practices.


**Example 1: Technology Stack Decision**
* A particular technology stack is chosen for a project, but it later turns out to be ill-suited, causing significant rework.
* After the problems become apparent, developers and stakeholders might claim that it was clear from the beginning that this technology stack was not a good choice. They might forget that at the time of selection, the decision was made based on the best available information, the perceived advantages of the stack, and the extensive procurement process.

**Example 2: Bug Discovery**
* A critical bug is discovered in the production environment that causes significant downtime.
* After the bug is found, developers and stakeholders assert that the bug was easy to spot and should have been caught during the testing phase. This perspective disregards the complexity and number of potential issues that testers were dealing with and that the bug was not apparent among the other potential problems at the time.

**Example 3: Performance Issues**
* A software system experiences performance degradation under high load conditions that were not tested.
* After the performance issues arise, team members and stakeholders might say that it was clear the system would not handle high load and that stress testing should have been prioritized. This perspective ignores that other pressing issues and constraints influenced the original decision-making process.

**Example 4: Post-Mortem Analysis**
* A software project fails due to unexpected integration issues with third-party services.
* During the post-mortem analysis, team members and management claimed that the integration issues were obvious and should have been anticipated. They overlooked that the integration appeared straightforward at the time of decision-making, and the issues were not foreseeable with the information available.

**Example 5: Feature Failure**
* A new feature is released but fails to gain user adoption, which is considered a failure.
* Team members and management might claim that they always had doubts about the feature's success and that it was destined to fail. This can lead to the erroneous belief that the failure was evident from the start, even if the decision to proceed with the feature was based on thorough research and positive initial feedback.

**Example 6: Security Breach**
* A security vulnerability is exploited in a production system, leading to a data breach.
* Post-breach, it is often stated that the vulnerability was obvious and should have been addressed sooner. This belief neglects the context in which security measures were evaluated and the myriad of potential vulnerabilities that needed to be managed simultaneously.

**Example 7: Project Timeline Overruns**
* A software project exceeds its deadline due to unforeseen technical challenges.
* Once the challenges are known, team members might argue that the delays were predictable and that the original timeline was overly optimistic. This view ignores the uncertainty and the incomplete information available when the original timeline was set.



By acknowledging the role of hindsight bias, teams can foster a more realistic and fair evaluation of past projects and decisions.

### Confirmation Bias

**Confirmation bias** is like having a pair of magical glasses that only let you see what you already believe. When you stumble upon a new fact, your brain gives it a makeover to fit your beliefs, even before your morning coffee.


![](assets/images/istock/iStock-1307396842.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/designer491">designer491</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>


Awareness of this sneaky bias is essential because your brain loves playing tricks on you. It makes you think you're being objective while sneakily **reinforcing your pre-existing ideas.** This subconscious nudge can twist your understanding and decision-making without you even noticing.

Businesses are jumping on the data science bandwagon, hiring data scientists to make supposedly unbiased, data-driven decisions. But guess what? These decisions are often not as data-driven as they claim. For a decision to follow the data, it should be the data leading the dance, not your preconceived notions or biases—a simple idea harder to pull off than a flawless magic trick.

Confirmation bias is like your brain's way of playing a one-sided game of telephone with data. Even the most complex math won't save you if you still interpret results through your belief-tinted glasses. Extensive data analysis can be as helpful as a screen door on a submarine if it's warped by confirmation bias. The real challenge is resisting the urge to twist the story after seeing the data. So, watch for your brain's tricks and let the data speak for itself—or risk your analysis being as misleading as a carnival funhouse mirror.

Beating confirmation bias is like prepping for a magic show: you need a plan before the curtain goes up. **Set clear objectives** before you peek at the data. Consider what the data should mean to you beforehand so you don't get dazzled by surprising plot twists. This way, you can make genuinely data-driven decisions instead of falling into the trap of your brain's sneaky biases.

Confirmation bias in IT can lead to suboptimal decisions and hinder the effectiveness of problem-solving and innovation in IT:

**Example 1: Tool Selection**
* A development team prefers using a specific development framework because of their past experiences with it.
* When choosing a framework for a new project, team members only seek out positive reviews and success stories about their preferred framework, ignoring or downplaying any negative feedback or alternative frameworks that might be better suited for the project's requirements.

**Example 2: Technology Adoption**
* A company decides to adopt a new technology stack based on industry trends and some initial positive experiences.
* The team focuses on success stories and favorable benchmarks supporting the decision while disregarding case studies or reports highlighting challenges and failures associated with the new technology. This can lead to underestimating the risks and difficulties of the adoption process.

**Example 3: Debugging**
* A developer believes that a particular module is the source of a bug.
* The developer focuses exclusively on the suspected module, interpreting any evidence to support this belief, and may overlook or disregard indications that the bug originates from another part of the code. This can lead to extended debugging time and potentially missing the actual source of the issue.

**Example 4: Performance Testing**
* A team is confident that their application will perform well under high load due to recent optimizations.
* When conducting performance tests, they may primarily focus on scenarios where they expect the application to perform well, ignoring or not thoroughly testing edge cases or scenarios that might reveal performance bottlenecks. As a result, they might miss critical issues that only appear under certain conditions.

**Example 5: Estimating Project Timelines**
* A project manager strongly believes the team can meet an aggressive deadline.
* The project manager seeks out and emphasizes information and past examples where similar deadlines were met while ignoring or discounting instances where similar projects encountered delays. This can lead to unrealistic project timelines and potential burnout.

**Example 6: Code Reviews**
* A senior developer has a high opinion of a specific junior developer's skills.
* During code reviews, the senior developer may be more inclined to approve the junior developer's code with minimal scrutiny, interpreting any ambiguities or minor issues as acceptable or easily fixable, while being more critical of other developers' code.

**Example 7: User Feedback**
* The team has a preconceived notion that users will love a new feature they developed.
* When gathering user feedback, they may give more weight to positive comments and downplay or dismiss negative feedback. They might also ask leading questions likely to elicit positive responses, thus reinforcing their belief that the feature is well-received.

To mitigate the impact of confirmation bias, teams should actively seek out and consider disconfirming evidence, adopt a critical thinking approach, and encourage diverse perspectives. By being aware of this bias, teams can make more balanced and informed decisions, ultimately leading to better software outcomes.


### Other Human Limitations Influencing Decision-Making

In a classic behavioral economics study, researchers showed that **how you say something** can be more magical than a rabbit out of a hat. They gave decision-makers the same facts but with some wordplay—different wording. Despite the identical information, decisions did a Houdini act and varied wildly. A tweak in phrasing or tossing in unrelated details can make people's choices wobble like a tightrope walker in a windstorm. Our brains are suckers for cognitive biases and illusions, even when the cold, hard facts are staring us in the face.

![](assets/images/istock/iStock-1333976612.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/AaronAmat">AaronAmat</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

This means that dealing with data isn't as objective as we like to think. How we mentally wrestle with data matters a lot. We may aim to use data to become more objective, but if we're not careful, it can pump up our pre-existing beliefs like a bouncy castle. Instead of uncovering new insights, we end up with our same old convictions, sabotaging our quest for objectivity and learning.

And let's be honest—your decision-making skills aren't precisely Olympic-level when you're **sleep-deprived, hungry, stressed**, or feeling the heat. These biological and emotional states can affect your ability to make top-notch decisions. Believing that sheer willpower or a PhD in decision-making will always lead to the best outcomes is like thinking you can win a marathon in flip-flops.

A jaw-dropping example is in the legal system: studies show that judges can hand out different sentences before and after lunch. Even these wise, experienced folks, whose decisions shape lives, can be swayed by something as simple as a rumbling stomach. This should be a big, flashing neon sign warning us about the limits and quirks of our decision-making processes. So next time you're about to make a big decision, grab a snack and a nap first!





<br>
## Understanding Power and Limitations of Human Intuition in Decision-Making

Human intuition plays a vital role in decision-making. Robert Glass provided one of the best definitions of intuitions, describing it as a function of our mind that allows it to access **a rich fund of historically gleaned information** we are not necessarily aware we possess by **a method we do not understand** ([Glass, 2006; page 125)](https://www.amazon.com/Software-Creativity-2-0-Robert-Glass/dp/0977213315). But oOur unawareness of such knowledge does not mean we cannot use it.

![](assets/images/istock/iStock-1193842896.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/metamorworks">metamorworks</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>


One of the main advantages of intuition in decision-making is that accessing it is a rapid process, making intuitive decisions straightforward. Intuition is particularly useful for low-value decisions with low stakes, and a quick resolution is preferable. As we'll explore in future discussions on prioritization and decisiveness, seeking perfection in every decision is impractical due to limited time and energy. Therefore, it's essential to choose where to focus your efforts.

Intuition is especially appropriate under certain conditions:
* **Time Pressure**: When time is limited and a detailed analysis isn't feasible, intuition can guide you when otherwise you would be stuck.
* **Expertise**: If you have experience in a particular area, relying on intuition makes sense, as you've likely faced similar decisions before. In contrast, in unfamiliar contexts, intuition may not be reliable.
* **Unstructured Decisions**: Intuition can be valuable for decisions that lack a clear framework, like judging the quality of art. Expertise in the relevant field enhances the effectiveness of intuitive judgments.

Conversely, you should avoid relying on intuition too much when more effort is warranted, including those with ample time, high importance, lack of expertise, and the possibility to use a structured decision-making process.

Intuition in IT can be a **powerful tool** when informed by experience and used in conjunction with data and thorough analysis. It can guide efficient problem-solving and quick decision-making in familiar contexts. However, overreliance on intuition without considering empirical evidence and diverse viewpoints can lead to **significant mistakes,** especially in unfamiliar or complex situations. 

### Good Example: Intuitive Debugging

**Scenario:** A seasoned software engineer is working on a complex system that suddenly starts behaving unexpectedly. The logs provide little information, and initial debugging efforts do not yield apparent clues.

**Good Use of Intuition**

1. **Pattern Recognition**: Drawing on years of experience, the engineer intuitively suspects that the issue might be related to a recent configuration change rather than a code issue.
2. **Focused Investigation**: Based on this intuition, the engineer quickly narrows down the potential causes, focusing on recent changes in the configuration files.
3. **Quick Resolution**: This intuition-driven approach reveals a misconfiguration in minutes, saving the team hours of potentially fruitless debugging.

**Outcome**: The engineer's intuition, honed by experience, helps quickly identify and resolve the issue, demonstrating how intuition can efficiently guide problem-solving in complex scenarios and under time pressure.

### Bad Example: Intuitive Decision on Technology Stack

**Scenario:** A new project is starting, and the team needs to decide on the technology stack. The team lead has a strong intuitive preference for a specific new programming language and framework they have used.

**Bad Use of Intuition**

1. **Ignoring Data**: The team lead dismisses team members' concerns and data about the scalability and community support of the chosen technology. There was ample time to do proper analysis.
2. **Overconfidence**: Relying solely on personal intuition and past experience, the team lead pushes forward with the technology despite its known limitations for the project's specific needs.
3. **Future Problems**: As the project progresses, the team encounters significant issues related to performance and maintainability. These issues could have been mitigated or avoided by choosing a more appropriate technology stack based on objective criteria and thorough evaluation.

**Outcome**: The team lead's overreliance on intuition leads to a poor technology choice, resulting in increased technical debt, reduced productivity, and ultimately a less successful project. This example highlights how intuition can lead to suboptimal decisions when used without adequate consideration of data and other perspectives.

Balancing intuition with data-driven decision-making and collaborative input often leads to the best outcomes in software engineering.


<br>
## Understanding Human Indecisiveness

We frequently fall into the indecisiveness trap. Why? Well, people can be indecisive for all sorts of amusing reasons.


### Delaying Decisions

Many folks don't realize that **dodging a decision is still a decision**. It's like standing in front of an ice cream shop, unable to choose a flavor until the shop closes, and boom—you've "decided" to go home without ice cream. Delaying, postponing, or deprioritizing the decision-making process is an implicit choice.

![](assets/images/istock/iStock-2143629746.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/dragonclaws">Dragon Claws</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

Dodging decisions often lead to significant consequences, even if they aren't immediately obvious. Here are a few examples:

**Microservices vs. Monolithic Architecture**
   - **Scenario**: A team is debating whether to move to a microservices architecture or continue with their existing monolithic system. Rather than making a decision, they keep delaying it, hoping that some perfect clarity will emerge.
   - **Implicit Decision**: The team effectively "decides" to stay with their monolithic system by not choosing. Over time, this makes it harder to scale, introduces more technical debt, and slows deployment and innovation. They've made a choice—whether they realize it or not.

**Code Refactoring vs. Feature Development**
   - **Scenario**: Engineers know that a particular part of the codebase needs refactoring, but with each sprint, the refactoring task gets postponed in favor of new features.
   - **Implicit Decision**: By deprioritizing refactoring, the team implicitly decides to live with a growing pile of technical debt, leading to more bugs, slower performance, and increasingly difficult maintenance.

**Cloud Migration**
   - **Scenario**: A company wants to move its infrastructure to the cloud but keeps postponing the decision, citing the need for further research or budgetary constraints.
   - **Implicit Decision**: By delaying the migration, they implicitly decide to continue using outdated on-premise systems, which may be less efficient and more expensive in the long run. They also miss out on the agility and scalability benefits of cloud infrastructure.

**Testing Strategy**
   - **Scenario**: A team debates about the scope of automated vs. manual testing. However, because they can't decide, they continue relying on an inconsistent mix of both without a comprehensive strategy.
   - **Implicit Decision**: The lack of a solid testing strategy leads to reduced code quality, longer release cycles, and more defects slipping into production. The choice to not formalize testing becomes a costly implicit decision.

**Single Sign-On (SSO) Integration**
   - **Scenario**: A company debates whether to implement SSO for its internal systems to streamline user authentication. However, security and engineering teams defer the decision to focus on more "urgent" projects.
   - **Implicit Decision**: By not implementing SSO, the company has multiple login systems, causing frustration for users and increased security risks due to inconsistent authentication methods.

In all of these cases, failing to make a decision is itself a decision—and often a costly one. The key takeaway here is that avoiding decisions in technical scenarios can lead to significant consequences, even if they aren't immediately obvious.

### Overwhelmed by Numerous Decisions

Then there's the classic "**too many choices**" dilemma. When faced with an array of decisions, especially those of lower priority, our brains feel like an overstuffed suitcase. Our cognitive capacity is limited—we can't focus intensely on everything simultaneously. Suppose we spend too much mental energy deciding what color to paint the break room. In that case, we might leave no brainpower for the big decisions, like how to keep the servers from catching fire.

![](assets/images/istock/iStock-1304877755.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/cyano66">cyano66</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

The "too many choices" dilemma is a common problem where teams or decision-makers become overwhelmed by many low-priority decisions, often detracting from critical, high-impact choices. Here are a few examples:

**Library and Dependency Updates**
   - **Scenario**: Developers ask the IT architect to review and approve every minor version upgrade for third-party libraries, even those that involve minimal risk or functionality changes.
   - **Problem**: By focusing the architect's attention on these low-impact updates, critical decisions (like system scalability, security measures, or architectural design) may get delayed. It's like asking the architect to approve every paint stroke while the house's foundation needs reinforcement.

**Code Formatting Standards**
   - **Scenario**: The engineering team spends excessive time debating the best code formatting or style guidelines, like whether to use 2 or 4 spaces for indentation.
   - **Problem**: While consistency in code formatting is important, over-allocating time to decisions like these diverts attention from more significant decisions, such as improving the application's architecture or fixing major bugs. It's like worrying about the snacks in the break room while production servers are down.

**Platform or Tool Selection**
   - **Scenario**: The team chooses between different code editor plugins, build tools and minor productivity tools. Each option is reviewed in detail, with countless meetings to compare feature lists.
   - **Problem**: Overanalyzing small tooling decisions causes unnecessary delays and burns mental energy that is better spent on high-impact decisions, such as selecting a cloud provider or deciding the proper microservices orchestration approach.

**Server Naming Conventions**
   - **Scenario**: The IT department holds extensive discussions on naming the new servers or virtual machines in the cloud environment—should they use city names, numbers, or specific animal species?
   - **Problem**: This seemingly minor debate consumes valuable time and energy, while more critical infrastructure decisions, like disaster recovery planning or server load balancing, get delayed or ignored.

**Approving Minor Configuration Changes**
   - **Scenario**: IT architects are asked to approve every minor configuration tweak, such as adjusting the timeout for a service or tweaking memory limits for non-critical applications.
   - **Problem**: The architects drown in trivial decisions, leaving them little bandwidth to focus on higher-priority issues, like designing robust, scalable system architectures or improving application security.

In these examples, the team's limited cognitive capacity is consumed by trivial choices, leaving insufficient mental energy for critical decisions that genuinely impact system performance, security, or scalability. This issue highlights the importance of delegating or automating low-priority decisions and reserving strategic brainpower for what truly matters.

### Emotions and Grief

Indecisiveness also loves to rear its head when emotions are involved, especially when all options are as appealing as a soggy sandwich. When faced with **undesirable choices**, the practical move is to pick the **least bad option.** After thoroughly evaluating your choices and identifying the least awful one, it's time to bite the bullet and make the call.

People often get tangled in a web of **grief or frustration** when stuck with lousy options, hoping for a miracle solution that'll never come. It's like searching for unicorns in a petting zoo. Once it's clear that no better options will appear, it takes courage to move forward with the least terrible choice.


![](assets/images/istock/iStock-2031282851.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/VioletaStoimenova">VioletaStoimenova</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

Teams often face situations where every option feels undesirable, and indecisiveness can creep in due to emotional frustration or the hope for a perfect solution. Here are some examples:

**Legacy System Migration**
   - **Scenario**: A company runs critical applications on a legacy system that is slow, costly to maintain, and increasingly prone to failure. The options are to either:
     1. Perform a risky, costly, and time-consuming migration to a modern system.
     2. Continue investing in patching the legacy system, with the risk of a major outage.
   - **Emotional Factor**: No one wants to be responsible for the potential failures of a complex migration, but continuing with the legacy system feels like kicking the can down the road.
   - **Least Bad Option**: After evaluating the long-term costs and risks, the team decides to proceed with the migration, accepting the immediate pain of potential downtime and cost over the unsustainable alternative of maintaining the outdated system. It's not a great choice, but it's the least bad one, so they bite the bullet.

**Technical Debt Management**
   - **Scenario**: A project has accumulated significant technical debt. The options are:
     1. Allocate several sprints to pay the debt, delaying new feature development.
     2. Continue adding features on top of a shaky codebase, which will inevitably slow development and increase the risk of defects.
   - **Emotional Factor**: Teams often feel frustrated by technical debt, wishing it would somehow resolve itself. However, neither option is appealing—both involve trade-offs between immediate feature delivery and long-term stability.
   - **Least Bad Option**: Recognizing that continued development on a brittle foundation will lead to far greater problems, the team accepts the frustration of delaying features and tackles the technical debt, understanding it's the least bad way to ensure future scalability and maintainability.

**Vendor Lock-In**
   - **Scenario**: A company is heavily invested in a particular cloud provider but realizes the cost is much higher than anticipated. The choices are:
     1. Stay with the current provider and absorb the higher costs.
     2. Undertake a complex and costly migration to a new provider, risking downtime and re-engineering efforts.
   - **Emotional Factor**: Switching vendors feels overwhelming and risky, while staying locked into an expensive provider feels frustrating. Hoping for a "magic" solution (e.g., the provider reducing costs) isn't realistic.
   - **Least Bad Option**: After weighing the costs and risks, the company decides to stay with the current vendor, accepting the cost over the uncertainty of migration. It's not ideal, but it's the least bad choice given the alternatives.

**Monolithic vs. Microservices Split**
   - **Scenario**: A monolithic application has grown too large, and the team knows it needs to break it into microservices. The options are:
     1. Undertake a complex, high-risk rewrite of the monolithic application into microservices.
     2. Continue maintaining the monolith, accepting slower release cycles and scaling limitations.
   - **Emotional Factor**: Rewriting a system always feels daunting, and no one wants to own the risk of disrupting the system during the transition. However, maintaining the monolith comes with its own set of frustrations, especially as it grows.
   - **Least Bad Option**: Recognizing that continuing with the monolith will lead to stagnation, the team opts for a phased approach to break the system into microservices. It's a difficult and risky path, but the alternative of doing nothing is worse.

**Security Fixes vs. Feature Development**
   - **Scenario**: A critical vulnerability is discovered in an application, but fixing it will require a full sprint of engineering time, delaying a high-priority feature release.
     1. Delay the feature and fix the vulnerability immediately, which will frustrate stakeholders and users awaiting the feature.
     2. Continue with the feature release and address the security issue later, increasing the risk of a breach.
   - **Emotional Factor**: The team is pressured by stakeholders eager for new features, but the security risk is causing anxiety. Neither option is appealing, as both involve security and feature delivery trade-offs.
   - **Least Bad Option**: The team addresses the security issue first, accepting the frustration of delaying the feature because the consequences of a breach are far worse. It's not a great situation but the least bad decision.

In each case, the choices are less than ideal, and emotions like frustration, anxiety, or fear of failure can cloud judgment. However, teams can move forward with clarity and purpose by acknowledging that no perfect option exists and focusing on the least detrimental path.

<br>
## Understanding Group Dynamics in Decision-Making

Effective decision-making often involves recognizing that **you might not be the sole decision-maker**. In organizations, it's crucial to identify the actual decision-makers and understand how decision responsibility is distributed among them. Mastering this skill is essential for navigating organizational decision-making processes. It's important to question who really has the final say in decisions. In many cases, decision-making is more complex than it appears.

![](assets/images/istock/iStock-1198639725.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/Milkos">Prostock-Studio</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

Group decision-making offers significant advantages. While you might believe you have the best solutions, incorporating diverse perspectives can help cover your blind spots. Multiple decision-makers can counterbalance an individual's extreme tendencies and compensate for human limitations like fatigue.

### Characteristics of Group-Decision Making

While group decision-making might sometimes constrain individual creativity, it also **provides safeguards against poor decisions** and **aligns individual motives with the organization's goals**. Having several independent decision-makers can align individual incentives with the organization's needs, addressing this problem.

However, group decision-making isn't perfect. It **increases complexity** as it **requires higher decision-making skills** from each member. True **collaboration in decision-making** is more challenging than individual decision-making. It also tends to **slow down the decision process**.

Moreover, the benefits of group decision-making, like balancing individual biases, **rely on the independence of the decision-makers**. If everyone is in the same room, independence can be compromised by factors like **charisma or status**, potentially allowing the loudest voice to dominate rather than the wisest.

Group settings can also **devolve into social exercises**, where **personal ego overshadows open-mindedness** to new information. Awareness of these pitfalls allows you to create rules that foster independent perspectives.

The **role of the note-taker** in group settings is also influential, as is the phenomenon of **responsibility diffusion**, where **unclear responsibilities** lead to reduced individual contribution.

In summary, **the more people involved in a decision, the higher the skill level required** to maximize the benefits and minimize the downsides of group decision-making. It's vital to structure the process to maintain independence, possibly by limiting decision-makers and increasing advisors. This approach distinguishes between making a decision and advocating for the execution of an already-made decision.

### Examples 

Group decision-making dynamics in IT can take various forms, including consensus, hierarchical, voting, and conflict resolution approaches. Group decision-making dynamics in IT can vary widely depending on the context, team structure, and decision at hand. Here are some examples illustrating different aspects of group decision-making dynamics in IT:

#### Example 1: Consensus Decision-Making for Technology Adoption

**Scenario:** An IT team must decide which cloud platform to use for a new project. The options are AWS, Azure, and Google Cloud.

**Dynamics:**
1. **Information Sharing**: Team members share their experiences and knowledge about each platform. This includes presenting pros and cons, costs, and performance benchmarks.
2. **Brainstorming**: An open discussion is held where everyone is encouraged to voice their opinions and suggest potential solutions.
3. **Evaluation**: Each option is evaluated based on predefined criteria such as scalability, cost, ease of integration, and existing team expertise.
4. **Consensus Building**: The team works towards a consensus by discussing the trade-offs and attempting to agree on the platform that best meets the project's needs.
5. **Decision**: After a thorough discussion, the team decides to use AWS due to its robust ecosystem and familiarity with it.

**Influence**: Consensus decision-making ensures that all team members feel heard and can contribute to the decision, leading to higher buy-in and commitment to the chosen platform.

#### Example 2: Hierarchical Decision-Making for Security Policy

**Scenario:** A decision must be made about implementing a new security policy to comply with regulatory requirements.

**Dynamics:**
1. **Top-Down Directive**: Senior management decides on the necessity of the new security policy based on compliance needs and risk assessments.
2. **Expert Input**: Security experts within the organization are consulted to provide detailed recommendations on implementing measures.
3. **Implementation Plan**: The IT manager creates an implementation plan based on the expert recommendations and communicates it to the team.
4. **Team Execution**: The IT team is tasked with executing the plan, following the directives provided by management.

**Influence**: Hierarchical decision-making can be efficient, especially when quick, decisive action is required and the decision involves specialized knowledge. However, it may result in less buy-in from the team if they are not involved in the decision-making process.

#### Example 3: Voting for Feature Prioritization

**Scenario:** A software development team needs to prioritize features for the next release of their product.

**Dynamics:**
1. **Feature List**: A list of potential features is compiled based on customer feedback, market research, and internal brainstorming sessions.
2. **Discussion**: The team discusses the importance and impact of each feature, considering factors such as user value, development effort, and strategic alignment.
3. **Voting**: Each team member votes on their top features, often using a point system where they can allocate a certain number of points across the features.
4. **Ranking**: Features are ranked based on the total points received, and the top-ranked features are selected for the next release.

**Influence**: Voting democratizes the decision-making process and ensures that the prioritization reflects the team's collective opinion. This approach can enhance team morale and provide diverse perspectives are considered.

#### Example 4: Conflict Resolution in Architecture Decisions

**Scenario:** The development team is divided over whether to build a new application using a microservices or monolithic architecture.

**Dynamics**

1. **Initial Positions**: Team members present their initial positions, with some advocating for microservices due to their scalability and flexibility and others for a monolithic architecture due to its simplicity and ease of deployment.
2. **Evidence Gathering**: Both sides present evidence, including case studies, technical articles, and expert opinions, to support their arguments.
3. **Facilitated Discussion**: A neutral facilitator (such as an architect) leads a structured discussion to explore the pros and cons of each approach.
4. **Compromise and Integration**: The team seeks a compromise or an integrated solution, such as starting with a monolithic architecture and planning to evolve to microservices as the application grows.
5. **Final Decision**: After thoroughly discussing and considering all viewpoints, the team decides to balance immediate needs with future scalability.

**Influence**: Structured conflict resolution ensures that all voices are heard and helps the team make a well-considered decision. Combining the strengths of different viewpoints can enhance mutual understanding and lead to better decisions.

Each method has its advantages and can be suitable for different decisions. Understanding these group dynamics can help teams navigate complex choices more effectively, leading to better outcomes and stronger team cohesion. 

<br>
## Final Thoughts

Navigating the complex landscape of human biases and decision-making limitations is an ongoing journey rather than a one-time task. Outcome bias can lead us to mistakenly **attribute success to skill instead of luck**, while hindsight bias may convince us that past decisions were obviously flawed. Additionally, confirmation bias can **blind us to important evidence**. Indecision and excessive reliance on intuition can stall our progress or lead us down the wrong path.

To reduce the negative impact of these biases, it is helpful to **actively document our decision-making processes**, encourage open discussions, and welcome diverse perspectives. Group decision-making can help mitigate individual biases, but it requires **intentional structure** to be effective. By adopting a balanced approach—one that values intuition informed by experience while rigorously checking against objective data and alternative viewpoints—we can empower teams to make consistently better decisions. Ultimately, this appraoch leads to more successful outcomes and sustainable growth.

<br>
## Questions to Consider

* *How do your personal biases, such as outcome, hindsight, and confirmation bias, influence your decision-making process? Can you identify a recent decision where these biases might have played a role?*
* *Reflect on a situation where the outcome was bad, but the quality of your decision-making process was solid. How did you respond to this outcome, and what lessons did you learn?*
* *In what ways do you think hindsight bias has affected your ability to evaluate past decisions accurately? Can you think of a decision that seemed obvious in retrospect but was unclear at the time?*
* *Consider a decision you made recently. Did you document the decision-making process? If not, how could documenting this process help you in evaluating your decisions more effectively in the future?*
* *How does confirmation bias impact your interpretation of new information? Can you recall an instance where you ignored or misinterpreted data to fit your pre-existing beliefs?*
* *Think about a decision where changing your perspective or how information was presented (e.g., through different wording) might have led you to a different conclusion. How does this realization affect your approach to decision-making?*
* *Can you identify any habits or emotional factors contributing to your indecisiveness? What strategies can you employ
  to overcome these challenges?*
* *Reflect on a time when your physical or emotional state might have influenced a decision. What does this tell you about the importance of being aware of your condition when making decisions?*
* *Consider a decision where intuition played a significant role. Was the decision effective, and would you rely on intuition under similar circumstances in the future?*
* *How do you balance the benefits of group decision-making with its challenges, such as social dynamics and the diffusion of responsibility?*
