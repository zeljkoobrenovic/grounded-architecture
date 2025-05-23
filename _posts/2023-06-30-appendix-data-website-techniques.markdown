---
layout: post
section: "Appendix 6: Software Tools"
title: "Building Lightweight Architectural Analytics"
position: 17130
podcast: data-website.mp3
spotify: https://open.spotify.com/episode/6XNKQ45ofTHJtA3VEzY5n0?si=4d5786a282b64923
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: data-website
icon: data-website.png
timetoread: 15 min
excerpt: A few practical tips on building lean architecture dashboards and documents (e.g., to create Lightweight Architectural Analytics) using simple, widely available tools.

---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover"
src="assets/images/education-6241609_1280.png">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/jozefm84-10215106/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=6241609">Jozef Mikulcik</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=6241609">Pixabay</a>
</div>
<style>
    h1 {
        font-size: 210%;
    }
</style>

> **IN THIS SECTION, YOU WILL:**Get a few practical tips on building lean architecture dashboards and documents (e.g., to create Lightweight Architectural Analytics) using simple, widely available tools.

<br>
While the lessons in this book are not limited to specific technologies and tools, I will share a few of my secrets for easily and affordably creating dashboards and documents that are crucial for data-informed decision-making.

Have you ever felt overwhelmed by the many specialized tools for creating architectural artifacts? Fear not! I'm here to show you that simplicity is often the key to brilliance. Imagine crafting high-quality documentation and stunning visualizations without complex software or extensive training. Not only is it possible, but it's also incredibly efficient.

In this guide, I'll explore the power of leveraging simple, lean tools that are widely available and easy to use. You don't need to be a tech wizard to create impressive [Lightweight Architectural Analytics](analytics) dashboards and architectural documents. I hope you will find these techniques refreshingly straightforward and efficient.

Here are two examples to illustrate the power of simplicity:

- I've developed several plain [HTML/CSS/DOM templates](https://zeljkoobrenovic.github.io/grounded-architecture-dashboard-examples/apps/docs/index.html) (with [open-source code](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples)) that I leverage in my daily work, and you can use for free yourself.
- [Sokrates.dev](https://sokrates.dev), a tool I developed, generates all reports in plain old HTML without any special libraries. Check out the example of the Apache Foundation [source code landscape](https://d3axxy9bcycpv7.cloudfront.net/asf/_sokrates_landscape/index.html).

These documents work on any browser, can be hosted on any simple HTTP server, and can be opened directly on any laptop or PC. They are also easy to maintain since no complex frameworks are used.

So, grab your digital toolkit and join us on this exciting journey. We'll harness the power of everyday tools to create extraordinary results. Get ready to transform your architectural documentation process and discover the magic of simplicity!

<br>
## Implementation Principles

When setting out on any journey, it's having a clear set of principles is vital to guide you. These principles are your trusty map and compass, ensuring you navigate the architectural landscape efficiently and effectively. Here are the fundamental principles that will keep you on track:

- **Leverage Existing Infrastructure**: Why reinvent the wheel when you can turbocharge what you already have? Utilizing existing infrastructure saves time and resources.
- **Maintainable by a Small Architecture Team**: Keep it simple! The architecture team normally does not have much time to polish self-created tools.
- **Broad Access Inside Organization**: Everyone should have a ticket to the show. Broad access ensures that all stakeholders can engage and contribute.

<br>
## Lean Implementation Techniques

Here are a few techniques I leverage in my work.

### Visualization With Plain Old HTML/CSS/DOM

Who says you need a high-tech toolbox to create dazzling visuals? Sometimes, sticking with the basics can yield the most elegant and practical results. Embrace the simplicity and power of plain old HTML, CSS, and the DOM.

Earlier, I always used heavyweight visualization and UI frameworks to build interactive tools. But nowadays, I leave the heavy frameworks at the door. You can create beautiful, functional interfaces with just the basics—no React, Angular, or Vue here – just pure, unadulterated HTML and CSS magic.

![](assets/images/data_site_simple_html.png)
***Figure 1:** Simple generated HTML visual of source code analysis results.*

<br>
### Embedding JSON in HTML Documents

Most of the documents I create are data-driven. This approach means that I generate visuals using templates based on structured data. For my tools, I primarily export data in JSON format and embed it into a copy of an HTML template. JSON is the lifeblood of these data-driven applications. I can dynamically display data by insode HTML documents. This method makes the documents more portable and ensures you can open and view them on various devices.

### Simple Proven HTML-Based 2D & 3D Visuals

Let's talk visuals. Here are some simple, proven methods I always use (you can find HTML templates of these visuals [here](https://github.com/zeljkoobrenovic/grounded-architecture-dashboard-examples/tree/main/template/templates/visuals)):

- **[Bar Charts](https://d3axxy9bcycpv7.cloudfront.net/asf/activemq/_sokrates_landscape/index.html)**: Classic and practical, perfect for showing comparisons.
- **[Graphviz](https://d3axxy9bcycpv7.cloudfront.net/asf/_sokrates_landscape/visuals/extension_dependencies_30d.svg)**: Ideal for easily creating complex graphs and diagrams.
- **[3D Node Graph](https://d3axxy9bcycpv7.cloudfront.net/asf/_sokrates_landscape/visuals/people_dependencies_including_repositories_30_2_force_3d.html)**: Add an extra dimension to your data visualization.
- **[Bubble Chart](https://d3axxy9bcycpv7.cloudfront.net/asf/_sokrates_landscape/visuals/bubble_chart_extensions_contributors_30d.html)**: Perfect for showing relationships between data points in a visually engaging way.
- **[Zoomable Circles](https://d3axxy9bcycpv7.cloudfront.net/asf/activemq/activemq/html/visuals/zoomable_circles_main.html) / [Sunbursts](https://d3axxy9bcycpv7.cloudfront.net/asf/activemq/activemq/html/visuals/zoomable_sunburst_main.html)**: Great for exploring hierarchical data with interactive zoom.
- **[Treemap](https://d3axxy9bcycpv7.cloudfront.net/asf/_sokrates_landscape/visuals/tree_map_extensions_contributors_30d.html)**: Perfect for visualizing nested data structures in a compact form.

### Icon Libraries

Icons are the unsung heroes of data visualization. They add clarity and visual appeal and help communicate concepts quickly. Explore websites like thenounproject.com (my favorite) for a treasure trove of icons to enhance your visualizations.

![](assets/images/data_site_icons.png)
***Figure 2:** A screenshot from thenounproject.com.*

<br>
## Version Controlled Lean Documents

I generate documents that are small, lean, and capable of being version-controlled, along with the data used to generate them.

### Small and Lean Documents

The documents must be compact, ensuring they do not consume excessive storage space and are suitable for large projects. They are efficient, containing only essential information without unnecessary bloat, which makes them easy to read, understand, and manage.

### Version Controlled

I manage these documents using a version control system (VCS) like Git. This system tracks changes over time and allows users to revert to previous versions if needed. It also enables multiple users to work on the same documents simultaneously, providing a clear history of changes, which improves collaboration and reduces conflicting edits.

### Together with Data

I also store data used to generate the documents alongside the documents. This approach ensures that the documents and data are always in sync. The approach allows for reproducing any document version precisely as it was at any point in time, maintaining integrity and reliability.

### Lean Hosting Techniques

When it comes to hosting static HTML documents, two simple yet crucial requirements are essential:

1. **Open Documents on Your Laptop**: You can easily open your documents directly on your laptop without needing to install any servers or special frameworks. This ensures accessibility anytime, anywhere—no setup required!

2. **Share Across the Organization**: Use any simple HTTP server (like GitHub Pages) for straightforward sharing. There is no complex setup; it is just pure, effortless sharing.

Keeping things simple keeps your documents accessible, easy to share, and maintainable. No advanced technical knowledge or elaborate configurations are necessary. So, create your documents, open them anywhere, and share them effortlessly!

### Benefits

Lean documents are efficient to generate, easy to store, and fast to process. They provide detailed traceability, enhancing transparency and accountability through a comprehensive history of changes. Consistency is maintained as the context and basis for documents are always available, preventing inconsistencies and errors. Multiple users can efficiently collaborate with clear mechanisms to resolve conflicts and track contributions.

By ensuring all generated documents are small, lean, and version-controlled along with their data, the system maximizes efficiency, consistency, and collaboration while maintaining high traceability and reproducibility.


<br>
## Collaborative Editing via Google Sheets

To facilitate collaborative editing of data that requires manual changes, I frequently relied on Google Sheets to provide a controlled collaborative editor to a broader audience. By leveraging Google Sheets, multiple users can simultaneously access, edit, and update data in real-time, ensuring that everyone works with the most current information. 


![A simple runtime architecture leveraging GitHub pages and Google Sheets.](assets/images/data_site_actors.png)
***Figure 3:** A collaborative editing model.*

I embedded a JavaScript script within the Google Sheet to further streamline this process. This script's primary function was to export the data into a JSON format, which you can use to generate visual documents using HTML templates.

![](assets/images/data_site_sheet_json.png)
***Figure 4:** Exporting Google Sheet data to JSON for document generation.*

<br>
## Two Examples Deployments

In my recent experiences, I have utilized the following two examples to create a dynamic ecosystem of collaborative, data-driven dashboards.

**Simple Setup with GitHub Pages and Google Sheets:** Start with a straightforward setup using GitHub Pages for hosting and Google Sheets for data management. This combination is powerful, easy to maintain, and highly accessible. The open-source example is available at [the Grounded Architecture resources site](https://zeljkoobrenovic.github.io/grounded-architecture-dashboard-examples/apps/docs/index.html) 

![A simple runtime architecture leveraging GitHub pages and Google Sheets.](assets/images/data_site_simple_arch_1.png)
***Figure 5:** A simple runtime architecture leveraging GitHub pages and Google Sheets.*

**Simple Setup with GitHub Pages and Google Sheets:** Start with a straightforward setup using GitHub Pages for hosting and Google Sheets for data management. This combination is powerful, easy to maintain, and highly accessible. The open-source example is available at 

![Slightly more flexible runtime architecture leveraging CDNs, internal IAM, and Google Sheets.](assets/images/data_site_simple_arch_2.png)
***Figure 6:** Slightly more flexible runtime architecture leveraging CDNs, internal IAM, and Google Sheets.*


<br>
## It's Your Turn Now!

By adhering to the principles and techniques described, you'll be well-equipped to create stunning, maintainable architectural documentation and visualizations that everyone in your organization can appreciate and utilize. Happy architecting!
