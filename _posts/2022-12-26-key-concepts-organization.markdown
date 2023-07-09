---
layout: post
section: "Appendices"
title: "High-Performing Organizations"
position: 12126
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: concepts-org
icon: productivity_tools.png
timetoread: 15 min
excerpt: Tools I've built and use in daily architectural work.

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover"
src="assets/images/arch/car-engine-1701029_1280.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/paulbr75-2938186/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1701029">Paul Brennan</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1701029">Pixabay</a>
</div>
<style>
    h1 {
        font-size: 210%;
    }
</style>

> **IN THIS SECTION, YOU WILL:** Get an overview of several tools I've built and use in daily architectural work.


## Metrics
* **Lead time for changes:** Elite performers have a lead time for changes of less than 1 hour (from code committed to code successfully running in production).
* **Deployment frequency:** Elite performers have a deployment frequency of multiple times per day.
* **Time to restore service:** Elite performers have an mean time to recover (MTTR) that is less than 1 hour.
* **Change failure rate:** Elite performers have a change failure rate between 0-15%.

## Continuous Delivery
* **Use version control for all production artifacts:** For all production artifacts, including application code, application configurations, system configurations, and scripts for automating build and configuration of the environment.
* **Automate your deployment process:** The degree to which deployments are fully automated and do not require manual intervention.
* **Implement continuous integration:** Code is regularly checked in, and each check-in triggers a set of quick test to discover serious regressions, which developers fix immediately.
* **Use trunk-based development methods:** Fewer than three active branches; branches and forks having very short lifetimes (e.g. less than a day); teams rarely or never having "code lock" periods.
* **Implement test automation:** Software tests are run automatically (not manually) continuously through the development process.
* **Support test data management:** Test data requires careful maintenance, and test data management is becoming an increasingly important part of automated testing.
* **Shift left on security:** Integrating security into the design and testing phases of the software development process is key to driving IT performance.
* **Implement continuous delivery (CD):** Software is in a deployable state throughout its lifecycle, and the team prioritize keeping the software in a deployable state over working on new features.

## Architecture
* **Use a loosely coupled architecture:** The extent to which a team can test and deploy their applications on demand, without requiring orchestration with other services.
* **Architect for empowered teams:** Teams that can choose which tools to use do better as continuous delivery, and, in turn, drive better software development and delivery performance.

## Product and Process
* **Gather and implement customer feedback:** Actively and regularly seek customer feedback and incorporate this feedback into the design of products.
* **Make the flow of work visible through the value stream:** Teams should have a good understanding of and visibility into the flow from the business all the way through to customers, including the status of products and features.
* **Working in small batches:** Teams should slice work into small pieces that can be completed in a week or less.
* **Foster and enable team experimentation:** Team experimentation is the ability of developers to try out new ideas and create and update specifications during the development process, without requiring approval from outside of the team, which allows them to innovate quickly and create value.


## Lean Management and Monitoring Capabilities
* **Have a lightweight change approval process:** A lightweight change approval process based on peer review (pair programming or intrateam code review) produces superior IT performance than using external change approval boards (CABs).
* **Monitor across application and infrastructure to inform business decisions:** Use data from application and infrastructure monitoring tools to take action and make business decisions. This goes beyond paging people when things go wrong.
* **Check system health proactively:** Monitor system health, using threshold and rate-of-change warnings, to enable teams to preemptively detect and mitigate problems.
* **Improve process and manage work with work-in-progress (WIP) limits:** The use of work-in-progress limits to manage the flow of work is well known in the Lean community. When used effectively, this drives process improvement, increases throughput, and makes constraints visible in the system.
* **Visualize work to monitor quality and communicate throughout the team:** Visual displays, such as dashboards or internal websites, used to monitor quality and work in progress have been shown to contribute to software delivery performance.

## Culture
* **Support a generative culture (as outlined by Westrum):** Hallmarks of this measure include good information sharing, high cooperation and trust, bridging between teams, and conscious inquiry.
* **Encourage and support learning:** Is learning, in your culture, considered essential for continued progress? Is learning thought of as a cost or an investment?
* **Support and facilitate collaboration among teams:** Reflects how well teams, which have traditionally been siloed, interact in development, operations, and information security.
* **Provide resources and tools that make work meaningful:** This particular measure of job satisfaction is about doing work that is challenging and meaningful, and being empowered to exercise your skills and judgment.
* **Support or embody transformational leadership:** Compromised of five factors: vision, intellectual stimulation, inspirational communication, supportive leadership, and personal recognition.