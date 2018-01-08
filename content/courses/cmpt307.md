title: "Data Structure and Algorithm II"
date: 2017-09-16
semester: "Fall 2017"
code: "CMPT 307"
# On Gale Shapely Algorithm (G.S)

## Terminologies
*Stable Pair* - A pair where one of the two, or both, are happy. this means either both prefers their match , or (one prefers their match, and the other doesn't) . so the opposite of this is unstable match.  

*Unstable Pair* - both members are unhappy, they both prefer someone else than their current match. __key idea is that both people in this pair can improve by breaking this pair__


*Perfect Matching* -  every person is matched, so this means there's equal number of men and women. 

*Stable Match* - situation where there is no unstable pairs, and also there is perfect matching.

*Valid Partner* - person 'A' is valid partner with 'B', and 'C' if there exists some stable matching in which A-B , OR A-C are matched. 

### Dating game 
For the sake of short hand, I will call proposer 'men' and proposee 'women'

in this game, each men and women individually rank their preferences of the other sex. and list from most desirable to least.

the game goes in rounds. 

Each round, the moves are:
1. All single man,  proposes, they propose to the woman on the top of their list who they have not proposed before. the men who have paired off or have proposed to everyone does not participate.  

2. a. If a woman is not engaged, then she says yes. 

2. b. otherwise, she compares who she's with with the new proposer, and pairs off with the man who's higher on her list. 

2. c. otherwise, she rejects man. 

the game repeats in rounds, until there is no more single man (ie everyone is paired off)
returns S stable matches. 

### G.S deferred acceptance algorithm
The algorithm claims the above game always produces a stable matching 

The algorithm runs at most n^2 times, because there is equal men and women 

#### Proof of correctness - this algo can end:
Observation 1 - men propose to women in decreasing order of preference 

Observation 2 - once a woman is matched, she only "trades up", so women don't become available again. 

#### Proof Of corectness - everyone get's matched
Proof By Contradiction - 

1. Suppose someone doesn't get matched by the end of the game , say man 'A' 
2. This mean A proposed to everyone on his list, and was rejected because woman prefer their current pair than him (because if the woman is single, by the rule of this game, she has to accept him)
3. but this is not possible, as there are equal number of men and women, so one woman must have accept 'A'

#### Proof of correctness:  there is no unstable pair 

Direct Proof - 

1. Man 'A' propose to women base off his list from most to least desirable. suppose he propose to lady 'X'
2. Two outcomes can happen - 
	
	a. X accepts him, because she's either single or likes 'A' more than her current man 'B', either way, A-X is a stable pair.

	b. X rejects him, then it's because she prefers B than A 


#### Proof - All Execution of GS yields man-optimal match
	:::code 
	Claiming there is a man optimal match S that 
	Y - A 
	Z - B
		
		
	Proof by contradiction -

1. suppose G.S created a non-man optimal match. as in, there is a man 'Y' pairs with valid partner woman 'B' . but its not his best partner. 

	:::code 
	this means there is a stable match S* where men Y, Z and women A, B 

	Y - B 
	Z - A 

	and 

	man Y's   preference - A > B
	man Z's   preference - not known
	woman A's preference - not known 
	woman B's preference - not known


2. Y is the first person to be rejected, since he prefers A over B , Y was rejected by A. This means lady A prefers her current partner than Y (if she didn't have a partner, she would of accept Y)

	:::code 
	woman A's preference - Z > Y


2. Y is rejected by A, so he propose to the next woman on his list, B, and is accepted

3. Since Y is the first person to be rejected, that means Z has never been rejected. since Z is paired with A, this means he proposed to A as well.  

	:::code 
	man  Z's preference - A > B


4. Here is the problem, Z would not have propose to B. Z is paired off with A before reaching B. thus S is not possible. and not a stable match.  

man Y matches with woman A 

#### Proof - All Execution of GS yields Woman Pessimality
This is saying the proposee is worst off than the proposer.

Each Woman receives the *worst valid partner*
	
	:::code 
	 Context:
	 Preference:
	 proposer:  
	 X prefers A > B > C 
	 Y prefers B > A > C 
	 Z prefers A > B > C 

	 proposer: 
	 A prefers Y > X > Z 
	 B prefers X > Y > Z 
	 C prefers X > Y > Z 

	 stable match S* (produce by G.S)
	 {X-A, Y-B. Z-C}

	 stable match S 
	 {X-B, Y-A, Z-C}


*Proof By Contradiction* - suppose GS generates match S, rather than match S*

1. so woman A matches with Y, instead of X 
2. that means Y was rejected by B
3. that means B has a partner better than Y , so X 
4. but X's preference is A > B, so he would of proposed to A first , never reaching B 

5. Therefore, match S would not happen under G.S algo. contradiction.  

#### Does G.S always produce the same matches?
Yes, because G.S produces man (proposer) - optimal matches.
And man-optimal match are subset of all stable matches

# GRAPHS

## Terminologies
Path	    - a sequence of nodes join by edges
Simple Path - if all nodes are distinct
Connected Graph - if for every pair of nodes, there is a path 
Cycle 		- Same as Simple path, but start and end at the same node


### Adjacency Matrix

Graphs can be represented by a \\(n x n\\) adjacency matrix
where n is number of nodes. if there is an edge between two nodes, there is a 1 on the matrix. otherwise 0.

so takes \\(O(n^2)\\) space 

### Adjacency List 
This is another way to represent a graph. It has a better way to find neighbors of each node. there is a n size list. each item in the list is a linked list of the neighbors that node has. so, each item is an edge to its neighbour.

Space is \\(theta(m+n)\\) where m is number of edges, and n is number of nodes

say there are 3 nodes, and there are edges {(a,b), (b,c), (a,c)} then the adjacency list is 

	:::code
	node a:  -> b  > c
	node b:  -> c
	node c: 


#### Properties

AL. is good for sparse graphs, because there will be fewer linked lists. and we can approximate the space as {O(n)}

checking if there is an edge between two nodes \\(u , v\\) takes \\(O(degree(u))\\) time 

Even if it is very dense, the size of the AL is at most the sum of the degrees of the nodes. 

### Tree Properties 
If \\(G)\\) is a undirected graph on \\(n)\\) nodes, any two of the following statements imply the third. 

- G is connected
- G does not contain a cycle 
- G has \\(n - 1\\) edges

## Breadth First Search 

Explores from start node S. and add layers, one layer at a time.

Each layer \\(n\\) is neighbors of layer \\(n-1\\) node. 

Another property of BFS tree is that if there is an edge between nodes \\((x,y)\\), then \\(x, y\\) are either one level apart, or on same level. 

*Theorem* For each \\(i\\), \\(L_i\\) consists of all nodes at exactly \\(i\\) from \\(s\\). and there is a path from \\(s\\) to \\(t\\) \\(IFF\\) \\(t\\) appears in some layer 

*Theorem* BFS runs in \\(O(m+n)\\) time , if in adjacency list 

- In Adjacency lists, there are \\(m\\) nodes and \\(n\\) edges representing the node's neighbours.
- when we consider node \\(u\\), there are degree(u) incident edges (u,v)
- total time processing edges is sum of of all degress = 2 * number of edges


## Bipartite graph 
short way to remember this is that if all nodes can be colored such that each edge has a blue node on one end and white on the other. 

If a graph is bipartite, then there cannot be an odd length cycle. 

### Bipartite graph and BFS Tree 
to check if something is a bipartite graph, you run BFS to generate a BFS tree, then see if you can color each layer distinct color. 

Exactly one of the following holde:

1. No edge of G joins two nodes of the same layer, then G is bipartite

2. an edge of G joins two nodes of the same layer, and G has odd-length cycle, so not bipartite

### Directed Graphs
### Terminologies
Mutually Reachable - if there is a directed path from node \\(u\\) to \\(v\\) and vice versa 

Strongly Connected - if every pair of nodes is mutually reachable, then the graph is *Strongly Connected*

Strong Component - maximal subset of mutually reachable nodes. (cannot add more nodes without breaking 'strong connectness')
Directed Acyclic Graph - a directed graph that contains no directed cycles. 

Topological order 	   - is an ordering of its nodes \\(v1, v2, .. vn\\) so that every edge \\((v_i,v_j)\\) we have \\(i < j\\)

*Theorem* - Can see if \\(G\\) is strongly connected in \\(O(m+n)\\) time

1. Pick any node s 
2. Run BFS from s in G 
3. Run BFS from s in G reverse 
4. if all nodes are reached in both BFS, then G is strongly connected


### Lemma, If G has a topological order, then G is a DAG 

Proof by Contradiction. 

1. Suppose G is not a DAG , then this means there exists a directed cycle
2. let \\(v_x\\) be the vertex with the lowest index in the cycle 
so \\(v_x...v_{x+1}.. v_{x+2}... v_{j}  ... v_x\\)

3. for \\(v_j\\) to go to \\(v_x\\), \\(j < x\\) , per topological order but \\(j > x\\)
hence contradiction

### Topological Sort Given a DAG 
the Topological Sort is just a DFS with an extra temporary stack.
	::: code 
	Version 1 From GeeksForGeeks
	instantiate a temp. stack 

	for each node x in unvisited nodes:
		mark x as visited 
		do recursive DFS on x (remember neighbor is only adjacent if theres an arc from x to its neighbor)
			mark every node in this DFS as visited
		when the DFS reach its end, push that end node onto the stack(this node has the lowest index)
	next 

	pop / print the stack , this is the topological sort. 

Version 2 From Class 
Find a node v with no incoming edge and order it first 
'Delete' v from graph G 
	Recursively Compute a topological ordering of G - {v}
		append this order after v

## Shortest Path Problems

### Dijkstra's Algorithm (DA)
Greedy algorithm takes the best best choice with information available. and does not adjust it even if theres new information. Dijkstra's algo is greedy because it has an initial set S of shortest path, and every round, it adds to it given the info. at the time, but does not remove from S.

This algorithm maintains the invariant that 

for each node in S, d(u) is the length of the shortest path from root to u

*Proof Of Correctness*

### Efficient Implementation of DA
1. Use a Min Priority Queue to the nodes not in S , organize by their distance. 
2. explicity maintain each unexplore node's distance instead of computing the formula. 

Priority queue can be used to improve Prim's algorithm as well , by sorting the lowest cost edges 

### Recurrence Equation Time Complexity Refresher

Recurrence	Algorithm	Big-Oh Solution
\\(T(n) = T(n/2) + O(1)\\)	Binary Search	\\(O(log n)\\)

\\(T(n) = T(n-1) + O(1)\\)	Sequential Search	\\(O(n)\\)

\\(T(n) = 2 T(n/2) + O(1)\\)	tree traversal	\\(O(n)\\)

\\(T(n) = T(n-1) + O(n)\\)	Selection Sort (other n2 sorts)	\\(O(n^2)\\)

\\(T(n) = 2 T(n/2) + O(n)\\)	Mergesort (average case Quicksort)	\\(O(n log n)\\)

### Cycle Property 
The edge with the heaviest weight would not be selected for the minimum spanning tree 

*intuition* you can connect to all the nodes in the cycle and not use this edge.  	

### Cut Property
The edge with the minimum weight in a cycle would be selected first 

*intution* imagine the minimum weight edge \\(e_m\\) and some other edge in the cycle connects nodes from two components \\(S \, T\\) 
then \\(e_m\\) would be the one used to connect the two component. 

### Greedy Algorithm - General ways to prove them 
the algorithm always maintains the invariant of 

\\(S_i\\) is subset of \\(S_{opt}\\) for all iterations of \\(i\\)


### General way to prove Kruskal and Prim algorithm 
we can use the cycle and cut property to prove these two algorithm, and also the greedy algo algo. invariant 

### Union Find Algo AKA Disjoint Set
This D.S handles finding which element does a set belongs to quickly. It has two operations.

Kruskal Algorithm uses this D.S to detect cycles. If two nodes point to the same parent, then they have cycle. otherwise, you can union them.

 
1. Find() 
	find the root of the tree containing x	
2. Union() 
	merge two sets together. 
	Quick Union - is implemented as a forest, so separate trees. each tree is
	identified by their root. When we union two trees together, its updated in the root. the 	 bigger of the tree swallows the smaller tree, this means the resulting tree is wide. 



## Greedy Algorithm Interval Scheduling
### Greedy Algorithm Template
1. Organize the jobs in some order, like Heaviest First, Earliest First, Shortest first, etc. note a priori its hard to tell 
which one makes sense 
2. Iterate through this list, and accept answer as it goes. 

### Minimizing lateness 
Use Earliest Deadline First 
\\(O(nlogn)\\) time for sorting

* Earliest Deadline first (EDF) has no idle time 
* EDF Has no inversions 
* If a schedule  (with no idle time) has an inversion, it has one with pair of inverted job scheduled consecutively

swapping two adjacent, inverted jobs reduces the number of inversions by one and **does not increase the max lateness**

suppose there is an inversion, in Greedy it chose job x, then job y
and in another scheduler it chose job y ahead of job x.

	1. Job x duration must be less than Job y because Greedy chosed it
	2. All other jobs except for x and y still have the same lateness
	3. we must show that the greedy x + y is <= schedule o y+x

	



### Interval Partitioning
We now have jobs, and resources, such as lectures and rooms. we want to minimize the number of rooms and schedule all the lectures. 

We can resolve this using greedy algo again. 

Using *Earliest Start Time First*

	:::code
	SORT lectures by earliest start time first
	d = number of allocated class room
	
	For j = 1 to n number of jobs
		If j is compatible with some class room
			schedule lecture j in this class room
		Else 
			allocate a new classroom d+1
			schedule j in classroom d+1
		d + d+!
	return schedule

we can implement this in \\(O(logn)\\) time by storing the classrooms in a *priority queue* where the key is the finish time if its last lecture. 

#### Lower Bound of Interval Partitioning
*Depth* is the maximum number of conflicting jobs at any given time. if three jobs have time conflict at 10 am. then the depth is 3. 

The key obsevation is that, the optimized algorithm can't beat the depth. 
 
### Minimizing Lateness: Earliest Deadline first
Sorting by E.D first means there are no inversions, whic means job i and j such that i < j but j scheduled before i.

We claim that fixing the inversion does not increase the max lateness. (because it was worst off before)	


### Merge Sort 
Uses divide and conquer paradigm

*Merging* takes \\(O(n)\\) time 
*Sorting* takes \\(O(log_2n)\\)

so merge sort is \\(O(log(n) * n)\\)

### Counting Inversions
Question is, how to count the inversions in an array. 
 
We can use divide and conquer to solve this,

	:::code
	we divide the array into A and B sub array
	sort them
	scan A nd B from left to right
	if a_i <  b_i then no inversion with anything in B
	if a_i >  b_i then b_i is inverted with everything in A
	Append smaller element to sorted list C

incidentally, we can also output the sorted list this way. 

the sort and count algo runs in \\(O(nlogn)\\) time 

as in \\(T(n) = T({n/2}) + T({n/2}) + O(n)\\) when n > 1

### Dynamic Programming
In general, dynamic programming is done in these four steps

1. Describe an array and say how to obtain an optimal solution from the array
2. Give a recurrence for your array, and prove its correctness
3. Give pseudo code algo for filling the array
4. give an algo for finding an optimal solution to the original problem, using the values in array

#### Weighted Interval Scheduling

\\(p(j)\\) is the largest index i and i < j, so intervals i and j are disjoint. 

\\(OPT(j) = max(V_j + OPT(p(j)), OPT(j-1))\\) 

this means either the optimal interval has interval J, or it has not, in which case we look at \\(OPT(j-1)\\)

Job J belongs to an optimal solution if and only if \\(v_j + OPT(p(j)) >= OPT(j-1)\\)

To run the algorithm faster, we store all the optimal subpath in an array, so that we do not have to process it again. this is 
fundamental in dynamic programming. 

#### Shortest Path and Negative Weight (Dynamic Programming)
#### Bellman Ford Algorithm
When we do shortest path we can't have graph with negative cycle, because then we would use negative cycle many times to drive down our cost of path

this algo fixes this. 

	1.) Bellman(Graph, Weight, Source) Graph G is initalize in adjacency lists

		memoize d[n] <- initialize as infinity
		for i = 1 to V - 1 // shortest path has V-1 edges
			for each edge(u,v) in E
				if d[v] > d[u] + w(u,v) // Relax Function
					set d[v] = d[u] + w(u,v)
					pi[v] = u
		//Checks for negative cycle below
		for each edge (u,v) in E 
			if d[v]  > d[u] + w(u,v) 
			//then report negative cycle exists

Complexity is O(VE) for first part, and O(V) one pass for the check. note remember in a dense graph the edges could be V^2. 
so compexlity could be O(v^3)

Proof Of Belman Ford:
	Claim - Algorithm will return shortest path or negative cycle in V-1 iterations 
	
	Proof by induction. 
		-Let p be a shortest path with minimum number of edges.  
		-Since no negative weight cycle, it implies p is simple, and it implies k <= v-1
		
		in this algo, we are examining (relaxing) every edge every pass, so we are going to be building towards the k. 		     

#### Floyd Warshall Shortest Path Algorithm 
Discovers shortest path between ALL vertices, 


### Flow Network
#### Residual Graphs
Given a directed graph with capacities for each edge, we can think of its residual graph G_f as a graph that shows all the unspent capacities (forward edge residuals), along with its flows that can be reverse out (backward edge residuals)

Ford Fulkerson algorithm uses the idea of residual graph , and "augment path"
to determine the max flow. The augment path is a path from the source S to the sink T along the residual graph

Flow networks can solve all sorts of problem, like finding the max number of matching in a set, or finding the number of projects to choose in project management (max revenue and min cost)

#### Halls Theorem
Given a bipartite graph , where the left side and right side are the same size. 

If for all subset S belonging to one side, (say L) , 

find all the neighbor nodes of that S , call it N(S)

if the size of S is <= size of N(S) then there is perfect matching. 

#### Edge Disjoint Path
two paths are disjoint if they have no edge in common (but they can have nodes in common)

#### Mengers Theorem
Mengers Theorem says if the paths are unit weight . The max number of edge disjoint paths is the max flow. 

intuition: since edges are unit weight, they are either 1 or 0 by integrality, so they either participate in the path or not. 



### NP Complete

#### Reduction
take something from NP Complete, and convert(reduces) it to another problem

colloquially, we take the input from the NP complete problem x, and do something with it (blackbox) and turn it into the input of another problem y. 

this blackbox has properties:
if the y is a yes, then x was a yes too
if y is a no, then x was a no too

the reduction has to be polynomial time (fast) because we dont want reduction to take more than solving the algo itself.
hence the term \\(<=_p\\)

### General way to prove new problem is NP -complete (Reduction)
1. Prove that X belongs to NP (ie easy to check a solution, but hard to prove how it was calculated)
2. Choose a problem Y that is known to be NP - Complete
3. Prove that Y <= p X

#### 3 Satisfy
any number of variable but 3 per clause

let number of variable be n,
m number of clauses. 



#### Vertex Cover
We say a subset of S nodes are vertex covers if every edge in graph G at least have one edge in S.


#### Clique
is a maximum problem, given a graph and a number k, can we find the maximum clique of k 

if I fix the k to a small number then it might be easier. if our machine cannot find a k clique, then it wont be able to find any k+1 more clique, because k+1 clique contains a k clique

#### Hamiltonian Circuit reduce to Travelling Salesmen
Hamiltonian Circuit (HC) looks for a path with no repeating vertices that traverse the whole graph
TSP looks for a path that traverse the whole graph with the minimum cost (bound by some number B)

we want to show HC <=p TSP 

we observe that HC is a special case of TSP,

**Reduction**
We have the original graph G for Ham Circuit.

we construct a graph G' of TSP that has all edges weight of 1. and bound by N (number of vertices)

solving G' would solve G


#### Independent Set and Vertex Cover
Independent Set (IS) - each node in the independent set S does not share edges

Vertex cover (VC) - all edges in the graph connects to the vertex cover set S'

IS usually are types asked like this, given a k number, can we find an IS of size k or more?

VC is usually given a k number, can we find an VC of size k or less?

IS can be reduce to VC

**Reduction**
Let G=V,E be a graph, then S is an independent set IFF its complment V-S is a vertex cover.

then

Independent Set <=p Vertex Cover
Vertex Cover <=p Independent Set

**Coping with NP Completeness**

***Vertex Cover*** - theory says it takes \\(O(k*n^{k+1})\\) subset size of k

we aim to cap the \\(k\\) value down to a feasible size, so that our brute force algorithm can actually run

for vertex cover \\(S\\) of size \\(k\\), we can remove a node \\(u\\) from \\(S\\), then \\(S\\) - \\(u\\) will still be a vertex cover of the original graph without \\(u\\)


we also observe that for each node n, there is at most \\(n-1\\) edges it can have. 

so the VC of size \\(k\\) covers at most \\(k*(n-1)\\) edges

this means any graph with more than that many edges, cannot have a vertex cover

so our algorithm goes like this

	:::code
	VertexCover(G, k):
		if G has more than k*(n-1) edges return False
		
		if G has no edges then return true // base case

		let (u,v) be any edge of G
			hasVC1 = VertexCover(G-u, k-1)
			hasVC2 = VertexCover(G-v, k-1)
		return hasVC1 OR hasVC2

the depth of the recursion tree is \\(k\\). there is 2^k calls

each method takes \\(O(kn)\\) time. so result is \\(O(2^k*kn)\\)

Improving ***Independent Set*** algorithm 

we notice that the __maximum__ independent set on trees will contain the leafs of trees. we can proof it by the exchange argument.

1. if the maximum set \\(S\\) has leaf \\(v\\) then we are done
2. if \\(S\\) does not have \\(v\\) but has its parent \\(u\\) then removing \\(u\\) and add \\(v\\) will be just as same size.
3. if \\(S\\) does not have either, then adding \\(v\\) into \\(S\\) will improve it

	:::code
	Indepedent-Set-In-A-Forest(F):
		initialize S = {} max indep. set
		while forest F has at least one edge:
			Let e=(u,v) where v is a leaf
			Add v to S
			Delete nodes u,v from forest F, and all of its associated edges
	return S

this runs in \\(O(n)\\) time

***Vertex Cover*** and ***Matching***

let \\(M\\) be matching, and let \\(S\\) be vertex cover
then the size of \\(M\\) is <= \\(S\\)

The proof is, each vertex can cover at most one edge in any matching.

__Konig-Egervary__ Theorem says in any bipartite graph, the max cardinality of a matching equals to the min cardinality of vertex cover

This leads to us being able to approximate a vertex cover in a graph
if our algorithm is 

	:::code
	algoVC(Graph (G,E)):
		S = empty
		while E is not empty:
			pick an edge e=(u,v) in E
			add both u and v into S
			remove from G all edges touching u or v
		end while
		return S

the above algorithm will find a vertex cover VC. the VC won't be the minimum size, but it runs in linear time.

if we compare this VC \\(S\\) with the optimal VC \\(S*\\)
we will find \\(|S| <= 2|S^*|\\). The two is the approximate factor. 

proof -> notice in the code, we are adding both u and v into the S, and stripping their related edges. S is in effect a set of disjointed pairs bundled together. 

any vertex cover for G must use at least one vertex per edge in the matching, so \\(|S*| >= |matching| = |S|/2\\)

***Knapsack Problem***

the standard dynamic programming solution to knapsack problem is not polynomial to the input size, so we can improve the solution of knapsack by shrinking the weight limit of nodes proportionally.

