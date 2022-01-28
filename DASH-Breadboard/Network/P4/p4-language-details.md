---
title: P4 language details
description: Learning P4 language
author: michael
last update: 01/24/2022
---

# P4 language details


## Background


The P4 language was desogned based on the following main requirements:

1. **Reconfigurability**. Programmers should be able
to change the way switches process packets once they are
deployed. 
1. **Protocol independence**. Switches should not be tied to any specific network protocols.
1. **Target independence**. Programmers should be able to describe packet processing functionality independently of the specifics of the underlying hardware. 


We'll show an example on how to use P4 to configure a switch to add a new hierarchical label.

From [Programming Protocol-Independent Packet Processors](https://www.cs.princeton.edu/~jrex/papers/of2.pdf)


## Overview

The **Programming Protocol-independent Packet Processors** (P4) is a domain-specific language that is designed to be implementable on a large variety of targets including programmable **network interface cards** (NIC), **FPGAs**, **software switches**, and **hardware ASICs**. As such, the language is restricted to constructs that can be efficiently implemented on all of these platforms. 

The P4 language itself is meant to implement an abstraction on top of compliant hardware. This abstraction will support the dual modes of hardware operation: **configuration** and **population**. 
In order to do so, a P4 program contains definitions of the following key components:

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


## Hardware assumptions

P4 is intended to be target-independent so that one P4 program can be compiled to switches supplied by multiple
different vendors. Compliant hardware platforms will have to satisfy some basic requirements:

1. The switch must support two modes of execution:
    1. A **configuration mode** in which information about **packet formats** and the **structure of match+action tables** 
    is communicated to the switch for planning purposes.
    1. A **population mode** in which **rules** conforming to the specifications are **added and removed from the tables**. 
    
1. To implement P4 in its full generality, it must be possible to **configure the hardware’s packet parser** to identify and 
extract new fields from a packet. 
1. Tables within the target must support matching of all defined fields. 
1. The target must support implementation of a range of protocol-independent packet-processing primitives, 
including **copying**, **addition**, **removal**, and **modification** of both old and new fields as well as metadata.

This model makes more requirements of the underlying hardware than conventional OpenFlow. In particular, 

- OpenFlow assumes a fixed parser, whereas P4 model supports a **programmable parser** that allows new headers to be defined.
- OpenFlow assumes the **match+action tables** are laid out in sequence whereas P4 supports both sequential and parallel
processing units. 
- Finally, P4 requires **actions to be defined using reusable, protocol-independent primitives**.


## Analyzing P4 program structure 

From [Programming Protocol-Independent Packet Processors](https://www.cs.princeton.edu/~jrex/papers/of2.pdf). 


The P4 language implements an abstraction on top of compliant hardware. 
This abstraction supports the dual modes of hardware operation: switch **configuration** and **population**. 
In order to do so, a P4 program contains definitions of the following key components:

- **Headers**. A header definition describes the sequence and structure of a series of fields. It includes information
about field width, as well as constraints on field values.
- **Parsers**. A parser definition determines the presence and order of headers within a packet.
- **Tables**. **Match+action tables** are the mechanism for packet processing. The P4 program defines the fields on which a
table may match and the actions it may execute.
- **Actions**. P4 supports construction of complex actions from simpler protocol-independent primitives. 
These complex actions are available within **match+action tables**.
- **Control Program**. The control program determines the order of matches and actions that are applied to a packet. 
Simple imperative programs describe the flow of control between match+action tables.


This section shows how each of the components described above contributes to the definition of an **idealized mTag packet processor** in P4.
The mTag combines the hierarchical routing with simple tags. In particular

- The routes through the core are encoded by a **32-bit tag** composed of **four single-byte fields**. 
- The 32-bit tag can carry a **source route** or a **destination locator** (like a Pseudo MAC). 
- Each core switch need only examine one byte of the tag and switch on that information.

In the example, the tag is added by the first ToR switch, although it could also be added by the end-host NIC.


### Header formats

A P4 program design begins with the **specification of header formats**.
Several domain-specific languages have been proposed and P4 borrows a number of ideas from them.
In general, each header is specified by declaring an **ordered list of field names along with their widths**. 
Optional field annotations allow constraints on value ranges or maximum lengths for variable-sized fields. 
For example, standard **Ethernet** and **VLAN** headers are specified as follows:

```p4
header ethernet {
    fields {
        dst_addr : 48; // width in bits
        src_addr : 48;
        ethertype : 16;
    }
}

header vlan {
    fields {
        pcp : 3;
        cfi : 1;
        vid : 12;
        ethertype : 16;
    }
}
```

The **mTag** (custom) header can be added without altering existing declarations. 

- The **field names indicate that the core has two layers of aggregation**. 
- Each **core switch** is programmed with rules to examine one of the specified bytes depending on its location in the hierarchy 
and the direction of travel (up or down).

```p4
header mTag {
    fields {
        up1 : 8;
        up2 : 8;
        down1 : 8;
        down2 : 8;
        ethertype : 16;
    }
}
```

### Packet parser

P4 assumes the following:

- The underlying switch can implement a **state machine** that **traverses packet headers** from start to finish, **extracting field values** as it goes. 
- The **extracted field values** are sent to the **match+action tables for processing**.

P4 **describes this state machine** directly as the **set of transitions from one header to the next**. 
Each transition may be triggered by values in the preceding header. 

The following example describes the **mTag state machine**. The parser for mTag is very simple—it has just four different states. Parsers in real networks require many more states.

```p4
// start state
parser start{
    ethernet;
}

// ethernet state
parser ethernet {
    switch(ethertype) {
        case 0x8100: vlan;
        case 0x9100: vlan;
        case 0x800: ipv4;
        // Other cases
    }
}

// vlan state
parser vlan {
    switch(ethertype) {
        case 0xaaaa: mTag;
        case 0x800: ipv4;
        // Other cases
    }
}

// mTag state
parser mTag {
    switch(ethertype) {
        case 0x800: ipv4;
        // Other cases
    }
}
```
The folllowing are the state machine steps:

1. Parsing begins in the **start state** and proceeds until an explicit **stop state** is reached or an unhandled case is encountered (which may be marked as an error). 
1. Upon reaching a state for a new header, the state machine extracts the header using its specification and proceeds to compute its next transition. 
1. The extracted header is **forwarded to match+action processing** in the back-half of the switch pipeline.


### Table specification

The programmer describes how the defined **header fields are to be matched in the match+action stages**. For example, should they be 
exact matches, ranges, or wildcards?, and what actions should be performed when a match occurs.

In the simple mTag example, the **edge switch matches on the L2 destination and VLAN ID**, and **picks an mTag to add to the header**. 

The programmer therefore specifies a table to match on these fields, with the action to add the mTag header. 

The **reads attribute** declares which fields to match, qualified by the match type (exact, ternary, etc).
The **actions attribute** lists the possible actions which may be applied to a packet by the table.  Actions are explained in the following section. 
The max size attribute specifies how many entries the table should support.
The table specification allows a compiler to decide how much memory it needs, and the type (e.g., TCAM or SRAM) to implement the table.

```p4
table mTag_table {
    reads {
        ethernet.dst_addr : exact;
        vlan.vid : exact;
    }
    actions {
        // At runtime, entries are programmed with params
        // for the mTag action. See below.
        add_mTag;
    }
    max_size : 20000;
}
```

For completeness and for later discussion, we present brief definitions of other tables that are referenced by the control program (control plane).

```p4
table source_check {
    // Verify mtag only on ports to the core
    reads {
    mtag : defined; // Was mtag parsed?
    metadata.ingress_port;
    }
    actions {
    // If inappropriate mTag, send to CPU
    fault_to_cpu;
    // If mtag found, strip and record in metadata
    strip_mtag;
    // Otherwise, allow the packet to continue
    pass;
    }
    max_size : 64; // One rule per port
}
```

```p4
    table local_switching {
    // Reads destination and checks if local
    // If miss occurs, goto mtag table.
    }
```

```p4
    table egress_check {
    // Verify egress is resolved
    // Do not retag packets received with tag
    // Reads egress and whether packet was mTagged
}
```

### Action specifications
P4 defines a collection of primitive actions from which more complex actions are built. 
To keep the table specification simple, actions are defined in action functions. 
Each P4 program declares **its own action functions**.

The add mTag action referred above is implemented as follows:

```p4
action add_mTag(up1, up2, down1, down2, egr_spec) {
    add_header(mTag);
    // Copy VLAN ethertype to mTag
    copy_field(mTag.ethertype, vlan.ethertype);
    // Set VLAN’s ethertype to signal mTag
    set_field(vlan.ethertype, 0xaaaa);
    set_field(mTag.up1, up1);
    set_field(mTag.up2, up2);
    set_field(mTag.down1, down1);
    set_field(mTag.down2, down2);
    // Set the destination egress port as well
    set_field(metadata.egress_spec, egr_spec);
}
```
If an action needs parameters (e.g., the up1 value for the mTag), it is supplied **from the match table at runtime**.

In this example, the switch performs the following actions:

- Inserts the mTag after the VLAN tag.
- Copies the VLAN tag’s ethertype into the mTag to indicate what follows.
- Sets the VLAN tag’s ethertype to `0xaaaa` to signal mTag. 

The programmer would also define a table and action to strip mTags from packets in
the egress edge switch. This action would copy the mTag’s ethertype back to the VLAN tag.

P4’s primitive actions include:
- set field: Set a specific field in a header to a value. Masked sets are supported.
- copy field: Copy one field to another.
- add header: Set a specific header instance (and all its fields) as valid.
- remove header: Delete (“pop”) a header (and all its fields) from a packet.
- increment: Increment or decrement the value in a field.
- checksum: Calculate a checksum over some set of header fields (e.g., an IPv4 checksum).

It is expected that most switch implementations would restrict action processing to permit only header modifications that are consistent with the specified packet format.

### Control program

Once **tables** and **actions** are defined, the only remaining task is to specify the **flow of control from one table to the next**. 
**Control flow** is specified as a program via a collection of:
- functions
- conditionals
- table references

**mTag control flow**

![p4-mtag-control-flow](./images/p4-mtag-control-flow.png)

The previous figure shows the control flow for the **mTag implementation on edge switches**. 
After parsing, the `source_check` table verifies consistency between the received packet and the ingress port. 
For example, mTags should only be seen on ports connected to core switches. This table also strips mTags from the packet, but records whether the packet had an mTag in metadata. 
Tables later in the pipeline may analyze the metadata to avoid retagging the packet.
A `local_switching` table is then executed. If this table *misses*, it indicates that the packet is not destined for a locally connected host. 
In that case, the `mTag-table` is applied to the packet. 
Both **local** and **core forwarding** control can be processed by the `egress_check` table which handles the case of an unknown destination by
sending a notification up the SDN control stack. 
The imperative representation of this packet processing pipeline is as follows:


```P4
control main() {
    // Verify mTag state and port are consistent
    table(source_check);
    // If no error from source_check, continue
    if (!defined(metadata.ingress_error)) {
        // Attempt to switch to end hosts
        table(local_switching);
        if (!defined(metadata.egress_spec)) {
        // Not a known local host; try mtagging
        table(mTag_table);
        }
    // Check for unknown egress state or
    // bad retagging with mTag.
    table(egress_check);
    }
}

```

## Compiling a program 

For a network to implement a P4 program, you need a compiler to **map the target-independent description** onto
the **target switch’s specific hardware or software platform**.

This involves **allocating the target’s resources** and **generating appropriate configuration** for the device.

### Compiling packet parser

For devices with programmable parsers, the compiler **translates the parser description into a parsing state machine**.
For fixed parsers, the compiler merely verifies that the parser description is **consistent with the target’s parser**. 

The following table shows state table entries for the vlan and mTag
sections of the parser. Each entry specifies the current state, the field value to match, and a next state. 
Other columns are omitted for brevity.

**Parser state table entries for the mTag**

|current state|lookup value|next state|
|-------------|------------|----------|
| vlan | 0xaaaa| mTag|
| vlan | 0x800 | ipv4|
| vlan| * | stop |
| mTag | 0x800 | ipv4 |
| mTag | * | stop |



3.2 Compiling Control Programs
The imperative control-flow representation in a convenient way to specify the logical forwarding behavior of a switch, but does not explicitly 
call out dependencies between tables or opportunities for concurrency. We therefore eemploy a compiler to analyze the control program to identify
dependencies and look for opportunities to process header fields in parallel. 
Finally, the compiler generates the target configuration for the switch. There are many potential targets: for example, 
a software switch, a multicore software switch, an NPU, a fixed function switch, or a reconfigurable match table (RMT) pipeline.

We follow a two-stage compilation process. First, we convert the control program to an intermediate table graph representation. 
The table graph is an extension of the tables declared in the P4 program. 
The nodes of the graph are the table declarations, and the edges indicate the order of processing. 
Conditional tests in the control program (e.g., if defined(mTag)) are replaced with “static” table instances with fixed entries whose 
actions determine the next table to execute, rather than populated at runtime.
Second, the compiler analyzes the table graph to generate a device-specific configuration for the target switch. 
Each target supporting P4 requires a dedicated compiler (or compiler back-end) with knowledge of the table resources and
supported parallelism of the target to enable the correct mapping of tables. 
We briefly examine how the mTag example would be implemented in different kinds of switches:
- Software switches: A software switch provides complete flexibility: the table count, table configuration, and parsing
are under software control. The compiler directly maps the mTag table graph to switch tables. 
The compiler uses table type information to constrain table widths, heights, and matching criterion (e.g., exact, prefix, or wildcard) of each
table. The compiler might also optimize ternary or prefix matching with software data structures.
- Hardware switches with RAM and TCAM: A compiler can configure hashing to perform efficient exact-matching using RAM, for the mTag table in edge switches. 
In contrast, the core mTag forwarding table that matches on a subset of tag bits would be mapped to TCAM.
- Switches supporting parallel tables: The compiler can detect data dependencies and arrange tables in parallel or in series. In the mTag example, the tables `local_switching`
and `mTag_table` can execute in parallel up to the execution of the action of setting an mTag. 

## References
- [P4 Network Programming Language—what is it all about?](https://codilime.com/blog/p4-network-programming-language-what-is-it-all-about/). This is a very good starting point; step by step intro. 
- [P4 Language Specification](https://p4.org/p4-spec/p4-14/v1.0.5/tex/p4.pdf#:~:text=The%20P4%20language%20uses%20a%20%EF%AC%82at%20typing%20structure%2C,expressed%20in%20P4%20in%20binary%2C%20decimal%20and%20hexadecimal) PDF format with good diagrams and definitions about the P4 langauge structure. 
- [Programming Protocol-Independent Packet Processors](https://www.cs.princeton.edu/~jrex/papers/of2.pdf). A white paper and another good intro to the language and the underlying principles. 
- [P4 Language Tutorial](https://cs344-stanford.github.io/lectures/Lecture-2-P4-tutorial.pdf) Power point and diagrams.
- [BEHAVIORAL MODEL (bmv2)](https://github.com/p4lang/behavioral-model)
- [Why Does the Internet Need a Programmable Forwarding Plane with Nick McKeown](https://www.youtube.com/watch?v=zR88Nlg3n3g)

