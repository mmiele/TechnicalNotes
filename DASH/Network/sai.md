# Switch Abstraction Interface (SAI) 

> [!WARNING] 
> The **Switch Abstraction Interface** (SAI) has been replaced by [SONiC](https://github.com/Azure/Sonic).

The **Switch Abstraction Interface** (SAI) is a hardware abstraction
model for switching silicon (ASICs). It is an open-source framework that
allows ASICs to be represented in software. This means you can use a
Broadcom ASIC the same way as one from Mellanox or Cavium XPliant. This
framework let developers target switching platforms in an agnostic way;
as long the necessary ASIC drivers are available. SAI locates the
abstraction in **the user space**, while other frameworks, such as
switchdev, locate the abstraction in the kernel space.

## Background

SAI is part of the [Azure Cloud
Switch](https://azure.microsoft.com/en-us/blog/microsoft-showcases-the-azure-cloud-switch-acs/)
(ACS) that is a cross-platform modular operating system for data center
networking built on Linux. ACS allows to debug, fix, and test software
bugs much faster. It also allows to share the same software stack across
hardware from multiple switch vendors. This is done via the **Switch
Abstraction Interface (SAI) specification**, the first open-standard C
API for programming network switching ASICs, of the Open Compute Project
(OCP). The figure below shows the main ACS stack functional blocks. This
framework allows for disaggregating the switch software from the switch
hardware

![ACS Stack](../%E2%81%AFDocumentation/images/sdn//asc.png)

**Applications**. These include open-source applications such as Quagga,
Microsoft specific applications that could relate to an entire
configuration management system like Autopilot or a feature like SWAN,
and also third-party applications.

**Switch State Service (SSS).** The SSS is a subset of the global
network state. It helps in driving the switch towards its goal state. It
avails open-source key-value pair stores like **Redis** to manage all
switch states requirements. Having a database layer which is also a
**SAI object management sublayer** helps in the object sharing and
dependency among different applications. The database is modular and
provides application with a view of the states.

**SAI**. Before SAI, the underlying complexity of the hardware, with its
strict coupling of protocol stack software, denied the freedom to choose
the best combination of hardware and software for networking needs. SAI
allows software to program multiple switch chips without any changes,
thus making the base router platform simple, consistent, and stable. A
standardized API also allows network hardware vendors to develop
innovative hardware architectures to achieve great speeds while keeping
the programming interface consistent. Additionally, SAI also enables
open and easier software development of features, stacks, and
applications.

**Vendor provided hardware and software**. This comprises of the actual
ASICs, drivers, the software development kits (SDKs) which **talk
northbound to the SAI**.

### Some historical notes

In the summer of 2014 at an [OCP Engineering
Workshop](http://opencompute.org/wiki/Networking/Workshop-2014-07) at [UNH-IOL](https://www.iol.unh.edu/),
Microsoft and Dell both presented work around the idea of a user-space
switching application; Microsoft through the Azure Cloud Switch (ACS)
presentation and Dell through the switching abstraction. Then, during
the [2015 OCP
Summit](http://opencompute.org/wiki/Networking/Workshop-2015-03), the
team demonstrated SAI with a 4-node CLOS setup with various
implementations from Dell, Microsoft, Broadcom, and Mellanox.

Over the summer, SAI was officially accepted as an OCP project, followed
by an [announcement](https://azure.microsoft.com/en-us/blog/microsoft-showcases-the-azure-cloud-switch-acs/) from
Microsoft regarding ACS.

It took Microsoft less than a year with about 10 FTEs to build a NOS
that supports multiple ASICs.

See the article: [What Are SAI And Switchdev And Why Do We Need Them To
Succeed?](https://packetpushers.net/sai-and-switchdev-need-to-succeed/)

## Disaggregating the network

Disaggregation here means decoupling the network software from the
hardware. This is like buying a network silicon from any vendor and then
loading a Network Operating System (NOS) of your choice. In this case,
one can have a variety of options for the switching silicon and
open-source NOS. Switching silicon hardware can be from, Broadcom,
Barefoot, Centec, Mellanox etc. and NOS can be Open Switch (OPX), SONiC,
dNOS etc.

**Modularity and liberty in selecting NOS and switching silicon**

To adapt the network disaggregation concept, big players like Microsoft,
Facebook, Dell, Intel, Broadcom, Mellanox, Marvell etc. have muscled up
to tackle the problem of traditional network stack. They have formed the
Open Compute Project (OCP) group and introduced the standard abstraction
of network switch: the **Switch Abstraction Interface** (SAI).

### SAI - Solution to adapt the Disaggregation

In the past, in order to a functional switch, it was necessary to piece
together all the components of the network stack, aka NOS, specific for
each vendor. These components included the following:

-   Switching Silicon's Software Kit
-   Platform specific drivers
-   Management (control) plane.

While in the past each silicon vendor provided an SDK to be integrated
with the NOS. Now for the smooth and easy integration, vendors provide
standard interfaces to access its silicon. The standard interface is
well accepted and widely used by the various open-sourced NOS. Since it
is standard, developer should only need to know the standard APIs which
is vendor neutral.

The standard interface in discussion here is the **Switch Abstraction
Interface** (SAI). The figure below shows the traditional network stack
on the left vs. the disaggregated network stack (using SAI) on the
right.

![sai-in-stack](../%E2%81%AFDocumentation/images/sdn/sai-in-stack.png)


See the article [Switch Abstraction Interface (SAI) - Breaking the
Network Aggregation](https://www.design-reuse.com/articles/44519/switch-abstraction-interface-sai.html).

As you can see from the previous figure, SAI is a user space abstraction
model; this means:

-   A user space application is driving the ASIC, bypassing the kernel.

-   It also means that a hardware cache representation (switch state
    service using ACS parlance) is done in user space as well.
    Typically, this is a key-value store like **Redis** (ACS), **OVSDB**
    (OpenSwitch), or **SysDB** (Arista EOS).

-   Using the user space abstraction also requires applications to be
    either re-written or modified to support communication with the
    switch state service.

One advantage of doing everything in user space is the developer/vendor
can take a stock Linux distribution and add their necessary
changes/applications. No Linux kernel expertise required. No need to
make sure things are upstreamed. You just need the SAI driver for your
ASIC. Hell, you can move hardware as well (Broadcom to Mellanox) by just
changing the SAI driver.

The following is the traditional process to use a silicon switch:

1.  You must possess the Broadcom SDK, which isn't freely available and
    must be obtained via a channel (you know: a lawyer to approve the
    NDA, a tech lead to ensure you really need the SDK, and so on).

2.  Once you have access to the SDK--including source, documentation,
    and examples--you can build and run your application.

3.  But if you want to distribute your product, it can only be in binary
    form as per the license requirements.

#### Problems with the traditional approach

1.  For some vendors, the traditional approach maybe fine. For others
    that develop open-source network operating systems (NOSes), you have
    an open NOS that doesn't do packet forwarding. Might as well drop
    the 'N' from NOS at this point, or the word 'open,' because the
    forwarding engine is not.

2.  Not only is the acquisition of the SDK cumbersome and a barrier to
    entry for open-source projects, it doesn't always come bug-free. For
    example, suppose the SDK has a bug that you find and like a good
    developer, you submit a bug ticket to Broadcom. How long do you
    think it'll take before an updated version of the SDK with the fixed
    bug will be available? Days, ideally? Weeks, maybe? Months, most
    likely.

    a.  So where does that leave the developer/vendor that wants to ship
        with the Broadcom chip? Well, the clout of the developer/vendor
        will influence how fast a fix is supplied.

    b.  However, some developers that have intimate knowledge of the
        Broadcom chips may attempt to work around the issue by
        reading/writing registers directly. This essentially bypasses
        what the SDK is supposed to provide.

3.  To make matters worse, the Broadcom SDK documentation reads like an
    errata appendix; meaning when changes to the SDK happen (like adding
    a new chip, e.g. Tomahawk), what documentation is supplied reads
    like a patch one sends to a mailing list. To fully comprehend the
    SDK at a particular point in time, you need to know what the
    previous versions had in them.

It sounds like Broadcom-bashing, but truth be told, all vendors
face these same issues to varying degrees.

See related article [Why The Industry Needs An Open Source Framework For
Switching Silicon](https://packetpushers.net/industry-needs-open-source-framework-switching-silicon/).

> [!NOTE] 
> Today, it's fair to say Broadcom is the #1 provider of merchant silicon
for switches, with Mellanox and others chomping at the bit. This is true
for traditional vendors (Cisco, Arista, Juniper) and is true for Open
Networking vendors (Accton, Celestica, Dell, DNI, HP, Penguin, Quanta,
and so on).