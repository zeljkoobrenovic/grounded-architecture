---
layout: post
section: "Guiding Principles"
title: "In the Eye of the Storm"
position: 6002
date: 2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: storm
icon: storm.png
timetoread: 15 min
excerpt: "I found it crucial to align on a shared vision on architecture across all departments. In particular, I wanted to prevent positioning of architecture as an ivory tower, disconnected from realities of complex organization."

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/storm-g90b7263c8_1920.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/fiquetdidier1-25748628/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7018311">Didier</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=7018311">Pixabay</a>
</div>


To ensure that organizations maximally benefit from Grounded Architecture, I want architecture to address one of the most challenging problems that our organization is facing: a tension between technology, product, organization, and business functions (Figure 1). 

While technology, product, organization, and business function face their challenges, the additional problem occurs when there is tension among them. For example, we may organize teams according to a well-defined domain model. Still, if our system is a monolith, our teams will collaborate in a different pattern than domain splits would suggest. On the other hand, if our teams are well aligned with the technology implementation (e.g., clear ownership of microservices) but the product architecture is different from the microservice domain split, we may end up changing dozens of microservices when we need to introduce relatively simple product features. Similarly, business objectives need to be better aligned with product or technology; otherwise, tense interactions will happen (e.g., try reducing short-term costs while adding new features and migrating to the public cloud). Too frequently architecture sits on the side, shouting principles and abstract ideals that everyone ignores.

![](assets/images/tension.png)
***Figure 1:** The tensions between technology, product, organization, and business functions.*


The main problem of these tensions is that they slow things down due to miscommunications and misalignment, lead to bad decisions due to lack of information, introduce unnecessary complexity, and lead to many missed opportunities.

Considering this problem, I always wanted architecture to reduce the tension between technology, product, organization, and business functions. Architecture should ensure that conversations happen between the technical, product, organizational, and business functions.

![](assets/images/tension-architecture.png)
***Figure 2:** Architect should be in the middle reducing tensions between technology, product, organization, and business functions.*

Getting this product/technology/organizational/business alignment right takes a lot of work, and this is one of the main problems of architecture. It is a "soft" area without explicit external constraints, and we need to constantly experiment and change domain boundaries. Numerous acquisitions can worsen such problems, as you have many completely different architectures and technologies stacks built by various people that you may need to combine in one platform. Grounded architecture can help by making this "soft" problem more data-informed.

Legacy structures and monoliths are challenging to change once in place. It can take several years to rebuild a monolith from scratch as a microservices ecosystem. Therefore, a more pragmatic approach is to gradually "strangulate" the monolith by minimizing changes and incrementally extracting pieces of it into separate microservices. But such an approach takes years. Grounded architecture can provide data about legacy landscapes and connect people to share scarce legacy knowledge to do such changes.

There is always some essential tension between system architecture, team organization, and product organization. Ideally, these structures all change simultaneously and stay in perfect sync. But in practice, these structures change and move at different speeds. For instance, the product may quickly pivot in another direction, but it may take months to reorganize teams to have new product elements as separate domains with clear ownership. It may take several years to reorganize code and services to align microservices well with new team structures. In the meantime, the company may acquire two other companies that need to be integrated with the ecosystems, and the product is already pushing in another direction. Grounded architecture can help by making such changes and gaps more visible.
