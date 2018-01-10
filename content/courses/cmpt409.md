title: "Competitive Programming"
date: 2018-01-05
code: "CMPT 409"
semester: "Spring 2018"


### Data Structures to Know

stacks, priority queue (in an array), dictionaries, sets, 

most of these are in standard libraries, otherwise you have to create your own code book or look at the stanford codebook in the lecture slide

__Stack__ used for DFS traversal (push on discovering a node, pop on leaving for first time)

__Queue__ BFS traversal, waiting line, representing a card deck for shuffling, usually use circular queue for empty space.

__Dictionaries__ content-based retrieval, implemented in sorted arrays, BST and hash tables, note with hash tables, deletion is not supported, deletion in open addressing scheme is very ugly. 

we use chaining as collision resolution instead of open address.


__sets__

unordered collections key methods include member(x,S) is an item x an element of subset S?

union(A,B) construct subset A union B

intersection(A,B) construct subset A intersect B

Insert, Delete.

__union find structure__

every set is represented by tree, and every node points to its parent

if we don't know the size of the subsets, and we want to find the sizes, then we can visit two sets in parallel and the first one to finish visiting is the smaller subset. 

path compression refers to trimming the subset tree so that if d -> b -> a and a is the parent, then just have d -> a.

__Augmenting Data Structures__

we have a BST, and want to efficiently count the number of elements < x or . we could go through all vertices, but that is slow O(n). 

the way to improve this is to also store the size of the subtree at each node.

this can also help find the k'th smallest element,

__Representing Graphs__

when we use adjacency list, the storage is O(number of edges + number of nodes)

with adjacency matrix, we have an advantage of accesing an edge directly (whereas the list we have to traverse until we find it)

but with A.Matrix its not advantangeous if the graph is sparse. 

### Analyzing Running Time ### 

in a competition , if N <= 100 and you have an O(N^3) you should fix the bug in the algo by finding the edge cases because N is quite small

but if N <= 1000,000, then you can't use O(N^3)

__Data structure for the poker hand question__

we can treat a hand as a 64 bit vector, bit 1 if its a straight flush, 0 other,bit 2 holds 1  if 4 of a kind,  


__String Matching__ 

problem is to find naive string matching,

trick is to use a hash functions

preprocess T to speed up queries, hash every substring of length k, and k is a small constant

for each query P, hash the first k letters to P to retrieve all occurences of it within T. 

Pro: Hash table easy to implmeent  significant speed up in practice

Con: doesn't help the asymptotic efficiceny, and a lot of memory consumption

**A better way** Robin Karp - do preprocessing to eliminate locations that could not possibly match. 

example. P=010111
T = 0010110101001010011

the parity of binary value is to count the number of ones, if odd the parity is 1, if even the parity is 0. since pattern is six bit long, counting six bit ahead, call this f[i] where f[i] is the parity of the string T[i..i+5]


**KMP Knuth Morris Pratt** algo. famous linear time running string matching algoachieves O(m+n)

**Use suffix tree** let A be string of length n, let A_i be suffix A that begins at position i

A suffix trie of A is made by compressing all the suffixes.  
