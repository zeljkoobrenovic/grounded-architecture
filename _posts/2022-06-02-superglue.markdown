---
layout: post
section: "Being Architect"
title: "Architects as Superglue"
position: 6002
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: superglue
icon: superglue.png
timetoread: 15 min
excerpt: "Architects in IT organizations should develop as “superglue,” people who hold architecture, technical details, business needs, and people together across a large organization or complex projects."

---
<style>
     h2 {
          margin-top: 40px;
     }
     h3 {
          margin-top: 40px;
     }
</style>
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/superglue/superglue.png">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
</div>
> **IN THIS SECTION, YOU WILL:**  Understand the view on architects as superglue (people who hold architecture, technical details, business needs, and people together across a large organization or complex projects) and get valuable tips on developing "superglue" abilities.
>
> **KEY POINTS:**
>
> * Architects in IT organizations should develop as “superglue,” people who hold architecture, technical details, business needs, and people together across a large organization or complex projects.
> * Architects need to be technically strong. But their unique strengths should stem from being able to relate, or glue, technical issues with business and broader issues.
> * Architects should stand on three legs: Skills, Impact, Leadership.
<style>
 .quote {
     border-left: 8px solid skyblue;
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
In my view, architects in IT organizations should develop as “superglue.” I borrow the "superglue" view from [Adam Bar-Niv and Amir Shenhav from Intel](https://saturn2016.sched.com/event/63m9/cant-find-superheroes-to-help-you-out-of-a-crisis-how-about-some-architecture-and-lots-of-superglue). They pointed out that instead of the superhero, we need "superglue" architects - the people who hold architecture, technical details, business needs, and people together across large organizations or complex projects. More recently, Tanya Reilly presented a [similar view](https://noidea.dog/glue) concerning software engineering positions.

The superglue characteristics mean serving as the organizational connective tissue, linking the "business wheelhouse" and the "engine room." Architects, of course, need to be technically strong. But their unique strengths should stem from being able to relate, or glue, technical issues with business and broader issues.

<div class="quote">
Architects, of course, need to be technically strong. But their unique strengths should stem from being able to relate, or glue, technical issues with business and broader issues.
</div>

From discussions I've had with our technology leaders, engineers, and architects, the picture below has crystallized as a representation of the "superglue" metaphor for architects (Figure 1).

![](assets/images/superglue/architect-as-superglue.png)
***Figure 1:** Architects serve as a superglue, connecting development teams with business stakeholders while linking teams with the internal communities and the external world.*

Architects must have good relationships with developer teams, local business stakeholders, and functions. Simultaneously, such a person needs to be well-connected with broader internal communities. External visibility is essential for architects, who can bring ideas from outside into the organization and promote the organization to the outside world. 

<br>
## Supergluing in Action: Reducing Tension among Business Function, Product, Technology, Organization

The primary value of superglue architects in an organization is aligning business, product, technology, and organizational functions. While technology, product, organization, and business function face challenges, additional problems occur when there is tension among them (Figure 2). For example, we may organize teams using a well-defined domain model (organizational design). Still, if our system is a monolith (technical design), our teams will collaborate in a different pattern than domain splits suggest. On the other hand, if our teams are well aligned with the technology implementation (e.g., clear ownership of microservices), but the product architecture differs from the microservice domain split, we may need to change dozens of microservices when introducing relatively simple product features. Similarly, business benefits if they align their objectives with product or technology; otherwise, tense interactions will happen (e.g., try reducing short-term costs while adding new features and migrating to the public cloud). 

<div class="quote">
While technology, product, organization, and business function face challenges, additional problems occur when there is tension among them.
</div>


![](assets/images/tension.png)
***Figure 2:** The tensions between technology, product, organization, and business functions.*


The main problem of these tensions is that they slow things down due to miscommunications and misalignment, lead to bad decisions due to lack of information, introduce unnecessary complexity, and lead to many missed opportunities. Too frequently, architecture sits on the side, shouting principles and abstract ideals that everyone ignores. By acting as a superglue, the architecture function can help reduce tension between technology, product, organization, and business functions (Figure 3). Architecture should ensure that conversations happen between the technical, product, organizational, and business functions.

![](assets/images/tension-architecture.png)
***Figure 3:** Architects should be in the middle of reducing tensions between technology, product, organization, and business functions.*

Getting the product/technology/organizational/business alignment right takes a lot of work, which is one of the main areas of architecture work. There will always be essential tension between system architecture, team organization, and product organization. Ideally, these structures all change simultaneously and stay in perfect sync. But in practice, these structures change and move at different speeds. All in all, this situation guarantees the job security of superglue architects.


<br>
## Superglue Abilities

Setting the architects' goals to be "superglue" also requires some thought on developing architects as a superglue. Borrowing from Gregor Hohpe's view on architect development from his book Software Architecture Elevator, I share the view that our architects should stand on three legs (Figure 4):

* Skills
* Impact
* Leadership

![](assets/images/superglue/architect-skills.png)
***Figure 4:** Architect Profile: Skills + Impact + Leadership.*

### Skills 

Architects have to have proper skill sets. By skills, I mean possessing knowledge and the ability to apply relevant knowledge in practice. These skills should include both technical (e.g., cloud architecture or Kubernetes technology) as well as communication and influence skills.

A typical skillset of an architects includes:
* **Hard (technical) skills**, including extensive knowledge of for both new technology and legacy technology stacks,
* **Soft skills**, and
* **Business Domain knowledge**.

The section [Skills](skills) provides more details.


### Impact 

Impact should be measured as a benefit for the business. Architects need to ensure that what they are doing profits the business:
* They identify, tackle and deliver on **strategic problems** at the organization and area level.
* They have a **track record of deep and/or broad impact** on a product or technology area. 
* They **deliver solutions that few others can**, either by your **heavy lifting** or the **ability to orchestrate large group efforts**.

Architects need to get out into the world and make an impact. Architects that do not make an impact **do not have a place in a for-profit business**. 

Examples of such impact may include:
* **Aligning** business, product, technology and organizatinal strategies (see [this section](superglue) for more details),
* **Process** optimizations and improvements, with real measurable impact on work of an organization,
* **Cost** optimizations of systems, based on data informed decisions,
* Developing pragmatic **technology strategies**, helping business reach goals in a sustainable way,
* Driving **delivery of products**, supporting teams to increase quality and speed of delivery,
* Supporting **business innovation**, bringing new ideas in a pragmatic way aligned with business strategy and goals.

The section [Impact](impact) provides more details.
In my view, architects in IT organizations should develop as “superglue.”

### Leadership

Lleadership acknowledges that experienced architects should do more than make architecture: 
* They are a **role model for others** in the company on both the **technical** and **cultural** front.  
* Their **technical influence** may extend **beyond you organization and reach the industry at large**. 
* They **lead efforts** that **solve important problems** at the engineering area level. 
* They may **contribute to the broader technical community** through **tech talks**, **education**, **publications**, **open source projects**, etc. 
* They **raise the bar of the engineering culture** across the company.

Mentoring junior architects is the most crucial aspect of senior architects' leadership. Feedback cycles in (software) architecture are inherently slow. Mentoring can save new architects many years of learning by doing and making mistakes. The [People Pillar](people) should create spaces for such coaching and collaborations.


The section [Leadership](leadership) provides more details.


### Balanced Development

Architects need to have a minimal "length" of all of these "legs" to be successful (Figure 5). For instance, having skills and impact without leadership frequently leads to hitting a glass ceiling. Such architects plateau at an intermediate level and cannot lead the company to innovative or transformative solutions. Leadership without impact lacks foundation and may signal that you have become an ivory tower architect with a weak relation to reality. And having impact and leadership qualities but no skills leads to impractical decisions not informed by in-depth knowledge.

![](assets/images/arch/architect-legs.png)
***Figure 5:** Architects need to have a minimal "length" of all of these "legs" to be successful.*

 
## Questions to Consider

Being a superglue architect means constantly developing and redefining your role to benefit a changing organization. Ask yourself the following questions:

* *How well do you think you currently embody the characteristics of a "superglue" architect? Which areas could you improve on to become more effective in this role?*
* *Reflect on your ability to connect the "business wheelhouse" and the "engine room" within your organization. How effectively do you bridge the gap between technical issues and business needs?*
* *How strong are your relationships with developer teams, local business stakeholders, and broader internal communities? What strategies could you employ to strengthen these connections?*
* *How much external visibility do you currently have? How could this be enhanced to promote the flow of ideas into and out of the organization?*
* *Can you identify specific instances where tension occurred between your organization's technology, product, organization, and business functions? What caused this tension, and how was it addressed?*
* *How does your current architecture aid in reducing tension between these functions? If it doesn't, what changes can you make to align these functions better?*
* *Reflecting on your organization, have you witnessed the architecture sitting on the side, being ignored? If so, what steps can you take to involve architecture in decision-making processes actively?*
* *Are conversations between the technical, product, organizational, and business functions encouraged and facilitated within your organization? If not, how might they be initiated and supported?*
* *Considering the three legs of a successful architect (skills, impact, leadership), which do you consider your strongest? Which might need more development?*
* *Assess your technical skills and ability to apply this knowledge in practice. How well do you balance hard (technical) skills, soft skills, and business domain knowledge?*
* *How do you currently measure your impact within your organization? Could you identify and address more strategic problems to benefit the business?*
* *Reflect on your leadership abilities. How are you acting as a role model within your organization and contributing to the broader technical community?*
* *How do you balance skill development, impact, and leadership? Where should you focus more on ensuring a balanced development as an architect?*
* *In what ways could you be more of a mentor for junior architects? What spaces could you create or utilize to facilitate more effective coaching and collaboration?*
