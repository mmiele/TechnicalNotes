/* -*- mode: P4_16 -*- */
/*
Copyright 2017 Cisco Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

/*
 * standard #include in just about every P4 program.  You can see its
 * (short) contents here:
 * https://github.com/p4lang/p4c/blob/master/p4include/core.p4
 */
#include <core.p4>

/* v1model.p4 defines one P4_16 'architecture', which answer questions like: 
 * 1) Is there an ingress and an egress pipeline, or just one?  
 * 2) Where is parsing done, and how many parsers does the target device have?  etc.
 * 
 * You can see its contents here:
 * https://github.com/p4lang/p4c/blob/master/p4include/v1model.p4
 *
 * The standard P4_16 architecture called PSA (Portable Switch Architecture) 
 * version 1.1 was published on November 22, 2018 here:
 * https://p4.org/specs/
 *
 * P4_16 programs written for the PSA architecture should include the file psa.p4 
 * instead of v1model.p4, and several parts of the program after that would use 
 * different extern objects and functions than this example program shows.
 */
#include <v1model.p4>


/*************************************************************************
***************************** HEADERS  ***********************************
*************************************************************************/

/* Header types are required for all headers you want to parse in
 * received packets, or transmit in packets sent. */

header ethernet_t {
    bit<48> dstAddr;
    bit<48> srcAddr;
    bit<16> etherType;
}

header ipv4_t {
    bit<4>  version;
    bit<4>  ihl;
    bit<8>  diffserv;
    bit<16> totalLen;
    bit<16> identification;
    bit<3>  flags;
    bit<13> fragOffset;
    bit<8>  ttl;
    bit<8>  protocol;
    bit<16> hdrChecksum;
    bit<32> srcAddr;
    bit<32> dstAddr;
}


/*************************************************************************
**************************** METADATA  ***********************************
*************************************************************************/

/* "Metadata" is the term used for information about a packet, but
 * that might not be inside of the packet contents itself, e.g. a
 * bridge domain (BD) or VRF (Virtual Routing and Forwarding) id.
 * They can also contain copies of packet header fields if you wish,
 * which can be useful if they can be filled in from one of several
 * possible places in a packet, e.g. an outer IPv4 destination address
 * for non-IP-tunnel packets, or an inner IPv4 destination address for
 * IP tunnel packets.
 *--------------------------------------------------------------------
 * You can define as many or as few structs for metadata as you wish.
 * Some people like to have more than one struct so that metadata for
 * a forwarding feature can be grouped together, but separated from
 * unrelated metadata. 
 */

struct fwd_metadata_t {
    bit<32> l2ptr;
    bit<24> out_bd;
}

/* You must also define another type that contains all metadata fields
 * that you use in your program.  It is typically a struct type, and
 * may contain bit vector fields, nested structs, or any other types
 * you want. */

struct metadata_t {
    fwd_metadata_t fwd_metadata;
}

/* The v1model.p4 and psa.p4 architectures require you to define one
 * type that contains instances of all headers you care about, which
 * will typically be a struct with one member for each header instance
 * that your parser code might parse.
 */

 struct headers_t {
    ethernet_t ethernet;
    ipv4_t     ipv4;
}

 
/* Instances of these two types are then passed as parameters to the
 * top level controls defined by the architectures.  For example, the
 * ingress parser takes a parameter that contains your header type as
 * an 'out' parameter, returning filled-in headers when parsing is
 * complete, whereas the ingress control block takes that same
 * parameter with direction 'inout', since it is initially filled in
 * by the parser, but the ingress control block is allowed to modify
 * the contents of the headers during packet processing.
 *-------------------------------------------------------------------
 * Note: If you ever want to parse an outer and an inner IPv4 header
 * from a packet, the struct containing headers that you define should
 * contain two members, both with type ipv4_t, perhaps with field
 * names like "outer_ipv4" and "inner_ipv4", but the names are
 * completely up to you.  Similarly the struct type names 'metadata'
 * and 'headers' can be anything you want to name them. */


/*************************************************************************
*********************** P A R S E R  ***********************************
*************************************************************************/

/* The ingress parser here is pretty simple.  It assumes every packet
 * starts with a 14-byte Ethernet header, and if the ethernet type is
 * 0x0800, it proceeds to parse the 20-byte mandatory part of an IPv4
 * header, ignoring whether IPv4 options might be present. 
 * The parser FSM below has three states.*/

parser parserImpl(packet_in packet,
                  out headers_t hdr,
                  inout metadata_t meta,
                  inout standard_metadata_t stdmeta)
{
    // Defien ethernet type. 
    const bit<16> ETHERTYPE_IPV4 = 16w0x0800;

    /* A parser is specified as a finite state machine, with a 'state'
     * definition for each state of the FSM.  There must be a state
     * named 'start', which is the starting state.  
     * The 'transition' statement indicates what the next state is going to be. 
     * Also, there are special states 'accept' and 'reject' indicating that parsing is
     * complete. Where 'accept' indicates no error during parsing, and
     * 'reject' indicates some kind of parsing error. */

    /* First state is the start state.
     * The parser's execution model starts with a 'pointer' 
     * to the beginning of the received packet. */
    state start {
        transition parse_ethernet;
    }

    // Second state is the parse_ethernet state.
    state parse_ethernet {

         /* The extract() is the name of a method defined for packets,
         * declared in core.p4 #include above.  The parser's
         * execution model starts with a 'pointer' to the beginning of
         * the received packet. 
         * Whenever you call the extract() method, it takes the size of the 
         * argument header in bits B, copies the next B bits from the packet 
         * into that header (making that header valid), and advances the pointer 
         * into the packet by B bits.  Some P4 targets, such as the
         * behavioral model called BMv2 simple_switch, restrict the
         * headers and pointer to be a multiple of 8 bits. */
        packet.extract(hdr.ethernet);

        /* The 'select' keyword introduces an expression that is like
         * a C 'switch' statement, except that the expression for each
         * of the cases must be a state name in the parser.  This
         * makes convenient the handling of many possible Ethernet
         * types or IPv4 protocol values. */
        transition select(hdr.ethernet.etherType) {
            ETHERTYPE_IPV4: parse_ipv4;
            default: accept;
        }
    }

    // Third state is the parse_ipv4 state.
    state parse_ipv4 {
        packet.extract(hdr.ipv4);
        transition accept;
    }
}


/*************************************************************************
******************************  PIPELINE   *******************************
*************************************************************************/

/* This example program is for a P4 target architecture that has an ingress
 * and an egress match-action 'pipeline'.
 * Notice that the P4 language does not require that the target hardware 
 * must have a pipeline in it, but 'pipeline' is the word often used since 
 * the current highest performance target devices do have one.
 */

/* The ingress match-action pipeline specified here is very small with
 * simple tables applied in sequence, each with simple actions. */

/*************************************************************************
**************  I N G R E S S   P R O C E S S I N G   *******************
*************************************************************************/



control ingressImpl(inout headers_t hdr,
                    inout metadata_t meta,
                    inout standard_metadata_t stdmeta)
{
     /*
     * Why bother creating an action that just does one primitive
     * action?  That is, why not just use 'mark_to_drop' as one of the
     * possible actions when defining a table?  Because the P4_16
     * compiler does not allow primitive actions to be used directly
     * as actions of tables.  You must use 'compound actions',
     * i.e. ones explicitly defined with the 'action' keyword like
     * below.
     *
     * mark_to_drop is an extern function defined in v1model.h,
     * implemented in the behavioral model by setting an appropriate
     * 'standard metadata' field with a code indicating the packet
     * should be dropped.
     *
     * See the following page if you are interested in more detailed
     * documentation on the behavior of mark_to_drop and several other
     * operations in the v1model architecture, as implemented in the
     * open source behavioral-model BMv2 software switch:
     * https://github.com/p4lang/behavioral-model/blob/master/docs/simple_switch.md
     */
    action my_drop() {
        mark_to_drop(stdmeta);
    }


    action set_l2ptr(bit<32> l2ptr) {
        meta.fwd_metadata.l2ptr = l2ptr;
    }
    table ipv4_da_lpm {
        key = {
            /* lpm means 'Longest Prefix Match'.  It is called a
             * 'match_kind' in P4_16, and the two most common other
             * choices seen in P4 programs are 'exact' and
             * 'ternary'. */
            hdr.ipv4.dstAddr: lpm;
        }
        actions = {
            set_l2ptr;
            my_drop;
        }
        /* If at packet forwarding time, there is no matching entry
         * found in the table, the action specified by the
         * 'default_action' keyword will be performed on the packet.
         *
         * In this case, my_drop() is only the default action for this
         * table when the P4 program is first loaded into the device.
         * The control plane can choose to change that default action,
         * via an appropriate API call, to a different action.  If you
         * put 'const' before 'default_action', then it means that
         * this default action cannot be changed by the control
         * plane. */
        default_action = my_drop;
    }

    /* If the control plane adds an entry to this table and chooses
     * for that entry the action set_bd_dmac_intf, it must specify
     * values for the dstAddr and egress??. */

    action set_bd_dmac_intf(bit<24> bd, bit<48> dmac, bit<9> intf) {
        meta.fwd_metadata.out_bd = bd;
        hdr.ethernet.dstAddr = dmac;
        stdmeta.egress_spec = intf;
        hdr.ipv4.ttl = hdr.ipv4.ttl - 1;
    }
    table mac_da {
        key = {
            /* Perform a 'match_kind' in P4_16. */
            meta.fwd_metadata.l2ptr: exact;
        }
        actions = {
            set_bd_dmac_intf;
            my_drop;
        }
        /* If at packet forwarding time, there is no matching entry
         * found in the table, the action specified by the
         * 'default_action' keyword will be performed on the packet.
         */
        default_action = my_drop;
    }

    /* Every control block must contain an 'apply' block.  The
     * contents of the apply block specify the sequential flow of
     * control of packet processing, including applying the tables you
     * wish, in the order you wish.
     *
     * This one is particularly simple -- always apply the ipv4_da_lpm
     * table, and regardless of the result, always apply the mac_da
     * table.  It is definitely possible to have 'if' statements in
     * apply blocks that handle many possible cases differently from
     * each other, based upon the values of packet header fields or
     * metadata fields. */
    apply {
        ipv4_da_lpm.apply();
        mac_da.apply();
    }
}


/*************************************************************************
****************  E G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

/* The egress match-action pipeline is even simpler than the one for
 * ingress. */

control egressImpl(inout headers_t hdr,
                   inout metadata_t meta,
                   inout standard_metadata_t stdmeta)
{
    
    action my_drop() {
        mark_to_drop(stdmeta);
    }
    
    // Reassign the mac address.
    action rewrite_mac(bit<48> smac) {
        hdr.ethernet.srcAddr = smac;
    }
    table send_frame {
        key = {
            /* Perform a 'match_kind' in P4_16. */
            meta.fwd_metadata.out_bd: exact;
        }
        actions = {
            rewrite_mac;
            my_drop;
        }
        /* If at packet forwarding time, there is no matching entry
         * found in the table, the action specified by the
         * 'default_action' keyword will be performed on the packet.
         */
        default_action = my_drop;
    }

    apply {
        send_frame.apply();
    }
}


/*************************************************************************
***********************  D E P A R S E R  *******************************
*************************************************************************/

/* The deparser controls what headers are created for the outgoing
 * packet. */
 
control deparserImpl(packet_out packet,
                     in headers_t hdr)
{
    apply {
        packet.emit(hdr.ethernet);
        packet.emit(hdr.ipv4);
    }
}


/*************************************************************************
************   C H E C K S U M    V E R I F I C A T I O N   *************
*************************************************************************/

/* In the v1model.p4 architecture this program is written for, there
 * is a 'slot' for a control block that performs checksums on the
 * already-parsed packet, and can modify metadata fields with the
 * results of those checks, e.g. to set error flags, increment error
 * counts, drop the packet, etc. */

control verifyChecksum(inout headers_t hdr, inout metadata_t meta) {
    apply {
        verify_checksum(hdr.ipv4.isValid() && hdr.ipv4.ihl == 5,
            { hdr.ipv4.version,
                hdr.ipv4.ihl,
                hdr.ipv4.diffserv,
                hdr.ipv4.totalLen,
                hdr.ipv4.identification,
                hdr.ipv4.flags,
                hdr.ipv4.fragOffset,
                hdr.ipv4.ttl,
                hdr.ipv4.protocol,
                hdr.ipv4.srcAddr,
                hdr.ipv4.dstAddr },
            hdr.ipv4.hdrChecksum, HashAlgorithm.csum16);
    }
}

control updateChecksum(inout headers_t hdr, inout metadata_t meta) {
    apply {
        update_checksum(hdr.ipv4.isValid() && hdr.ipv4.ihl == 5,
            { hdr.ipv4.version,
                hdr.ipv4.ihl,
                hdr.ipv4.diffserv,
                hdr.ipv4.totalLen,
                hdr.ipv4.identification,
                hdr.ipv4.flags,
                hdr.ipv4.fragOffset,
                hdr.ipv4.ttl,
                hdr.ipv4.protocol,
                hdr.ipv4.srcAddr,
                hdr.ipv4.dstAddr },
            hdr.ipv4.hdrChecksum, HashAlgorithm.csum16);
    }
}

/*************************************************************************
***********************  S W I T C H  *******************************
*************************************************************************/
/* This is a "package instantiation".  There must be at least one
 * named "main" in any complete P4_16 program.  It is what specifies
 * which pieces to plug into which "slot" in the target
 * architecture. */

V1Switch(parserImpl(),
         verifyChecksum(),
         ingressImpl(),
         egressImpl(),
         updateChecksum(),
         deparserImpl()
) main;
