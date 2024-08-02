---
layout: post
section: "On Human Complexity"
title: "Effortless Architecture"
position: 7019
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
icon: effortless.png
permalink: effortless
timetoread: 11 min
excerpt: "A summary of lessons learned from Greg McKeown's Effortless book, which offers invaluable insights that are particularly relevant for IT architects and software engineers. McKeown's emphasis on simplifying tasks and processes is crucial in the tech industry, where complexity often dominates."

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/iStock-1183657530.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>
> **IN THIS SECTION, YOU WILL:** Get summary of lessons learned from the Effortles s book on how you functionally structure your work to make the most essential activities the easiest ones to achieve.
>
> **KEY POINTS:**
>
> * Greg McKeown's "Effortless: Make It Easier to Do What Matters Most" advocates for a paradigm shift from hard work to smart, effective work by simplifying tasks and processes. 
> * Key principles include prioritizing important tasks, leveraging automation, and embracing a mindset that values ease and enjoyment in work.
> * Greg McKeown's book offers invaluable insights that are particularly relevant for IT architects and software engineers. McKeown's emphasis on simplifying tasks and processes is crucial in the tech industry, where complexity often dominates. 

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
        [class= "quote"] {
            display: none;
        }
    }
</style>



<br>
Greg McKeown's **"[Effortless: Make It Easier to Do What Matters Most](https://gregmckeown.com/books/effortless/) "** advocates for a paradigm **shift from hard work** to innovative, effective work by simplifying self-created complicated tasks and processes. The book emphasizes achieving goals with minimal strain by fostering an effortless state characterized by clarity and focus. Fundamental principles include prioritizing essential tasks, leveraging automation, and embracing a mindset that values ease and enjoyment in work. McKeown provides practical strategies for reducing unnecessary effort, enhancing productivity, and maintaining sustainable high performance, ultimately enabling individuals to achieve better results with less effort and stress. 

I see the Effortless books as a perfect complement to Fred Brooks' essay "[**No Silver Bullet**](https://en.wikipedia.org/wiki/No_Silver_Bullet)." Fred Brooks posits that no single technological breakthrough will dramatically improve software development productivity because of the inherent, **essential complexity** of the tasks involved. In contrast, Greg McKeown emphasizes the importance of reducing **accidental complexity**—those unnecessary complications we can eliminate to streamline processes and simplify tasks we complicate ourselves. While Brooks highlights the unavoidable challenges intrinsic to software development, McKeown offers a crucial reminder that streamlining and optimizing workflows can significantly reduce extraneous difficulties, thus enhancing overall efficiency and effectiveness. Or, as McKeown put it *"life doesn't have to be as hard and complicated as we make it."* 

<br>
## IT Doesn't Have To Be As Hard and Complicated As We Make It

One of the main tasks of architects is to remind everyone that our technical designs, products, and organizational structures don’t have to be as complex and complicated as we make them. A fantastic example of this comes from Pragmatic Dave Thomas (I heard this anecdote on the [SE-Radio podcast with Neal Ford](https://se-radio.net/2017/04/se-radio-episode-287-success-skills-for-architects-with-neil-ford/), ~32 minutes in). A company had problems with its mail post not getting to the proper departments. It wanted a complex optical-character recognition (OCR) system for routing mail posts. However, Dave Thomas suggested using simple and cheap colored envelopes instead. The company did not need to invest millions in building a complex software system with machine-learning capabilities; it solved the problem in a few weeks and saved a lot of money.

Greg McKeown's book summarizes many well-known practices into a pragmatic framework with a mindset of effortlessness. As such, it offers a fresh look at the daily practice of IT architects and software engineers:

* **Simplifying tasks** and processes is crucial in the tech industry, where complexity often dominates. Effortless principles align closely with critical system design and coding practices, such as modular design, clean code, and lean architecture. IT professionals can significantly enhance efficiency by breaking complex systems into manageable modules, writing maintainable code, and focusing on essential features without over-engineering.

* **Prioritization,** another core aspect of McKeown's book, is vital in the fast-paced IT industry. Effectively prioritizing tasks can dramatically impact project outcomes, helping professionals focus on what truly matters. This prioritization leads to more effective project management, resource optimization, and strategic planning, aligning development efforts with business goals.

* **Efficiency and productivity** are also central themes in "Effortless." For software engineers, this translates to practices like automated testing and deployment through CI/CD pipelines, optimization techniques to enhance code performance, and using development tools that streamline workflows.

* McKeown's advocacy for shifting from hard work to smart work is particularly pertinent in the tech world. This mindset shift promotes **continuous learning,** a healthy **work-life balance,** and **resilience strategies** to handle challenges positively.

* **Collaboration and communication,** highlighted in "Effortless," are essential for IT professionals. They enhance collaboration between development, operations, and business teams and ensure stakeholder engagement, leading to more aligned and informed teams.

* In high-pressure environments like the tech industry, **managing stress** is crucial. McKeown's strategies for reducing unnecessary effort and anxiety can help IT professionals focus on high-value tasks, improve mental health, and boost team morale, creating a more enjoyable work experience.

In the following sections, I will review critical advice from McKeown's work, grouped into Effortless State, Effortless Action, and Effortless Results.

<br>
## Effortless State

Many have encountered the Effortless State, a **peak experience** when their physical, emotional, and mental well-being align perfectly. You feel physically rested, emotionally unburdened, and mentally energized in this state. You become entirely aware, alert, present, attentive, and focused on what's important. This state allows you to **concentrate on what matters** more quickly and efficiently.

When you achieve the Effortless State, it's a sign that **your brain is operating at its full capacity.** In this optimal condition, tasks that usually feel difficult become significantly easier. You can navigate challenges with a sense of flow and clarity, making decisions and performing actions with a heightened **sense of purpose and precision.** This state enhances your productivity and opens up new avenues for personal growth and development.

However, reaching and maintaining this state can be impeded by **mental clutter.** Clutter can take many forms, including outdated assumptions, negative emotions, and toxic thought patterns. These mental obstacles drain your cognitive resources and make everything feel more complicated than it should be. By clearing this clutter and fostering a supportive mental environment, you can unlock your brain's full potential and access the Effortless State consistently.

<br>
### 1. INVERT: What If This Could Be Easy?

Feeling overwhelmed is often not due to a situation's inherent complexity but because we are **overcomplicating it in our minds.**  Instead of asking, *"Why is this so hard?"* invert the question by asking, *"What if this could be easy?"* Challenge the assumption that the "right" way is necessarily harder. When faced with overwhelming tasks, ask yourself, *"How am I making this harder than it needs to be?"* 

By asking, *"What if this could be easy?"* you can reset your thinking. This simple yet powerful question can transform your approach, making tasks more manageable and less daunting. Or, as Kent Beck famously stated, for each desired change, **make the change easy, then make the easy change.**

![](assets/images/iStock-1359088740.jpg)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

IT and software engineering have integrated the principles of effortless inversion, transforming many complex tasks into efficient processes. But we must always remind ourselves not to overthink our work. 

Here are a few examples that IT architects as an inspiration to help their organizations make things easier:

* **Simplifying Code Maintenance With Clean Design:**
Creating a modular source code design with clear, simple, and well-tested functions makes code maintenance easier. Clean and modular code leverages existing libraries and prioritizes readability and maintainability over micro-optimizations. These widely known practices simplify maintenance, reducing the time and effort needed for debugging and updates. Still, developers are not universally following them.

* **Streamlining Deployment Processes:**
Teams implement Continuous Integration/Continuous Deployment (CI/CD) pipelines using tools like Jenkins, GitHub Actions, or GitLab CI. Automating testing, building, and deployment processes minimizes human error and expedites the deployment process, making it more reliable and significantly less effortful.

* **Simplifying User Interface (UI) Design:**
Designers and front-end developers prioritize user-centered design principles, emphasizing ease of use and intuitive navigation. They use UI frameworks like Material Design to create consistent and straightforward interfaces. A simplified and user-friendly UI enhances user experience and reduces the cognitive load on developers and end-users, making the application more straightforward to use and maintain.


<br>
### 2. ENJOY: What If This Could Be Fun?

Combining essential tasks with pleasurable activities can enhance your productivity while maintaining a sense of well-being. Accept that it is possible and beneficial to **integrate work and play.** Pair the most essential activities with the most enjoyable ones. Embrace the idea that work and play can co-exist harmoniously. Transform tedious tasks into meaningful rituals, infusing them with purpose and enjoyment. Allow laughter and fun to lighten more of your moments, turning routine activities into opportunities for joy and creativity.

This approach helps you stay engaged and motivated, making even the most mundane tasks feel more fulfilling and less burdensome. Letting joy and laughter permeate your daily routine creates a positive, dynamic environment where productivity and happiness thrive together.

<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-1294958620.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

Pairing essential activities with enjoyable ones creates a harmonious and engaging work environment for IT and software engineering professionals. This approach enhances productivity, promotes well-being, and increases job satisfaction by turning routine tasks into opportunities for joy and creativity. 

Here are a few examples that IT architects as an inspiration to help their organizations integrate work and play:

* **Architecture and Code Reviews as Collaborative Learning Sessions:**
Architecture and code reviews, often seen as tedious and time-consuming, can be transformed into collaborative learning sessions. Pair programming or review parties allow team members to discuss and review code over snacks and drinks. Adding a gamification element, such as rewarding the most insightful feedback, makes code reviews social and enjoyable. This engagement leads to better code quality and stronger team cohesion.

* **Writing Technical Documentation:**
Technical documentation, often perceived as monotonous, can be made more enjoyable by infusing creativity. Using storytelling techniques or incorporating visual elements like diagrams, infographics, and comic strips can make the task engaging. Encouraging personal anecdotes or humor where appropriate results in more comprehensive and user-friendly documentation, making the process enjoyable for both writers and readers.

* **Keeping Up with New Technologies:**
Continuous learning and keeping up with new technologies can feel overwhelming and exhausting. Aligning learning activities with personal interests and hobbies helps maintain motivation and enthusiasm. For instance, exploring game development or gamification techniques for team members who enjoy gaming, or delving into UI/UX design trends for those who love graphic design, makes continuous learning more enjoyable and fulfilling.


<br>
### 3. RELEASE: The Power Of Letting Go

As the saying goes, ***"the best thing one can do when it is raining is to let it rain."*** By acknowledging and embracing our circumstances, we can focus on what we have rather than what we lack, fostering gratitude and emotional resilience. 

Regrets that continue to haunt us, grudges we can't seem to let go of, and expectations that once were realistic but now hinder us all contribute to our emotional burdens. When we fall victim to misfortune, we easily obsess, lament, or complain about all we have lost. **Complaining** is one of the easiest things to do.

<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-1464747516.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

Similarly, IT and software engineering professionals can release unnecessary **emotional burdens,** fostering a positive and resilient mindset that enhances personal well-being and professional effectiveness. 

Here are a few examples that IT architects as an inspiration to help their organizations let go:

* **Overcoming Regret Over Past Decisions:** Engineers and IT architects may regret choosing a certain technology stack or making architectural decisions that later proved suboptimal. Accept that every decision was made with the best knowledge available at the time and focus on learning from past experiences rather than dwelling on them. When regret surfaces, reflect on a positive outcome or lesson learned from that decision and express gratitude for the growth it provided. Shifting focus from regret to learning fosters a growth mindset and empowers engineers to make informed decisions without being weighed down by past mistakes.

* **Letting Go of Grudges Against Team Members:** Holding grudges against colleagues for past misunderstandings or conflicts can create a toxic work environment. Address and resolve conflicts through open communication and empathy, recognizing that holding grudges serves no constructive purpose. Each time a grudge resurfaces, consciously let it go by acknowledging the colleague's positive trait or contribution. Releasing grudges promotes a harmonious and collaborative team environment, improving morale and productivity.


* **Embracing Change and Letting Go of Resistance:** Resistance to adopting new technologies or methodologies can hinder progress and innovation. Be open to change and willing to experiment with the latest tools and approaches, viewing change as an opportunity for growth rather than a threat. When encountering resistance to change, identify one positive aspect or potential benefit of the new approach and express gratitude for the opportunity to innovate. Embracing change fosters innovation and keeps the team adaptable and forward-thinking, driving continuous improvement and success.



<br>
### 4. REST: Take a Break

By incorporating periods of **rest and reflection,** you create a balanced routine that enhances productivity and overall quality of life. This structured approach allows you to maintain high levels of energy and concentration, preventing burnout and ensuring that you can consistently perform at your best. Embrace the art of doing nothing. Avoid overextending yourself by not doing more today than you can fully recover from by tomorrow. This approach promotes sustainable productivity and well-being.

<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-1474437915.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

By embracing the art of doing nothing and incorporating structured work sessions, rest periods, and balanced routines, IT and software engineering professionals can enhance their productivity and well-being. This approach promotes sustainable productivity, prevents burnout, and ensures that engineers can consistently perform at their best.

Here are a few examples that IT architects as an inspiration to help their organizations take a break:

* **Incorporating Rest and Reflection Periods:** Engineers frequently move from one task to another without taking time to reflect and rest, leading to mental fatigue. Scheduling short breaks after each focused session for rest and reflection can mitigate this. Activities such as walking, meditating, or simply quietly sitting can be beneficial. For instance, after each 90-minute session, a 15-minute walk outside or 10 minutes of meditation can help clear the mind. These regular breaks help maintain mental clarity and focus, enhancing overall productivity and well-being.

* **Balancing Workload and Recovery:** Taking on more work than one can recover overnight leads to cumulative fatigue and stress for engineers. Effectively managing the workload ensures daily tasks are balanced and realistic, avoiding overextension. Tools like task lists and time-blocking can help manage workload effectively. Prioritizing tasks and allocating time based on their complexity and importance while avoiding scheduling back-to-back high-intensity tasks ensures recovery and consistent performance, preventing long-term fatigue.

* **Creating a Balanced Routine with Leisure Activities:** Continuous work without leisure can drain motivation and creativity. Incorporating leisure activities into the daily routine provides a mental break and stimulates creativity. Dedicating time in the evening for hobbies, social activities, or simply relaxing with a book or movie can be refreshing. Balancing work with leisure activities promotes overall well-being and helps maintain motivation and creativity.


<br>
### 5. NOTICE: How to See Clearly

Too often, we are physically with people but **not mentally present.** We struggle to notice them and see them truly. Being fully present makes others feel like the most important person in the world, even for a brief moment. This experience of undivided attention has a magical power that can leave a lasting impact long after the moment has passed.

People often describe the feeling of being with someone who is fully present as if that person had moved mountains for them. The power of presence is not about grand gestures but about being **wholly attentive** and **engaged** in the moment. This profound presence can transform relationships and create meaningful connections that resonate deeply.

Harness the power of presence to achieve a state of heightened awareness. Train your brain to focus on what is essential and ignore the irrelevant. This practice improves your productivity and enriches your interactions with others.

Set aside your opinions, advice, and judgment to truly see others. Prioritize their truth above your own. Clear the clutter in your physical environment before tackling the clutter in your mind. This process of decluttering helps create a space conducive to presence and mindfulness.



<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-514368940.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

IT and software engineering professionals can achieve a state of heightened awareness, improving productivity and enriching their interactions with others. This approach fosters a work environment where presence and mindfulness lead to meaningful connections and effective collaboration.

Here are a few examples that IT architects as an inspiration to help their organizations see clearly:

* **Truly Seeing and Listening to Colleagues:** Meetings and discussions often involve multitasking, where participants check emails or think about other tasks, leading to ineffective communication. Active listening is essential to fully engaging with colleagues during meetings and one-on-one interactions. During a meeting, put away your phone and close unnecessary tabs on your computer. Make eye contact, listen actively, and acknowledge the speaker's points before responding. This engagement ensures that colleagues feel valued and heard, improving team dynamics and fostering a collaborative work environment.

* **Decluttering Physical and Digital Workspaces:** A cluttered workspace can lead to a cluttered mind, reducing efficiency and increasing stress. Clearing physical and digital clutter helps create an organized and focused work environment. An organized workspace reduces distractions, helping you maintain focus and clarity throughout the day.

* **Prioritizing Important Tasks Over Urgent Ones:** Engineers often get caught up in urgent but less important tasks, neglecting critical long-term projects. Using a prioritization matrix like the Eisenhower Matrix helps distinguish between important and urgent tasks. Categorize your tasks into four quadrants: urgent and important, important but not urgent, urgent but not important, and neither. Prioritize tasks in the "important but not urgent" quadrant. Focusing on essential tasks enhances long-term productivity and progress, preventing the constant firefighting of urgent but less impactful tasks.


<br>
## Effortless Action

When you reach an Effortless State, you can perform Effortless Actions. Effortless Action is the art of **accomplishing more by trying less.** It involves finding a natural flow in your tasks and responsibilities, allowing you to achieve your goals with minimal strain. The process begins with taking the first obvious step, which helps overcome procrastination and sets you in motion. By avoiding overthinking, you can focus on reaching completion without getting bogged down in unnecessary details, preventing mental fatigue and keeping you moving forward.

Progress in Effortless Action is made by **pacing yourself** rather than powering through. This sustainable approach ensures a steady momentum without the risk of burnout. Effortless Action allows you to exceed expectations without excessive effort, enabling you to overachieve while preserving your energy and well-being. Ultimately, it's about aligning your efforts with a natural rhythm, making work feel less like a struggle and more like a seamless part of your day.



<br>
### 6. DEFINE: What "Done" Looks Like

To begin an important project effectively, start by defining what "done" looks like. Establish **clear conditions for completion,** outlining specific criteria that indicate the project is finished. This clarity **helps you stay focused** and prevents **unnecessary overextension.** Once these conditions are met, stop and acknowledge your progress.

McKeown suggests some simple techniques that everyone can use daily to focus and have a stronger sense of establishment. Spend **sixty seconds focusing** on your desired outcome. **Visualize** what success looks like, and remember this image as you work. This brief period of concentration can align your efforts and provide a clear direction. Or create a **"Done for the Day"** list, limited to items that would constitute meaningful progress. This list should include achievable tasks that contribute significantly toward your overall goal. Focusing on these critical activities ensures that each day ends with a sense of accomplishment and forward momentum.

<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-1569348514.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

Similarly, by defining what "done" looks like, IT and software engineering professionals can stay focused on their goals, prevent overextension, and maintain a clear direction in their work. This approach fosters productivity, ensures high-quality outcomes, and provides a satisfying sense of accomplishment.

Here are a few examples that IT architects as an inspiration to help their organizations better define what "done" looks like:

* **Completing a Feature Development:** 
Developing a new feature for a software application can often lead to scope creep without clear boundaries. To address this, defining what constitutes "done" for the feature is essential, as well as specifying criteria such as passing all unit and integration tests, undergoing code review, and updating Documentation. By documenting these conditions—"Feature X is done when it passes all unit tests, integrates without errors, is reviewed by a peer, and is documented in the user manual"—the development team can stay focused, avoid unnecessary additions, and ensure timely completion.

* **Finishing a Bug Fix:** 
Bug fixes can create a cycle of finding new issues without a clear endpoint. To prevent this, determine the conditions under which the bug fix is complete. These conditions include reproducing the problem, implementing the fix, testing it in different environments, and updating the issue tracker. Document the steps required to complete the bug fix: "Bug Z is done when the issue is reproduced, fixed, tested in staging and production environments, and marked as resolved in the issue tracker." Explicit criteria for "done" help developers avoid endless bug-fixing cycles and ensure fixes are properly verified and documented.


* **Completing a Code Review:** 
Code reviews can drag on indefinitely without clear criteria for completion. To streamline this process, set clear criteria for a complete code review, such as checking for adherence to coding standards, verifying functionality, and ensuring no critical issues remain. Outline the steps: "The code review is done when the code adheres to our standards, all tests pass, and any identified issues have been addressed or noted for future improvement." Clear completion criteria make code reviews more efficient and ensure they add value without becoming a bottleneck.


<br>
### 7. START: The First Obvious Action

"Done" not only helps finish a project, but it also helps start it. Establishing clear conditions for completion and outlining specific criteria that indicate the project is finished enables you to stay focused, prevents unnecessary overextension, and provides a clear starting point. 

But "done" is not enough. People still get stuck because they do not know how to start. Make the **first action the most obvious one.** Break this initial action into the tiniest, most concrete step possible, and then name it. For example, if the project is to write a report, the first step could be as simple as "open a new document."

McKeown suggests some simple techniques to identify the first obvious action:
* Spend **sixty seconds focusing** on your desired outcome. Visualize what success looks like, and remember this image as you work. This brief period of concentration aligns your efforts and provides clear direction.
* Gain maximum learning from a minimal viable effort by starting with a **ten-minute microburst** of focused activity. This short, intense work period can boost motivation and energy, making diving deeper into the project more manageable. This approach helps you overcome the inertia of starting and builds momentum for continued progress.


<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-471660478.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

By breaking down the first action into the most apparent, tiny steps and visualizing the desired outcome, IT and software engineering professionals can effectively begin essential projects, build momentum, and ensure clear direction from the start. This approach reduces inertia and makes it easier to dive deeper into tasks confidently.

Here are a few examples that IT architects as an inspiration to help their organizations find first obvious actions:

* **Beginning a New Feature Development:** 
In developing a new feature for a software application, the feature is considered complete when it passes unit tests, is integrated into the main codebase, and is documented. The first obvious action is to create a new branch in the version control system. This action involves opening the version control tool (e.g., Git) and executing the command to create a new branch: `git checkout -b new-feature-branch`. This small, concrete action provides a clear starting point and sets up the environment for feature development.

* **Initiating a Bug Fix:** 
When fixing a critical bug in the software, the bug fix is considered complete when the issue is reproduced, fixed, tested, and verified in the staging environment. The first obvious action is to reproduce the bug in the development environment. This action involves identifying the conditions under which the bug occurs and replicating those conditions in your development setup. Successfully reproducing the bug provides a clear starting point for identifying the cause and developing a fix. 

* **Initiating a Documentation Task:** 
In updating the user manual with new feature details, the documentation update is complete when all new features are described with examples and integrated into the manual. The first obvious action is opening the text editor's documentation file. Locate the user manual file and open it using your preferred text editor (e.g., MS Word, Google Docs). Opening the document creates a starting point for adding new information.



<br>
### 8. SIMPLIFY: Start With Zero

To simplify the process of completing an essential project, don't focus on simplifying the steps; instead, remove unnecessary steps altogether. Recognize that not everything requires going the extra mile. Minimizing the actions you need to take will streamline your workflow and conserve energy. Maximize the steps not taken and measure progress in the smallest increments to ensure steady advancement.

This concept aligns with the "Swedish Death Cleaning philosophy," which involves decluttering your life by eliminating accumulated unnecessary items. Apply this principle to your project by removing redundant tasks and focusing only on what truly matters. This approach helps you maintain clarity and efficiency, ensuring that your efforts are directed toward meaningful progress without being bogged down by extraneous activities.


<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-665241484.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>


By applying the "Start With Zero" approach, IT and software engineering professionals can eliminate unnecessary steps, streamline workflows, and focus on what truly matters. This approach enhances productivity and ensures that efforts are directed toward meaningful progress, making projects more efficient and manageable.

Here are a few examples that IT architects as an inspiration to help their organizations start with zero:

* **Streamlining Feature Development:** 
In developing a new feature for a software application, the traditional approach typically involves extensive planning, multiple design iterations, and comprehensive testing phases. The simplified approach starts with zero by eliminating unnecessary steps like excessive design iterations and over-engineering. Implementation begins with writing a simple prototype or MVP (Minimum Viable Product) that includes only the core functionality, focusing on delivering the essential feature first. By removing unnecessary steps and focusing on the core functionality, the feature is developed more quickly and can be tested and iterated based on user feedback.

* **Reducing Meetings:** 
The traditional approach for a collaborative team project involves frequent status meetings, detailed progress reports, and extensive planning sessions. The simplified approach starts with zero by eliminating unnecessary meetings and excessive reporting. Frequent meetings are replaced with asynchronous updates using collaboration tools like Slack or Trello, and only essential meetings with clear agendas and time limits are held. Reducing unnecessary meetings frees up time for actual work, increasing productivity and maintaining focus on important tasks.

* **Optimizing Deployment Processes:** 
The traditional approach to deploying a new software application version involves multiple manual steps, extensive testing environments, and comprehensive deployment checklists. The simplified approach starts with zero by removing redundant manual steps and streamlining the process. The implementation uses Continuous Integration/Continuous Deployment (CI/CD) pipelines to automate the deployment process, ensuring automated tests are in place to catch issues early. Automating the deployment process reduces human error, speeds up releases, and provides consistent quality.



<br>
### 9. PROGRESS: The Courage to Be Rubbish

When beginning a project, it is crucial to adopt the mindset that it is perfectly acceptable to **start with less-than-perfect work.** Embracing a "zero-draft" approach, simply putting any words on the page, can be incredibly liberating. This technique effectively bypasses the paralysis often caused by perfectionism, allowing creativity to flow more freely. Accepting the idea of failing cheaply and making small and manageable mistakes early in the process accelerates learning and enhances decision-making skills over time.

Fred Brooks encapsulated this wisdom: *"Good judgment comes from experience, and experience comes from bad judgment."* This quote highlights the necessity of mistakes for achieving mastery. Initial drafts are not meant to be perfect. Courage to produce imperfect work is a vital component of growth. By starting messy and allowing for errors, a solid foundation for continuous improvement and eventual mastery is established.

<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-1276946528.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

By embracing the courage to be rubbish and starting with imperfect versions, IT and software engineering professionals can bypass perfectionism, accelerate learning, and create a foundation for continuous improvement and eventual mastery. This approach encourages experimentation and iteration, leading to better outcomes over time.

Here are a few examples that IT architects as an inspiration to help their organizations have the courage to create rubbish:

* **Starting a New Feature:** 
In developing a new feature for a software application, adopt the mindset that the first version might be rudimentary and full of flaws. Begin with zero-draft code, writing the initial version of the feature without worrying about perfection. Focus on getting a basic version that works, even if it's not optimized or clean. Start by coding the main functionality with simple logic, ignoring edge cases and optimizations for now. This "rubbish" version allows you to quickly identify the main challenges and requirements, setting a foundation for iterative improvements.


* **Initial Project Planning:** 
When planning a new software development project, accept that the first project plan will be incomplete and potentially unrealistic. Begin with a zero-draft plan, drafting a rough outline of the project timeline, key milestones, and resource allocations without striving for perfect accuracy. Create a simple Gantt chart or list of milestones using tools like Trello or a whiteboard. This initial plan provides a starting point for discussion and refinement, allowing the team to identify potential issues and adjust accordingly.

* **Learning a New Technology:** 
When learning a new programming language or framework, accept that your first attempts will be full of mistakes and inefficiencies. Begin with zero-draft learning, writing simple programs or small projects to get a feel for the syntax and features without worrying about best practices. Follow beginner tutorials and write code to replicate examples, making mistakes. These initial attempts build familiarity with the new technology and provide a foundation for more advanced learning and application.

<br>
### 10. PACE: Slow if Smooth, Smooth is Fast

Maintaining a deliberate and measured pace can achieve more meaningful and lasting results without exhausting yourself. This balanced approach allows you to work efficiently while preserving your well-being and maintaining a high output standard. 

To achieve sustained productivity, set an effortless pace: slow is smooth, smooth is fast. Reject the false economy of "powering through," which often leads to burnout and decreased efficiency. Instead, create a balanced approach to your work by defining a suitable range for your efforts: determine that you will never do less than X and never more than Y. This ensures a consistent, manageable workload that promotes steady progress. Recognize that not all progress is created equal. Focus on the quality and significance of your achievements rather than merely the quantity. 



<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-2038048731.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

By adopting a balanced approach and setting a sustainable pace, IT and software engineering professionals can maintain high productivity while ensuring quality and preserving their well-being. This method emphasizes the importance of consistent, manageable efforts that lead to meaningful and lasting results.

Here are a few examples that IT architects as an inspiration to help their organizations set an effortless pace:

* **Learning a New Technology:** 
When learning a new programming language or framework, the traditional approach might involve intensive, uninterrupted study sessions that lead to quick burnout and poor retention. A balanced approach involves studying for 30 minutes and no more than 2 hours per day. Integrate learning into daily routines with consistent, shorter study sessions, allowing time for reflection and practice. Steady, consistent learning leads to better understanding and retention of new skills.

* **Managing Code Development:** 
The traditional approach to developing a complex feature for a software application often involves powering through long hours of coding without breaks, leading to burnout and errors. A balanced approach involves determining that you will code for no less than 4 hours and 6 hours a day, with breaks in between. Implement this by scheduling coding sessions with regular short breaks. This steady pace prevents burnout, reduces mistakes, and ensures high-quality code over time.

* **Debugging and Testing:** 
The traditional approach to debugging and testing a new feature often involves marathon sessions that lead to frustration and oversight. A balanced approach allocates no less than 1 hour and 3 hours daily for debugging and testing. Approach debugging methodically with regular breaks to reassess and strategize. This measured pace allows for more effective problem-solving and thorough testing, leading to more robust software.




<br>
## Effortless Results

Effortless Results are the natural outcome of consistently cultivating your Effortless State and taking Effortless Action. By maintaining a clear objective, breaking tasks into tiny, obvious first steps, and working at a consistent, manageable pace, you achieve your desired outcomes with greater ease. However, the true power of Effortless Results lies in their sustainability.

Effortless Results are those that continue to flow to you repeatedly, with minimal additional effort. You've established a system where success becomes a cycle rather than a one-time event. By refining your process and eliminating unnecessary steps, you ensure that your efforts yield ongoing benefits. This approach allows you to maintain high productivity and achieve your goals consistently, creating a seamless and continuous flow of accomplishments.

In essence, Effortless Results are about creating a self-sustaining loop of success. By leveraging the principles of the Effortless State and Effortless Action, you set the stage for ongoing achievement, making it possible to reach your objectives repeatedly without constant exertion.




<br>
### 11. LEARN: Leverage the Best of What Others Know

To achieve Effortless Results, McKeown argues, it is crucial to **stand on the shoulders of giants.** That is, to leverage the best of what experts and pioneers have discovered. Use their knowledge as a foundation to build upon, enabling you to achieve more with less effort. 

In addition, one must focus on **learning principles,** not just facts and methods. Understanding first principles allows you to apply them repeatedly across various contexts. You can quickly adapt and innovate by grounding yourself in these fundamental truths, making complex tasks more straightforward and manageable.

Effortless Results stem from a deep understanding of first principles and the ability to apply them creatively and consistently. By building on the knowledge of others and developing your unique insights, you create a sustainable pathway to continuous achievement and innovation.


<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-467625592.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>


By understanding and applying first principles, leveraging experts' knowledge, and building unique insights, IT and software engineering professionals can achieve effortless results. This approach fosters innovation and continuous improvement, ensuring that complex tasks become more manageable and maximize productive efforts.

Here are a few examples that IT architects as an inspiration to help their organizations leverage the best of what others know:

* **Applying Design Patterns in Software Development:** 
When developing a scalable and maintainable software application, start with the first principles by learning the fundamentals behind common design patterns such as Singleton, Factory, Observer, and MVC. Study books like "Design Patterns: Elements of Reusable Object-Oriented Software" by the Gang of Four. Apply these patterns appropriately in the software architecture to address scalability and maintainability issues. Leveraging well-established design patterns allows for efficiently building a robust and flexible application framework.

* **Innovating with New Technologies:** 
To integrate machine learning into an existing product, start with the first principles by understanding the basics of machine learning algorithms, data preprocessing, model training, and evaluation. Use open-source libraries like TensorFlow or PyTorch and build on existing models and research to implement the solution. Using foundational knowledge and the work of experts facilitates the seamless integration of advanced technologies, enhancing functionality with minimal effort.

* **Optimizing Database Performance:** 
To optimize the performance of a relational database, start with first principles by learning the fundamentals of database normalization, indexing, query optimization, and transaction management. Study best practices and methodologies from experts. Apply indexing strategies, optimize queries based on execution plans, and configure database settings according to expert recommendations. Achieving optimal database performance through a deep understanding of underlying principles and expert advice leads to faster and more efficient data handling.



<br>
### 12. LIFT: Harness the Strength of Ten

Teaching others is an accelerated way to learn. When you prepare to teach, you increase your engagement, focus more intently, listen to understand and think about the underlying logic so you can articulate the ideas in your own words. This process not only reinforces your own understanding but also enhances your ability to convey complex concepts.

Use teaching as a lever to harness the strength of ten, achieving a far-reaching impact by teaching and by teaching others to teach. You'll notice how much you learn when you live what you teach. You can disseminate knowledge effectively by telling stories that are easy to understand and repeat.

Ensuring your messages are easy to understand and hard to misunderstand is not just a communication strategy. It's a powerful tool for amplifying your impact. By simplifying and clarifying your communication, you make it easier for others to grasp and remember the knowledge you share, thereby increasing the reach and effectiveness of your message. This underscores the crucial role you play in knowledge sharing and the impact you can have on others.

One motivation for writing this book is to create reusable material that teaches others about pragmatic approaches to running architecture practices and give them material they can reuse to teach others the same.

<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-1049828098.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>


By teaching and teaching others to teach, IT and software engineering professionals can amplify their impact and foster a culture of continuous learning and improvement. This approach reinforces their knowledge and equips the team with the skills and understanding necessary for greater efficiency and innovation.

Here are a few examples that IT architects as an inspiration to help their organizations harness the strength of ten:

* **Promoting Continuous Integration/Continuous Deployment (CI/CD):** 
An engineer who has successfully implemented CI/CD pipelines in past projects runs workshops to teach the team how to set up and maintain CI/CD pipelines. Providing hands-on experience with popular tools like Jenkins, GitHub Actions, or GitLab CI, the engineer creates step-by-step tutorials and shares best practices. Using real examples from the current project to demonstrate the impact of CI/CD, the team learns to automate testing and deployment, leading to more reliable releases and a faster development cycle.

* **Enhancing Security Practices:** 
A security expert aims to improve the team’s approach to cybersecurity by conducting security training sessions to educate team members on best practices, common vulnerabilities, and mitigation strategies. Using simple, memorable stories to illustrate the importance of security, the expert provides checklists and templates for secure coding and threat modeling. The outcome is that team members become more security-conscious and capable of implementing robust security measures, reducing the risk of breaches.

* **Mentoring on Effective Documentation:** 
A developer who excels at creating clear, concise documentation holds workshops to teach the team how to write effective documentation. Sessions cover different types of documentation, such as API docs, user guides, and technical specs. By providing examples of well-written documentation and highlighting key elements that make it effective, the developer encourages team members to practice and peer-review each other’s work. Improved documentation quality across the team leads to better knowledge sharing and easier onboarding for new team members.



<br>
### 13. AUTOMATE: Do It Once and Never Again



Automating as many essential tasks as possible frees up space in your brain. This space allows you to focus your mental energy on more important matters. One effective way to ensure consistency and accuracy is using checklists, which help you get it right every time without relying on memory. Automation creates a more efficient and less cluttered mental environment, enabling you to perform at your best with minimal effort.


<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-1442064282.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>


By automating essential tasks and using checklists for routine processes, IT and software engineering professionals can streamline their workflows, reduce errors, and free up mental space for more important activities. This approach leads to increased efficiency, consistency, and overall productivity.

Here are a few examples that IT architects as an inspiration to help their organizations automate things:

* **Automating Code Quality Checks:** 
Ensuring code quality through manual reviews and testing can be time-consuming and inconsistent. The approach involves high-tech automation by integrating automated code quality tools like SonarQube or ESLint into your CI/CD pipeline. Configure the tools to run automated checks on every commit, providing immediate feedback on code quality issues. The outcome is consistent and automated code quality checks that improve overall code standards and reduce the need for manual reviews.


* **Standardizing Development Environments:** 
Setting up development environments manually for new team members or new projects can be time-consuming and error-prone. The approach involves high-tech automation by using containerization tools like Docker to create standardized development environments. Create Docker images that include all necessary tools, libraries, and configurations, and share them with the team. The outcome is that new environments can be set up quickly and consistently, reducing setup time and avoiding configuration issues.

* **Automating Data Management:** 
Managing and updating databases manually can be prone to errors and inconsistencies. The approach involves high-tech automation by implementing automated data management scripts using tools like Python or SQL scripts scheduled with cron jobs or similar scheduling tools. Write scripts to handle routine data management tasks such as backups, updates, and migrations. The outcome is automated data management that ensures data integrity and frees up time for more strategic tasks.


<br>
### 14. TRUST: The Engine of High-Leverage Teams

When trust exists in your relationships, they require less effort to maintain and manage. You can quickly and efficiently split work between team members. People feel comfortable discussing problems openly and honestly, sharing valuable information rather than hoarding it. This environment encourages team members to ask questions when they don't understand something. Consequently, the speed and quality of decisions improve, political infighting decreases, and you may even enjoy the experience of working together. This dynamic allows you to focus your energy and attention on getting important tasks done rather than on simply getting along.

Conversely, when trust is low, everything becomes difficult. Sending a simple text or email is exhausting as you weigh every word for how it might be perceived. Responses may induce anxiety, and every conversation feels like a grind. Without trust in someone's ability to deliver, you need to check up on them constantly, remind them of deadlines, hover over their work, or avoid delegating tasks altogether, believing it's easier to do it yourself. This lack of trust can cause work to stall and impede team performance.

Inside every team are individuals with interrelated roles and responsibilities, moving at high speeds. Without trust, conflicting goals, priorities, and agendas create friction and wear everyone down. Trust acts like engine oil, lubricating the team's interactions and keeping them working smoothly together. A team running out of trust will likely stall or sputter out.

Every relationship involves three parties, Person A and Person B, and the structure that governs them. When trust becomes an issue, most people point fingers at the other person, be it the manager blaming the employee or vice versa. However, every relationship has a structure, even if it's an unspoken and unclear one. Unclear expectations, incompatible or conflicting goals, ambiguous roles and rules, and misaligned priorities and incentives characterize a low-trust structure.

High-trust agreements help mitigate these issues by clarifying:
- **Results:** What results do we want?
- **Roles:** Who is doing what?
- **Rules:** What minimum viable standards must be kept?
- **Resources:** What resources (people, money, tools) are available and needed?
- **Rewards:** How will Progress be evaluated and rewarded?

Establishing clear expectations and structures creates a high-trust environment that enables teams to function efficiently and effectively.

Leverage trust as the essential lubricant of frictionless and high-functioning teams. Making the right hire once can produce results repeatedly. Follow the Three I's Rule: hire people with integrity, intelligence, and initiative. Design high-trust agreements to clarify results, roles, rules, resources, and rewards.

Being an architect is much easier in high-trust organizations. In low-trust organizations, people frequently expect architects to be police agents. IT governance processes frequently associated with architecture practice are used or misused to force bureaucratic controls as teams often do not trust each other. 


<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-1387451522.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

By establishing and maintaining a high-trust environment, IT and software engineering teams can work more efficiently and effectively. Trust reduces friction, enables better decision-making, and fosters a positive, collaborative culture where team members feel valued and empowered.

Here are a few examples that IT architects as an inspiration to help their organizations create a high-trust environment:

* **Making the Right Hire:** 
When hiring a new software engineer for a critical project, the approach involves following the Three I's Rule: focus on candidates with integrity, intelligence, and initiative. Design interview questions and assessments that evaluate these traits, such as scenario-based questions to gauge problem-solving skills and ethical dilemmas to assess integrity. The outcome is hiring the right candidate who increases team efficiency and reduces the need for constant oversight, as they can be trusted to deliver high-quality work independently.

* **Open Communication and Problem-Solving:** 
To address a critical bug in the software that could delay the release, encourage an environment where team members feel comfortable discussing problems openly. Regularly schedule team stand-ups and retrospectives where issues can be raised without fear of blame. Encourage a culture where questions are welcomed, and information is shared freely. The outcome is an effective collaboration among team members to identify and resolve the bug quickly, leveraging their collective knowledge and skills.

* **Delegating Tasks Efficiently:** 
When delegating a complex module development to a junior engineer, trust their capability to handle the task while providing guidance and support as needed. Communicate the task requirements and expected outcomes. Provide access to resources and be available for consultation, but allow the engineer autonomy to approach the problem. The result is that the junior engineer gains confidence and develops skills, while senior team members can focus on other critical tasks, improving overall team productivity.





<br>
### 15. PREVENT: Solve the Problem Before It Happens

Just as you can find small actions to make your life easier in the future, look for small actions that will prevent your life from becoming more complicated. Simple preventative measures (such as setting reminders, automating tasks, or creating checklists) can significantly reduce the likelihood of future problems. Focusing on these small, strategic actions ensures a smoother, more efficient path forward, allowing you to achieve more with less effort and stress.

Don’t just manage problems—solve them before they happen. Seek simple actions today that can prevent complications tomorrow. By investing a small amount of effort now, you can eliminate recurring frustrations and streamline your future.

This proactive approach is the long tail of time management. When you invest your time in actions with a long tail, you reap the benefits over a long period. For example, spending two minutes to organize your workspace can save you countless hours of searching for items in the future. Catch mistakes before they occur by adopting a measure-twice, cut-once mentality.



<br>
<img style="margin-top: -20px; width: 100%; " 
     src="assets/images/iStock-1441914456.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by iStock
</div>

IT and software engineering teams can solve potential problems before they occur, leading to smoother operations, fewer disruptions, and a more efficient workflow. This proactive approach saves time and resources, allowing teams to focus on innovation and continuous improvement.

Here are a few examples that IT architects as an inspiration to help their organizations prevent problems:

* **Regular Code Reviews:** 
Inconsistent code quality and frequent issues from unreviewed code changes necessitate preventative action by establishing a regular code review process. Make code reviews a mandatory part of the development workflow. Use pull request templates and review tools like GitHub or GitLab to ensure thorough reviews. The outcome is that regular code reviews maintain high code quality, catch potential issues early, and promote knowledge sharing among team members.

* **Setting Up Monitoring and Alerts:** 
Frequently discovering system outages or performance issues after they impact users requires preventative action by implementing monitoring and alerting systems. Use tools like Prometheus, Grafana, and New Relic to monitor system performance and uptime. Set up alerts to notify the team of any anomalies or performance degradation. The outcome is early detection of issues, allowing the team to address problems before they impact users, improving system reliability and user satisfaction.

* **Regular Security Audits:** 
Discovering security vulnerabilities after a breach, leading to significant downtime and data loss, requires preventative action by conducting regular security audits and implementing best practices. Schedule regular security audits using tools like OWASP ZAP and Nessus. Train the team on secure coding practices and conduct periodic security reviews. The outcome is that regular security audits and training reduce the risk of vulnerabilities, preventing potential breaches and ensuring data protection.




<br>
## The Road to Effortless Achievement

The path to achieving great results doesn’t have to be tortuous. Embracing the idea that things can be easy and even enjoyable opens you up to effortless solutions. By clearly defining your goal and identifying a small yet significant first step, you set yourself on a journey of effortless actions that lead to steady and meaningful progress.

When you leverage knowledge, automation, and trust, you create a system that produces recurring results. This system simplifies your life and enhances productivity, demonstrating that life doesn’t have to be as hard and complicated as we often make it. By adopting a mindset that prioritizes ease and enjoyment, you enable a more streamlined and fulfilling approach to achieving your goals.

<br>
## To Probe Further
* [Execution Management Matrix](https://obren.io/tools/matrix/?matrix=executionManagement)
* [The Eisenhower Matrix](https://obren.io/tools/matrix/?matrix=eisenhowerMatrix)


<br>
## Questions to Consider

* *How does the idea of achieving goals with minimal strain resonate with your personal work ethic and habits?*
* *What tasks could benefit from automation to enhance your productivity and reduce unnecessary effort?*
* *Have you experienced moments when you were physically rested, emotionally unburdened, and mentally energized? What facilitated these moments?*
* *What mental clutter currently hinders your productivity, and how can you clear it to foster an effortless state?*
* *How can you apply the concept of "make the change easy, then make the easy change" in your work?*
* *How can you combine essential tasks with pleasurable activities to enhance your productivity and well-being?*
* *What regrets, grudges, or unrealistic expectations are you holding onto that might be hindering your progress?*
* *How do you currently balance work and rest to prevent burnout and maintain high performance?*
* *What structured routines can you implement to incorporate rest and reflection periods into your workday?*
* *What steps can you take to declutter your physical and digital workspaces to improve focus and efficiency?*
* *What experts and pioneers in your field can you learn from to build on their knowledge and achieve more with less effort?*
* *How can you leverage teaching as a tool to reinforce your knowledge and multiply your impact?*
* *What complex concepts can you simplify and clarify to make them easier for others to understand and remember?*
* *What clear expectations and structures can you establish to create a high-trust agreement in your projects?*
* *How can you adopt a proactive approach to identify and solve potential problems before they occur?*