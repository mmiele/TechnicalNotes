---
title: Glossary
description: Network terminlogy definitions 
author: michael
last update: 12/10/2021
---

# Glossary #

<p style="font-size:1.5em;">
<a href="#a" >A</a> <a href="#b">B</a> <a href="#c" >C</a> <a href="#d">D</a> <a href="#e" >E</a> <a href="#f">F</a> <a href="#g" >G</a> <a href="#h">H</a> <a href="#i" >I</a> <a href="#j">J</a> <a href="#k" >K</a> <a href="#l">L</a> <a href="#m" >M</a> <a href="#n">N</a> <a href="#o" >O</a> <a href="#p">P</a> <a href="#q" >Q</a> <a href="#r">R</a> <a href="#s" >S</a> <a href="#t">T</a> <a href="#u" >U</a> <a href="#v">V</a> <a href="#w" >W</a> <a href="#x">X</a> <a href="#y" >Y</a> <a href="#z">Z</a>  
</p>

<hr style="border-top: 2px dashed blue"/>

## A ##

### ASIC ###  

An **Application specific integrated circuit (ASIC)** is an integrated circuit (IC) chip customized for a particular use, rather than intended for general-purpose use. For example, a chip designed to run in a digital voice recorder is an ASIC. ASIC chips are typically built using metal-oxide-semiconductor (MOS) technology, as MOS integrated circuit chips. For more information, see [Application specific integrated circuit](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit).


## D ##

### DASH ###  

Microsoft Azure has created a sub-group of [SONiC](#sonic) (Software for Open Networking in the Cloud) that extends SONiC’s functionality to stateful workloads also known as **Disaggregated APIs for SONiC Hosts** or SONiC DASH. The goals are the following:

- With the help of network hardware vendors, create an open forum that capitalizes on the use of **programmable networking hardware** including [SmartNICs](https://blogs.nvidia.com/blog/2021/10/29/what-is-a-smartnic/), SmartToRs, SmartAppliances. 
- Optimize [Stateful L4](#stateful-l4) performance and connection scale by 10x or even 100x when compared to implementations that make extensive use of software. As host networking in the cloud is performed at L4 the resulting performance improvements should be truly significant.


### Decap ###
Data De-encapsulation is the reverse process of data [encapsulation](#encap). The encapsulated information is removed from the received data to obtain the original data. This process takes place at the receiver’s end. The data is de-encapsulated at the same layer at the receiver’s end to the encapsulated layer at the sender’s end. The added header and trailer information are removed from the data in this process. For more information, see [What is Data Encapsulation and de-encapsulation in networking?](https://afteracademy.com/blog/what-is-data-encapsulation-and-de-encapsulation-in-networking).


### DPU ###

A **Data Procssing Unit** (DPU) is a new class of programmable processor that combines three key elements. A DPU is a system on a chip, or **SoC**, that combines:
- An industry-standard, high-performance, software-programmable, multi-core CPU, typically based on the widely used Arm architecture, tightly coupled to the other SoC components.
- A high-performance network interface capable of parsing, processing and efficiently transferring data at line rate, or the speed of the rest of the network, to GPUs and CPUs.
- A rich set of flexible and programmable acceleration engines that offload and improve applications performance for AI and machine learning, security, telecommunications and storage, among others.

The DPU can be used as a stand-alone embedded processor. But it’s more often incorporated into a SmartNIC, a network interface controller used as a critical component in a next-generation server.

For more information, see [What Is a DPU?](https://blogs.nvidia.com/blog/2020/05/20/whats-a-dpu-data-processing-unit/).

## E ##

### Encap ###
Data Encapsulation is the process in which some extra information is added to the data item to add some features to it. The OSI or the TCP/IP model for data transmission in a netowr which takes place through various layers in these models. Data encapsulation adds the protocol information to the data so that data transmission can take place properly through the layers. 

The data is encapsulated on the sender’s side, starting from the application layer to the physical layer. Each layer takes the encapsulated data from the previous layer and adds some more information to encapsulate it and some more functionalities with the data. These functionalities may include proper data sequencing, error detection and control, flow control, congestion control, routing information, etc. For more information, see [What is Data Encapsulation and de-encapsulation in networking?](https://afteracademy.com/blog/what-is-data-encapsulation-and-de-encapsulation-in-networking).



## F ##

### FPGA ###  

A **[Field Programmable Gate Array](https://en.wikipedia.org/wiki/Field-programmable_gate_array)** (FPGA) is an integrated circuit designed to be configured by a customer or a designer after manufacturing, hence the term field-programmable. The FPGA configuration is generally specified using a hardware description language (HDL), similar to that used for an application-specific integrated circuit (ASIC). 


## L ##

### Layers ###

The [OSI](#osi) model partitions the flow of data in a communication system into **seven abstraction layers**, from the physical implementation of transmitting bits across a communications medium to the highest-level representation of data of a distributed application. **Each intermediate layer serves a class of functionality to the layer above it and is served by the layer below it**. Classes of functionality are realized in software by standardized communication protocols.

This [list of network protocols](https://en.wikipedia.org/wiki/List_of_network_protocols_(OSI_model)) article categorize the network protoocol by the nearest layer in the Open Systems Interconnection model. This list is not exclusive to only the OSI protocol family. Many of these protocols are originally based on the Internet Protocol Suite (TCP/IP) and other models and they often do not fit neatly into the OSI layers.

## N ##

### NAT ###

The **Network address translation (NAT)** is a method of mapping an IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device. The technique was originally used to avoid the need to assign a new address to every host when a network was moved, or when the upstream Internet service provider was replaced, but could not route the networks address space. It has become a popular and essential tool in conserving global address space in the face of IPv4 address exhaustion. One Internet-routable IP address of a NAT gateway can be used for an entire private network.

As network address translation modifies the IP address information in packets, NAT implementations may vary in their specific behavior in various addressing cases and their effect on network traffic. The specifics of NAT behavior are not commonly documented by vendors of equipment containing NAT implementations. For more information, see [Network address translation](https://en.wikipedia.org/wiki/Network_address_translation). 

### NBI ###

In computer networking and computer architecture, a northbound interface (NBI) of a component is an **interface that allows the component to communicate with a higher level component, using the latter component's southbound interface**. The northbound interface conceptualizes the lower level details (e.g., data or functions) used by, or in, the component, allowing the component to interface with higher level layers.

In architectural overviews, the northbound interface is normally drawn at the top of the component it is defined in; hence the name northbound interface. A southbound interface decomposes concepts in the technical details, mostly specific to a single component of the architecture. **Southbound interfaces are drawn at the bottom of an architectural overview**.


### NIC ###

The **network interface controller (NIC)**, also known as a network interface card, network adapter, LAN adapter or physical network interface, is the hardware component that connects a computer to a computer network.

Early network interface controllers were commonly implemented on expansion cards that plugged into a computer bus. The low cost and ubiquity of the Ethernet standard means that most newer computers have a network interface built into the motherboard, or is contained into a USB-connected dongle.

Modern network interface controllers offer advanced features such as interrupt and DMA interfaces to the host processors, support for multiple receive and transmit queues, partitioning into multiple logical interfaces, and on-controller network traffic processing such as the TCP offload engine.

For more information, see [Network interface controller ](https://en.wikipedia.org/wiki/Network_interface_controller). 

## O ##

### OCP ###

The [Open Compute Project Foundation](https://www.opencompute.org/) (OCP) was created in 2011 with a mission to apply the benefits of open source and open collaboration to hardware and rapidly increase the pace of innovation around the data center. The OCP is a collaborative community focused on redesigning hardware technology to efficiently support the growing demands on compute infrastructure. 

In 2009 Facebook started a project to **design the world’s most energy efficient data center**, one that could handle unprecedented scale at the lowest possible cost. A small team of engineers spent the next two years designing and building one from the ground up: **software, servers, racks, power supplies, and cooling**. The result now stands in Prineville, Oregon.

It was 38% more energy efficient to build and 24% less expensive to run than the company’s previous facilities and has led to even greater innovation.

In 2011, Facebook shared its designs with the public and—along with Intel and Rackspace, Goldman Sachs and Andy Bechtolsheim—launched the **Open Compute Project** and incorporated the **Open Compute Project Foundation**. The five members hoped to create a movement in the hardware space that would bring about the same kind of creativity and collaboration we see in open source software. 

### ONIE ###

Created by Cumulus Networks, Inc. in 2012, the [Open Network Install Environment](https://www.opencompute.org/wiki/Networking/ONIE) (ONIE) Project is a small operating system, pre-installed as firmware on bare metal network switches, that provides an environment for automated operating system provisioning.

Incubated and adopted by the [OCP](#ocp) in 2013, the ONIE project enables a bare metal network switch ecosystem where end users can choose among different network operating systems. ONIE enables switch hardware suppliers to manage their operations based on a small number of hardware SKUs. This in turn creates economies of scale in manufacturing and distribution enabling a thriving ecosystem of both network hardware and operating system alternatives.

### ONL ###

Initially proposed at [OCP](#ocp) engineering workshop in San Antonio by [Big Switch Networks](http://bigswitch.com/) in 2013, [Open Network Linux](http://opennetlinux.org/) (ONL) is a Linux distribution for "bare metal" switches.

Adopted by the [OCP](#ocp) in 2014, ONL is the reference Network Operating System for the [OCP](#ocp).

### OSI ###

The [Open Systems Interconnection](https://en.wikipedia.org/wiki/OSI_model#Layer_4:_Transport_layer) (OSI) model is a conceptual model that characterizes and standardizes the communication functions of a telecommunication or computing system without regard to its underlying internal structure and technology. Its goal is the interoperability of diverse communication systems with standard communication protocols.


## P ##

### Plane ###

In networking, a **plane** is an abstract conception of where certain processes take place. The term is used in the sense of "plane of existence." The two most commonly referenced planes in networking are the **control plane** and the **data plane** (also known as the **forwarding plane**).

- The **control plane** controls how data packets are forwarded, that is how data is sent from one place to another. A **routing table** is part of the control plane. Routers use various protocols to identify network paths, and they store these paths in routing tables.
- The **data plane** actually forwards the packets. The data plane is also called the **forwarding plane**.

Think of the control plane as being like the stoplights, while the data plane is more like the cars that drive on the roads, which stop at the intersections, and obey the stoplights.

For more information, see [Control and data plane](https://www.cloudflare.com/learning/network-layer/what-is-the-control-plane/).

## R ##

### RDMA ###

The **Remote Direct Memory Access** (RDMA) is a direct memory access from the memory of one computer into that of another without involving either one's operating system. This permits high-throughput, low-latency networking, which is especially useful in massively parallel computer clusters. For more information, see [Remote Direct Memory Access](https://en.wikipedia.org/wiki/Remote_direct_memory_access).




## S ##

### SAI ### 

The **Switch Abstraction Interface** (SAI), on which SONiC is built, defines a standard API. Network hardware vendors can use it to develop innovative hardware platforms that can achieve great speeds while keeping the programming interface to ASIC (application-specific integrated circuit) consistent. Microsoft open sourced SAI in 2015. This approach enables operators to take advantage of the rapid innovation in silicon, CPU, power, port density, optics, and speed, while preserving their investment in one unified software solution across multiple platforms.

### SDN ### 

The **Software-defined networking** (SDN) technology is an approach to network management that enables dynamic, programmatically efficient network configuration in order to improve network performance and monitoring, making it more like cloud computing than traditional network management. SDN is meant to address the fact that the static architecture of traditional networks is decentralized and complex while current networks require more flexibility and easy troubleshooting. SDN attempts to centralize network intelligence in one network component by **disassociating the forwarding process of network packets (data plane) from the routing process (control plane)**. 

The **control plane consists of one or more controllers, which are considered the brain of the SDN network where the whole intelligence is incorporated**. However, the intelligent centralization has its own drawbacks when it comes to security, scalability and elasticity and this is the main issue of SDN.

SDN was commonly associated with the OpenFlow protocol (for remote communication with network plane elements for the purpose of determining the path of network packets across network switches) since the latter's emergence in 2011. However, since 2012 OpenFlow for many companies is no longer an exclusive solution, they added proprietary techniques. These include Cisco Systems' Open Network Environment and Nicira's network virtualization platform. For more information, see [Software-defined networking](https://en.wikipedia.org/wiki/Software-defined_networking).


### Stateful L4 ###

The stateful layer-4 (L4) load balancers scale out services hosted in cloud datacenters by mapping packets destined to a service with a virtual IP address (VIP) to a pool of servers with multiple direct IP addresses (DIPs or DIP pool). L4 load balancing is a critical function for inbound trac to the cloud and trac across tenants. A study reports that an average of 44% of cloud trac is VIP trac and thus needs load balancing function. For more information see [Making Stateful Layer-4 Load Balancing Fast and
Cheap Using Switching ASICs](http://cs.yale.edu/homes/yu-minlan/writeup/sigcomm17.pdf). 

### SONiC ###

Microsoft has pioneered the **Software for Open Networking in the Cloud** (SONiC), for network switch operations and management. It is a **collection of software networking components** required to build network devices with rich functionality and addresses the following main requirements, when runnig a cloud platform like Microsoft Azure:

- Use best-of-breed switching hardware for the various tiers of the network.
- Deploy new features without impacting end users.
- Roll out updates securely and reliably across the fleet in hours instead of weeks.
- Utilize cloud-scale deep telemetry and fully automated failure mitigation.
- Enable software-defined networking software to easily control all hardware elements in the network using a unified structure to eliminate duplication and reduce failures.

Microsoft open-sourced this innovation to the community, making it available on [SONiC GitHub](https://azure.github.io/SONiC/) repository.  It can **run on various switching platforms conformant to the [SAI](#sai) Switch Abstraction Interface specification**. SONiC enables cloud operators to take advantage of hardware innovation while giving them a **framework to build upon an open source code for network switch apps and the ability to integrate with multiple platforms**.  For more information, see [SONiC: The networking switch software that powers the Microsoft Global Cloud](https://azure.microsoft.com/en-us/blog/sonic-the-networking-switch-software-that-powers-the-microsoft-global-cloud/). 


![Sonic-context](../media/generic/SONiC-context.jpg)
<figcaption><i>Simplified view of the SONiC context</i></figcaption><br/>

#### SONiC and the OCP community ####

The OCP is the best platform to grow a fully open sourced stack holistically from the ground up. Open sourcing SONiC under the OCP umbrella is a logical step to growing the stack holistically at the OCP. SONiC brings together all the **building blocks to form an open sourced, fully functional, secure, and reliable cloud switch**. It gives the freedom to choose the hardware and software that is best suited for the required networking needs.

SONiC integrates with the standardized [SAI](#sai) interface and allows to exploit new hardware faster and enables to keep the pace with [ASIC](#asic) innovation while simultaneously being able to operate on multiple platforms. Initial contributions of SONiC also come with supported open source platform drivers for certain switches, enabling SONiC to run as a fully functional Layer2/Layer3 switch.

All his can be extended into a new scenario where Linux distributions could offer support for SONiC and SAI through kernel modules. More vendors can open source their platform drivers. Existing OCP certified switches can integrate with SAI via the Open Network Linux (ONL). Additionally, more software components can be open sourced.

#### SONiC and SAI ####

[SAI](#sai) is a key step towards open networking and a stepping stone to SONiC. Since its inception, SAI continues to grow within the community, attracting increasing numbers of contributors, consumers and features. Some SAI contributors fro SONiC adoption are Barefoot Networks, Broadcom, Cavium, Centec, Dell, Mellanox and Metaswitch.

After being accepted by the OCP, SAI is includes key features such as unified tunneling, an approach to have common APIs to address tunnels and L3 ingress and egress interfaces, and warm reboot, in service restart and upgrade of SAI without impacting the data plane. This is in addition to features that ensure full L3 routing functionality as well as other complex features such as Quality of Service (QoS). It also introduced a Python Test Framework (PTF), an effort to drive towards SAI compliancy at the OCP.

Both SAI and SONiC are available in binary and source code for vendor supported platforms. As a consumer, you can either get a binary or build one depending on supported platforms and versions for both SAI and SONiC to prototype your own data center switch. As a contributor, developers can contribute to both SAI and SONiC via the GitHub repositories. 

#### SONiC ecosystem ####

The following are highlights of the ecosystem in which SONiC operates.

![Sonic-ecosystem](../media/generic/SONiC-ecosystem.jpg)
<figcaption><i>Simplified view of the SONiC ecosystem</i></figcaption><br/>

##### Network switch ASICs #####

An **Application specific integrated circuit (ASIC)** is purpose built for a particular use. In this case, these are built to provide as much network throughput as possible. They are two orders of magnitude faster than general purpose CPUs for forwarding packets. While these ASICs can do x Billion PPS, with careful software work, CPUs can do x 10s of Millions PPS. For more information, see [ASIC](#asic).

##### Network switch hardware #####

A network switch (also called switching hub, bridging hub, and, by the IEEE, MAC bridge) is networking hardware that connects devices on a computer network by using packet switching to receive and forward data to the destination device. For more information, see [Switch](#switch). 


### Switch ###

A **network switch** (also called switching hub, bridging hub, and, by the IEEE, MAC bridge) is networking hardware that connects devices on a computer network by using packet switching to receive and forward data to the destination device.

A network switch is a multiport network bridge that uses MAC addresses to forward data at the data link layer (layer 2) of the OSI model. Some switches can also forward data at the network layer (layer 3) by additionally incorporating routing functionality. Such switches are commonly known as layer-3 switches or multilayer switches. For more information, see [Network switch](https://en.wikipedia.org/wiki/Network_switch). 

## V ##

### VNET ###

The **Azure Virtual Network (VNET)** is a basic building block of the Azure Virtual Networking. VNET is an collection of address space in datacenter networking which is very critical for proper Network design. You need VNET to deploy VMs in Azure. VMs deployed in same VNET can talk to each other. You don’t need to enable any routing to make it work. In other words, routing is configured by default between subnets created in the same VNET. However, if you need to connect to the services outside a VNET, you need to establish site to site VPN. It needs a component called as Azure Virtual Network Gateway. For more information, see [Key terminology for Azure Networking](https://www.vembu.com/blog/key-terminology-azure-networking/).

### VPC ###

The **virtual private cloud (VPC)** is an on-demand configurable pool of shared resources allocated within a public cloud environment, providing a certain level of isolation between the different organizations, denoted as users, using the resources. The isolation between one VPC user and all other users of the same cloud (other VPC users as well as other public cloud users) is achieved normally through allocation of a private IP subnet and a virtual communication construct (such as a VLAN or a set of encrypted communication channels) per user. In a VPC, the previously described mechanism, providing isolation within the cloud, is accompanied with a [VPN](#vpn) function (again, allocated per VPC user) that secures, by means of authentication and encryption, the remote access of the organization to its VPC resources. With the introduction of the described isolation levels, an organization using this service is in effect working on a 'virtually private' cloud (that is, as if the cloud infrastructure is not shared with other users), and hence the name VPC. For more information see [Virtual private cloud](https://en.wikipedia.org/wiki/Virtual_private_cloud). 

### VPN ###

The **virtual private network (VPN)** extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network. The benefits of a VPN include increases in functionality, security, and management of the private network. It provides access to resources inaccessible on the public network and is typically used for telecommuting workers. Encryption is common, although not an inherent part of a VPN connection.

A VPN is created by establishing a virtual point-to-point connection through the use of dedicated circuits or with tunneling protocols over existing networks. A VPN available from the public Internet can provide some of the benefits of a wide area network (WAN). From a user perspective, the resources available within the private network can be accessed remotely. For more information see [Virtual private network](https://en.wikipedia.org/wiki/Virtual_private_network)


<br/><br/>

<hr style="border-top: 2px dashed yellow"/>

## References ##

- [SONiC Wiki](https://azure.github.io/SONiC/)
- [SONiC Source Repositories](https://github.com/Azure/SONiC/blob/master/sourcecode.md)
- [Microsoft showcases “Software for Open Networking in the Cloud (SONiC)](https://azure.microsoft.com/en-us/blog/microsoft-showcases-software-for-open-networking-in-the-cloud-sonic/)
- [Network Basics](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)
- [Gartner technology glossary ](https://www.gartner.com/en/information-technology/glossary?glossaryletter=A)


[LPM](https://en.wikipedia.org/wiki/Longest_prefix_match)
[DPDK](https://blog.selectel.com/introduction-dpdk-architecture-principles/)





