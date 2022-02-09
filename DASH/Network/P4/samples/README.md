**Table of contents**
- [P4 samples](#p4-samples)
  - [Prerequisites](#prerequisites)
  - [P4 samples collection](#p4-samples-collection)
    - [P4 tutorial samples](#p4-tutorial-samples)
    - [P4 fingerhut's samples](#p4-fingerhuts-samples)
  - [References](#references)

# P4 samples

The samples shown here can be found in the public GitHub repository: [P4 Tuorials](https://github.com/p4lang/tutorials) and also [Guide to the included demo programs](https://github.com/jafingerhut/p4-guide/blob/master/README-demos.md#guide-to-the-included-demo-programs) by jafingerhut. 
We'll note it in the examples related documentation as appropriate.

## Prerequisites

- Create a virtual machine to run the examples. For related information, see [How to Install VirtualBox on Ubuntu](../../../Ubuntu/ubuntu-notes.md#how-to-install-virtualbox-on-ubuntu). 
- Activate the virtual machine and clone the sample repositories.
- Follow the steps described in the related documentation for each example.


## P4 samples collection

The following is a colelction of P4 samples. 

![pgm-target-via-p4](../images/pgm-target-via-p4.svg)

### P4 tutorial samples  

|Example|Description|Area|
|--------|-----------|---|
|[basic forwarding](p4-basic-forwarding.md)|Implements basic forwarding for IPv4|Language basics|

### P4 fingerhut's samples  

|Example <img width=200/>|Description|Area <img width=200/>|
|------------------------|-----------|---------------------|
|[simple demo 1](p4-simple-demo1.md)|Compile and execute the program, add table entries to the running program (in real time), send packets to the running program|Language basics|


## References

- [P4 guide](https://github.com/jafingerhut/p4-guide) by jafingerhut
    - [Guide to the included demo programs](https://github.com/jafingerhut/p4-guide/blob/master/README-demos.md#guide-to-the-included-demo-programs)
        - [heavily commented P4_16 program](https://github.com/jafingerhut/p4-guide/blob/master/demo1/demo1-heavily-commented.p4_16.p4)
- [Implementing Basic Forwarding](https://github.com/p4lang/tutorials/tree/master/exercises/basic)
- [Using P4 in Mininet on BMV2](bmv2.md)

