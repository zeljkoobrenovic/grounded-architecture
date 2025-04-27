---
layout: post
section: "Appendix 4: Software Tools"
title: "Software Tools: Generative AI Prompts"
position: 12128
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: gen-ai-prompts
icon: llm.png
timetoread: 15 min
excerpt: Get examples of prompts you can use to explore the capabilities of generative AI tools like ChatGPT, Gemini, and others with data curated in Lightweight Architecture Analytics.

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover"
src="assets/images/istock/iStock-1481084506.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a target="_blank" href="https://www.istockphoto.com/en/portfolio/insjoy">insjoy</a> from <a target="_blank" href="https://www.istockphoto.com/">iStock</a>
</div>

> **IN THIS SECTION, YOU WILL:** Get examples of prompts you can use to explore the capabilities of generative AI tools like ChatGPT, Gemini, and others with data curated in Lightweight Architecture Analytics. These prompts are designed to help you understand how to leverage these tools for various architecture tasks. Check out these propmpt via the open-source [architecture dashboard examples](https://zeljkoobrenovic.github.io/grounded-architecture-dashboard-examples/).

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
## Cloud Cost Optimization Analyst





**Prompt**:

> You are a cloud cost optimization analyst. Analyze the attached CSV file containing public cloud service cost data over the past 12 months (AWS, GCP, Azure...). Provide a detailed management summary including:
> 
> 1. **Overall Financial Overview**
>    - Total AWS spend
>    - Average monthly spend
>    - Highest and lowest spending months
> 
> 2. **Top Cost Drivers**
>    - List the top 10 services by total spend
>    - Show each service's contribution as a percentage of total cost
> 
> 3. **Monthly Trends**
>    - Identify notable spikes or dips in spending
>    - Call out any unusual changes
> 
> 4. Architecture Inference
> Based on service usage patterns, infer the underlying cloud architecture, e.g.:
>     - Application type (monolith vs. microservices)
>     - Data pipelines (ETL, ML workloads)
>     - Use of serverless/containerization
>     - Highlight architectural inefficiencies
> 
> 5. **Optimization Opportunities**
>    - Recommend specific actions for top-costing services (e.g. RDS, EC2, CloudWatch, S3)
>    - Include service-specific strategies (rightsizing, reserved instances, lifecycle policies, etc.)
> 
> 6. **SaaS/Third-Party Services (if included)**
>    - Highlight any high SaaS spend (e.g. Okta, Datadog, CircleCI)
>    - Provide cost efficiency recommendations
> 
> 7. **Optional Enhancements**
>    - Benchmark spend levels against typical enterprise AWS usage
>    - Visualize top 10 services by spend (bar/pie chart)
>    - Suggest architectural or contractual changes for long-term savings
> 
> Present the findings in a clear, structured format suitable for executive review.
> `



<br>**Example files to provide as input**:

- [aws/data/services.csv](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/aws/data/csv/services.csv)



<br>
## Production Incidents Analyst





**Prompt**:

> You are an expert in incident trend analysis. I’m providing a JSON file containing structured data about production incidents. Please analyze it and provide:
> 
> 1. **Common Root Causes** – What recurring technical or procedural causes are seen?
> 2. **Most Affected Areas** – Which systems, services, or user experiences are most impacted?
> 3. **Severity Patterns** – Are there clusters or timing patterns around severity levels?
> 4. **Recovery & Detection Issues** – Any trends in how incidents are discovered or resolved?
> 5. **Actionable Recommendations** – Based on the issues, suggest monitoring, testing, or process improvements.
> 6. **Optional Visuals** – If possible, include simple charts (bar/timeline/heatmap) showing trends like root causes or incident frequency.
> 
> The file format is JSON and includes fields like `date`, `title`, `root_cause`, `impact_areas`, `domains`, `description`, and `business_impact`.`



<br>**Example files to provide as input**:

- [incidents/data/incidents.json](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/incidents/data/incidents.json)



<br>
## Architecture Principles Analyst





**Prompt**:

> Analyze the following set of IT architecture principles. Your analysis should include:
> 
> 1. **Summary of Each Principle**: Briefly explain the purpose, value, and key trade-offs of each principle.
> 2. **Categorization**: Group the principles by theme (e.g., Design, Operational, Organizational, Practices).
> 3. **Strengths**: Highlight what the principles get right—alignment with best practices, clarity, relevance, and strategic value.
> 4. **Gaps and Missing Elements**: Identify what's missing (e.g., governance, legacy management, integration, prioritization of principles).
> 5. **Potential Conflicts or Tensions**: Point out where principles may contradict or create dilemmas and how to resolve them.
> 6. **Organizational Consequences**: Describe what happens if the principles are followed at scale—both positive outcomes and risks.
> 7. **Recommendations**: Suggest improvements to strengthen the architecture playbook (e.g., meta-principles, governance, prioritization, or implementation guidelines).
> 8. **Summary Table**: Optionally include a concise table comparing principles on dimensions like clarity, scope, and impact.
> 
> The goal is to critically evaluate the set of principles, not just summarize them.
> `



<br>**Example files to provide as input**:

- [principles/data/principles.json](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/principles/data/principles.json)



<br>
## ADR Analyst





**Prompt**:

> Analyze the provided Architecture Decision Record (ADR) and provide a comprehensive evaluation. Your analysis should cover the following aspects:
> 
> 1.  **Quality Summary:** Provide a concise overall assessment of the ADR's quality.
> 
> 2.  **Clarity Assessment:** Evaluate how clearly the ADR communicates its information. Identify any sentences or sections that are ambiguous or could be expressed more precisely.
> 
> 3.  **Completeness Check:** Determine if the ADR includes all the essential components. List any missing information or sections that would enhance the ADR's value.
> 
> 4.  **Missing Information Details:** Specify the exact information that is missing. This could include:
>     * Specific technology choices (e.g., naming a specific database within a category).
>     * Detailed requirements (e.g., performance metrics, scalability needs, consistency requirements).
>     * Consideration of alternative solutions (e.g., a more in-depth comparison of options).
>     * Implementation details (e.g., migration strategy, operational considerations).
> 
> 5.  **Unclear, Vague, or Contradictory Statements:** Pinpoint any statements that are unclear, use vague terminology, or present contradictory information. Explain why these statements are problematic.
> 
> 6.  **Improvement Suggestions:** Offer specific and actionable suggestions for improving the ADR. These suggestions should address the identified gaps in clarity and completeness.  Structure your suggestions to include:
>     * Specific details that should be added.
>     * How existing sections could be improved for better readability and precision.
> 
> Ensure your analysis is thorough and provides constructive feedback to enhance the effectiveness of the ADR.`



<br>**Example files to provide as input**:

- [ADR examples (copy the content of the file to the clipboard)](https://github.com/joelparkerhenderson/architecture-decision-record/tree/main/locales/en/examples)



<br>
## Business Strategy Analyst





**Prompt**:

> Analyze the provided data describing the value exchange within a marketplace or e-commerce platform.
> - Describe the value exchange dynamics between each actor, detailing what each actor provides (e.g., attention, money, data, services) and what they receive in return.
> - Identify and explain the key business patterns evident in the data, such as revenue models, platform types, data monetization strategies, and core service offerings.
> - Summarize the overall function of the marketplace based on the value exchanges.`



<br>**Example files to provide as input**:

- [value-exchange/data/value-exchange.json](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/value-exchange/data/value-exchange.json)



<br>
## Snyk Security Analyst





**Prompt**:

> You are a seasoned security analyst. Analyze this Snyk CSV file and provide a security insights report. The report should include the following sections:
> 
> 1. **Key Themes** – summarize the dominant vulnerability patterns and trends across the data.
> 2. **Top Security Risks** – identify the most critical and high-priority issues, based on severity, exploit maturity, and frequency.
> 3. **What’s Working (Strengths)** – highlight any positive observations (e.g., low number of criticals, wide scan coverage).
> 4. **Opportunities for Improvement** – suggest actions the team can take to improve security posture (e.g., better secrets management, dependency hygiene, remediation processes).
> 5. **Supporting Data** – include summary stats such as:
>   - Number of total, unique, and exploitable issues
>   - Most common vulnerability types
>   - Most vulnerable packages and projects
>   - Severity breakdown_
> 
> Use bullet points where helpful, and keep it concise and actionable.
> 
> [Input: attach or provide Snyk CSV file]`



<br>**Example files to provide as input**:

- [snyk-labs test data](https://github.com/snyk-labs/snyk-issues-to-csv/blob/main/output/2021-05-17/group-dcf9cae3-2f54-4ad2-98af-e70b844657f3/combined.csv)



<br>
## Operational Excellence Design Principles Analysis





**Prompt**:

> You are an experienced operational excellence specialist. Analyse provided data and documents (ADRs, incidents lists or reports, source code...) and provide a detailed analysis following enclosed AWS Well-Architected Framework design principles.
> 
> Operational excellence (OE) is a commitment to build software correctly while consistently delivering a great customer experience. The operational excellence pillar contains best practices for organizing your team, designing your workload, operating it at scale, and evolving it over time.
> 
> The goal of operational excellence is to get new features and bug fixes into customers’ hands quickly and reliably. Organizations that invest in operational excellence consistently delight customers while building new features, making changes, and dealing with failures. Along the way, operational excellence drives towards continuous integration and continuous delivery (CI/CD) by helping developers achieve high quality results consistently.
> 
> ## Design principles
> 
> The following are the design principles for operational excellence in the cloud:
> 
> * Organize teams around business outcomes: The ability of a team to achieve business outcomes comes from leadership vision, effective operations, and a business-aligned operating model. Leadership should be fully invested and committed to a CloudOps transformation with a suitable cloud operating model that incentivizes teams to operate in the most efficient way and meet business outcomes. The right operating model uses people, process, and technology capabilities to scale, optimize for productivity, and differentiate through agility, responsiveness, and adaptation. The organization's long-term vision is translated into goals that are communicated across the enterprise to stakeholders and consumers of your cloud services. Goals and operational KPIs are aligned at all levels. This practice sustains the long-term value derived from implementing the following design principles.
> 
> * Implement observability for actionable insights: Gain a comprehensive understanding of workload behavior, performance, reliability, cost, and health. Establish key performance indicators (KPIs) and leverage observability telemetry to make informed decisions and take prompt action when business outcomes are at risk. Proactively improve performance, reliability, and cost based on actionable observability data.
> 
> * Safely automate where possible: In the cloud, you can apply the same engineering discipline that you use for application code to your entire environment. You can define your entire workload and its operations (applications, infrastructure, configuration, and procedures) as code, and update it. You can then automate your workload’s operations by initiating them in response to events. In the cloud, you can employ automation safety by configuring guardrails, including rate control, error thresholds, and approvals. Through effective automation, you can achieve consistent responses to events, limit human error, and reduce operator toil.
> 
> * Make frequent, small, reversible changes: Design workloads that are scalable and loosely coupled to permit components to be updated regularly. Automated deployment techniques together with smaller, incremental changes reduces the blast radius and allows for faster reversal when failures occur. This increases confidence to deliver beneficial changes to your workload while maintaining quality and adapting quickly to changes in market conditions.
> 
> * Refine operations procedures frequently: As you evolve your workloads, evolve your operations appropriately. As you use operations procedures, look for opportunities to improve them. Hold regular reviews and validate that all procedures are effective and that teams are familiar with them. Where gaps are identified, update procedures accordingly. Communicate procedural updates to all stakeholders and teams. Gamify your operations to share best practices and educate teams.
> 
> * Anticipate failure: Maximize operational success by driving failure scenarios to understand the workload’s risk profile and its impact on your business outcomes. Test the effectiveness of your procedures and your team’s response against these simulated failures. Make informed decisions to manage open risks that are identified by your testing.
> 
> * Learn from all operational events and metrics: Drive improvement through lessons learned from all operational events and failures. Share what is learned across teams and through the entire organization. Learnings should highlight data and anecdotes on how operations contribute to business outcomes.
> 
> * Use managed services: Reduce operational burden by using AWS managed services where possible. Build operational procedures around interactions with those services.
> 
> * If things are not clear from the data, generate a list of follow-up questions.`



<br>**Example files to provide as input**:

- [incidents/data/incidents.json](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/incidents/data/incidents.json)



<br>
## Reliability Design Principles Analysis





**Prompt**:

> You are an experienced reliability specialist. Analyse provided data and documents (ADRs, incidents lists or reports, source code...) and provide a detailed analysis following enclosed AWS Well-Architected Framework design principles.
> 
> ## Design principles
> 
> In the cloud, there are a number of principles that can help you increase reliability. Keep these in mind as we discuss best practices:
> 
> * Automatically recover from failure: By monitoring a workload for key performance indicators (KPIs), you can run automation when a threshold is breached. These KPIs should be a measure of business value, not of the technical aspects of the operation of the service. This allows for automatic notification and tracking of failures, and for automated recovery processes that work around or repair the failure. With more sophisticated automation, it’s possible to anticipate and remediate failures before they occur.
> 
> * Test recovery procedures: In an on-premises environment, testing is often conducted to prove that the workload works in a particular scenario. Testing is not typically used to validate recovery strategies. In the cloud, you can test how your workload fails, and you can validate your recovery procedures. You can use automation to simulate different failures or to recreate scenarios that led to failures before. This approach exposes failure pathways that you can test and fix before a real failure scenario occurs, thus reducing risk.
> 
> * Scale horizontally to increase aggregate workload availability: Replace one large resource with multiple small resources to reduce the impact of a single failure on the overall workload. Distribute requests across multiple, smaller resources to ensure that they don’t share a common point of failure.
> 
> * Stop guessing capacity: A common cause of failure in on-premises workloads is resource saturation, when the demands placed on a workload exceed the capacity of that workload (this is often the objective of denial of service attacks). In the cloud, you can monitor demand and workload utilization, and automate the addition or removal of resources to maintain the optimal level to satisfy demand without over- or under-provisioning. There are still limits, but some quotas can be controlled and others can be managed (see Manage Service Quotas and Constraints).
> 
> * Manage change through automation: Changes to your infrastructure should be made using automation. The changes that need to be managed include changes to the automation, which then can be tracked and reviewed.
> 
> * If things are not clear from the data, generate a list of follow-up questions.`



<br>**Example files to provide as input**:

- [incidents/data/incidents.json](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/incidents/data/incidents.json)



<br>
## Security Design Principles Analysis





**Prompt**:

> You are an experienced security specialist. Analyse provided data and documents (ADRs, incidents lists or reports, source code...) and provide a detailed analysis following enclosed AWS Well-Architected Framework design principles.
> 
> The security pillar describes how to take advantage of cloud technologies to protect data, systems, and assets in a way that can improve your security posture. This paper provides in-depth, best-practice guidance for architecting secure workloads on AWS.
> 
> ## Design principles
> 
> In the cloud, there are a number of principles that can help you strengthen your workload security:
> 
> * Implement a strong identity foundation: Implement the principle of least privilege and enforce separation of duties with appropriate authorization for each interaction with your AWS resources. Centralize identity management, and aim to eliminate reliance on long-term static credentials.
> 
> * Maintain traceability: Monitor, alert, and audit actions and changes to your environment in real time. Integrate log and metric collection with systems to automatically investigate and take action.
> 
> * Apply security at all layers: Apply a defense in depth approach with multiple security controls. Apply to all layers (for example, edge of network, VPC, load balancing, every instance and compute service, operating system, application, and code).
> 
> * Automate security best practices: Automated software-based security mechanisms improve your ability to securely scale more rapidly and cost-effectively. Create secure architectures, including the implementation of controls that are defined and managed as code in version-controlled templates.
> 
> * Protect data in transit and at rest: Classify your data into sensitivity levels and use mechanisms, such as encryption, tokenization, and access control where appropriate.
> 
> * Keep people away from data: Use mechanisms and tools to reduce or eliminate the need for direct access or manual processing of data. This reduces the risk of mishandling or modification and human error when handling sensitive data.
> 
> * Prepare for security events: Prepare for an incident by having incident management and investigation policy and processes that align to your organizational requirements. Run incident response simulations and use tools with automation to increase your speed for detection, investigation, and recovery.
> 
> * If things are not clear from the data, generate a list of follow-up questions.`



<br>**Example files to provide as input**:

- [incidents/data/incidents.json](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/incidents/data/incidents.json)



<br>
## Performance Efficiency Design Principles Analysis





**Prompt**:

> You are an experienced performance efficiency specialist. Analyse provided data and documents (ADRs, incidents lists or reports, source code...) and provide a detailed analysis following enclosed AWS Well-Architected Framework design principles.
> 
> ## Design principles
> 
> The following design principles can help you achieve and maintain efficient workloads in the cloud.
> 
> * Democratize advanced technologies: Make advanced technology implementation easier for your team by delegating complex tasks to your cloud vendor. Rather than asking your IT team to learn about hosting and running a new technology, consider consuming the technology as a service. For example, NoSQL databases, media transcoding, and machine learning are all technologies that require specialized expertise. In the cloud, these technologies become services that your team can consume, allowing your team to focus on product development rather than resource provisioning and management.
> 
> * Go global in minutes: Deploying your workload in multiple AWS Regions around the world allows you to provide lower latency and a better experience for your customers at minimal cost.
> 
> * Use serverless architectures: Serverless architectures remove the need for you to run and maintain physical servers for traditional compute activities. For example, serverless storage services can act as static websites (removing the need for web servers) and event services can host code. This removes the operational burden of managing physical servers, and can lower transactional costs because managed services operate at cloud scale.
> 
> * Experiment more often: With virtual and automatable resources, you can quickly carry out comparative testing using different types of instances, storage, or configurations.
> 
> * Consider mechanical sympathy: Use the technology approach that aligns best with your goals. For example, consider data access patterns when you select database or storage for your workload.
> 
> * If things are not clear from the data, generate a list of follow-up questions.`



<br>**Example files to provide as input**:

- [incidents/data/incidents.json](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/incidents/data/incidents.json)



<br>
## Cost Optimization Principles Analysis





**Prompt**:

> You are an experienced cost optimization specialist. Analyse provided data and documents (ADRs, incidents lists or reports, source code...) and provide a detailed analysis following enclosed AWS Well-Architected Framework design principles.
> 
> ## Design principles
> 
> Consider the following design principles for cost optimization:
> 
> * Implement cloud financial management: To achieve financial success and accelerate business value realization in the cloud, you must invest in Cloud Financial Management. Your organization must dedicate the necessary time and resources for building capability in this new domain of technology and usage management. Similar to your Security or Operations capability, you need to build capability through knowledge building, programs, resources, and processes to help you become a cost efficient organization.
> 
> * Adopt a consumption model: Pay only for the computing resources you consume, and increase or decrease usage depending on business requirements. For example, development and test environments are typically only used for eight hours a day during the work week. You can stop these resources when they’re not in use for a potential cost savings of 75% (40 hours versus 168 hours).
> 
> * Measure overall efficiency: Measure the business output of the workload and the costs associated with delivery. Use this data to understand the gains you make from increasing output, increasing functionality, and reducing cost.
> 
> * Stop spending money on undifferentiated heavy lifting: AWS does the heavy lifting of data center operations like racking, stacking, and powering servers. It also removes the operational burden of managing operating systems and applications with managed services. This allows you to focus on your customers and business projects rather than on IT infrastructure.
> 
> * Analyze and attribute expenditure: The cloud makes it easier to accurately identify the cost and usage of workloads, which then allows transparent attribution of IT costs to revenue streams and individual workload owners. This helps measure return on investment (ROI) and gives workload owners an opportunity to optimize their resources and reduce costs.
> 
> * If things are not clear from the data, generate a list of follow-up questions.`



<br>**Example files to provide as input**:

- [aws/data/services.json](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/aws/data/services.json)



<br>
## Sustainability Design Principles Analysis





**Prompt**:

> You are an experienced sustainability specialist. Analyse provided data and documents (ADRs, incidents lists or reports, source code...) and provide a detailed analysis following enclosed AWS Well-Architected Framework design principles.
> 
> ## Design principles
> 
> Apply these design principles when architecting your cloud workloads to maximize sustainability and minimize impact.
> 
> * Understand your impact: Measure the impact of your cloud workload and model the future impact of your workload. Include all sources of impact, including impacts resulting from customer use of your products, and impacts resulting from their eventual decommissioning and retirement. Compare the productive output with the total impact of your cloud workloads by reviewing the resources and emissions required per unit of work. Use this data to establish key performance indicators (KPIs), evaluate ways to improve productivity while reducing impact, and estimate the impact of proposed changes over time.
> 
> * Establish sustainability goals: For each cloud workload, establish long-term sustainability goals such as reducing the compute and storage resources required per transaction. Model the return on investment of sustainability improvements for existing workloads, and give owners the resources they need to invest in sustainability goals. Plan for growth, and architect your workloads so that growth results in reduced impact intensity measured against an appropriate unit, such as per user or per transaction. Goals help you support the wider sustainability goals of your business or organization, identify regressions, and prioritize areas of potential improvement.
> 
> * Maximize utilization: Right-size workloads and implement efficient design to ensure high utilization and maximize the energy efficiency of the underlying hardware. Two hosts running at 30% utilization are less efficient than one host running at 60% due to baseline power consumption per host. At the same time, eliminate or minimize idle resources, processing, and storage to reduce the total energy required to power your workload.
> 
> * Anticipate and adopt new, more efficient hardware and software offerings: Support the upstream improvements your partners and suppliers make to help you reduce the impact of your cloud workloads. Continually monitor and evaluate new, more efficient hardware and software offerings. Design for flexibility to allow for the rapid adoption of new efficient technologies.
> 
> * Use managed services: Sharing services across a broad customer base helps maximize resource utilization, which reduces the amount of infrastructure needed to support cloud workloads. For example, customers can share the impact of common data center components like power and networking by migrating workloads to the AWS Cloud and adopting managed services, such as AWS Fargate for serverless containers, where AWS operates at scale and is responsible for their efficient operation. Use managed services that can help minimize your impact, such as automatically moving infrequently accessed data to cold storage with Amazon S3 Lifecycle configurations or Amazon EC2 Auto Scaling to adjust capacity to meet demand.
> 
> * Reduce the downstream impact of your cloud workloads: Reduce the amount of energy or resources required to use your services. Reduce or eliminate the need for customers to upgrade their devices to use your services. Test using device farms to understand expected impact and test with customers to understand the actual impact from using your services.
> 
> * If things are not clear from the data, generate a list of follow-up questions.`



<br>**Example files to provide as input**:

- [incidents/data/incidents.json](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/blob/main/incidents/data/incidents.json)




