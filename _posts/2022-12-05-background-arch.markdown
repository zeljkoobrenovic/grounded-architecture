---
layout: post
title: "IT and Enterprise Architecture"
position: 10002
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: background-it-architecture
icon: books.png
timetoread: 15 min
excerpt: ...


---
![](assets/images/hybrid-vehicles-a-short-history-of-the-alternative-drive_4.jpeg)

Good background readings...

## The Software Architect Elevator: Redefining the Architect's Role

<img src="assets/images/software-architecture-elevator.webp" style="width: 178px">

"Staying grounded in reality and receiving feedback on decisions from real project implementations is vital for
architects. Otherwise, control remains an illusion"

"Many companies are penny-wise and pound-foolish by not placing sufficient emphasis on nurturing their
architects. They fear that any distraction from daily project work will be unproductive. However, they miss out
on growing world-class architects."

"The worst-case scenario materializes when people holding relevant information or expertise aren’t empowered
to make decisions, whereas the decision makers lack relevant information."

"It’s about designing software and solving problems within a specific organizational context, and being aware of
what’s happening around you, so that you can successfully navigate and influence that context where necessary.
It’s crucial, therefore, that architects realize they need to communicate and influence at different levels, with
different audiences, both inside and outside of their immediate team environment."

"To transform an organization, you don’t need to solve mathematical equations. You need to move people"

"architects should be part of a trusted but diverse network of experts, which can provide unbiased information"

"When asked to characterize the seniority of an architect, I apply a simple framework: a successful architect must
stand on three “legs”: Skill The foundation for practicing architects. It requires knowledge and the ability to
apply it to solve real problems. Impact The measure of how well an architect applies his or her skill to benefit
the company. Leadership Determines whether an architect advances the state of the practice."

"Lastly, sharing openly and demonstrating thought leadership offers another huge benefit: it can give you access
to a powerful community of other thought leaders, which in turn makes you a better architect."



## Scaling the Practice of Architecture

<img src="assets/images/andrew_harmel-law.png" style="width: 178px">

[Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html)


![](assets/images/scaling-architecture-conversationally.png)

## Team Topologies


also [esilva.net/tla_insights/architecture-topologies](https://esilva.net/tla_insights/architecture-topologies)


![](https://esilva.net/assets/team-architecture-topologies.png)

"The key takeaway here is that thinking of software architecture as a standalone concept that can be designed in isolation and then implemented by any group of teams is fundamentally wrong."

"Team Topologies provides four fundamental team types—stream-aligned, platform, enabling, and complicated- subsystem—and three core team interaction modes—collaboration, X-as-a-Service, and facilitating."

Team-First approach: "We need to put the team first, advocating for restricting their cognitive loads. Explicitly thinking about cognitive load can be a powerful tool for deciding on team size, assigning responsibilities, and establishing boundaries with other teams."

"[Conway’s law] creates an imperative to keep asking: “Is there a better design that is not available to us because of our organization?”"

"Team assignments are the first draft of the architecture."

"Organization Design Requires Technical Expertise" and vice versa

"it is very ineffective (perhaps irresponsible) for organizations that build software systems to decide on the shape, responsibilities, and boundaries of teams without input from technical leaders."

"More than ever I believe that someone who claims to be an Architect needs both technical and social skills, they need to understand people and work within the social framework. They also need a remit that is broader than pure technology—they need to have a say in organizational structures and personnel issues, i.e. they need to be a manager too."

"not all communication and collaboration is good. Thus it is important to define “team interfaces” to set expectations around what kind of work requires strong collaboration and what doesn’t. Many organizations assume that more communication is always better, but this is not really the case." "What we need is focused communication between specific teams."

"If we stress the team by giving it responsibility for part of the system that is beyond its cognitive load capacity, it ceases to act like a high-performing unit and starts to behave like a loosely associated group of individuals, each trying to accomplish their individual tasks without the space to consider if those are in the team’s best interest."

"The first anti-pattern is ad hoc team design."

"Organizations must design teams intentionally by asking these questions: Given our skills, constraints, cultural and engineering maturity, desired software architecture, and business goals, which team topology will help us deliver results faster and safer? How can we reduce or avoid handovers between teams in the main flow of change? Where should the boundaries be in the software system in order to preserve system viability and encourage rapid flow? How can our teams align to that?"

"Non-blocking dependencies often take the form of self-service capabilities (e.g., around provisioning test environments, creating deployment pipelines, monitoring, etc.) developed and maintained by other teams."

"three different categories of dependency: knowledge, task, and resource dependencies."

"reduced ambiguity around organizational roles is a key part of success in modern organization design."

"Trying to fix engineering issues by mandating them from above is doomed to failure, as you really need buy-in from the folks working at the coalface."

"enforcing standardization upon teams actually reduces learning and experimentation, leading to poorer solution choices."

The role of the central architecture team "small group of software and systems architects can be hugely effective within an organization when the remit of architecture is to discover, adjust, and reshape the interactions between teams, and therefore, the architecture of the system."

"when designing modern organizations for building and running software systems, the most important thing is not the shape of the organization itself but the decision rules and heuristics used to adapt and change the organization as new challenges arise; that is, we need to design the design rules, not just the organization."

## Thinking In Systems

"A system is a set of things—people, cells, molecules, or whatever—interconnected in such a way that they produce their own pattern of behavior over time. The system may be buffeted, constricted, triggered, or driven by outside forces. But the system’s response to these forces is characteristic of itself, and that response is seldom simple in the real world."

"Managers are not confronted with problems that are independent of each other, but with dynamic situations that consist of complex systems of changing problems that interact with each other. I call such situations messes.... Managers do not solve problems, they manage messes."

The same apply to architects: we do not solve problems, we manage messes.

"the basic operating unit of a system: the feedback loop."

The importance of prupose: "A system* is an interconnected set of elements that is coherently organized in a way that achieves something. If you look at that definition closely for a minute, you can see that a system must consist of three kinds of things: elements, interconnections, and a function or purpose."

"Many of the interconnections in systems operate through the flow of information. Information holds systems together and plays a great role in determining how they operate."

"Purposes are deduced from behavior, not from rhetoric or stated goals."

Dynamics management (interconnections and purposes): "A system generally goes on being itself, changing only slowly if at all, even with complete substitutions of its elements—as long as its interconnections and purposes remain intact."

"
To be a highly functional system, hierarchy must balance the welfare, freedoms, and responsibilities of the subsystems and total system—there must be enough central control to achieve coordination toward the large- system goal, and enough autonomy to keep all subsystems flourishing, functioning, and self-organizing."

"Bounded rationality means that people make quite reasonable decisions based on the information they have. But they don’t have perfect information, especially about more distant parts of the system."

Avoiding (local) system traps:

THE TRAP: DRIFT TO LOW PERFORMANCE Allowing performance standards to be influenced by past performance, especially if there is a negative bias in perceiving past performance, sets up a reinforcing feedback loop of eroding goals that sets a system drifting toward low performance. THE WAY OUT Keep performance standards absolute. Even better, let standards be enhanced by the best actual performances instead of being discouraged by the worst. Use the same structure to set up a drift toward high performance!

"THE TRAP: RULE BEATING Rules to govern a system can lead to rule beating—perverse behavior that gives the appearance of obeying the rules or achieving the goals, but that actually distorts the system. THE WAY OUT Design, or redesign, rules to release creativity not in the direction of beating the rules, but in the direction of achieving the purpose of the rules."

"THE TRAP: SEEKING THE WRONG GOAL System behavior is particularly sensitive to the goals of feedback loops. If the goals—the indicators of satisfaction of the rules—are defined inaccurately or incompletely, the system may obediently work to produce a result that is not really intended or wanted."

## Cover Art

The [Lohner–Porsche Mixed Hybrid](https://en.wikipedia.org/wiki/Lohner%E2%80%93Porsche) 1900. Credit: Wikimedia Commons.
