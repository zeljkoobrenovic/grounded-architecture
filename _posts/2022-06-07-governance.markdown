---
layout: post
section: "Principles & Lessons Learned"
title: "Flexible Governance"
position: 6007
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: flexible-governance
icon: flexible.png
timetoread: 15 min
excerpt: "We wanted to create a governance model that acknowledges the complexity and diversity of our organization. We aimed at promoting a technology governance model as a well-balanced hybrid of three different ways of governing: mandates and bans, taxes, and leading by context."

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/parliament-366199_1920.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/cocoparisienne-127419/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=366199">Anja-#pray for ukraine# #helping hands# stop the war</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=366199">Pixabay</a>
</div>


We wanted to create a governance model that acknowledges the complexity and diversity of our organization. By governing, we mean guiding technology choices in the organization in a particular direction aligned with the technology strategy. We tried to prevent a simplistic view of architecture as defining directives for the rest of the organization.

Consequently, we aimed at promoting a technology governance model as a well-balanced hybrid of three different styles of governing:
* mandates and bans,
* taxes, and
* leading by context.


## Mandates and Bans Governance Style

By governing with mandates and bans I mean guiding people by explicitly defining what they should or should not do. In places I worked in, such mandates and bans have had a limited by important place to define broader strategic boundaries of choices that people can make. For instance, limiting the usage of public cloud providers to specific vendors or following strict privacy and security procedures needs to be explicitly defined and controlled. 

The role of architecture in this form of governing should be to be a stakeholder but not a sole owner of in defining mandates and bans. Mandates and basn frequelty need to be defined in collaboration with others, such as security and legal functions. The architecture can help in creating clarity, and providing transparency.

The Data pillar was a helpful element in creating clarity and transparency. For instance, we have created different maps of areas in source code or infrastructure that needed to be monitored and controlled based on privacy or security requirements.

The People pillar helps propagate the decision and ensure its positive impact. You should never order or forbid people to do some things routinely. Spending enough time with all stakeholders to explain the reasons and motivations behind introducing some limitations is crucial to ensure the effective working of mandates and bans. Having a strong People pillar ensures that you already have strong connections with key stakeholders and can leverage them to change ways of working more smoothly.


## Taxation Governance Style

Governing with taxes is a form of guiding in which people are not forbidden to make some decisions but need to "pay" some form of taxes on used resources. For instance, costs of the public cloud usage could be cross-charged across the organization, providing a helpful feedback loop to optimize our systems and avoid unnecessary resource consumption, avoiding "tragedy of commons" which frequently happens when there are no limits or significant costs of increasing shared resource consumption (e.g., public cloud budget). 


The role of architecture in this form of governance should be to ensure that "taxation" is data driven and transaprent, and to create efficient feedback loops on key metrics related to "taxes."

* Visibility
* Being a part of budgeting process
* OKRs, Tech Debt Tracking, Balanced scorecard

Data platform should include and provide all data regarding taxes. People platform should align processes, golas and ways of working to ensure that taxation leads to desired and meaningful change.


## Leading by Context Governance Style

Leading the context is a form of governing in which we do not forbid people to make some choices, nor do they need to "pay" taxes. Instead, we wanted to create a shared context that can facilitate people making informed decisions. Such contexts should include sharing of lessons learned by others, both good and bad, and places to get feedback on ideas and plans. The role of the architecture in this form of governing should be to create mechanisms for sharing experiences and obtaining feedback on plans and decisions. It should also include mechanisms to capture artifacts that can help people to make informed decisions, such as architecture decision resources (ADRs), principles, golden paths, or best practices.

* Data platform provides transparency and clarity. This insights alone can lead to change. 
* Sharing and generalizing lessons learned.
* External visibility.


