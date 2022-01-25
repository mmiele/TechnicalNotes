---
title: P4 language details
description: Learning P4 language
author: michael
last update: 01/24/2022
---

# P4 language details


## Background


The P4 languaeg was created based on the following main goals:

1. **Reconfigurability**. Programmers should be able
to change the way switches process packets once they are
deployed. 
1. **Protocol independence**. Switches should not be tied to any specific network protocols.
1. **Target independence**. Programmers should be able to describe packet processing functionality independently of the specifics of the underlying hardware. 


We'll show an example on how to use P4 to configure a switch to add a new hierarchical label.

From [Programming Protocol-Independent Packet Processors](https://www.cs.princeton.edu/~jrex/papers/of2.pdf)


## Overview

The **Programming Protocol-independent Packet Processors** (P4) is a domain-specific language that is designed to be implementable on a large variety of targets including programmable **network interface cards** (NIC), **FPGAs**, **software switches**, and **hardware ASICs**. As such, the language is restricted to constructs that can be efficiently implemented on all of these platforms. 

The following are some of the main core constructs provided by the P4 lanaguage:

- **Header types** describe the format (the set of fields and their sizes) of each header within a packet.
- **Parsers** describe the permitted sequences of headers within received packets, how to identify those header sequences, and the headers and fields to extract from packets.
- **Tables** associate user-defined keys with actions. P4 tables **generalize traditional switch tables**. They can be used to implement **routing tables**, **flow lookup tables**, **access-control lists**, and other user-defined table types, including complex multi-variable decisions.
- **Actions** are code fragments that describe how packet header fields and metadata are manipulated. Actions can include data, which is supplied by the control-plane at runtime.
- **Match-action units** perform the following sequence of operations:
    - Construct lookup keys from packet fields or computed metadata.
    - Perform table lookup using the constructed key, choosing an action (including the associated data) to execute.
    - Finally, execute the selected action.
- **Control flow** expresses an **imperative program that describes packet-processing on a target**, including the data-dependent sequence of match-action unit invocations. **Deparsing** (packet reassembly) can also be performed using a control flow.
- **Extern objects** are **architecture-specific constructs** that can be manipulated by P4 programs through well-defined APIs, but **whose internal behavior is hard-wired** (e.g., checksum units) and **hence not programmable using P4**.
- **User-defined metadata** are user-defined data structures associated with each packet.
- **Intrinsic metadata** is metadata **provided by the architecture associated with each packet** (e.g., the input port where a packet has been received).


## P4 language abstract model

The P4 machine operates with only a few simple rules as shown in the following high level representation of the P4 abstract model. From [P4 Language Specification](https://p4.org/p4-spec/p4-14/v1.0.5/tex/p4.pdf#:~:text=The%20P4%20language%20uses%20a%20%EF%AC%82at%20typing%20structure%2C,expressed%20in%20P4%20in%20binary%2C%20decimal%20and%20hexadecimal).

**P4 abstract model**

![p4-abstract-model](./images/p4-abstract-model.png)

1. For **each packet**, the parser produces a **parsed representation** on which **match+action** tables operate.
1. The **match+action tables** in the **ingress pipeline** generate an **egress specification** which determines the **set of ports** and number of **packet instances** for each port to which the packet will be sent.
1. The **queuing mechanism** processes this **egress specification**, generates the necessary **instances of the packet** and submits each to the **egress pipeline**. Egress
queuing may buffer packets when there is over-subscription for an output port, although this is not mandated by P4.
1. A **packet instance’s physical destination** is determined before entering the *egress
pipeline*. Once it is in the *egress pipeline**, this destination is assumed not to
change (though the packet may be dropped or its headers further modified).
1. After all processing by the *egress pipeline* is complete, the packet instance’s header
is formed from the **parsed representation** (as modified by match+action processing) and the resulting packet is transmitted.
Although not shown in this diagram, P4 supports recirculation and cloning of packets.

P4 focuses on the **specification of the parser**, **match+action tables** and the **control flow** through the pipelines. Programmers control this by writing a P4 program which **specifies the switch configuration** as shown at the top of the figure.
A machine that runs a P4 program is called **target**. Although a target may directly execute a P4 program, it is assumed that the program is compiled into a suitable configuration for the target. 
For example, currently, P4 does not expose the functionality of the queuing Mechanism and does not specify the semantics of the egress specification beyond what is mentioned above. Currently they are defined in target specific input to the compiler and exposed in conjunction with other interfaces that provide run time system management and configuration. 
Future versions of P4 may expose configuration of these mechanisms allowing consistent management of such resources from the P4 program.



## References
- [P4 Network Programming Language—what is it all about?](https://codilime.com/blog/p4-network-programming-language-what-is-it-all-about/). This is a very good starting point; step by step intro. 
- [P4 Language Specification](https://p4.org/p4-spec/p4-14/v1.0.5/tex/p4.pdf#:~:text=The%20P4%20language%20uses%20a%20%EF%AC%82at%20typing%20structure%2C,expressed%20in%20P4%20in%20binary%2C%20decimal%20and%20hexadecimal) PDF format with good diagrams and definitions about the P4 langauge structure. 
- From [Programming Protocol-Independent Packet Processors](https://www.cs.princeton.edu/~jrex/papers/of2.pdf). A white paper and another good intro to the lanaguage and the underlying principles. 
- [P4 Language Tutorial](https://cs344-stanford.github.io/lectures/Lecture-2-P4-tutorial.pdf) Power point and diagrams.
- [BEHAVIORAL MODEL (bmv2)](https://github.com/p4lang/behavioral-model)
- [Why Does the Internet Need a Programmable Forwarding Plane with Nick McKeown](https://www.youtube.com/watch?v=zR88Nlg3n3g)

