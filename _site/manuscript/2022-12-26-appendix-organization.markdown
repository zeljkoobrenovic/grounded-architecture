

# High Performing Technology Organizations {#concepts-org}

![](assets/images/arch/car-engine-1701029_1280.jpg)
^image by paul brennan from pixabay^

**IN THIS SECTION, YOU WILL:** Get a summary of characteristics of high-performing technology organizations.

{pagebreak}

## Overview 

Characteristics of High Performing Organizations from the [Accelerate book](https://www.oreilly.com/library/view/accelerate/9781457191435/) by Nicole Forsgren, Jez Humble, and Gene Kim are excellent sources of empirical knowledge about high-performing IT organizations.

I summarized several critical insights from this book:

* Overview of **four key metrics**, describing metrics that provide suitable measures of organization performance. 
* Overview of critical practices of high-performing technology organizations grouped into the following categories: Continuous Delivery, Architecture, Product and Process,  Lean Management and Monitoring Capabilities, Culture

## Four Key Metrics
* **Lead time for changes:** Elite performers have a lead time for changes of less than 1 hour (from code committed to code successfully running in production).
* **Deployment frequency:** Elite performers have a deployment frequency of multiple times daily.
* **Time to restore service:** Elite performers have a mean time to recover (MTTR) of less than 1 hour.
* **Change failure rate:** Elite performers have a 0-15% change failure rate.

## Practices

### Continuous Delivery
* **Use version control for all production artifacts:** For all production artifacts, including application code, application configurations, system configurations, and scripts for automating the build and configuration of the environment.
* **Automate your deployment process:** The degree to which deployments are fully automated and do not require manual intervention.
* **Implement continuous integration:** Code is regularly checked in, and each check-in triggers a set of quick tests to discover serious regressions, which developers fix immediately.
* **Use trunk-based development methods:** Fewer than three active branches; branches and forks having very short lifetimes (e.g., less than a day); teams rarely or never having "code lock" periods.
* **Implement test automation:** Software tests are run automatically (not manually) continuously through the development process.
* **Support test data management:** Test data requires careful maintenance, and test data management is becoming an increasingly important part of automated testing.
* **Shift left on security:** Integrating security into the design and testing phases of the software development process is vital to driving IT performance.
* **Implement continuous delivery (CD):** Software is in a deployable state throughout its lifecycle, and the team prioritizes keeping the software in a deployable state over working on new features.

### Architecture
* **Use a loosely coupled architecture:** The extent to which a team can test and deploy their applications on demand without requiring orchestration with other services.
* **Architect for empowered teams:** Teams that can choose which tools to use do better as continuous delivery and, in turn, drive better software development and delivery performance.

### Product and Process
* **Gather and implement customer feedback:** Actively and regularly seek customer feedback and incorporate this feedback into the design of products.
* **Make the flow of work visible through the value stream:** Teams should have a good understanding of and visibility into the flow from the business to customers, including the status of products and features.
* **Working in small batches:** Teams should slice work into small pieces that can be completed in a week or less.
* **Foster and enable team experimentation:** Team experimentation is the ability of developers to try out new ideas and create and update specifications during the development process without requiring approval from outside of the team, which allows them to innovate quickly and create value.

### Lean Management and Monitoring Capabilities
* **Have a lightweight change approval process:** A lightweight change approval process based on peer review (pair programming or intrateam code review) produces superior IT performance than using external change approval boards (CABs).
* **Monitor across applications and infrastructure to inform business decisions:** Use data from application and infrastructure monitoring tools to take action and make business decisions. This monitoring goes beyond paging people when things go wrong.
* **Check system health proactively:** Monitor system health using threshold and rate-of-change warnings to enable teams to detect and mitigate problems preemptively.
* **Improve process and manage work with work-in-progress (WIP) limits:** The use of work-in-progress limits to manage work flow is well known in the Lean community. When used effectively, this drives process improvement increases throughput, and makes constraints visible in the system.
* **Visualize work to monitor quality and communicate throughout the team:** Visual displays, such as dashboards or internal websites, used to monitor quality and work in progress have contributed to software delivery performance.

### Culture
* **Support a generative culture (as outlined by Westrum):** Hallmarks of this measure include good information sharing, high cooperation, and trust, bridging between teams, and conscious inquiry.
* **Encourage and support learning:** Is learning, in your culture, considered essential for continued progress? Is learning thought of as a cost or an investment?
* **Support and facilitate collaboration among teams:** Reflects how well traditionally siloed teams interact in development, operations, and information security.
* **Provide resources and tools that make work meaningful:** This particular measure of job satisfaction is about doing challenging and meaningful work and being empowered to exercise your skills and judgment.
* **Support or embody transformational leadership:** Compromised of five factors: vision, intellectual stimulation, inspirational communication, supportive leadership, and personal recognition.
