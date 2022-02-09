---
title: P4 language getting started
description: Getting started with the P4 language
author: michael
last update: 02/08/2022
---

**Table of contents**
- [P4 language getting started](#p4-language-getting-started)
  - [Getting started with P4](#getting-started-with-p4)
    - [Suggested steps](#suggested-steps)
  - [Vscode support](#vscode-support)
  - [References](#references)
  

# P4 language getting started

The **Programming Protocol-independent Packet Processors** (P4, in other word PPPP that is P4) is a domain-specific language for network devices, specifying how data plane devices (switches, NICs, routers, filters, etc.) process packets. For more information, see [P4 Open-Source Programming Language](https://p4.org/).

P4 is a domain-specific language that is designed to be implementable on a large variety of targets including programmable **network interface cards** (NIC), **FPGAs**, **software switches**, and **hardware ASICs**. As such, the language is restricted to constructs that can be efficiently implemented on all of these platforms. The following are some of the main core constructs provided by the P4 lanaguage:

## Getting started with P4

1. Go to [P4 Open-Source Programming Language](https://p4.org/), then select the **Learn More** button. This takes you to the [Learn](https://p4.org/learn/) section.
1. Scroll to the end of the page. In the *Educational Working Group* section select the [Getting Started](https://github.com/p4lang/education/blob/master/GettingStarted.md) link.  This takes you to the GitHub **education** repository. 
1. Select the link [P4 Language and Related Specifications](https://p4.org/specs/) and read it or at least some of it. 
1. Then we suggest to watch the videos, specifically the **P4 tutorial in four parts**.
1. Finally you can go to the [tutorials](https://github.com/p4lang/tutorials) to start playing with the code examples. We suggest the alternative as described next.

### Suggested steps

1. You'll need a Linux machine - I installed Virtualbox hypervisor and then installed an Ubuntu 20.04 VM. it's
    a bit of a process. All the p4 stuff runs exclusively on Linux.  For more information, see [How to Install VirtualBox on Ubuntu ](../../Ubuntu/ubuntu-notes.md#how-to-install-virtualbox-on-ubuntu).
1. Once you have a VM, you might visit [https://github.com/jafingerhut/p4-guide](https://github.com/jafingerhut/p4-guide), it's one of the best resources I'm aware of. Andy Fingerhut put it together as a personal project. He's a big player in the P4 community and attends DASH meetings.
1. If you follow Andy's instructions, you'll end up installing a huge pile of tools with one convenient script.
    > [!NOTE]
    > You need more than just the compiler to do anything useful.
    > You need something to run the output on - e.g., the bmv2 simulator. Then you'll need example programs, which Andy's repo has in abundance.
1. Listen to video: [Goodbye Scapy, Hello Snappi (DEMO) - Chris Sommers & Ankur Sheth, Keysight technologies](https://www.youtube.com/watch?v=Db7Cx1hngVY)
1. See related slides: [Goodbye Scapy,Hello snappi](https://opennetworking.org/wp-content/uploads/2021/05/2021-P4-WS-Chris-Sommers-Ankur-Sheth-Slides.pdf)



## Vscode support

Install the extension: Name: [p4 language support in vscode](https://marketplace.visualstudio.com/items?itemName=ZhanghanWang.p4-lang)


## References

- [Getting started](https://github.com/p4lang/education/blob/master/GettingStarted.md)
- [Tutorials](https://github.com/p4lang/tutorials) Official tutorials
- [P4 Language presentation](https://opennetworking.org/wp-content/uploads/2020/12/P4_tutorial_01_basics.gslide.pdf)
- [Example of startjng with P4](https://opennetworking.org/news-and-events/blog/getting-started-with-p4/) It needs cloud deployment.
- [Fingerhut p4-guide](https://github.com/jafingerhut/p4-guide)
- [P4PI Introduction](https://youtu.be/UdQh38SCBKA) - Interesting experimental environment that includes a specific designed hardware.
- [P4 Language Tutorial](https://youtu.be/U3Mn6o2j4zQ)
- [P4 programming language - introduction to network programming with P4](https://youtu.be/UEMAvXXNWsY)
- [P4 Tutorial](https://youtu.be/pk_s53l6-Ec)

