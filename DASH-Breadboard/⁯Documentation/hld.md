---
title: DASH High Level Design 
description: DASH High Level Design draft
author: michael
last update: 01/21/2022
---


# DASH High Level Design 




## Overview


![](images/architecture/draft-simple-layered-architecture.png)



## SDN controller

The SDN controller is **primarily responsible for controlling the DASH overlay services** as oposed to the traditional SONiC stack is used to manage the underlay (L3 routing) and hardware platform. 
The **SDN controller communicates with a DASH device through a gNMI endpoint served by a new SDN agent running inside a new SONiC DASH container**. 

## DASH container

This container **translates SDN configuration modeled in gNMI into SONiC APPL_DB config objects**. In particular 
- The SONiC orchagent will be enhanced to translate these objects into SAI_DB objects, including the new DASH-specific SAI objects. 
- An enhanced syncd will then configure the dataplane using the vendor-specific SAI library.


## Switch State Service (SWSS)



## Switch Abstraction Interface (SAI) DASH


## ASIC Drivers



## DASH capable ASICs




## References
- [Difference between Underlay Network and Overlay Network](https://ipwithease.com/difference-between-underlay-network-and-overlay-network/)
- [https://ipwithease.com/](https://ipwithease.com/)
