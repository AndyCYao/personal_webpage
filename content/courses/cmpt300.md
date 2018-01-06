title: "Operating Systems"
date: 2017-03-01
code: "CMPT 300"
semester: "Spring 2017"


## CMPT 300 Operating Systems Winter 2017

### Bankers Algorithm:
This is an algorithm that keeps track of allocated resources, total resources, and needed resources. The idea is that process deadlocks can be prevented if operating system ensures it is in a safe state.

Safe State: there exists a sequence of processes that can allow all process to finish. 

Unsafe state: there is not such sequence. 

### Master Boot Record (MBR)
The MBR stores the details of the various partitions, their start address, end addresses etc. 

It is loaded when the computer is booted, and the BIOS starts the MBR, which finds the active partition to load the operating system. 

### Memory Management
there is a distinction between virtual memory , and physical memory.
Processes do not access physical memory directly, they access virtual memory, and there is a memory management unit MMU that connects the virtual address to physical addresses.

There are two approach to connect virtual and physical memory, Page Base memory management, and segment based memory management. Page base is the dominant form of memory management and what we study. 

#### MMU memory management unit
every CPU has a MMU, and the MMU is responsible for translating the virtual memory and physical address.
it is also responsible for reporting faults, such as illegal access etc. 

a MMU also has a translation lookaside buffer, which is a cache that stores some information for faster look up. 

### Registers
The hardware has designated registers for address translation. Which are pointers to the page table, it has information about the base, the limit size, and number of segments etc. 

### Page base memory management 
A page table is a component of page base memory managment , it's like a map that connects the virtual memory to the physical memory. The table stores the virtual page number, and goes through an offset, to create the physical frame number. 

When there is a new virtual memory being accessed, there is nothing in the page table. The page table arranges for a free physical frame to be used.  

The page table is created per every process. the OS has to perform context switch to switch out the different page tables in the register. 

#### Page Table 
Page table keeps bit flags such as isPresent, isDirty, isReadOnly etc. these flags provide the decision for page fault. 

#### Hiearchicial Page Table 
This is a lay out of page table in an effort to save space. 

Outer Page or Top Page Table is the page table directory. The outer page acts as a pointer to the inner table, 
the Internal page table is only for valid virtual memory region. The total number of virtual addresses are still the same as compare to the flat tables. However, the various internal tables are only allocated when needed. in this way it saves space. 

Multi Level PT Trade off 
-Adding more internal layers offers smaller granuarity of coverage in terms of addresses 
however, the trade off is there is more latency in accessing data. 

##### Translation Look Aside Buffer
The TLB is a MMU level address translation cache, it is used to speed up looking through page table. It stores some page table record. MMU looks to the TLB before looking at page table (which is stored in memory)

### Segmentation 
Is logical addresses that are arranged arbitrarily, could be arranged due to code, heap data, stack, etc. 

the logical address has the form 
	<segment-number, offset>
and uses the segment table to translate from logical to physical address

### Demand Paging
Note physical memory is less than virtual memory. 

### Deadlock vs Livelock vs Starvation 

Deadlock is when two processes are both waiting for the other process before they proceed. Example is 

Given process A and B, both needs resource x and y to proceed. There is a possibility that an OS gives A x, and B y, but A now needs y, and B needs x. The processes are now deadlocked. 

Livelock is when two processes are continously changing their state in response to changes in the other process. 

Example. person A and B are walking towards each other and passing by in a narrow hallway. A moves to his left to allow B to pass, and B moves to his right. now the two are blocked, so they move the other way, and are blocked again. 

Starvation is when a thread is not getting scheduled to run because another thread is always getting scheduled. This may be caused by having a lower priority than the other. 

