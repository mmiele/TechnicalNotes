---
title: P4 basic forawarding
description: P4 basic forawarding example
author: michael
last update: 01/30/2022
---

This example implements basic forwarding for IPv4.

In IPv4 forwarding, the **switch performs the following actions for every packet**: 

1. **Update** the **source** and **destination** MAC addresses.
1. **Decrement** the **time-to-live (TTL)** in the **IP header**.
1. **Forward** the packet to the **appropriate port**.

## Requirements

1. The switch has a **single table**, which the **control plane** populates with **static rules**. 
1. Each rule **maps an IP address to the MAC address** and **output port** for the **next hop**. 
1. The control plane rules have already been defined, you only need to implement the **data plane** logic of the P4 program.

The following topology is used, which is a **single pod of a fat-tree topology** referred to as **pod-topo**.