---
layout: post
title: "Architecture Data Platform (ADP)"
position: 3000
date:   2021-10-21 21:12:01 +0100
categories: architecture
author: by Željko Obrenović (obren.io)
permalink: data-platform
icon: curation.png
timetoread: 15 min
excerpt: This article summarizes my experiences in replacing classical architectural documentation with data-driven documents.


---
![](assets/images/640px-Instrument_Cluster,_Mercedes-Benz_S350_Bluetec_4Matic_(US)_-_Flickr_-_skinnylawyer.jpeg)

![](assets/images/model-data-platform.png)

## The Problem

> "I am a mapmaker and a traveler." Brené Brown

In this article, I present some of my lessons learned in solving the problem of getting a complete, up-to-date picture of critical elements of technology landscapes of big organizations. I mean organizations with hundreds or thousands of developers organized in dozens or hundreds of teams by big organizations. Manual documentation does not scale in such an organizational context. 

But, more often than not, big organizations have lots of data that, if used wisely, can provide an excellent basis for architectural documentation. With some automation, and curation, getting a good overview of the technology landscape may be closer than it initially appears.   

![](assets/images/archdata/recipe.png)
<br>
**Figure 1:** *The recipe for data-driven documents: data + automation + curation = useful documentation.*

The main inspiration for my work is mapmaking (see [Atlas of the Heart](https://brenebrown.com/book/atlas-of-the-heart/) for a discussion on a mapmaking metaphor). As noted by Brené Brown, maps are the one of the most important documents in human history. They give us tools to store and exchange knowledge about space and place. While there are differences between maps and layers they show, the one thing that all maps do is provide readers with orientation. A sense of place is central to meaning-making. Maps are also composed from multiple layers. Similalry, the data-driven documents provide layers of data about our systems, describing their size, connections, quality, security, or human activity.


## Using Data-Driven Documents

Data-driven documents can provide lots of data. Sometimes, as in an ordinary map or atlas, such data could directly be helpful for those who want to orient themselves and understand the context. More insights could be obtained from such data. However, it requires active effort to find ways to interpret and use data. In other words, the documents can give you the answers, but [we may not know the questions](https://en.wikipedia.org/wiki/42_(number)#The_Hitchhiker's_Guide_to_the_Galaxy). Here are some of the questions I frequently ask and answers with data from the documents:
* Are we going in the same direction? Tools such as source code overviews, public cloud usage explorers, or tech radars can point out differences and trigger discussions.
* Are we using technology optimally? Comparing usage trends between teams can show interesting outliners (both positive and negative).
* Are there indicators of poor code quality? Too big systems, duplication, long units, long files.
* Productivity: is more more or is more less. For instance, comparing the number of git merges with the number of developers can indicate if our dev processes are scalable. When we scale up teams, we want to speed up our delivery (but if team structure is not right, it can easily be the opposite as people "step on each other toes").
* Do we collaborate in the way we want? Repository analysis can point out team topologies and (un)desired dependencies.
* Do we work on the things we want? We may want to focus more on innovations, but in reality, we may spend too much time on legacy maintenance.


## Summary

This article summarized my experiences in replacing classical architectural documentation with curated data-driven architecture documents. I presented some of my lessons learned in solving the problem of getting a complete, up-to-date picture of critical elements of technology landscapes of big organizations. Data-driven documents generate multiple views on relevant architectural topics based on data sources such as source code, commit history, public cloud billing reports, and finance reports.

To summarize, the data-driven documents offer an efficient, scalable, and pragmatic way to keep a complete overview of the organizational technology landscape. But as with many tools, they are not the panacea. They need to be a part of processes and activities to impact the organization positively. 

I consider the data and transparency, together with architects, to be two main pillars of any technology governance (Figure 6). Data and transparency provide a basis for data-informed decision-making. People and communities enable governance to have an impact ([read more about this pillar in another post](../superglue)). Without these two strong pillars, the architecture becomes an abstract ivory tower exercise.

![](assets/images/archdata/transparency.png)
<br>
***Figure 6:** IT architecture relies on two pillars: transparency and community. Data and transparency provide a basis for data-informed decision-making. People enable governance to have an impact. Without these two strong pillars, the architecture becomes an abstract ivory tower exercise. This article focuses on transparency.*



<br>
#### [Cover Art]

[Instrument Cluster, Mercedes-Benz S350](https://commons.wikimedia.org/wiki/File:Instrument_Cluster,_Mercedes-Benz_S350_Bluetec_4Matic_(US)_-_Flickr_-_skinnylawyer.jpg). Credit: skinnylawyer / Wikimedia Commons. 
