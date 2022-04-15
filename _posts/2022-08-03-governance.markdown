---
layout: post
title: "Governance"
startSection: "Governance (Steering)"
position: 4004
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: governance
icon: goals.png
timetoread: 15 min
excerpt: "Change culture by positioning architecture as a cross-organizational superglue, distribute decision-making, strengthening architectural muscle across the organization, from opinions-based to data-informed decision-making, a flexible technology governance model."

---
![](assets/images/640px-Instrument_Cluster,_Mercedes-Benz_S350_Bluetec_4Matic_(US)_-_Flickr_-_skinnylawyer.jpeg)

With our hybrid architecture operating model (HAOM) we wanted to achieve the following goals: 

1. Increase the Quality of Decision-Making with Data, 
2. Align Architecture Culture: Break Up the Ivory Towers, 
3. Embrace Architectural Diversity, Distribute Decision-Making,
4. Strengthen Architectural Muscle Across the Organization
5. Leverage Architectural Communities to Maximize Organizational Alignment & Learning
6. Promote a Hybrid Governance Model (Mandates + Taxes + Leading by Context)

![](assets/images/model-governance.jpg)

## Goal 6: Promote a Hybrid Governance Model (Mandates + Taxes + Leading by Context)

We wanted to create a governance model that acknowledges the complexity and diversity of our organization. By governing, we mean guiding technology choices in the organization in a particular direction aligned with the technology strategies. We tried to prevent a simplistic view of architecture as defining directives for the rest of the organization, in line with our "breaking up to monoliths" goal. Consequently, we aimed at promoting a technology governance model as a well-balanced hybrid of three different ways of governing:
* mandates and bans,
* taxes, and
* leading by context.

Governing with mandates and bans means defining what people should or should not do. In our context, such mandates and bans have a place to define broader strategic boundaries of choices that people can make. For instance, limiting the usage of public cloud providers to specific vendors or following strict security procedures should be explicitly defined and controlled. The role of architecture in this form of governing should be to participate in defining manates and bans with strategic stakeholders and to create clarity about mandates and bans and create transparency.

Governing with taxes is a form of guiding in which people are not forbidden to make some decisions but need to pay some form of taxes on used resources. For instance, costs of the public cloud usage could be cross-charged across the organization, providing a helpful feedback loop to optimize our systems and avoid unnecessary resource consumption, avoiding "tragedy of commons" which frequently happens when there are not limits or significant costs of increasing shared resource consumption (e.g., public cloud budget). The role of architecture in this form of governance should be to create efficient feedback loops on key metrics related to taxes.

Leading the context is a form of governing in which we do not forbid people to make some choices, nor do they need to pay taxes. Instead, we wanted to create a shared context that can facilitate people making informed decisions. Such contexts should include sharing of lessons learned by others, both good and bad, and places to get feedback on ideas and plans. The role of the architecture in this form of governing should be to create mechanisms for sharing experiences and obtaining feedback on plans and decisions. It should also include mechanisms to capture artifacts that can help people to make informed decisions, such as architecture decision resources (ADRs), principles, golden paths, or best practices.


<br>
## Goal 1: Increase the Quality of Decision-Making with Data
> *"If we have data, let's look at data. If all we have are opinions, let's go with mine."* -— Jim Barksdale

There are great benefits of making our decision process as much as possible data-driven. I see it as one of the most critical tasks for any architect to maintain high-quality data on relevant technology developments, both internal and external, providing fuel for data-driven decision-making.

One of the problems we face is that we have lots of data on technology, but they are not well-connected, and manual data input and gathering are still frequent. For that reason, we need to work on developing automated tools that facilitate insights into technology and business.

In line with becoming more data-driven, we need to create shared frameworks to move from opinion-based decisions to data-driven economic risk modeling. Such frameworks should achieve the following:
* dismantle the buzzwords, present the problem in clear terms, understandable to a broader audience
* identify the real drivers behind buzzwords based on internal and external research
* bring internal data and external trends
* translate drivers into an economic risk model, and use the model to find the best spot for the given business context


## Goal 2: Align Architecture Culture: Break Up the Ivory Towers

While we wanted to embrace diversity, we found it crucial to align on a shared vision on architecture across all departments. In particular, we wanted to prevent positioning of architecture as an ivory tower exercize, disconnected from realities of complex organization.

More specifically, we wanted architecture to address one of the toughest problem that our organization is facing: a tension between technolgy, product, organization, and business functions (Figure #). Wlile technology, product, organization and business fucntions face their own challenges, big problem occurs when there is a tension among them. For example, we may organize teams according to a nice domain model, but if our technology is implemented as a monolith, our teams will collaborate in a different pattern then a domain splits would suggest. On the other hand, if our teams are well aligned with the technology implementation (e.g. clear ownership of microservices) but product architecture is different that microservice domain split, we may end up changing dozens of microservices when we need to introduce relatively simple product features. Similarly, if business objectives are not well aligned with product or technology ones (e.g. reducing costs, while adding new feature, and migrating to the public cloud) lots of tense interactions will happen. In an ivory tower model, architecture sites on side, shouting principles and abstract ideals that everyone ignores.     

![](assets/images/tension.png)

The main problem of these tensions is that they show things down due to miscommunications and misalignment, lead to bad decisions  due to lack of information, introduce unnecessary complexity, and lead to many missed opportunities.

With this problem in mind, we wanted architecture to overall in organization focuses on reducing the tension between technology, product, organization and business functions. 

Architecture should ensure that conversations happen between the technical, product, organizational, and business functions.

![](assets/images/tension-architecture.png)

As a guiding principle, we promoted a view that senior architects in our organization should develop as "superglue." We borrow this view from [Adam Bar-Niv and Amir Shenhav from Intel](https://resources.sei.cmu.edu/library/asset-view.cfm?assetID=454541). They pointed out that instead of the superhero, we need "super glue" architects - the fellows who hold architecture, technical details, business needs, and people together across a large organization or complex projects.

The superglue characteristics mean serving as the organizational connective tissue, linking the "business wheelhouse" and the "engine room." 

## Goal 3: Embrace Architectural Diversity, Distribute Decision-Making
> *“Rather than inject itself in every decision loop, architecture should design mechanisms for teams to make better decisions - they'll know better anyhow, and slowing them down carries a high cost.”*
> *“Autonomy does not mean you're all alone and don't align with anyone, don't get feedback from anyone and just do whatever you want.”

The first of our aims was to keep architectural decision-making distributed across the organization embedded in the local units. Local units traditionally have the best insights and most information relevant for making a decision. As Gregor Hohpe mentioned, the worst case of organizational decision-making happens when people with relevant information do not have the mandate to make decisions, while people who lack sufficient information can make all decisions.

![](https://esilva.net/assets/team-architecture-topologies.png)
***Figure 1:** A model for organizing (local) architects. Credit: [Gregor Hohpe](https://architectelevator.com/architecture/organizing-architecture/).*

As a part of distributed decision-making goal, we also wanted to embrace architectural diversity. Our organizational units have very diverse structures and sizes. There is no one-fit-all solution about how departments should assign architecture responsibilities. We generally accepted three types of architectural structures in line with Gregor Hohpe's view of architects and their teams' relationships. That means that some units have lead architects coordinating or leading multiple teams. We often have cases where an architect was a full-time member of a team working over specific products or other features. We also have themes that did not have an architect but several senior developers making architectural decisions.

We wanted to make explicit that every unit needs to have some attention or ways of making architectural decisions rather than having them simply happen. If noone is consciously performing the task of architecture, the result is often excessive complexity and reduced velocity, meaning the teams come to a grinding halt.




<br>
## Goal 4: Strengthen Architectural Muscle Across the Organization

Our next goal was to strengthen the architecture muscle across the organization. We want to invest additional efforts to ensure that all parts of the organization have proper people to make informed decisions, while keeping a high level of autonomy and accountability. To do this, we defined two subgoals: 
* collectively grow architectural talent, and 
* increase architectural talent density via virtual communities.


### Goal 4a: Grow Individual Architectural Talent

The superglue characteristics we use defined as a view on the function of architecture, mean serving as the organizational connective tissue, linking the "business wheelhouse" and the "engine room." In terms of individual architects, we expected them to be technically strong but their unique strengths should stem from being able to relate, or glue, technical issues with business and broader issues.

From discussions I've had with our technology leaders, engineers, architects, the picture below has crystallized as a representation of the "superglue" metaphor for architects (Figure 1).

![](assets/images/superglue/architect-as-superglue.png)
***Figure 1:** Architects serve as a superglue, connecting development teams with business stakeholders while also linking their teams with the internal communities and the external world.*

IT organizations need persons who look broader, linking architecture, technical details, business needs, and people together. These persons may not necessarily have a title of an architect. But they need to have good working relationships with developer teams and the local business stakeholders and functions. Simultaneously, such a person is well connected with the internal communities and has external visibility. They promote what we are doing, and on the other hand, they bring back the ideas from the outside.

Setting the architects' goals to be "superglue" also requires some thought on developing as a superglue. Borrowing from Gregor Hohpe's view on architect development from his book Software Architecture Elevator, I share the view that our architects should stand on three legs:

* Skills
* Impact
* Thought leadership

![](assets/images/superglue/architect-skills.png)
***Figure 2:** Architect Profile: Skills + Impact + Thought Leadership.*

**Skills:** Architects have to have proper skill sets. By skills, I mean possessing knowledge and the ability to apply relevant knowledge in practice. These skills should include both technical (e.g., cloud architecture or Kubernetes technology) as well as communication and influence skills.

**Impact:** Impact should be measured as a benefit for the business. Architects need to ensure that what they are doing profits the business. New architects start as students or trainees having skills but little impact. But sooner than later, fresh architects need to get out into the world and make an impact. Architects that do not make an impact do not have a place in a for-profit business.

**Though leadership:** Thought leadership acknowledges that experienced architects should do more than make architecture. This "more" can have different forms but should include at least some of the following activities: mentoring junior architects and engineers, publishing articles, giving talks, starting initiatives, and driving decisions.

Architects need to have minimal "length" of all of these "legs" to be successful. For instance, having skills and impact without leadership frequently leads to hitting a glass ceiling. Such architects plateau at an intermediate level and cannot lead the company to innovative or transformative solutions. Leadership without impact lacks foundation and may signal that you have become an ivory tower architect with a weak relation to reality.

In all scenarios, it is crucial for an organization that a senior architect mentors junior architects. Feedback cycles in (software) architecture are inherently slow. Mentoring can save new architects many years of learning by doing and making mistakes [Hohpe 2020]. We looked at multiple opportunities to create coaching opportunities.

### Goal 4b: Increase Talent Density Via Virtual Communities

With our goal of distributed decision-making, architects are always a part of some team, where they may be the only architects. We wanted to create spaces and opportunities for architects from all units to collaborate globally with architects in other units. 

More specifically, we wanted to create virtual architecture teams as peer-to-peer communities, working part-time on shared issues. We wnated to support and make architects collectively responsible for identifying and growing architectural talent, mentoring, and helping each other. We wanted to create vibrant, diverse communities where architects can leverage and build on each other's work.

![](assets/images/superglue/community.png)
***Figure 1:** Architects work together as community of peers helping each other in their architectural activities.*


<br>

## Goal 5: Leverage Architectural Communities to Maximize Organizational Alignment & Learning
> *" I expect you to learn to be better each day. I challenge you to look at each working day as an opportunity to learn more, and by doing so, to grow as a person."* -- L. David Marquet
>
> *"Good judgment comes from experience, and experience comes from bad judgment."* -- Fred Brooks

When we have virtual teams of architects, such a group can transform individual experiences into collective knowledge that can benefit the whole organization.

Our next goals was to create mechanisms to leverage and accelerate local decision-making while not taking autonomy and accountability for decisions from local units. In particular, we aim to develop global structures that can help people before and after they make an architectural decision: 
* Before people decide, we want to stimulate people working simultaneously on the same topics to work together, minimize effort duplication, and in that way save time and resources. 
* After making a decision, we want to make sure that we make other parts of the organization aware of it and that the distributes or lessons learned so that organization can profit from lessons learned in one unit. Get all the experiences and lessons learned from other parts of organization working with similar issues.

![](assets/images/Misalignment-1024x523.png)
Credit: [Henrik Kniberg](https://blog.crisp.se/2016/05/30/henrikkniberg/misalignment).



One of our primary daily tasks is learning. We need to discover new things about our domain, teams, new tools, and technologies. As individual architects, we need to use each day as an opportunity to learn something new. We need to maximize personal learnings, transforming individual lessons learned into shared guidelines.

One of the problems I frequently see in organizations, particularly complex and international ones, is that they may not have natural spaces for group knowledge sharing. Consequently, architects' superglue attributes may uniquely position them to work together to create spaces for sharing knowledge about architecture and technology. These spaces include but are not limited to regular update calls, knowledge sharing sessions, or conferences.

In addition to creating spaces, as a community, we can further increase our learnings' value by deriving generalized insights from cross-group cases.

We also need to expose our knowledge externally to promote what we are doing, and get valuable external feedback. We wanted dto pro-activelly look for opportunities to give talks, write blog posts, or organize meetups.

One of the problems that many organizations face is that due to their complexity and size, they have more challenges in introducing new technologies compared to their disruptors (Figure 3). We have less time to understand and utilize new technology developments while the number of new technologies is increasing due to, e.g., continuous and accelerating evolution of cloud and mobile products.

As architects, we need to be proactive in the identification of relevant new technology developments. Based on our understanding of these developments, we need to create pragmatic technology recommendations for concrete platforms and across the organization.


![](assets/images/superglue/internalizing-tech-trends.png)
***Figure 3:** One crucial aspect of Architects' work is following external trends and finding pragmatic ways to introduce these trends in the organization. Credit: [thoughtworks.com/insights/blog/whats-hurry-building-digital-enterprise](https://www.thoughtworks.com/insights/blog/whats-hurry-building-digital-enterprise)*




