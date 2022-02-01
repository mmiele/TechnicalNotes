---
title: P4 basic forwarding
description: P4 basic forwarding example
author: michael
last update: 01/30/2022
---

# P4 basic forwarding

This article describes how to build and test a P4 example that implements **basic forwarding for IPv4**. The example is from in the public repository at [Implementing Basic Forwarding](https://github.com/p4lang/tutorials/tree/master/exercises/basic). 

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


The P4 example is written for the **V1Model architecture** implemented on **P4.org's bmv2 software switch**. The architecture file for the V1Model can be found at: [v1model.p4](https://github.com/p4lang/p4c/blob/main/p4include/v1model.p4). This file describes the interfaces of the P4 programmable elements in the architecture, the supported externs, as well as the architecture's standard metadata fields. Take a look at it.


## About the control plane
A P4 program defines a packet-processing pipeline (match-action tables) for the data plane, but the rules within each table are inserted by the **control plane**. When a **rule matches a packet**, its action is invoked with **parameters supplied by the control plane as part of the rule**.

In this exercise, the control plane logic is already implemented. As part of bringing up the Mininet instance, the **make run** command will **install packet-processing rules in the tables of each switch**. These are defined in the `sX-runtime.json` files, where X corresponds to the switch number.

### Important

**P4Runtime** is used to install the **control plane rules**. The content of files **sX-runtime.json** refer to specific names of tables, keys, and actions, as defined in the **P4Info** file produced by the compiler (look for the file build/basic.p4.p4info.txt after executing make run). Any changes in the P4 program that add or rename tables, keys, or actions will need to be reflected in these sX-runtime.json files.


## References

- [Implementing Basic Forwarding](https://github.com/p4lang/tutorials/tree/master/exercises/basic)
- [Using P4 in Mininet on BMV2](bmv2.md)

