---
layout: post
section: "Grounded Architecture Framework: Generative AI"
title: "Leveraging Generative AI: First Steps"
position: 3021
podcast: gen-ai.mp3
spotify: https://open.spotify.com/episode/33yE0ngCoL8JVM4uACFPJ5?si=daa89a886b50485f
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
icon: gen-ai.png
permalink: gen-ai
timetoread: 15 min
excerpt: "Generative AI, when used wisely and critically, can empower IT Architects to work faster, think deeper, and stay grounded in real-world needs—amplifying creativity, governance, and innovation without losing human judgment."

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/istock/iStock-2157103268.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/MininyxDoodle">Mininyx Doodle</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>
> **IN THIS SECTION, YOU WILL:** Understand how Generative AI, when used wisely and critically, can empower IT Architects to work faster, think deeper, and stay grounded in real-world needs—amplifying creativity, governance, and innovation without losing human judgment.
>
> **KEY POINTS:**
>
> * Generative AI can act as a force multiplier for IT Architects by streamlining documentation, accelerating decision-making, enhancing design processes, supporting governance, fueling innovation, and keeping architecture models dynamic.
> * AI is best used as an assistant, not a replacement—helping draft, critique, and analyze while architects maintain control, judgment, and final accountability.
> *  Using AI aligns with the Grounded Architecture philosophy, staying practical, data-driven, and focused on real-world outcomes rather than abstract theory.
> *  First practical applications include: summarizing reports, critiquing designs, surfacing risks, brainstorming new solutions, simplifying compliance work, and making architecture models more accessible.
> * Success with AI depends on critical use, validation of AI outputs, careful prompting, and always combining machine speed with human strategic thinking.
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
        [class="quote"] {
            display: none;
        }
    }
</style>


<br>
Over the past year, like many others I've been exploring how **Generative AI** can make my work as an IT Architect faster, more innovative, and frankly, a lot more interesting. If you're like me—juggling strategy, system design, governance, innovation, and endless documentation—you know how easy it is to get buried in manual tasks. 

I've found that used wisely, AI fits perfectly into the **Grounded Architecture** mindset: staying connected to real-world needs, working with actual data, and avoiding ivory-tower abstractions. One of the biggest lessons I've learned, reflecting the views of many others, is this: **AI won't replace architects; they'll be replaced by architects who know how to leverage AI (and perhaps more importantly, know how not to).**

In this chapter, I'll share how I use generative AI today: streamlining documentation, speeding up decision-making, improving design, supporting governance, fueling innovation, and even enhancing modeling. I'll keep it practical, grounded, and real—just as Grounded Architecture teaches us.


In the [Generative AI Potential for IT Architecture](gen-ai-potential) section you can find a more detailed overview of the potential of Generative AI for IT Architecture. In this chapter, I want to share my practical experiences and insights on how to leverage AI effectively in our field. 

Let's dive in.

<br>
## Streamlining Documentation with AI

One of the first areas where AI greatly impacted me was **documentation**. The writing workload can get overwhelming, whether it's requirements, design specs, ADRs, or standards.


![](assets/images/istock/iStock-1975281324.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/lucadp">lucadp</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

Here's how I use AI day-to-day:
- **First drafts:** I'll throw in bullet points about a design and let AI generate a draft document. It saves me 50–70% of the time it would normally take to write from scratch.
- **Summarizing long texts:** When stakeholders send me 40-page reports, AI will summarize them into key points for quick decision-making.
- **Quality reviews:** I've trained AI to act like a junior reviewer. It spots vague requirements ("handle a large number of users") and reminds me to be specific ("10,000 concurrent users, peak").
- **Updating live documents:** If I get new info from a project team or monitoring reports, AI helps me update architecture descriptions without starting over.

Of course, it doesn't replace my judgment. I always review AI's output carefully. But it does take the heavy lifting off my plate so that I can focus on **thinking,** not typing.

<br>
## Using AI to Accelerate Decision-Making

Architects live and die by decisions: tech choices, patterns, risk tradeoffs. Generative AI has become my "research sidekick." 


![](assets/images/istock/iStock-2067248129.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/NicoElNino">NicoElNino</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

Here's what that looks like:
- **Comparing options:** You'll feed AI a question like, "Should we use a monolith or microservices for this project?" It spits out pros, cons, and considerations tailored to my context.
- **Cost and performance analysis:** You can upload billing data or performance logs for cloud optimization, and AI highlights trends, waste, and quick wins. It cuts hours of spreadsheet work into minutes.
- **Business translation:** When advising executives, you can ask AI to help frame tech decisions in business terms: "How does this solution affect uptime, costs, and customer satisfaction?"

You're still making the calls. AI just helps you gather better inputs—faster.


<br>
## Enhancing Design and Ideation with AI

Designing systems is where AI becomes a real partner, not just an assistant.


![](assets/images/istock/iStock-1221296734.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/Blue Planet Studio">Blue Planet Studio</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

When starting on a fresh architecture, you can ask AI open-ended questions like, *"What are possible designs for a real-time inventory system?"* It usually throws back several patterns—microservices, event sourcing, modular monoliths—with pros and cons you can chew on.

Sometimes, it suggests ideas you wouldn't have thought of immediately. It's like brainstorming with a very fast, well-read junior architect who's read every case study under the sun.

You can also use AI for quick **sanity checks**. After sketching a design, you'll describe it to the AI and ask, *"What security risks or bottlenecks should I watch for?"* It almost always surfaces helpful something—like reminding me to load-balance a service you had overlooked.

If you're stuck, you'll have it generate sample code snippets, database schema ideas, or system diagrams. It's not perfect, but it gives me something to react to, accelerating my creative flow.

In short, AI makes me a *faster, sharper designer*—without taking away my ownership of the architecture.

<br>
## Improving Governance and Compliance with AI

Governance isn't the sexiest part of architecture, but it's critical—and AI helps me manage it without getting buried.


![](assets/images/istock/iStock-2160417380.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/Alexander_Supertramp">Alexander Supertramp</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

For example, when you review a solution design, you can feed the AI the architecture description and ask it to check for gaps against our security or cloud standards. It acts like a first-pass reviewer, flagging missing backup strategies, single points of failure, or vague service descriptions.

You can also use AI to **summarize security scans** or compliance reports. Instead of digging through 100-page vulnerability lists, you get a clean executive summary: top risks, quick wins, and major concerns.

Another trick you can use: training AI on our internal policies, so teams can ask simple questions like, *"What's the standard for API security?"* and get a straight answer instantly. It democratizes governance without adding bureaucratic overhead.

The bottom line: AI helps me enforce standards without being a bottleneck and lets me spend more time on critical decisions rather than paperwork.

<br>
## Supporting Innovation and Strategy with AI

When you're working on *innovation*—scouting new tech, designing future states, proposing bold ideas—AI is a fantastic thought partner.

You can prompt it with questions like, *"How could blockchain improve our supply chain transparency?"* or *"What might edge computing enable for our IoT strategy?"* It often gives me 4–5 solid ideas plus some practical risks to watch out for.

You can also use AI to draft mini-business cases when you pitch new initiatives. If you describe an idea, AI can help outline benefits, risks, costs, and strategic alignment. It's not the final analysis, but it gives me a running start.

AI lowers the barrier for more people to join innovation conversations. A business analyst, a product owner, or even a junior dev can sketch ideas with AI's help, then bring them into architecture discussions. It spreads creativity beyond the architecture team.

AI can multiply human ingenuity.

<br>
## Augmenting Modeling and Analysis with AI

Keeping architecture models updated used to be one of my least favorite chores. Now, with AI, it's far more dynamic and collaborative.


![](assets/images/istock/iStock-2185931941.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/KrulUA">KrulUA</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

Today, You can often describe systems or processes in plain English—and AI helps draft architecture diagrams, component lists, or relationship maps. It's imperfect, but it saves hours of clicking in modeling tools.

More excitingly, you can start to **query architecture models in natural language**. Instead of manually hunting through layers of diagrams, I can ask, *"Which apps handle customer orders?"* and get a simple answer.

When models drift from reality, you can feed AI up-to-date infrastructure data (like cloud configs or microservice registries), and it suggests updates for the architecture view. It's like having an architecture auditor who never gets tired.

Even better, AI helps **translate models for different audiences**. From a technical diagram, you can draft a business capability map for executives or a deployment diagram for engineers—without manually redrawing everything.

These translations mean my architecture stays *living, accessible, and grounded in reality*as it should be.

<br>
## Final Thoughts: Staying Grounded Using AI

If there's one thing I've learned, it's that **Generative AI is a tool, not a replacement**.

It's great at speeding up documentation, surfacing insights, brainstorming options, and checking compliance. But it doesn't understand context, strategy, or business nuance like I do. If I'm not careful, it can hallucinate or miss critical subtleties.

So, I treat AI like a junior partner: fast, smart, helpful, but always needing my judgment and leadership. I prompt it carefully, review its output rigorously, and make the final decisions.

Used this way, AI doesn't make architecture less important—it makes **good architecture even more valuable**. It frees me up to focus on tangible business outcomes, strategic design, and connecting systems to human needs.

In short, just like Grounded Architecture, Generative AI helps me stay more **grounded**, more impactful, and (honestly) a lot more excited about the future of architecture.

<br>
## Questions to Consider

* *How could you start using AI today to streamline one repetitive task in your architecture practice?*
* *Where in your current workflow could faster research or summarization help you make better decisions?*
* *Have you considered using AI to help brainstorm multiple architectural options before committing to a design?*
* *How could AI assist your organization's governance processes without adding bureaucratic friction?*
* *What risks do you foresee if you rely too heavily on AI-generated outputs without validation?*
* *In your current architecture documentation, where would an AI “junior reviewer” be most valuable?*
* *Could AI help democratize architecture work in your organization, making innovation more inclusive?*
* *What would it take to make your architecture models more dynamic, searchable, and accessible via natural language?*
* *How can you maintain a “grounded” approach while experimenting with emerging AI tools?*
* *Where do you want to deliberately keep human expertise at the center, even when AI can assist?*