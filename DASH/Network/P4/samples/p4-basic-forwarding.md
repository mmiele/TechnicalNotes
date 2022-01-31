---
title: P4 basic forawarding
description: P4 basic forawarding example
author: michael
last update: 01/30/2022
---

# P4 basic forawarding

This article describes how to build and test a P4 example that implements **basic forwarding for IPv4**. The example derives from the one shown in the public repository [Implementing Basic Forwarding](https://github.com/p4lang/tutorials/tree/master/exercises/basic). 

In IPv4 forwarding, the **switch performs the following actions for every packet**: 

1. **Update** the **source** and **destination** MAC addresses.
1. **Decrement** the **time-to-live (TTL)** in the **IP header**.
1. **Forward** the packet to the **appropriate port**.

## Requirements

1. The switch has a **single table**, which the **control plane** populates with **static rules**. 
1. Each rule **maps an IP address to the MAC address** and **output port** for the **next hop**. 
1. The control plane rules have already been defined, you only need to implement the **data plane** logic of the P4 program.

The following topology is used, which is a **single pod of a fat-tree topology** referred to as **pod-topo**.

![pod-topo](images/pod-topo.svg)


The P4 example is written for the **V1Model architecture** implemented on **P4.org's bmv2 software switch**. The architecture file for the V1Model can be found at: /usr/local/share/p4c/p4include/v1model.p4. This file desribes the interfaces of the P4 programmable elements in the architecture, the supported externs, as well as the architecture's standard metadata fields. We encourage you to take a look at it.

## References

- [Implementing Basic Forwarding](https://github.com/p4lang/tutorials/tree/master/exercises/basic)
