---
layout: post
section: "Operating Principles"
title: "Aligning Culture: Breaking Up Ivory Towers"
position: 6001
date: 2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: superglue
icon: tower.png
timetoread: 15 min
excerpt: "While we wanted to embrace diversity, we found it crucial to align on a shared vision on architecture across all departments. In particular, we wanted to prevent positioning of architecture as an ivory tower exercize, disconnected from realities of complex organization."

---
![](assets/images/arch/fantasy-782001_1920.jpg)



While we wanted to embrace diversity, we found it crucial to align on a shared vision on architecture across all departments. In particular, we wanted to prevent positioning of architecture as an ivory tower exercize, disconnected from realities of complex organization.

More specifically, we wanted architecture to address one of the toughest problem that our organization is facing: a tension between technology, product, organization, and business functions (Figure #). While technology, product, organization and business function face their own challenges, big problem occurs when there is a tension among them. For example, we may organize teams according to a nice domain model, but if our technology is implemented as a monolith, our teams will collaborate in a different pattern then a domain splits would suggest. On the other hand, if our teams are well aligned with the technology implementation (e.g. clear ownership of microservices) but product architecture is different that microservice domain split, we may end up changing dozens of microservices when we need to introduce relatively simple product features. Similarly, if business objectives are not well aligned with product or technology ones (e.g. reducing costs, while adding new feature, and migrating to the public cloud) lots of tense interactions will happen. In an ivory tower model, architecture sites on side, shouting principles and abstract ideals that everyone ignores.

![](assets/images/tension.png)

The main problem of these tensions is that they show things down due to miscommunications and misalignment, lead to bad decisions  due to lack of information, introduce unnecessary complexity, and lead to many missed opportunities.

With this problem in mind, we wanted architecture to overall in organization focuses on reducing the tension between technology, product, organization and business functions.

Architecture should ensure that conversations happen between the technical, product, organizational, and business functions.

![](assets/images/tension-architecture.png)

As a guiding principle, we promoted a view that senior architects in our organization should develop as "superglue." We borrow this view from [Adam Bar-Niv and Amir Shenhav from Intel](https://resources.sei.cmu.edu/library/asset-view.cfm?assetID=454541). They pointed out that instead of the superhero, we need "super glue" architects - the fellows who hold architecture, technical details, business needs, and people together across a large organization or complex projects.

The superglue characteristics mean serving as the organizational connective tissue, linking the "business wheelhouse" and the "engine room."

## Essential Complexity

There are all sources of reason for described tension. Firstly, it is tough to get this product/technology/organizational/business alignment right, and this is one of the main problems of architecture and software engineering. It is "soft" area without clear external constraints, and we are constantly experimenting and changing our domain boundaries. Numerous acquisition (e.g. Leboncoin and Spain) have made such problems worse as you have many completely different architectures and technologies stacks, built by different people that you need to combine in one platform.

Second, legacy structures and monoliths are difficult to change once in place. It can take several years to rebuild a monolith from scratch as a microservices ecosystem. For that reason more pragmatic approach is to gradually "strangulate" monolith by minimizing changes to it , and incrementally extracting pieces of it into separate microservices. But such approach takes years.

Third, there is always some essential tension between system architecture, team organization, and product organization. Ideally these structures would all change at the same time and stay in perfect sync. But in practice these structures change and move with different speeds. For instance, product may quickly take a pivot in another direction, e.g. starting to experiment with payments and other transactional services. If such experiments are successful, it may take months or a year to get teams reorganised to have these new elements as separate domains with clear ownership. And then it may take several years to reorganize code and services to get microservices well aligned with new team structures. In the meantime, the company may acquire two other companies that need to be integrated in the ecosystems, product is already pushing in another direction, and we may have churn of 30%.

## Cover Art

Image by <a href="https://pixabay.com/users/dlee-271284/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=782001">Donna Kirby</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=782001">Pixabay</a>
