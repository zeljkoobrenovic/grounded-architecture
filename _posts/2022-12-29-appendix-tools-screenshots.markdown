---
layout: post
section: "Appendix 5: Software Tools"
title: "Software Tools: Examples and Screenshots"
position: 12129
podcast: screenshots.mp3
spotify: https://open.spotify.com/episode/3tND5tAxmykSEfy1qBvcWI?si=a542fae45de54786
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: screenshots
icon: examples.png
timetoread: 15 min
excerpt: Screenshots of concrete tools I built as a part of Lightweight Architectural Analytics websites.


---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover"
src="assets/images/sokrates_screenshot.png">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
A screenshot of a Sokrates report 
</div>

> **IN THIS SECTION, YOU WILL:** See a few screenshots of concrete tools I built as a part of Lightweight Architectural Analytics websites.

<style>
    .book {
        min-width: 100px;
        width: 100px;
    }
    .icon {
        min-width: 30px;
        width: 30px;
    }

    .icon-container {
    
    }

    @media only screen and (max-width: 768px) {
        [class="icon-container"] {
            display: none;
        }
    }
</style>

<br>
<br>
## Dashboards

Here are the screenshots from Lightweight Architectural Analytics websites I built in AVIV Group (Figure 1) and eBay Classifieds (Figure 2):

<br>
<img src="assets/images/apps.png" style="padding: 4px; padding-top: 8px; padding-bottom: 8px; box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px; margin-bottom: 6px">
<br>
 
**Figure 1:** *A screenshot of the start page of the architecture data dashboard we've built and used at AVIV Group.*


<br>
<img src="assets/images/apps-ebay.png" style="padding: 4px; padding-top: 8px; padding-bottom: 8px; box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px; margin-bottom: 6px">
<br>
 
**Figure 2:** *A screenshot of the start page of the architecture data dashboard we've built and used at eBay Classifieds.*
`
<br>
<br>
<br>
## Examples of Insights From Source Code Analyses

The source code and its commit history are like a treasure chest for creating data-driven architecture documentation—packed with nuggets of wisdom about technology, team activities, dependencies, and software quality. To help dig up this treasure without getting your hands too dirty, I've developed and actively maintain a project called [Sokrates](https://sokrates.dev).

Sokrates is designed with an architect's x-ray vision, allowing you to zoom in and out of source code landscapes. It provides a high-level overview of the IT landscape, summarizing data from various teams and groups, while also letting you dive deep into the code-level details. This dual functionality makes it the perfect sidekick for both CTO-level strategy powwows and developer-level code critiques.

Figures 3 to 7 show some insights from source code analyses with Sokrates. 

<br>
<br>
![](assets/images/archdata/src_1.png)

**Figure 3**: *Sokrates can instantly create a helicopter view of the technology landscape, programming languages, active contributors, and commit trends.*
<br>
<br>

<br>
<br>
![](assets/images/archdata/src_2.png)

**Figure 4**: *Sokrates can show detailed code and contributors' trends per repository, enabling zooming in each repository up to the code level.*
<br>
<br>
<br>
 
<br>
![](assets/images/archdata/src_5.png)

**Figure 5**: *Sokrates can create a tech radar by tagging projects with identified technologies.*
<br>
<br>
<br>

<br>
![](assets/images/archdata/src_3.png)

**Figure 6**: *Sokrates can show contributor trends, distribution of "veterans" and "rookies," and dependencies between people and repositories, enabling zooming in into patterns of the contribution of individual contributors.*
<br>
<br>
<br>
 
<br>
![](assets/images/arch/sokrates_teams.png)

**Figure 7**: *Sokrates can reveal the team topologies by plotting 2D and 3D graphs of dependencies that people create through working on the same repositories in the same period.*
<br>
<br>

<br>
![](assets/images/figures/kpis.png)

**Figure 8**: *Example Architecture Practice keyt performance indicators (KPIs) dashboard (generated from a JSON configuration file).*
<br>
<br>