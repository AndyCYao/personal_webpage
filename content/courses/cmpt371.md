title: "Computer Networking"
date: 2017-03-01
semester: "Winter 2017"

## CMPT 371 Computer Networking Winter 2017

## OSI MODEL 7 layers 

Layer 1 Physcial Layer 

Layer 2 Data Link 

Layer 3 Network Layer 

Layer 4 Transport Layer 

Layer 5 Session Layer 

Layer 6 Presentation Layer 

Layer 7 Application Layer 


### Layer 4 Transport Layer 
Provide logical communication between app processes running on different hosts. Provides flow control, segmentation desegmentation, and error control. Creates packets out of messages received from the application layer. 

two main ones are TCP and UDP 

handle data from multiple socket add transport header (multiplex) and use header info to receive segment to correct socket (demultiplex)

#### TCP

#### UDP 
no frill, uses for streaming multimedia (ok with some data loss). less delay due to no need for connection establishment. smaller header size. no congestion control 

UDP has checksum, which detects error

##### Checksum 

##### Parity Check 
Even check or Odd Check 

sender receiver agrees on whether the packet should have even ones or odd ones. 

suppose its even parity 

if the receiver receives a packet with odd 1s, then it knows theres an error 

the parity bit used to make it even, or odd. 

#### Congestion Control 
one of the 'top 10 problem in networking', congestion leads to lost packets, long delays. 

caused by 

- large queuing delay are experienced as the packet arrival rate near the link capacity. 
- sender must perform retransmission in order to compensate for dropped (lost ) packet due to buffer overflow. 
- when packets are dropped along a path, the transmission capacity that was used at each of the upstream link to forward that packet to the point at which it is dropped end up having been wasted. 

Two over arching congest control approach:

1. end to end congestion control - the network layer provides no support to the transport layer for congeston control. TCP uses this end to end approach.

2. Network assisted congestion control - the network layer provides explicit feedback to the sneder regarding the congestion state in the network. such as a confirmation bit. some protocols include 'ATM ABR congestion control' 

##### Available Bit Rate - Resource Management ABR 'Asyncronous Transfer Mode' (ATM)  
Rate based approach. the sender explicitly computes the maximum rate at which it can send packets. 
-uses EFCI bit. explicit forward congestion indication . 1 to signal congestion at destination host. 
-CI and NI bit. congestion indication and no increase (NI) bit 
-ER setting. Explicit Rate(ER field)

##### TCP congestion control - additive increase multiplicative decrease
sender increase transmission rate ( window size). increase cwnd by 1 (cwnd is allowable transmission rate) for every success RTT 

multiplicative decrease. cut cwnd by half after loss 

TCP sending rate - roughly send cwnd bytes. wait RTT for ACKS. then send more bytes 
rate ~~ cwnd/RTT bytes/sec 

Summary --  TCP congestion Control 

Slow start - every successful acknowledge doubles the cwnd. cwnd = cwnd + MSS

Congestion Avoidance - every new ack = cwd=cwnd + MSS * (MSS/cwnd)

#### Reliable Transport Protocol 

#### Pipeline protocol
sender allows multiple inflight yet to be acknowledge packets. this is better than stop and wait, which sends one packet, waits for ACK, then sends the next. 

Stop and Wait's utilization is calculated by 

/$$ U_sender = {L/R}/{RTT + {L/R}}$$

where RTT is the round trip time the sender is waiting 


##### Go-Back-N 
allow to send N amount of unacknowledgeable packets in the pipeline. 

has a base counter and a next sequence number for what is acknowledged. 

1. sender sends N amount of packets out. timer starts nextsequenceNumber gets increment by N amount , If acknowledge received is in sequence, base does as well (this means no packet was lost)
2. if there was an out of sequence acknowlege (call DUPACK), say, 4th packet was lost, then the receiver drops the subsequent packets, and base only gets increment to 4. N gets moved an equal amount.   cumulative acknowledge is tracked by the receiver. time out is incurred for 4th packet
3. timer starts again sender tries again at base 4. continues until it gets through 

##### Selective Repeat 
works similarly as Go-Back-N however, instead of dropping all subsequent packets that follows the lost packet . a selective (individual) acknowledgement is sent per packet. The bufffer is resized to accomodate the out of sync packets. 

### Layer 3 Network Layer 
This layer talks about the specific details of "forwarding" datagrams from one host to another host. and "routing", which is the network wide route taken to go from one point to another.  

## IPv4 addresing:
32 bit long, given as a.b.c.d. IP address has two parts, network part and host id part. both are identified by subnet mask

subnets are groups of devices that share the same subnet part of the ip address. does not need intervening routers to reach each other within. 

#### Classless InterDomain Routing 
subnet portion of address of arbitrary length.

address format: a.b.c.d/x where x is # bits in subnet portion of address 

#### Forwarding Table and Datagram Network 
In a datagram Network (as oppose to virtual ciruit), each packet is pass through series of router, each router uses the packet's destination address to determine its next output link interface. Each router has a forwarding table like below,

Destination Address Range | Link Interface
Prefix matches 			  | 
1						  | 0
10					      | 1
111 					  | 2 
otherwise				  | 3

#### What's inside a router
A router has four components
-Input Port
Handles the transferring of data from the incoming physicial link at the router.
Uses the forwarding table to determine the packet's direction in the switching fabric.
-Switching Fabric 
connects the input port to the output port. behaves like a network inside a router.
-Output Port
Receives the packets from the switching fabric, and transmit them to the outgoing link
-Routing Processor
Handles the routing protocol, maintains te routing table and link state information

*Head of Line Blocking* This is when queued datagrams at front of queue blocks others in the queue from moving forward. (kind of like process starvation in OS)

#### Analogy
Car coming from a highway enters a 'roundabout' that connects to different highway ramp.
there is an attendant who the driver asks for direction, once given the direction, the driver enteres the roundable and continues on his way. 

Car - Packet
Attendant - Routing Processor
Roundabout - Switching Fabric
Highway - Input Port / Output Port

#### Switching Techniques within the Switching Fabric
-Switching Via Memory

behaves like traditional I/O device in operation system. The incoming packet arrives at the processor, the processor copies the packet into its memory. dissects the header for outbound information. then copies the packet into the correct output ports buffer. Two packets canot be forwarded at the same time, *only one memory read write over the shared system bus.* 

-Switching Via Bus

in this type of switch, the incoming packet gets appended with a internal header, the packet then gets sent to *all* the output port without the intervention of the processor. But only the output port that matches whats on the internal header file will process the packet. the internal header label is removed upon switching. 
Note, there is one single bus. so packets have to wait one at a time for its turn. 

-Switching Via Interconnection (CrossBar)

This arrangement connects N input port with N output ports. This switch allows simultaneous forwarding of multiple packets. *Note, if two packets from two diff. input wants to go to the same output port, one would have to go after the other, since only one packet can be sent over any given bus at a time* 

#### Where does queuing occur 
Queuing of the packet can occur at both the input port and output port (before and after the roundable). It depends on the current traffic, the relative speed of the switching fabric, etc. Packet loss occurs when the queue gets too large and theres memory overflow. 

### Maximum Transmission Unit and Datagram
each link has a MTU, the sending host has to stamp the datagram with an ID, break the datagram into chunks that fit the MTU. (with the appropriate space for header size). Remember the offset (which is the start of the next fragment and divided by 8 byte). 

### Hierarchical Routing 
aggregates routers into regions call 'autonomous system', routers in same AS runs same routing protocol, 'intra-AS'. 

To connect with other AS. need to consult the forwarding table, which has both inter and intra AS details. and use the AS protocol.

when the AS knows that its destination can be reach via multiple ASs. It does a 'hot potato routing' it sends packets towards closest of two router. this finds the smallest least cost 

Some Intra - AS Routing include 

##### RIP (Routing Info. Protocol)
the RIP routing table is managed at the application level. and are UDP packets. 
uses distance vector algo. metric max= 15 hops, each link cost 1. 

DV advertises with its neighbour every 30 seconds. and each advertisement lists up to 25 destination subnets. 

if no advertisement heard after 180 sec, neighbor is considered dead. 
the route to that neigh is invalidated. 

not used anymore, because the size of network has increase, so the table has become too cumbersome . so RIP can run only on small network, where max hop count is 15. 
###### Distance Vector , how does it work 
each node keeps a table of distance to reach its neighbour.

*All nodes* then forward this information to its neighbour, the neighbour adjusts accordingly 

the idea is that if no topology changes, the tables would converge in a few rounds. Then the nodes would know the best way to reach wherever. 

no node has global knowledge, yet was able to find the info of the whole network. 

fully distributed

Distance vector is prone to 'counting to infinity problem', that is, neighbour still using out of date routing info while sending packet, not knowing that the best path has changed. 

Theres a 'Poisoned Reverse' that trys to solve this problem. which is , while the packet is looping, it hardcodes the original sender that distance is infinite, so in effect forces updates the senders table. 


##### OSPF (Open Shortest Path First)
uses link state algo. LS packet dissemination. uses dijkstra's algo. 
OSPF advertisement carries one entry per neighbour 
advertisement floods to entire AS. 
carries OSPF message over IP rather than TCP or UDP 

all OSPF message authenticated. 
multiple same cost paths are allowed 

multiple cost metrics can be considered 

hierarchical OSPF has two level hierarchy.

##### Border Gateway Protocol:
is the default inter-domain routing protocol. 'glue that holds internet together'

has external BGP. 

and 

iBGP internal

determines good routes to other networks based on reachability information and policy. 

Advertises prefixes, which 'promise' it will forward datagram towards that prefix. 

BGP message exchanged between peers over TCP connection. (open, update, keep alive, notification)

#### Why different Intra - , inter-AS routing?
Inter-AS , different admin might want to control how its traffics are routed. 

Scale - hierarchical routing saves table size. 

Performance - 
intra-AS . can focus on performance
inter-AS .  policy may dominate performance. 


##### IGRP (Interior Gateway routing Protocol (Cisco Proprietary))

#### Network Address Translation (NAT)
in small business, home offices, and other 'realm' private small scale networks. they all share the same internal address space. 10.0.0.0/8. Outside packets coming in and local device going out would need to go through a NAT enabled router, and modify their sender and receiver address respectively. 

The NAT router is hiding the details of the home network to the outside world. 

Arguments against using NAT 

- port numbers are meant to be used for addressing processes not for addresing hosts. this cause problems for servers running on the home network, since server processes wait for incoming request at wellknown port numbers. 
- routers are suppose to process packets only up to layer 3. 
- NAT protocol violates so call end-to-end argument. that hosts should be talking directly with each other, without interfering nodes modifying IP addreses and port number. 
- Should use IPv6 to solve the shortage of IP address, rather than patch with a stop gap solution like NAT. 

##### Universal Plug and Play (UPnP)
this is a solution to the server behind NAT problem. in situations such as bit torrent where people have to upload data. the UPnP asks the NAT to create a hole by mapping your host address to a NAT public port. that way, bit torrent can advertise this port and exchange packets throguh this. 

#### IPv6
Introduced in the 1990s, increased IP address from 32 bit to 128 bit. 

Anycast address - which allows datagram to deliver to any group of hosts. 

40 byte header - fixed length allow for faster processing of IP datagram. 

Datagram format include 

- Version Traffic class Flow label 
- Payload length , next header, hop limit
- Source Address 
- Destination Address 
- Data 

IPv6 dropped fragmentation/reassembly , they felt this should be done at the source , not in intermediate process 

they also dropped Header checksum, as both transport layer (TCP and UDP) and link layer (ethernet) already does checksum 

##### Transition from IPv4 to IPv6 
its very difficult to move network layer protocol - its like replacing foundation of a house. most IPv6 has backwards integration to IPv4 to accomodate. 

### Layer 2 Link Layer
This layer deals with how datagrams are encapsulated in this level (call framing)

other possible services include:
1. Medium Access Control - a protocol that deals with how frames are transmitted onto the link 
2. Reliable Delivery - to guarantee the datagrams move across link without error. (this is used more in wireless links, where theres more error rate)
3. Error Detection and Correction - due to electrical issues and magnetic noise, sometimes bit errors are introduced. Link layer hardware have to check for errors using internet checksum. 

Link layer is implemented at the network adapter level, so hardware stuff. 

#### Analogy
Travel Agent plans a tourist to travel from City A to City B. In which the tourist takes a car, an airplane, then a train. 

Tourist - Datagram
Plane, Car, Train are - Various links
Transportation Mode - is a link layer protocol.
Travel Agent - Routing Protocol.

#### Terminologies
*Node* - anything that runs a link layer. such as hosts, routers, switches, WIFI access points. 


#### Broadcast Channel
BC contains multiple hosts like wireless LAN, satellite network, hybrid fiber coaxial cable. (think cocktail party, one person speaks at a time and the group listens.) 
This needs a specific protocol call *multiple access protocool* to decide who's turn is it to speak.

In general, the protocol has the following idea
1. if there is one node that wish to send data, then it has a throughput of R bps
2. if there are m nodes that wish to send, then the throughput is R/m bps. 

#### Point To Point Communication Link
Found between two routers connected by long distance link, or between user's computer and nearby ethernet. this uses *point to point protocol*

### Error Detection and Error Correction
Three types of error detection is introduced in our course

1. Parity Check - the sender adds a '1' bit to the total number of bits of the datagram. such that the total number of 1s are either even or odd (predetermined). the receiver then can just count the 1s, if odd ones are found in an even scheme, then it has an error. note it would be an undetected error if the bits are even in a even scheme, but still there is error. 

2. Checksumming - basically sum up the k bit integers, take the 1s complement. the receiver then takes the 1s complement of the received datagram, and see if it all is 1 bits. If not, then there are errors. 

3. Cyclic Redundancy Check (CRC) - most widely used today. sender wants to send d bit pieces of data, D. sender and receiver agree on a 'Generator' G , the sender adds a 'r' additional bit to d. the receiver then divides this d+r with G. If the remainder is non zero. then an error has occured. 

#### Channel Partitioning Protocol 
This partitions the channel using time frames (similar to Time Division multiplex), so each node gets its time to broadcast.

down side is that not very efficient in low load. 1/N bandwitch allocated even if there is only one active node. 

#### Random Access Protocol
Transmitting node always transmit at full rate of the channel, when there is a collision. each node both wait in a randomly determined time before retransmitting again. the idea is that since each node came up with their wait time independently, one would retransit earlier than the other and resolve. One of the protocol called *Aloha*

#### Aloha.
1. any node can transmit at any time.
2. no carrier sensing, then collision is possible, there is acknowledgement, so no colission detection.
3. when there is collision there will be retransmit of data. 

analogy to both aloha protocol is a boorish frat boy talking while other guests are talking in a cocktail party. 

Concept of Vulnerable Time - time where the packet will be prone to collision
##### Pure Aloha
Since any node can transmit at *any* time, $$ n = G * e^{-2G} $$ where n is efficency, G is number of nodes. 

to find the maximum efficency, you have to differentiate the above equation, which gets you $$ G = 1/2 ,/ n_max=(1/2)*e^{-1} = .184 $$
this means, in one time slot half the node can transmit, so two timeslot, one node can transmit. 
##### Slotted Aloha
Time will be divided in slot, each node sends at start of slot and each slot has time 1T. so vulnerable time is 1T 

$$ n = G* e^-G derive this you get G = 1 plug back into equation you get n_max = 1* e_-1 = .368$$  

this can be thought of as when a large number of nodes have many frames to transmit, 
then (at best) only 37 percent of the slots do useful work

### Carrier Sense Multiple Access (CSMA)
modified from Aloha, incorporates *Carrier Sensing* ie. if other people are speaking, wait until they are finish before transmitting.  and  *Collision Detection* if someone else is talking at the sametime, then stop talking.  

How effective a node can detect collision depends on the propagation speed. see figure 5.12 Space-Time Diagram in textbook. 

#### Exponential Binary Backoff
in CSMA/CD the adapter waits k*512bit times, bit time refers to how long it takes to transmit 512 bits (so varies across different throughput). 

k can be drawn from [1... 2^{n-1}] n is number of times of the adapter experienced collision. 

#### Efficiency of CSMA/CD 
Efficiency = 1 /  (1 + 5* d_prop/ d_trans)


### Link Layer Address 

Hosts and routers have both network address, and link layer address (the adapters does actually). they are both indespensible , uses Address Resolution Protocol , which translates IP address to link layer address 

#### MAC Address 

No two adapter have the same MAC address, the address space is maintain by IEEE. the MAC address is permanent, its the same no matter where the computer is. 

#### Address Resolution Protocol (ARP)

This is a function that takes the IP address as input , and return the MAC address as output. each host and router has a ARP table in memory, which contains mapping of IP address to MAC address. when a sender requests a MAC address of a receiver, if the table has it , then it just returns it to sender. but if it doesn't it would send an ARP packet, which queries all other hosts and routers in the subnet to determine the MAC address. 

ARP packet header includes - time to live - checksum , destination IP address. 

### nslookup
allows host to run tools to query any DNS server for a DNS record. -type=NS sends authoritative DNS 

### ipconfig 
shows current TCP/IP information like address, DNS server address, adapter type. 

#### Ethernet Switches
has the role of store and forward ethernet frames, buffers packets, uses ethernet protocol 

has a switch table - each entry is a MAC address of hosts, inteface to reach host, and time stamp, looks like a routing table  

the switch 'self learns' this means it updates its switch table when it has a successful response. 

is transparent to hosts, 

switches do not need to be configured 


### Wireless Links 
#### Hidden Terminal Problem
this is when physicial obstruction causes weaken signal strength for wireless nodes to work efficiently. 

say A and B can't hear each other, they cannot sense any collision. but can connect through C. and are exchanging info through C.  as a result collision detection algorithm does not work well, CSMA/CD doesn't work here. 

#### 802.11 Wireless LAN protocol (WIFI)

Uses CSMA/CA (Carrier sense multiple access Collision avoidance). Since theres high bit error rate for wireless channels. there is an added scheme for collision avoidance. 

CSMA/CA doesn't use CD because it requires the ability to send and receive at the same time. it is very costly to build hardware that *can detect* collision. 

Latest and greatest is 802.11n , iphone 6 has 802.11g

802.11 has Basic service set. which is one or more wireless station , connected to a central base station call access point. 

In order to address hidden terminal problem, the protocol implements a 'Clear To Send' and 'Request to Send' frame handler,

sender has to send a RTS to the access point , and wait for the Clear To Send before they can transmit. 

The Clear to send frame is sent to all device. those that didn't send the RTS would understand this as, someone else has requested this signal. 

The rest of the devices waits for an acknowledgement sent from the AP. this signals that they can now send RTS. 

##### Collision Avoidance -
if two station sense channel is busy, the immediately enter random backoff, hopefully the two station would avoid each other successfully. Note collision can still happen. 



##### Link layer acknowledgement 
when the destination station receive a frame , it waits for a short time (Short Inter-frame spacing) SIFS. and sends back an acknowledgement 

if the sender doesn't receive any ack. in a given time, it assumes error and retransmits. 




