---
title: DASH High Level Design 
description: DASH High Level Design draft
author: michael
last update: 01/21/2022
---


# DASH High Level Design 




## Overview

The following is a high level view of the DASH architecture. 

![draft-simple-layered-architecture](images/architecture/draft-simple-layered-architecture.svg)



## SDN controller

The SDN controller is **primarily responsible for controlling the DASH overlay services**, while the traditional SONiC stack is used to manage the underlay (L3 routing) and hardware platform. 

The SDN controller controls the overlay built on top of the physical layer of the infrastructure.  From the point of view of the SDN control plane, when a customer creates an operation, for example a VNET creation, from the cloud portal, the controller allocates the resources, placement management, capacity, etc. via the  **NorthBound interface APIs**.

### SDN and DPU High-Availability (HA)

For **High Availability** (HA), the SDN controller selects the pair of cards and configures them identically.  The only requirement on the card from the HA perspective is for the cards to setup a channel between themselves for flow synchronization.  The synchronization mechanism is left for vendors to define and implement. For more information, see [High Availability]() document.   


## DASH container
 
The SDN controller communicates with a DASH device through a **[gNMI]() endpoint** served by a new DASH SDN agent **running inside a new SONiC DASH container**.  

In particular 
- The **SONiC orchagent** will be enhanced to translate these objects into **SAI_DB objects**, including the new **DASH-specific SAI objects**. 
- An **enhanced syncd** will then configure the dataplane using the **vendor-specific SAI library**.

A **gNMI schema** will manage the following DASH services: 
- Elastic Network Interface (ENI)
- Access Control Lists (ACLs) 
- Routing and mappings
- Encapsulations 
- Other  

### Multiple DPUs device

In the case of a multiple DPUs device the following applies:

- Each DPU provides a gNMI endpoint for SDN controller through a unique IP address. 
- An appliance or smart switch containing multiple DPUs therefore contains multiple gNMI endpoints for SDN controller, and the controller treats each DPU as a separate entity. 
- To conserve IPv4 addresses, such an appliance or switch _might_ contain a proxy (NAT) function to map a single IP address:port combination into multiple DPU endpoints with unique IPv4 addresses.  
- No complex logic will run on the switches (switches do not have a top-level view of other/neighboring switches in the infrastructure). 


## Switch State Service (SWSS)


## Switch Abstraction Interface (SAI) DASH

An **enhanced syncd** configures the dataplane using the vendor-specific SAI library.

## ASIC Drivers



## DASH capable ASICs




## References
- [Difference between Underlay Network and Overlay Network](https://ipwithease.com/difference-between-underlay-network-and-overlay-network/)
- [https://ipwithease.com/](https://ipwithease.com/)
