---
layout: post
title: "The Data Pillar"
section: "Grounded Architecture"
position: 3000
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: data-pillar
icon: curation.png
timetoread: 15 min
excerpt: The architecture data pillar serves as a medium to create a complete, up-to-date picture of critical elements of technology landscapes of big organizations. The platform provides an architecture-centric view on data about our technology landscape based on source code analyse, public cloud billing reports, vibrancy reports, or incident tickets.


---
<img src="assets/images/arch/architecture-1857175_1920.jpg" 
style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/3844328-3844328/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1857175">Lorenzo Cafaro</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1857175">Pixabay</a>
</div>

In every place I worked on creating any architectural functions, I put a strong emphasis on data. In past several years, I was also working on creating open-source tools, such as [Sokrates](https://sokrates.dev), that can help obtaining useful architectural insights from data sources, such as source code repositories, or public cloud usage. Consequently, I as one of the first steps I make in any architecure role is to create an architecture data pillar serves as a medium to create a complete, up-to-date picture of critical elements of technology landscapes of an organization. Manual documentation does not scale in [our context](context), and relying on data ensure reliability and scalability. 

![](assets/images/model-data.png)

Good news is that big organizations have lots of data that, if used wisely, can provide an excellent basis for an architectural data pillar. With some automation, and curation, getting a good overview of the technology landscape may be closer than it initially appears.

![](assets/images/archdata/recipe.png)
<br>
**Figure 1:** *The recipe for architecture data pillar: data + automation + curation = useful documentation.*

## Examples of Data Sources and Tools

I've always aimed to get reliable data about technology with as much as possible automation in my current positions (see Figure 2 for illustrations). Some examples of tools I built and used include:
* Source code contains an incredible amount of information about technology, people activity, team dependencies, and the quality of software systems.
* Public cloud usage reposts (e.g., billing reports), providing overview and trends on which team uses which services, regions, budgets.
* Incident reports, looking at trends and dependencies among incidents.
* Key business metrics, like vibrancy.
* Slack activity to understand team interactions.

In the following sections, I give more details on several of these architecture data pillar.

![](assets/images/apps.png)
<br>
**Figure 2:** *Examples of data-driven architecture documents I've built currently use.*

### Example 1: Source Code and Commit History As A Source of Data

I have repeatably found the source code to be an incredible source for creating data-driven architecture documentation. Source code and commit history include an astonishing amount of information about technology, people activity, team dependencies, and the quality of software systems. I've started and still actively maintain the project [Sokrates](https://sokrates.dev), with the idea to help further extract data from source code that can help my work as an architect. Figure 3 shows some of the insights from source code generated with Sokrates. I use these tools daily, improving them on the way.

In addition to standard source code and commit history analyses (see [Apache Software Foundation Sokrates analysis](https://www.sokrates.dev/) for examples), I also have built several special source code analysis to get further details:
* Travis and Jenkins files analyzers to understand how teams build CI/CD pipelines.
* Dockerfile scan to create a tech radar of runtime technologies.
* GitHub API pull requests analyses to identify deployment frequency.


![](assets/images/archdata/src_1.png)
![](assets/images/archdata/src_2.png)
![](assets/images/archdata/src_3.png)
<br>
***Figure 3:**Examples of insights from source code generated with my open-source project [Sokrates](https://sokrates.dev).*


### Example 2: Public Cloud Usage

Migrating to the cloud can dramatically increase transparency thanks to uniform automation and monitoring. Classic IT often has limited transparency in its operational environments. Simple questions like how many servers we provisioned, which applications run on them are often tricky and time-consuming to answer.

Figure 4 shows the anonymous screenshot of the Cloud usage explorer, a tool I built to visualize automatically-collected data about the Google Cloud Platform (GCP) usage.

![](assets/images/archdata/cloud-usage-explorer.png)
<br>
***Figure 4:** An example of an cloud usage explorer.*

Google, AWS, Azure, and other Public Cloud Providers give detailed data about which platform uses which services, resource family, budget. You can also understand which people and teams have access to each service. It is possible to get real-time information about our cloud usages and understand the trends in a fully automated fashion.

### Example 3: Financial and Vibrancy Data

Finance departments are very data-driven and have high-quality data that could be very relevant for architects. In addition to standard costs, budgets, and other pure financial data types, I frequently found that finance teams also have different data sources such as vibrancy or usage levels. These teams need such data to, for instance, correlate finance performance with usage levels. Such usage data are beneficial for architecture discussions. For example, linking usage levels and vibrancy of systems with their public cloud usage can identify areas of improvement and inefficiencies.

## Principles Behind Architecture Data Pillar

In general, the main driving principle behind my vision on architecture data pillar is "reducing subjectivity by use of data and insights." I follow several guiding principles (Figure 5).

![](assets/images/archdata/principles.png)
<br>
**Figure 5:** *Design principles behind architecture data pillar.*

Firstly, my goal is to move architectural discussion as far as possible from opinion battles to the domain of data-informed decision-making. Opinions have their value, but we do not need to debate which cloud resources or programming languages we use. We have reliable data for it.

Second, automation is the key to keeping documentation up to date and getting the data repeatable and reliable. While some manual actions may be required, most architecture data pillar I created automatically updated daily or weekly.

Third, I build the apps as self-service web applications to enable people to get any data themselves, rather than scheduling meetings and workshops to get and align the data. Whenever I created some of these apps, my schedule became more relaxed.

Fourth, documents must be as complete as possible, based on high-quality and curated data sets. On a scale of big organizations, a sample of data, e.g., cloud usage of one team, may not be representative and is practically useless and misleading.

Fifth, my goal is to use architecture data pillar to make architecture function an economic-risk modeling exercise. We should look at data to understand the current situation and create models to simulate scenarios. In this way, I want to make architecture less heroics, in the sense that architects jump in the last moment to prevent disasters based on their internal knowledge and insight. That heroic typically means that we have not looked at the data on time.

Six, I always build architecture data pillar as explorative applications, enabling filtering of data and zooming in and out of details. Different stakeholders have different needs, and the one-fits-all model cannot help everyone. Having exploration abilities enables a broader set of stakeholders to get relevant insights. For example, source code analyses can point our some CTO-level insights, such as programming languages trends and inter-team collaborations. At the same time, these tools enable individual developers to zoom into details of their systems and, for instance, get refactoring recommendations and code samples of complex or duplicated code.

> “Excessive complexity is nature's punishment for organizations that are unable to make decisions.” - Gregor Hohpe

Lastly, curation, the act of selecting, organizing, and looking after the data, is the crucial ingredient of the process to prevent creating useless, too detailed views. Curation means choosing what to include and exclude, ensuring data correctness and completeness, and engaging users to make documents helpful. Instead of carelessly bringing together all data we can find, we can add much more value by carefully choosing data and thoughtfully organizing documents. For example, source code analysis can automatically scan all repositories. Curation can increase the value of these analyses by grouping or tagging repositories to create sub-views, e.g., per technology or domain.





## Using Architecture Data Pillar

Architecture data pillar can provide lots of data. Sometimes, as in an ordinary map or atlas, such data could directly be helpful for those who want to orient themselves and understand the context. More insights could be obtained from such data. However, it requires active effort to find ways to interpret and use data. In other words, the documents can give you the answers, but [we may not know the questions](https://en.wikipedia.org/wiki/42_(number)#The_Hitchhiker's_Guide_to_the_Galaxy). Here are some of the questions I frequently ask and answers with data from the documents:
* Are we going in the same direction? Tools such as source code overviews, public cloud usage explorers, or tech radars can point out differences and trigger discussions.
* Are we using technology optimally? Comparing usage trends between teams can show interesting outliners (both positive and negative).
* Are there indicators of poor code quality? Too big systems, duplication, long units, long files.
* Productivity: is more more or is more less. For instance, comparing the number of git merges with the number of developers can indicate if our dev processes are scalable. When we scale up teams, we want to speed up our delivery (but if team structure is not right, it can easily be the opposite as people "step on each other toes").
* Do we collaborate in the way we want? Repository analysis can point out team topologies and (un)desired dependencies.
* Do we work on the things we want? We may want to focus more on innovations, but in reality, we may spend too much time on legacy maintenance.



## How To Build Architecture Data Pillar?

While each organization will need it own approach and unique sets of data that you can use, here are some tips I found useful in my approach to form the architecture data platform:

* Start with the source code. My motto is "Talk is expensive. Show me the code." I scan as soon as possible all source code using tools as [Sokrates](https://sokrates.dev). I highly recommend [Sokrates](https://sokrates.dev) as the basis for the data platform, but other simples analyses could also provide good starting point. Modern IT enterprises store almost everything as a code. It is the richest and most up-to-date documentation on most things happening in an IT enterprise.
* Connect with finance and governance teams to get exports of their data. Cloud billing reports, and data about vibrancy or revenue streams are collected anyway. By extracting more technology oriented data connecting (e.g., public cloud technology usage trends) and connecting them to other data, many new insights may be obtained without starting any new processes or asking people to provide more details. First leverage what you have, squeez all the value from it, then ask people for any missing elements.
* Use simple and easy to maintain infrastructures. For example, I publish results of Sokrates analyses and other simple data Web apps as static resources in our enterprise GithHub pages. Configuring more complex infrastructure swith complex databases, and backend software resuires more maintenance.
* Maintain the culture of transparency. It is much simpler an more effecting to share less data with everyone, than to have more data but with a complex authorization.
* Own the curation. People need to be able to trust your data. Spend enough time to understand data sets, curate them, and ensure presentation consistency. I consider myself to be a master curator and chief UX designer of a data platform.
* Build maps, not control units. The main inspiration for my work is map-making. As noted by Brené Brown, maps are the one of the most important documents in human history (see [Atlas of the Heart](https://brenebrown.com/book/atlas-of-the-heart/) for a discussion on a mapmaking metaphor). They give us tools to store and exchange knowledge about space and place. While there are differences between maps and layers they show, the one thing that all maps do is provide readers with orientation. A sense of place is central to meaning-making. Maps are also composed from multiple layers. Similalry, the architecture data pillar provides layers of data about our systems, describing their size, connections, quality, security, or human activity.

While I do not want to prescribe the best technology, I can tell what I use in daily work. I build most architecture data pillar as single-page web applications, taking data from JSON files hosted on a static web server. I usually use the latest version of Angular and the Material framework in my current work, hosting the app and data via GitHub pages.

See some of [my public tools](https://obren.io/tools) to illustrate how I build such simple web apps.
