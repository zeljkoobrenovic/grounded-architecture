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



> *“Rather than inject itself in every decision loop, architecture should design mechanisms for teams to make better decisions - they'll know better anyhow, and slowing them down carries a high cost.”*

> *“Autonomy does not mean you're all alone and don't align with anyone, don't get feedback from anyone and just do whatever you want.”

My aim was to keep architectural decision-making distributed across the organization embedded in the development teams. Development teams units traditionally have the best insights and most information relevant for making a decision. The worst case of organizational decision-making happens when people with relevant information do not have the mandate to make decisions, while people who lack sufficient information can make all decisions. Grounded architecture aims to make relevant information more readily available to a broader audience and better connect people when making decisions.

Organizational units have very diverse structures and sizes. There is no one-fit-all solution about how departments should assign architecture responsibilities. I generally worked three types of architectural structures in line with Gregor Hohpe's view of architects and their teams' relationships. That means that some units have lead architects coordinating or leading multiple teams. We often have cases where an architect was a full-time member of a team working over specific products or other features. We also have themes that did not have an architect but several senior developers making architectural decisions.

![](https://esilva.net/assets/team-architecture-topologies.png)
***Figure 1:** A model for organizing (local) architects. Credit: [Gregor Hohpe](https://architectelevator.com/architecture/organizing-architecture/).*

<br>
In daily work, we aimed to implement the following operational model:
* Most of the decisions should be made by individual teams, which should be a part of the people pillar via different communities, such as architecture guilds
* Architecture function should provide 
  * data to inform these decisions via the data pillar
  * decisions boundaries to enable the minimal level of compatibility and strategic alignment (e.g., cloud provider)
  * principles to facilitate consistency in decision-making
* Global architects should then spend their time in constant motion between the daily work of the teams and strategic topics, helping the organization to achieve alignment between strategy and implementation

Inspired by Gregor Hohpe's strategy-principles-decisions model, the following picture illustrates the process:

![](assets/images/arch/architecture-system.png)

