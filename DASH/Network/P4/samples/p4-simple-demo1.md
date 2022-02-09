---
title: P4 simple demo1 
description: P4 basic example
author: michael
last update: 02/08/2022
---

**Table of contents**
- [P4 simple demo1](#p4-simple-demo1)
  - [References](#references)


# P4 simple demo1 

This article describes how to perform the following tasks:

1. Compile a simple demo P4 program using the `p4c` P4 compiler.
1. Execute the compiled program using the `simple_switch` software switch.
1. Add table entries to the running P4 program (in real time) using the `simple_switch_CLI` command line utility.
1. Send packets to the running P4 program using `scapy`.

<!-- simple_switch_CLI uses a control message protocol that is not the P4Runtime API. If you are interested in adding table entries to the running P4 program using the P4Runtime API instead, see See README-p4runtime.md.-->

The example is based on the public repository sample [demo1](https://github.com/jafingerhut/p4-guide/tree/master/demo1). 

See code sample [demo1.p4_16.p4](basic/demo1.p4_16.p4).


## References 
- [p4-guide](https://github.com/jafingerhut/p4-guide) by jafingerhut