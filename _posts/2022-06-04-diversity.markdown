---
layout: post
section: "Guiding Principles"
title: "Embrace Diversity, Distribute & Align Decisions"
position: 6004
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: diversity
icon: diversity.png
timetoread: 15 min
excerpt: "My aim was to keep architectural decision-making distributed across the organization embedded in the development teams. Development teams units traditionally have the best insights and most information relevant for making a decision. The worst case of organizational decision-making happens when people with relevant information do not have the mandate to make decisions, while people who lack sufficient information can make all decisions."

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/city-4991094_1920.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/barbaracascao-15841899/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4991094">Bárbara Cascão</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4991094">Pixabay</a>
</div>
> **KEY POINTS:**
>
> * We need to keep architectural decision-making distributed across the organization embedded in the development teams. 
> * Development teams units traditionally have the best insights and most information relevant for making a decision. 
> * The worst case of organizational decision-making happens when people with relevant information do not have the mandate to make decisions, while people who lack sufficient information can make all decisions.

<br>
## Distributing Decisions

I aimed to keep architectural decision-making distributed across the organization and embedded in the development teams. Development teams traditionally have the best insights and most information relevant for making a decision. As noted by Gregor Hohpe, the worst case of organizational decision-making happens when people with relevant information are not allowed to make decisions, while people who lack sufficient information make all decisions. Grounded architecture aims to make relevant information more readily available to a broader audience and better connect people when making decisions.

While I aim to create a mechanism to give teams autonomy, autonomy does not mean that teams are alone and do not align with anyone, do not get feedback from anyone, and do whatever they want. Autonomy needs to be complemented with high transparency and proactivity in alignment with other teams. 

I have sometimes implemented the concept of a decision pyramid to give maximal autonomy to the teams while maintaining a minimal level of global alignment and compatibility (Figure 1).

![](assets/images/arch/decision-pyramid.jpg)
***Figure 1:** A decision pyramid. Most of decisions should be made by the development teams. However, several strategic and domain-level decisions may provide a decision boundaries for teams (e.g., cloud provider).*

Development teams should make most of the decisions. However, several strategic and domain-level choices may provide team decision boundaries. For example, selecting the public cloud provider is typically a CTO-level strategic decision. Similarly, domain engineering leaders may want to limit some choices, such as the number of programming languages, to more easily train new people, maintain code, and support moves between teams.

<br>
##  Embracing Diverse Team Structures 

Organizational units have very diverse structures and sizes. There is no one-fit-all solution about how departments should assign architecture responsibilities. I generally worked on three types of team-architect structures in line with Gregor Hohpe's view of architects and their teams' relationships (Figure 2). That means that some units have lead architects coordinating or leading multiple teams. We often have cases where an architect was a full-time member of a team working on specific products or other features. I also worked with teams that did not have an architect but several senior developers making architectural decisions.

![](https://esilva.net/assets/team-architecture-topologies.png)
***Figure 2:** A model for organizing (local) architects. Credit: [Gregor Hohpe](https://architectelevator.com/architecture/organizing-architecture/).*

In big organization, embracing diversity is a pre-requirements to have any broad impact.

