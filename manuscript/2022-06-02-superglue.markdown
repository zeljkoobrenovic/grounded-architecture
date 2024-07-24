

# Architects as Superglue {#superglue}

![](assets/images/superglue/superglue.png)
**IN THIS SECTION, YOU WILL:**  Understand the view on architects as superglue (people who hold architecture, technical details, business needs, and people together across a large organization or complex projects) and get valuable tips on developing "superglue" abilities.

{pagebreak}

A> **KEY POINTS:**
A> * Architects in IT organizations should develop as “superglue,” people who hold architecture, technical details, business needs, and people together across a large organization or complex projects.
A> * Architects need to be technically strong. But their unique strengths should stem from being able to relate technical issues with business and broader issues.
A> * Architects should stand on three legs: skills, impact, and leadership.

I believe architects in IT organizations should develop into "superglue." I borrowed this concept from [Adam Bar-Niv and Amir Shenhav from Intel](https://saturn2016.sched.com/event/63m9/cant-find-superheroes-to-help-you-out-of-a-crisis-how-about-some-architecture-and-lots-of-superglue), who suggested that instead of needing superheroes, we need "superglue" architects—**the people who hold architecture, technical details, business needs, and people together** across large organizations or complex projects. More recently, Tanya Reilly presented a [similar view](https://noidea.dog/glue) concerning software engineering roles.

Superglue architects act as the **organizational connective tissue**, linking the "**business wheelhouse**" with the "**engine room**." While technical prowess is essential, their unique strength lies in their ability to relate, or glue, technical issues with business and broader organizational matters.

Based on discussions with engineering leaders, engineers, and architects, Figure 1 illustrates the "superglue" metaphor for architects.

Architects must build strong relationships with developer teams, local business stakeholders, and various functions. Simultaneously, they need to be well-connected with broader internal communities. External visibility is also crucial, allowing architects to bring fresh ideas into the organization and promote the organization to the outside world.

In essence, while superheroes might be great for saving the day, it's the superglue architects who keep everything together, ensuring that the whole machine runs smoothly. So, forget about donning a cape—grab a bottle of superglue and start connecting the dots! 

## Supergluing in Action: Reducing Tension among Business Functions, Product, Technology, Organization

The primary value of superglue architects in complex organizations is **aligning business, product, technology, and organizational functions**. Each of these four parts has its own designs or architectures.

Technology, product, organization, and business functions face specific challenges. Ideally, these structures all change simultaneously and stay in perfect sync. But in practice, these structures change and move at different speeds, leading to **misalignment and tension among them** (Figure 2). For example, we may organize teams using a well-defined domain model (organizational design). However, our IT system is a monolith (technical design). In that case, our teams will have many dependencies and collaborate in a different pattern than the organizational design suggests. On the other hand, if our teams are well-aligned with the technical domain model and implementation (e.g., teams have full ownership of microservices and can deploy them independently), but the product architecture differs from the microservice modularization (e.g., product features are grouped differently than the technical services supporting them), we may need to change dozens of microservices when introducing a relatively simple product change. Similarly, tension occurs when business objectives are misaligned with product or technology objectives (e.g., reducing short-term costs while adding new features and migrating to the public cloud).

![](assets/images/tension.png)
***Figure 2:** The tensions between technology, product, organization, and business functions.*

The main problem with this tension is that it can significantly slow things down due to **miscommunication** or other **misalignments**, lead to costly and **detrimental decisions** due to lack of information, introduce overwhelming and **unnecessary complexity**, and cause critical **missed opportunities**. This is a pressing issue that needs immediate attention. Too frequently, architecture sits on the sidelines, shouting principles and abstract ideals that everyone ignores.

By acting as a superglue, the architecture practice can effectively help reduce tension between technology, product, organization, and business functions, ensuring that critical conversations happen between these units. As Figure 3 illustrates, architecture should not try to be superglue by adding new constructs between these four elements but by bringing them closer together. I sometimes joke that architecture practice is a self-destructive function because by bringing these elements together, you remove the need for an architecture practice. 

![](assets/images/tension-architecture.png)
***Figure 3:** Architects should be in the middle of reducing tensions between technology, product, organization, and business functions.*

While staying close to technology (the engine room), architects must ensure that technology serves the needs of customers and the business, and that technical architecture is well-aligned with organizational design. At the same time, architects can help ensure that business, product, and organizational designs are well-informed about the state, risks, and opportunities of an organization's technology to avoid creating impractical strategies, setting unrealistic goals, or missing opportunities. More specifically, there are several **key risks** that misalignment brings, and architects need to be aware of them:

* **Building the wrong products**: If technology implementation makes incorrect assumptions not aligned with product requirements, you might end up with a toaster when you really needed a coffee maker.
* **Wrong prioritization of activities**: Without clear business and product metrics, we may build "interesting" products that do not create value for our customers and business. Picture making an app that tracks how often your cat blinks—fascinating, but not exactly a bestseller.
* **Unexpected delivery delays**: Underestimating complexity, effort, and dependencies can lead to delays that make your project feel like it's stuck in a time loop.
* **Duplication of effort**: Without business or product harmonization needed to facilitate building shared components, you end up reinventing the wheel so often you could start a wheel shop.
* **Building too complex products**: Creating an overly complex, configurable system to address all possible cases can lead to a labyrinthine solution when a simpler, more harmonized approach would have sufficed. It's like using a Swiss Army knife when you just needed a spoon.
* **Overengineering**: A lack of pushback to simplify products and a lack of understanding of technology can lead to using a complex and expensive messaging middleware capable of handling millions of messages per hour for a use case where you only have a few thousand messages per day. It's like buying a monster truck to drive to the grocery store.
* **Building too simple, unscalable products**: Assuming we will simplify and harmonize our processes, but in reality, needing to keep essential complexity and support many variations, can result in a system that's as robust as a house of cards.
* **Building low-quality products**: Unnecessary complexity and a lack of critical knowledge and expertise in the organization can lead to products that fall apart faster than a dollar-store umbrella in a hurricane.
* **Having complicated dependencies between teams that slow them down**: Suboptimal organizational design and lack of awareness of all the links between systems and people can turn team coordination into a bureaucratic nightmare.
* **Creating fragile, unsustainable team structures**: Having only one or two developers in some critical technology can make your team as resilient as a chocolate teapot.

In summary, while architects stay close to the technology, they must ensure it's working for the business and customers, not the other way around. By keeping everyone in the loop and aligned, architects help steer clear of the many pitfalls of misalignment and keep the organizational machine running smoothly.

## Superglue Abilities

Setting the architects' goals to be "superglue" also requires some thought on developing architects as superglue. Borrowing from Gregor Hohpe's view on architect development from his book *Software Architecture Elevator*, I share the view that our architects should stand on three legs (Figure 4):

- Skills
- Impact
- Leadership

![Architect Profile](assets/images/superglue/architect-skills.png)
***Figure 4:** Architect Profile: Skills + Impact + Leadership.*

### Skills 

Architects must have a solid skill set, possessing both knowledge and the ability to apply relevant knowledge in practice. These skills should include technical (e.g., cloud architecture or Kubernetes technology) as well as communication and influence skills.

A typical skillset of an architect includes:
- **Hard (technical) skills**, including extensive knowledge of both new technology and legacy technology stacks,
- **Soft skills**,
- **Product development knowledge**,
- **Business domain knowledge**, and
- **Decision-making skills**.

The section [Skills](#skills) provides more details.

### Impact 

Impact should be measured as a benefit for the business. Architects need to ensure that what they are doing profits the business. Architects that do not make an impact do not have a place in a for-profit business.

Examples of such impact may include:
- **Aligning** business, product, technology, and organizational strategies,
- **Process** optimizations and improvements with real, measurable impact on the work of an organization,
- **Cost** optimizations of systems based on data-informed decisions,
- Developing pragmatic **technology strategies**, helping businesses reach goals sustainably,
- Driving **delivery of products**, supporting teams to increase quality and speed of delivery,
- Supporting **business innovation**, bringing new pragmatic ideas aligned with business strategy and goals.

The section [Impact](#impact) provides more details.

### Leadership

Leadership acknowledges that experienced architects should do more than make architecture:
- They are a **role model for others** in the company on both the **technical** and **cultural** front.
- Their **technical influence** may extend **beyond your organization and reach the industry at large**.
- They **lead efforts** that **solve important problems** at the engineering area level.
- They may **contribute to the broader technical community** through **tech talks**, **education**, **publications**, **open-source projects**, etc.
- They **raise the bar of the engineering culture** across the company.

**Mentoring junior architects** is the most crucial aspect of senior architects' leadership. Feedback cycles in (software) architecture are inherently slow. Mentoring can save new architects many years of learning by doing and making mistakes.

The section [Leadership](#leadership) provides more details.

### Balanced Development

Architects must have a **minimal "length"** of all of these "legs" to be successful (Figure 5). For instance, having skills and impact without leadership frequently leads to **hitting a glass ceiling**. Such architects plateau at an intermediate level and cannot direct the company to innovative or transformative solutions. Leadership without impact lacks foundation and may signal that you have become an **ivory tower architect** with a weak relation to reality. And having impact and leadership qualities but no skills leads to **impractical decisions** not informed by in-depth knowledge.

In summary, developing architects as "superglue" means fostering a balanced combination of skills, impact, and leadership. Just like a three-legged stool, if one leg is too short, the whole thing topples over—quite possibly spilling your coffee in the process.
![](assets/images/arch/architect-legs.png)
***Figure 5:** Architects must have a minimal "length" of all "legs" to be successful.*

 
## Questions to Consider

Being a superglue architect means constantly developing and redefining your role to benefit a changing organization. Ask yourself the following questions:

* *How well do you think you currently embody the characteristics of a "superglue" architect? Which areas could you improve on to become more effective in this role?*
* *Reflect on your ability to connect the "business wheelhouse" and the "engine room" within your organization. How effectively do you bridge the gap between technical issues and business needs?*
* *How strong are your relationships with developer teams, local business stakeholders, and broader internal communities? How could you strengthen these connections?*
* *How much external visibility do you currently have? How could this be enhanced to promote the flow of ideas into and out of the organization?*
* *Can you identify specific instances of tension between your organization's technology, product, organization, and business functions? What caused this tension, and how was it addressed?*
* *How could your current architecture aid in reducing tension between these functions?*
* *Have you witnessed the architecture sitting on the side, being ignored? If so, what steps can you take to actively involve architecture in decision-making processes?*
* *Are conversations between the technical, product, organizational, and business functions encouraged and facilitated within your organization? If not, how might they be initiated and supported?*
* *Considering the three legs of a successful architect (skills, impact, leadership), which are your strongest? Which might need more development?*

