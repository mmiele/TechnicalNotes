---
title: P4 language 
description: Learning P4 language
author: michael
last update: 01/10/2022
---

# P4 language

Programming Protocol-independent Packet Processors (P4, in other word PPPP that is P4) is a domain-specific language for network devices, specifying how data plane devices (switches, NICs, routers, filters, etc.) process packets. For more information, see P4 Open-Source Programming Language.


## Getting started with P4

Suggested by Chris

1.  Hi Michael, you'll need a Linux machine - I installed Virtualbox
    hypervisor under Windows and then install an Ubuntu 20.04 VM. it\'s
    a bit of a process. All the p4 stuff runs exclusively on Linux
    AFAIK.

2.  Once you have a VM, you might visit
    [[https://github.com/jafingerhut/p4-guide]{.underline}](https://github.com/jafingerhut/p4-guide),
    it\'s one of the best resources I\'m aware of. Andy Fingerhut put it
    together as a personal project. He\'s a big player in the p4
    community and attends DASH meetings.

3.  If you follow Andy\'s instructions, you\'ll end up installing a huge
    pile of tools with one convenient script.

    a.  You need more than just the compiler to do anything useful.

    b.  You need something to run the output on - e.g., the bmv2
        simulator. Then you\'ll need example programs, which Andy\'s
        repo has in abundance.

Listen to video: [[Goodbye Scapy, Hello Snappi (DEMO) - Chris Sommers &
Ankur Sheth, Keysight
Technologies]{.underline}](https://www.youtube.com/watch?v=Db7Cx1hngVY)

See related slides: [[Goodbye Scapy,Hello
snappi]{.underline}](https://opennetworking.org/wp-content/uploads/2021/05/2021-P4-WS-Chris-Sommers-Ankur-Sheth-Slides.pdf)

References

- [Getting started](https://github.com/p4lang/education/blob/master/GettingStarted.md)
- [Tutorials](https://github.com/p4lang/tutorials) Official tutorials
- [P4 Language presentation](https://opennetworking.org/wp-content/uploads/2020/12/P4_tutorial_01_basics.gslide.pdf)
- [Example of startjng with P4](https://opennetworking.org/news-and-events/blog/getting-started-with-p4/) It needs cloud deployment.
- [Fingerhut p4-guide](https://github.com/jafingerhut/p4-guide)

