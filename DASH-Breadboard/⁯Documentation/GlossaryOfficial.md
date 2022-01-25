---
title: Glossary
description: Network terminlogy definitions 
author: michael
last update: 12/10/2021
---

<p style="font-size:1.5em;">
<a href="#a" >A</a> <a href="#b">B</a> <a href="#c" >C</a> <a href="#d">D</a> <a href="#e" >E</a> <a href="#f">F</a> <a href="#g" >G</a> <a href="#h">H</a> <a href="#i" >I</a> <a href="#j">J</a> <a href="#k" >K</a> <a href="#l">L</a> <a href="#m" >M</a> <a href="#n">N</a> <a href="#o" >O</a> <a href="#p">P</a> <a href="#q" >Q</a> <a href="#r">R</a> <a href="#s" >S</a> <a href="#t">T</a> <a href="#u" >U</a> <a href="#v">V</a> <a href="#w" >W</a> <a href="#x">X</a> <a href="#y" >Y</a> <a href="#z">Z</a>  
</p>

<hr style="border-top: 2px dashed blue"/>

## A ##

### ACL 
Access Control List

### Appliance ###
Server with SmartNics installed (for CPS performance increase) to accept traffic redirected from the destination host.

### ARP 
Address Resolution Protocol

### ASN 
Autonomous System Number

### AZ
Availability Zones are unique physical locations within a cloud region, designed to provide a software and networking solution to protect against datacenter failures, and to provide increased high availability (HA) to customers. 

## B ##

### BGP 
Border Gateway Protocol

### Baremetal
Entire node not running any custom SDN software (connected to *SDN/VNET* via *intelligent* router/appliance)

### Bump in the wire
Bump = processing engine
2 bidirectional ethernet interfaces (1 for each side of processing engine)
Each direction provides 1/2 the capacity of the NIC.  Ex:  400G provides 200G bump-in-the-wire

## C ##

### Cluster 
Collection of Nodes across different Racks

### Connection 
Control plane communication between sender and receiver (usually involves handshake); any packet that does not hit the 'flow'

### Customer Address 
Address visible inside Customer VM

## D ##

### DC 
Data Center

### DHCP 
Dynamic Host Configuration Protocol (IPv4)

### DHCPv6 
Dynamic Host Configuration Protocol (IPv6)

### DSR 
Direct Server Return

### DSR VIP 
Virtual IP used for Direct Server Return

## E ##

### ELB 
External Load Balancer

### ENI 
Elastic Network Interface.
Eni, Vnic, VPort are used interchangeably. They all in the general sense mean a VM's NIC. 

## F ##

### Flow
Single transposition - Data plane stream of packets between sender and receiver that shares key IP header information. TCP conversation entered into device flow table as defined by Tuple (SrcIP, DestIP, Src Port, Dst Port, Protocol) between source and destination.  May also have modified Tuple attributes in future.

### Flow State Replication (Milestone)
In case of DPU failure, one appliance in passive/ one in active, traffic will switch and 2nd appliance will take over 

### Flow Table
Flow table is view into memory space of a device capturing established TCP connections, tuple information, and current TCP state.

## G ##

### gNMI
Google Network Management Interface. A model-based management API which sits on top of the gRPC messaging protocol. It supports traditional GET/SET/CAPABILITIES semantics as well as subscription-based streaming telemetry. See https://github.com/openconfig/gnmi.

### gRPC 
Google Remote Procedure Call - A high performance, open source universal RPC framework with many language bindings. Supports synchronous as well as streaming operations. Message and RPC semantics are defined using [Google Protobufs](https://developers.google.com/protocol-buffers). See https://grpc.io/

### GW 
Gateway

## H ##

### HA 
High Availability

## I ##

### IPSec 
IPSec tunnel or IPSec device

### ILB 
Internal Load Balancer

### IPv4 
IP protocol Version 4 (ex. `10.1.2.3`)

### IPv6
IP protocol Version 6 (ex. `2001:1234:abcd::1`)

## J ##

### JSON 
JavaScript Script Object Notation

## K ##

## L ##

### LB 
Load Balancer

### LPM 
Longest-Prefix-Match algorithm commonly used in routing

## M ##

### MAC 
MAC Address (Media Access Control)

### Mapping 
Mapping transformation between CA:PA:MAC. 
Integration point between Overlay and Underlay. 
Mappings can be shared; mappings will likely be a set of different global objects, which different policies can potentially refer to.  For example multiple high CPS VMs in the same VNET are sharing the same VNET address space so they can use 1 mapping table, and multiple policies can refer to the same mapping table.  

## N ##

### NA 
Neighbor Advertisement

### NDP 

### NMAgent 
Used to translate APIs to SAI

### Node/Blade 
Single Physical Machine in a Rack

### Northbound interfaces 
Define the way the SDN controller interact with the application plane. Applications and services are components like load-balancers, firewalls, security services and cloud resources. The idea is to abstract the network, so that application developers can connect to the network and make changes to accommodate the needs of the applications without having to understand exactly what that means for the network.

See also [Southbound interfaces](#southbound-interfaces)

### NS 
Neighbor Solicitation

### NVA 
Network Virtual Appliance (VM that might have forwarding or filtering functionality – ex. router or firewall deployed as Linux/Windows VM/baremetal appliance).

### NVGRE/GRE 
Generic Routing Encapsulation (Protocol)

## O ##

### Overlay  
The overlay network is a virtual network that is built on top of the [underlay](#underlay) network infrastructure.
In DASH, the overlay is generated automatically: it = the SDN pipeline tunneling, decapsulation, ST, and overlay ACLs (for example).  The overlay folder is designated for the DASH APIs.  (Please note, the overlay router is not the same as the SONiC router).  The DASH overlay API will be exposed for flexibility (and to refrain from introducing customer attributes into the SAI community).  There will be no overlap between the SAI/DASH APIs and DASH APIs.  For now, we consider the DASH API to be 'NB', SAI is 'SB'.  The Overlay is visible and configured by the end-customers.

## P ##

### P4
Programming Protocol-independent Packet Processors (P4, in other words PPPP that is P4) is a domain-specific language for network devices, specifying how data plane devices (switches, NICs, routers, filters, etc.) process packets. For more information, see [P4 Open-Source Programming Language](https://p4.org/p4-spec/docs/PNA-v0.5.0.html).

### PA 
Provider Address (internal data center address used for routing)

### Peering 
Network relationship between two entities (usually between two VNETs – ex. VNET Peering

### Policies
ACLs + Routes

### Prefix  
For IPv4: (0-32) – example `10.0.0.0/8`
For IPv6: (0-128) – example: `2001:1234:abcd::/48`

### Private Link outbound (Milestone)  
Before we Encap, we Transpose the packet; we transform and uplevel to become IPv6 to IPv6 

### Private Link service (Milestone)  
Destination side of Private Link; packet generated in Private Link arrives at destination - transposed and NAT'd

## Q ##

## R ##

### RA 
Router Advertisement

### Rack 
Standard size DC rack – a physical unit of containment for DC equipment, dependent upon Rack SKU.  Contains varying equipment including such as blades, switches (T0, MGMT, Console), PDUs, Rack Managers, etc…

### Region 
A set of datacenters deployed within a latency-defined perimeter and connected through a dedicated regional low-latency network. 

### RS 
Router Solicitation

## S ## 

### SDN 
Software Defined Networking (high level name for the Virtual Network and its elements)

### SONIC
Software for Open Networking in the Cloud.  See [SONiC](https://azure.github.io/SONiC/).

### Spoof Guard 
Rule put in place to prevent VM from spoofing traffic

### SAI ### 

The **Switch Abstraction Interface** (SAI) is a hardware abstraction model for switching silicon (ASICs). It is an open-source framework that allows ASICs to be represented in software. This means you can use a Broadcom ASIC the same way as one from Mellanox or Cavium XPliant. This framework let developers target switching platforms in an agnostic way; as long as you have the necessary ASIC driver, you’re good to go. SAI locates the abstraction in the **user space**, while other frameworks, such as switchdev, locate the abstraction in the kernel space. Microsoft open-sourced SAI in 2015. 

### SDN ### 

The **Software-defined networking** (SDN) technology is an approach to network management that enables dynamic, programmatically efficient network configuration in order to improve network performance and monitoring, making it more like cloud computing than traditional network management. SDN is meant to address the fact that the static architecture of traditional networks is decentralized and complex while current networks require more flexibility and easy troubleshooting. SDN attempts to centralize network intelligence in one network component by **disassociating the forwarding process of network packets (data plane) from the routing process (control plane)**. 

The **control plane consists of one or more controllers, which are considered the brain of the SDN network where the whole intelligence is incorporated**. However, the intelligent centralization has its own drawbacks when it comes to security, scalability and elasticity and this is the main issue of SDN.

SDN was commonly associated with the OpenFlow protocol (for remote communication with network plane elements for the purpose of determining the path of network packets across network switches) since the latter's emergence in 2011. However, since 2012 OpenFlow for many companies is no longer an exclusive solution, they added proprietary techniques. These include Cisco Systems' Open Network Environment and Nicira's network virtualization platform. For more information, see [Software-defined networking](https://en.wikipedia.org/wiki/Software-defined_networking).

### Smart ToR 

SmartToR (Smart Top-of-Rack), provides fully programmable switching, routing, and L4-L7 services.  
Merchant silicon has evolved from basic L2 switching to highest performance switching and routing solutions. SmartToR supports high-performance, advanced network services. For example, [Trident SmartToR](https://investors.broadcom.com/news-releases/news-release-details/broadcom-breaks-new-ground-trident-smarttor-converging-switching) by BroadCom enables a 100x performance increase with massive capacity: tracking 3 million connections with 3 million connection-level policies, as well as 1 million tunnels and over 1 million stateful counters for metering and telemetry.

See also [ToR](#tor).

### Southbound interfaces 
Define the way the SDN controller interact with the data plane (aka forwarding plane) to make adjustments to the network, so it can better adapt to changing requirements. 

See also [Northbound interfaces](#northbound-interfaces)

## T ##

### TCP 
Transmission Control Protocol

### ToR
Top of the Rack Switch (aka ToR or T0).

A Data Center has racks, each contains several computing devices. The Top of Rack (ToR) allows for network switches to be placed on every rack and the computing devices in the rack to be connected to them. Then these network switches are connected to aggregation switches using fewer cables.

ToR switches also handle operations such as Layer 2 and Layer 3 frame and packet forwarding, data center bridging and the transport of Fiber Channel over Ethernet for the racks of servers connected to them.

The following figure shows a simplified TOR network layout.

![TOR network layout](https://github.com/Azure/DASH/blob/main/Assets/wiki/tor-network-layout.png)


## U ##

### Underlay
The underlay network is the physical infrastructure upon which the [overlay](#overlay) network is built. It is the underlying network responsible for delivery of packets across networks.
In our implementation, it is controlled by SONiC via SAI.  The underlay deals with (for example) packet forwarding, setup of DEST MAC correctly, setup initializations (in a switch) such as 'how many ports available, port speed, FEC settings,', router interfaces, default route, etc...  these underlay header files are NOT automatically generated.  

## V ##

### VFP 
Virtual Filtering Platform

### VIP 
Virtual IP (IP exposed on Load Balancer)

### VM 
Virtual Machine

### VNET 
Virtual Network

### VNI 
VNI (Vnet Identifier) = VXLANID or GRE key

### VPort 
Eni, Vnic, VPort are being used interchangeably. They all in the general sense mean a VM's NIC. 

### VXLAN 
Virtual Extensive Local Area Network (Protocol)

## W ##

## X ##

### XML 
Extensible Markup Language (Format)

## Y ##

## Z ##



