---
layout: post
section: "Appendices"
title: "Cloud Design Patterns"
position: 12115
date:   2021-10-21 21:12:01 +0100
author: by Željko Obrenović (obren.io)
permalink: concepts-cloud
icon: productivity_tools.png
timetoread: 15 min
excerpt: Tools I've built and use in daily architectural work.


---
<img style="margin-top: -20px; width: 100%; height: 400px; object-fit: cover"
src="assets/images/arch/fantasy-782001_1280.jpg">
<div style="font-size: 70%; margin-top: -16px; color: grey; margin-bottom: 12px">
Image by <a href="https://pixabay.com/users/dlee-271284/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=782001">Donna Kirby</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=782001">Pixabay</a>
</div>
<style>
    h1 {
        font-size: 210%;
    }
</style>

> **IN THIS SECTION, YOU WILL:** Get an overview of several tools I've built and use in daily architectural work.

# ...

Source: [learn.microsoft.com/en-us/azure/architecture/patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/)

## Performance and Scalability
Make your system perform well under load and react well to the change of the load.

* **Command and Query Responsibility Segregation (CQRS):** Segregate operations that read data from operations that update data by using separate interfaces.
* **Event Sourcing:** Use an append-only store to record the full series of events that describe actions taken on data in a domain.
* **Materialized View:** Generate prepopulated views over the data in one or more data stores when the data isn't ideally formatted for required query operations.
* **Index Table:** Create indexes over the fields in data stores that are frequently referenced by queries.
* **Sharding:** Divide a data store into a set of horizontal partitions or shards.
* **Static Content Hosting:** Deploy static content to a cloud-based storage service that can deliver them directly to the client.
* **Cache-Aside:** Load data on demand into a cache from a data store.
* **Throttling:** Control the consumption of resources used by an instance of an application, an individual tenant, or an entire service.
* **Rate Limit Pattern:** Limiting pattern to help you avoid or minimize throttling errors related to these throttling limits and to help you more accurately predict throughput.
* **Geodes:** Deploy a collection of backend services into a set of geographical nodes, each of which can service any request for any client in any region.

## Resiliency
Gracefully handle and recover from failures.

* **Bulkhead:**  Isolate elements of an application into pools so that if one fails, the others will continue to function.
* **Retry:** Enable an application to handle anticipated, temporary failures when it tries to connect to a service or network resource by transparently retrying an operation that's previously failed.
* **Circuit Breaker:** Handle faults that might take a variable amount of time to fix when connecting to a remote service or resource.
* **Compensating Transaction:** Undo the work performed by a series of steps, which together define an eventually consistent operation.
* **Leader Election:** Coordinate the actions performed by a collection of collaborating task instances in a distributed application by electing one instance as the leader that assumes responsibility for managing the other instances.

## Messaging
Create a messaging infrastructure that connects the components and services, ideally in a loosely coupled manner to maximize scalability.

* **Publisher/Subscriber:** Enable an application to announce events to multiple interested consumers asynchronously, without coupling the senders to the receivers.
* **Competing Consumers:** Enable multiple concurrent consumers to process messages received on the same messaging channel.
* **Pipes and Filters:** Break down a task that performs complex processing into a series of separate elements that can be reused.
* **Priority Queue:** Prioritize requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority.
* **Queue-Based Load Leveling:** Use a queue that acts as a buffer between a task and a service that it invokes in order to smooth intermittent heavy loads.
* **Scheduler Agent Supervisor:** Coordinate a set of actions across a distributed set of services and other remote resources.
* **Asynchronous Request-Reply:** Decouple backend processing from a frontend host, where backend processing needs to be asynchronous, but the frontend still needs a clear response.
* **Choreography:** Have each component of the system participate in the decision-making process about the workflow of a business transaction, instead of relying on a central point of control.
* **Saga:** Manage data consistency across microservices in distributed transaction scenarios. A saga is a sequence of transactions that updates each service and publishes a message or event to trigger the next transaction step.
* **Sequential Convoy:** Process a set of related messages in a defined order, without blocking processing of other groups of messages.

## Management and Monitoring
Expose runtime information that administrators and operators can use to manage and monitor the system. Supporting changing business requirements and customization without requiring the application to be stopped or redeployed.
* **Health Endpoint Monitoring:** Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals.
* **Ambassador:** Create helper services that send network requests on behalf of a consumer service or application.
* **Anti-Corruption Layer:** Implement a façade or adapter layer between a modern application and a legacy system.
* **External Configuration Store:** Move configuration information out of the application deployment package to a centralized location.
* **Gateway Aggregation:** Use a gateway to aggregate multiple individual requests into a single request.
* **Gateway Offloading:** Offload shared or specialized service functionality to a gateway proxy.
* **Gateway Routing:** Route requests to multiple services using a single endpoint.
* **Sidecar:** Deploy components of an application into a separate process or container to provide isolation and encapsulation.
* **Strangler Fig:** Incrementally migrate a legacy system by gradually replacing specific pieces of functionality with new applications and services.

## Security
Prevent malicious or accidental actions outside of the designed usage, and prevent disclosure or loss of information.

* **Federated Identity:** Delegate authentication to an external identity provider.
* **Gatekeeper:** Protect applications and services by using a dedicated host instance that acts as a broker between clients and the application or service, validates and sanitizes requests, and passes requests and data between them.
* **Valet Key:** Use a token or key that provides clients with restricted direct access to a specific resource or service.
* **Claim Check:** Split a large message into a claim check and a payload.

## Other Patterns
Create good designs. Take care of consistency, coherence, maintainability, and reusability.

* **Compute Resource Consolidation:** Consolidate multiple tasks or operations into a single computational unit
* **Backends for Frontends:** Create separate backend services to be consumed by specific frontend applications or interfaces.
* **Deployment Stamps:** Deploy multiple independent copies of application components, including data stores.