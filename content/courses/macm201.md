---
layout: default
title: "Discrete Math II"
code: "Macm 201"
semester: "Winter 2017"
---
## MACM 201 Discrete Math II Winter 2017


### Find unique solution to a given recurrence
Given \$$ a_{n+1} - 1.5a_n = 0$$

Rearrange equation so \$$ a_{n+1} = 1.5a_n$$

then we can see that \$$ a_{n+2} = 1.5a_{n+1} = 1.5 * 1.5 * a_{n}$$

so the unique solution is \$$ a_{n} = 1.5^n * a_0 $$

### Solve a recurrence using characteristic polynomial
Given an equation such as \$$ a_n = 2a_{n-1} + 3a_{n} \quad a_0 = 1 \quad a_1 = 2 $$

Substitute \$$ a_n = cr^n $$

so the equation becomes \$$ cr^n = 2cr^{n-1} + 3cr^{n-2} $$

the key part is to divide both sides by \$$ cr^{n - lowest exponent} $$ 

in this case its 2, it becomes \$$ r^2 - 2r - 3 = 0 $$ 

move terms to one side rearrange and find the root \$$ (r+1)(r-3) = 0 $$

with r = -1 and r = 3, general equation for second order homogenous solution is \$$ a_n=A3^n+B(-1)^n $$

solve for A and B by using initial information \$$ a_1 = 1 \quad a_0 = 0 $$ 

we get 
$$ A = 3/4 \quad B=1/4 $$

The solution is thus 
$$ a_n = 3/4*3^n + 1/4*(-1)^{n} $$

### Table of reference for particular solutions in recurrence 
g(n) of $$ n^t $$ is $$\quad A_on^t + A_1n^{t-1} + A_2n^{t-2} + ... + A_0 $$

g(n) of $$ r^n $$ is $$\quad Ar^n $$

g(n) of $$ n^tr^n $$ is $$\quad r^n(A_tn^t + A_{t-1}n^{t-1} + A_{t-2}n^{t-2} + ... + A_1n^1 + A_0) $$

### Solve a nonhomogenous equation
1. Determine the recurrence solution, like 
\$$ a_n = 3a_{n-1} + 3^{n-1} $$
2. find the general solution for the homogenous portion 
\$$ a_n^h = Ar_1^n + Br_2^n $$ where A B are constants that solves the equation.
3. Find the particular solution $$ a_n^p $$ using textbook table, note if found to be symmetric with $$ a_n^h $$ you need to introduce a $$ n $$ to break the symmetry. 
\$$ a_n^p = C2^n + Dn^23^n $$ where C D are constants to solve for the particular solution 
4. the solution is now in the form of 
\$$ a_n = a_n^h + a_n^p = Ar_1^n + Br_2^n + C2^n + Dn^2(3^n) $$ 
5. Use coefficient comparision to solve for C and D in $$ a_n^p $$ by plugging $$ a_n^p $$ into the recurrence soluation at 1.
6. Once we found C, D , we can solve for A, B by setting up 4. $$ a_n $$ with the values from 5. 

### Extended Binomial Theorem
Formula for (fraction, n) and (negative, n) follows the form 

$$ (n,r) = (n(n-1)(n-2)...(n-r+1))/r! $$

for (negative, n) this simplies to 

$$ (-1)^r(n+r-1, r) $$
### Coefficient Extraction
Coefficient extraction is used to solve recurrence relations, and find combinatoric sums , amongsts other things.

There are several rules we can follow 
1. Sum Rule $$ [x^n](A(x)+B(x)) = ([x^n]A(x) + [x^n]B(x)) $$ (We can think of this like two mutually exclusive series, so we need to use sum rule to count them)
2. Power Rule $$ [x^n](A(kx) = k^n([x^n]A(X)) $$
3. Reduction Rule $$ [x^n](kx^mA(X)) = k[x^{n-m}A(x)] $$ (This is because we can think $$ x^m $$ is a shift of terms to the series, so we can find the correct coefficient by offset)
4. Product Rule $$ [x^n](A(x) * B(x)) = [x^k]A(x) * [x^{k-1}]B(x $$)

### What is a graph
graph is a collection of vertices, V, and edges E. 

### Traversal terms
- Cycle is a closed Path, a Path has no repeat vertices 
- Circuit is a closed Trail, a Trail has no repeat edges
- Walk is the most general case, no restrictions. 


### Euler Trail and Euler Circuits
if G is a connected graph. G has a *Euler circuit* if the circuit traverses every edge of the graph exactly once.

it's a *Euler trail* if it's open and traverse every edge once. 

$$ G=(V,E) $$ be a connected graph or multigraph, G has a Eulerian circuit *IFF* every vertex of G has even degree. 

*Corollary* $$ G=(V,E) $$ be a connected graph or multigraph. G has an Eulerian Trail *IFF* G has exactly two vertices of odd degree.

### Hamilton Path and Hamilton Cycle
This is a path/cycle (so no repeat vertice) that traverses all the vertices exactly once in the graph.

finding a hamilton path is NP complete, meaning there is no known algorithm that can find the solution in an appropriate amount of time. 

##### Necessary and Sufficient Condition
- *Sufficient* if p is true then q is true. 
- *Necessary* if q is true, then p is true. as in, 
	example, if p is necessary for q, then q cannot be true unless p is true
- *Necessary and Sufficient* p is true IFF q is true. Acing the test is *necessary* and *sufficient* for getting 100% on a test. 
	
- *Necessary But Not Sufficient* Steering well is *necessary* for driving well, but *not sufficient* , because you need to follow traffic rules, not hit pedestrians, etc. 

- *Sufficient But not Necessary* Boiling a potato is *sufficient* for cooking a potato, but not *necessary*, because its not the only way to cook, you could fry, roast, etc.

#### Sufficient Condition 1 for Identifying Hamilton Path / Cycle
/$$ for all vertices x, y/, with |V| >=2 x != y /, deg(x) + deg(y) >= n-1$$ 
and
/$$ for all vertices x, y/, with |V| >=3 x != y /, deg(x) + deg(y) >= n$$ 

This is a sufficient condition for a graph to admit a Hamilton cycle. 

#### Sufficient Condition 2 for Identifying Hamilton Path / Cycle
/$$ for all vertices x /, deg(x) >= (n-1)/2$$ 
This is another sufficient condition for having a HP

#### Necessary Condition for Identifying Hamilton *Cycle* in Bipartite Graph
given a bipartite graph organize by set V1 and set V2 . There needs to be |V1| = |v2| for there to be a hamilton cycle

### Theorem -  If G=(V, E) is an undirected graph or multi graph , then sum of all the degrees of the vertices are 2|E|

Proof - 
For each edge [a, b] in graph G, the edge countributes a count of 1 to deg(a) and deg(b) respectively.

consequently, for each edge, it contributes 2 to the sum of total degrees. 
Thus 2|E| accounts for deg(v), for all v in vertices. 

### Regular Graph
This is a graph where each vertex shares the *same* degrees. if deg(v) = k for all vertices v, then the graph is call k-regular.

if G is a k-regular graph, then 
$$ |E| = k|V|/2 $$
### Isomorphic,
If two graphs G1, and G2 are isomorphic, then there is a function f that is bijective, and f maps an edge E1 to E2. 

one can transform G1 into G2 by relabelling the vertice of G1 with the labels of vertices of G2 (AKA preserving adjacencies)

#### Tips on identifying graph isomorphism
1. If you think G and H are isomorphic, then you would need to show there is a bijective mapping between vertices of G and vertices of H that preserves the edge. 
2. If not isomorphic, you need to show they are different, including:
- number of vertices
- number of edges 
- degrees of distribution
- cycles length

### Planar Graphs 
Planar graph is a graph that can be drawn without intersecting edges. 
Each planar graph have planar embedding 
which are different variations of planar graph

#### A subgraph of a planar graph is planar
1. Given G is a planar graph, implying there's a planar embedding of G 
2. H is obtained from G by removing vertices and/or edges
3. Since G did not have crossing edges to begin with
4. H would not have crossing edges either
5. So H has a planar embedding, and is a planar graph


#### $$ K_5\,and\,K_{3,3} $$ are the first non planar graphs 
Kuratowsk Theorem says a graph is a planar IFF if it does not contain a subgraph of subdivision $$ K_5 \, and \, K_{3,3} $$

#### Faces 
Faces are regions in a *planar* graph. we can think of faces as regions closed off by a cycle within the graph. note not every cycle of G forms a face

##### Euler Formula
states \$$ faces = 2 + edges - vertices $$

### Hypercube
two binary sequences of w and w' have distance 1 if they differ in a single position. 

Hypercubes have strings as vertices, and edges if two strings differ by distance 1
#### Distance 
The distance between two vertices is the *shortest path* between the two
#### Hamming Distance 
two binary sequence w, and w' of length n, the hamming distance is the number of positions in the string where they are different. 

## Graph Proofs

### Proof for all x - y walks in a graph, there exists a x -y path
1. Define a w to be a minimal walk from x - y, so it is also the shortest. 

2. theres two cases for w . A.) either w has a repeated vertex, or B.) it does not.

3. for case 
  - A. Since there is a repeated vertex, call v1. this means this walk looks something like this . x - a - b - c -v1 - d -v1 - y. This means we can remove occurences of v1 so that only one v1 remains. This new walk w1 is now a path. 
  - B. we are done, as by definition it is also a path.

### Proof if graph G has a total number of vertices v. and total number of edges e. and G is loop free, undirected . prove that $$ 2e <= v^2 - v $$
the key is to note that the maximum edges a graph can have is given by the complete graph of vertices v. ie. (v, 2) edges.

then its a matter of rearranging the formula of (v,2) to get v(v-1)/2

### General notes on graph proofs
We should remember the property Sum of all degrees = 2 * total edges of a graph. 

a k+1 regular graph would also have the properties of a k regular graph. 
	so if k regular graph has a k walk, the k+1 graph would also have it. 

in a induction proof, when we have establish a base case, an induction hypothesis, and we are proofing for n+1, it may be sufficient to just draw a graph n abstractly, namely, we dont care about whether its bipartite, complete, or whatever. 
