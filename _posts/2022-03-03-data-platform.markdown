---
layout: post
title: "Data Pillar"
section: "Structure"
position: 3004
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: data-platform
icon: curation.png
timetoread: 15 min
excerpt: The architecture data pillar serves as a medium to create a complete, up-to-date picture of critical elements of technology landscapes of big organizations. The platform provides an architecture-centric view on data about our technology landscape based on source code analyses, public cloud billing reports, vibrancy reports, or incident tickets.


---
<img src="assets/images/arch/architecture-1857175_1920.jpg" 
style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/3844328-3844328/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1857175">Lorenzo Cafaro</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1857175">Pixabay</a>
</div>
> **KEY POINTS:**
>
> * The architecture data pillar serves as a medium to create a complete, up-to-date picture of critical elements of technology landscapes of big organizations. 
> * The data pillar provides an architecture-centric view on data about our technology landscape based on source code analyses, public cloud billing reports, vibrancy reports, or incident tickets.
> * I have been working on creating open-source tools, such as [Sokrates](https://sokrates.dev), that can help obtain valuable architectural insights from data sources, such as source code repositories.

In every place I worked on creating architectural functions, I strongly emphasized data. In the past several years, I have been working on creating open-source tools, such as [Sokrates](https://sokrates.dev), that can help obtain valuable architectural insights from data sources, such as source code repositories or public cloud billing reports. Consequently, one of the first steps I make in any architecture role is to create an architecture data pillar to get a complete, up-to-date picture of critical elements of the technology landscapes of an organization. Manual documentation does not scale in [our context](context), and relying on data ensures reliability and scalability. 

![](assets/images/model-data.png)

The good news is that big organizations have lots of data that, if used wisely, can provide an excellent basis for an architectural data pillar. With some automation and curation, getting a good overview of the technology landscape may be closer than it initially appears.

<br>
## Examples of Data Sources and Tools

I've always aimed to get reliable data about technology with as much as possible automation. Some examples of data I used include:
* Source code, which contains an incredible amount of information about technology, people's activity, team dependencies, and the quality of software systems.
* Public cloud billing reports, which provide an overview and trends on which projects use which services, in which regions, and on what budgets.
* Incident reports, which can reveal trends and dependencies among incidents.
* Key business metrics, like vibrancy, which can show user activity on our systems.
* Slack activity reports, which can help understand discussion topics and team interactions.

In the following sections, I detail several of these architectural data-driven tools.

<img src="assets/images/apps.png" style="padding: 4px; padding-top: 8px; padding-bottom: 8px; box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px; margin-bottom: 6px">
<br>
**Figure 1:** *A screenshot of the start page of the architecture data dashboard we've built and used at AVIV Group.*

<br>
### Source Code and Commit History

I have repeatably found the source code to be an incredible source for creating data-driven architecture documentation. Source code and its commit history include an astonishing amount of information about technology, people activity, team dependencies, and the quality of software systems. I've started and still actively maintain the project [Sokrates](https://sokrates.dev), with the idea to help further extract data from source code that can help my work as an architect. I use Sokrates daily, improving it on the way.

I've designed Sokrates from an architect's point of view, enabling quick zooming in and out into source code landscapes. On the one hand, Sokrates provides a high-level view of the landscape, summarizing data from all teams and groups. At the same time, you can zoom in on the details of particular systems, even to the code level. That means I could use the same tools to have CTO-level discussions looking at overall trends in our technology usage and costs. At the same time, I could engage with developers and discuss concrete code fragments and potential improvements in the code level (e.g., duplicated blocks, complex units, dependencies).

The Appendix at the end of this section shows some insights from source code analyses with Sokrates. For more complex examples of insights that Sokrates generates from source code, take a look at [Sokrates examples](https://www.sokrates.dev/), with analysis of complex open-source landscapes, such as:
* [**Apache Software Foundation Repositories**](https://d3axxy9bcycpv7.cloudfront.net/asf/_sokrates_landscape/index.html), with aggregated multi-level analysis of more than 1,000 repositories with more than 180 million lines of code, more than 22,000 historical contributors, and 2.4 million commits.
* [**Facebook/Meta OSS Repositories**](https://d3axxy9bcycpv7.cloudfront.net/meta/_sokrates_landscape/index.html), with aggregated multi-level analysis of around 800 repositories with 120 million lines of code, more than 20,000 historical contributors, and more than 2 million commits.
* [**Microsoft OSS Repositories**](https://d3axxy9bcycpv7.cloudfront.net/microsoft/_sokrates_landscape/index.html), with aggregated multi-level analysis of more than 2,400 repositories with more than 100 million lines of code, more than 18,000 historical contributors, and more than 1.2 million commits.
* [**Google OSS Repositories**](https://d3axxy9bcycpv7.cloudfront.net/google/_sokrates_landscape/index.html), with aggregated multi-level analysis of more than 1,600 repositories with more than 200 million lines of code, more than 27,000 historical contributors, and more than 2.4 million commits.
* [**Linux Source Code**](https://d3axxy9bcycpv7.cloudfront.net/asf/_sokrates_landscape/index.html), with aggregated multi-level analysis of 178 Linux repository sub-folders with more than 23 million lines of code, more than 17,000 historical contributors, and more than 1.7 million commits.
* [**Amazon OSS Repositories**](https://d3axxy9bcycpv7.cloudfront.net/amzn/_sokrates_landscape/index.html), with aggregated multi-level analysis of more than 2,700 repositories with more than 130 million lines of code, more than 13,000 historical contributors, and more than 600,000 commits.


In addition to standard source code and commit history analyses, I also have built several special source code analyses to get further details:
* Travis and Jenkins files analyzers to understand how teams build CI/CD pipelines.
* Dockerfile scan to create a tech radar of runtime technologies.
* GitHub API pull requests analyses to identify deployment frequency.

<br>
### Public Cloud Usage 

Migrating to the public cloud can dramatically increase transparency thanks to uniform automation and monitoring. The public cloud transparency offers an incredible amount of valuable data out-of-box.

Figure 1 shows the anonymous screenshot of the Cloud usage explorer, a tool I built to visualize automatically-collected data from standard Google Cloud Platform (GCP) usage reports.

![](assets/images/archdata/cloud-usage-explorer.png)
<br>
***Figure 1:** An example of a cloud usage explorer.*

[Amazon Web Services (AWS)](https://aws.amazon.com), [Google Cloud Platform (GCP)](https://cloud.google.com/), [Microsoft Azure](https://azure.microsoft.com/), and other Public Cloud Providers give detailed data about which platform uses which services, resource family, and budget. You can also understand which people and teams have access to each service. It is possible to get real-time information about our cloud usage and understand the trends fully automatically.

<br>
### Financial and Vibrancy Data

Finance departments are very data-driven and have high-quality data that could be relevant for architects. In addition to standard costs, budgets, and other pure financial data types, I frequently found that finance teams also have different data sources, such as vibrancy or usage levels. These teams need such data to, for instance, correlate finance performance with usage levels. Such usage data are beneficial for architecture discussions. For example, linking usage levels and vibrancy of systems with their public cloud usage can identify areas of improvement and inefficiencies.

<br>
<br>
## Principles Behind Architecture Data Pillar

My motto for the architecture data pillar is "**reducing subjectivity by use of data and insights**." More specifically, I follow several Reflections (Figure 2).

![](assets/images/archdata/principles.png)
<br>
**Figure 2:** *Design principles behind architecture data pillar.*

Firstly, I aim to move architectural discussion as far as possible from opinion battles to data-informed decision-making. Opinions are valuable, but we do not need to debate which cloud resources or programming languages we use. We have reliable data for it.

Second, automation is the key to keeping documentation up-to-date. While some manual actions may be required, most architecture data tools I created automatically updated all views daily or weekly.

Third, I build the apps as self-service web applications to enable people to get data rather than scheduling meetings and workshops to get and align the data. Whenever I created some of these apps, my schedule became more relaxed.

Fourth, documents must be complete and based on high-quality, curated data sets. On a scale of big organizations, a sample of data, e.g., cloud usage of several teams, may need to be more representative and can lead to wrong conclusions.

Fifth, I aim to use the architecture data tools to make architecture function an economic-risk modeling exercise. We should look at data to understand the current situation and create simulation models. In this way, I want to make architecture less heroic, replacing cold data architects jumping in at the last moment to prevent disasters based on their unique internal knowledge and insights. Such heroics typically means we have not looked at the data.

Six, I always build architecture data tools as explorative applications, enabling filtering of data and zooming in and out of details. Stakeholders have different needs, and the one-fits-all model can only help some. Having exploration abilities allows a broader set of stakeholders to get relevant insights. For example, source code analyses can highlight some CTO-level insights, such as trends in programming languages and inter-team collaborations. At the same time, these tools enable individual developers to zoom into the details of their systems and, for instance, get refactoring recommendations and code samples of complex or duplicated code.

Lastly, curation, the act of selecting, organizing, and looking after the data, is the crucial ingredient of the process to prevent creating useless, too-detailed views. Curation means choosing what to include and exclude, ensuring data correctness and completeness, and engaging users to make documents helpful. Instead of carelessly bringing together all data we can find, we can add much more value by carefully choosing data and thoughtfully organizing documents. For example, source code analysis can automatically scan all repositories. Curation can increase the value of these analyses by grouping or tagging repositories to create sub-views, e.g., per technology or domain.

The resulting winning formula for the architecture data tools is (Figure 3): data + automation + curation = useful data-driven documentation.

![](assets/images/archdata/recipe.png)
<br>
**Figure 3:** *The formula for architecture data pillar: data + automation + curation = useful data-driven documentation.*

<br>
## Using Architecture Data Pillar

The architecture data pillar can provide lots of data. Sometimes, as in an ordinary map or atlas, such data could be helpful for those who want to orient themselves and understand the context. But you could obtain more insights from such data. However, finding the right ways to interpret and use data requires active effort. In other words, the data can give you the answers, but [we may not know the questions](https://en.wikipedia.org/wiki/42_(number)#The_Hitchhiker's_Guide_to_the_Galaxy). Here are some of the questions I frequently ask and answers with data from the documents:
* Are we going in the same direction? Tools such as source code overviews, public cloud usage explorers, or tech radars can highlight differences and trigger discussions.
* Are we using technology optimally? Comparing usage trends between teams can show interesting outliners (both positive and negative).
* Are there indicators of poor code quality? Too big systems, duplication, long units, or long files.
* Productivity: is more really more or is more actually less. For instance, comparing the number of git merges with the number of developers can indicate if our dev processes are scalable. When we scale up teams, we want to speed up our delivery (but if team structure is not proper, it can easily be the opposite as people "step on each other toes").
* Do we collaborate in the way we want? Repository analysis can point out team topologies and (un)desired dependencies.
* Do we work on the things we want? We may want to focus more on innovations, but in reality, we may spend too much time on legacy maintenance.

<br>
## Building Data Pillar

While each organization will have its unique sets of data, here are some tips I found helpful in my approach to forming the architecture data pillar:

* **Start with the source code**. My motto is "Talk is expensive. Show me the code." I scan as soon as possible all source code using tools such as [Sokrates](https://sokrates.dev). I highly recommend [Sokrates](https://sokrates.dev) as the basis for the data pillar, but other simple analyses could also provide a good starting point. Modern IT enterprises store almost everything as a code. It is the richest and most up-to-date documentation on most things happening in an IT enterprise.
* **Connect with finance and governance teams** to get exports of their data (without sensitive parts, such as revenue projections). Cloud billing reports and data about vibrancy or revenue streams are collected anyway. By extracting more technology-oriented data (e.g., public cloud technology usage trends) and connecting them to other data, many new insights may be obtained without starting new processes or asking people to provide more details. First, leverage what you have, squeeze all the value from it, then ask people for any missing elements.
* **Use simple and easy-to-maintain infrastructures**. For example, I publish the results of Sokrates analyses and other simple data Web apps as static resources in our enterprise GithHub pages. Configuring more complex infrastructure with complex databases and backend software requires more maintenance.
* **Maintain a culture of transparency**. It is much simpler a more effective to share fewer data with everyone than to have more data, but complex authorization is needed.
* **Own the curation**. People need to be able to trust your data. Spend enough time to understand data sets, curate them, and ensure presentation consistency. I am a master curator and chief UX designer of a data pillar.
* **Build maps, not control units**. The main inspiration for my work is map-making. As noted by Brené Brown, maps are one of the most critical documents in human history (see [Atlas of the Heart](https://brenebrown.com/book/atlas-of-the-heart/) for a discussion on a mapmaking metaphor). They give us tools to store and exchange knowledge about space and place. While there are differences between maps and the layers they show, the one thing that all maps do is provide readers with orientation. A sense of place is central to meaning-making. Maps are also composed of multiple layers. Similarly, the architecture data pillar offers data layers about our systems, describing their size, connections, quality, security, or human activity.


![](assets/images/arch/eiffel-tower-construction-stages.webp)
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Credit: <a href="https://en.wikipedia.org/wiki/Eiffel_Tower">Wikipedia</a>
</div>


While I do not want to prescribe the best technology, I can tell what I use in daily work. I build most architecture data tools as simple web applications, taking data from JSON files hosted on a static web server. See some of [my public tools](https://obren.io/tools) to illustrate how I build such simple data-driven web apps.

<br>
## Appendix: Examples of Insights From Source Code Analyses with Sokrates

Figures 4 to 8 show some insights from source code analyses with Sokrates. 

<br>
![](assets/images/archdata/src_1.png)
**Figure 4**: *Sokrates can instantly create a helicopter view of the technology landscape, programming languages, active contributors, and commit trends.*
<br>
<br>

![](assets/images/archdata/src_2.png)
**Figure 5**: *Sokrates can show detailed code and contributors' trends per repository, enabling zooming in each repository up to the code level.*
<br>
<br>
 
![](assets/images/archdata/src_5.png)
**Figure 6**: *Sokrates can create a tech radar by tagging projects with identified technologies.*
<br>
<br>

![](assets/images/archdata/src_3.png)
**Figure 7**: *Sokrates can show contributor trends, distribution of "veterans" and "rookies," and dependencies between people and repositories, enabling zooming in into patterns of the contribution of individual contributors.*
<br>
<br>
 
![](assets/images/arch/sokrates_teams.png)
**Figure 8**: *Sokrates can reveal the team topologies by plotting 2D and 3D graphs of dependencies that people create through working on the same repositories in the same period.*
<br>
<br>
