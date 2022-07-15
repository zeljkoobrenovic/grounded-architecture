---
layout: post
section: "Lessons Learned"
title: "Lessons Learned: Data Pillar"
position: 8002
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: lessons-data-pillar
icon: building-data-platform.png
timetoread: 15 min
excerpt: While each organization has some unique sets of data that you can use, here are some tips I found useful in my approach to form the architecture data platform.


---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover" 
     src="assets/images/arch/building-1804030_1920.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/photomix-company-1546875/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1804030">Photo Mix</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1804030">Pixabay</a>
</div>

While each organization will need it own approach and unique sets of data that you can use, here are some tips I found useful in my approach to form the architecture data platform:

* Start with the source code. My motto is "Talk is expensive. Show me the code." I scan as soon as possible all source code using tools as [Sokrates](sokrates.dev). I highly recommend [Sokrates](sokrates.dev) as the basis for the data platform, but other simples analyses could also provide good starting point. Modern IT enterprises store almost everything as a code. It is the richest and most up-to-date documentation on most things happening in an IT enterprise.
* Connect with finance and governance teams to get exports of their data. Cloud billing reports, and data about vibrancy or revenue streams are collected anyway. By extracting more technology oriented data connecting (e.g., public cloud technology usage trends) and connecting them to other data, many new insights may be obtained without starting any new processes or asking people to provide more details. First leverage what you have, squeez all the value from it, then ask people for any missing elements.
* Use simple and easy to maintain infrastructures. For example, I publish results of Sokrates analyses and other simple data Web apps as static resources in our enterprise GithHub pages. Configuring more complex infrastructure swith complex databases, and backend software resuires more maintenance.
* Maintain the culture of transparency. It is much simpler an more effecting to share less data with everyone, than to have more data but with a complex authorization.
* Own the curation. People need to be able to trust your data. Spend enough time to understand data sets, curate them, and ensure presentation consistency. I consider myself to be a master curator and chief UX designer of a data platform.
* Build maps, not control units. The main inspiration for my work is map-making. As noted by Brené Brown, maps are the one of the most important documents in human history (see [Atlas of the Heart](https://brenebrown.com/book/atlas-of-the-heart/) for a discussion on a mapmaking metaphor). They give us tools to store and exchange knowledge about space and place. While there are differences between maps and layers they show, the one thing that all maps do is provide readers with orientation. A sense of place is central to meaning-making. Maps are also composed from multiple layers. Similalry, the architecture data pillar provides layers of data about our systems, describing their size, connections, quality, security, or human activity.

