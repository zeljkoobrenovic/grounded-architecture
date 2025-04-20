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




