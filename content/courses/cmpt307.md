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
1. All single man propose, they propose to the woman on the top of their list who they have not proposed before. 

2. If a woman is not engaged, then she says yes. otherwise, she compares who she's with with the new proposer, and pairs off with the man who's higher on her list. 

the game repeats in rounds, until there is no more single man (ie everyone is paired off)

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
NEED HELP ON THIS 

Direct Proof - 

1. Man 'A' propose to women base off his list from most to least desirable. suppose he propose to lady 'X'
2. Two outcomes can happen - 
	
	a. X accepts him, because she's either single or likes 'A' more than her current man 'B', either way, A-X is a stable pair.

	b. X rejects him, then it's because she prefers her current 


#### Proof - All Execution of GS yields man-optimal match
~~~code 
Claiming there is a man optimal match S that 
Y - A 
Z - B
~~~

Proof by contradiction -

1. suppose G.S created a non-man optimal match. as in, there is a man 'Y' pairs with valid partner woman 'B' . but its not his best partner. 

~~~code 
this means there is a stable match S* where men Y, Z and women A, B 

Y - B 
Z - A 

and 

man Y's   preference - A > B
man Z's   preference - not known
woman A's preference - not known 
woman B's preference - not known
~~~

2. Y is the first person to be rejected, since he prefers A over B , Y was rejected by A. This means lady A prefers her current partner than Y (if she didn't have a partner, she would of accept Y)

~~~code 
woman A's preference - Z > Y
~~~

2. Y is rejected by A, so he propose to the next woman on his list, B, and is accepted

3. Since Y is the first person to be rejected, that means Z has never been rejected. since Z is paired with A, this means he proposed to A as well.  

~~~code 
man  Z's preference - A > B
~~~

4. Here is the problem, Z would not have propose to B. Z is paired off with A before reaching B. thus S is not possible. and not a stable match.  

man Y matches with woman A 

#### Proof - All Execution of GS yields Woman Pessimality
This is saying the proposee is worst off than the proposer.

Each Woman receives the *worst valid partner*


~~~code 
 Context:
 Preference:
 proposer:  
 X prefers A > B > C 
 Y prefers B > A > C 
 Z prefers A > B > C 

 porposee: 
 A prefers Y > X > Z 
 B prefers X > Y > Z 
 C prefers X > Y > Z 

 stable match S* (produce by G.S)
 {X-A, Y-B. Z-C}

 stable match S 
 {X-B, Y-A, Z-C}
~~~

*Proof By Contradiction* - suppose GS generates match S, rather than match S*

1. so woman A matches with Y, instead of X 
2. that means Y was rejected by B
3. that means B has a partner better than Y , so X 
4. but X's preference is A > B, so he would of proposed to A first , never reaching B 

5. Therefore, match S would not happen under G.S algo. contradiction.  

#### Does G.S always produce the same matches?
Yes, because G.S produces man (porposer) - optimal matches.
And man-optimal match are subset of all stable matches

# GRAPHS

## Terminologies
Path	    - a sequence of nodes join by edges
Simple Path - if all nodes are distinct
Connected Graph - if for every pair of nodes, there is a path 
Cycle 		- Same as Simple path, but start and end at the same node


### Adjacency Matrix

Graphs can be represented by a ${n x n}$ adjacency matrix
where n is number of nodes. if there is an edge between two nodes, there is a 1 on the matrix. otherwise 0.

so takes O(n^2) space 

### Adjacency List 
This is another way to represent a graph. It has a better way to find neighbors of each node. there is a n size list. each item in the list is a linked list of the neighbors that node has. 

Space is ${theta(m+n)}$ where m is number of edges, and n is number of nodes

say there are 3 nodes, and there are edges {(a,b), (b,c), (a,c)} then the adjacency list is 

~~~code
node a:  -> b  > c
node b:  -> c
node c: 
~~~

#### Properties

AL is good for sparse graphs, because there will be fewer linked lists. and we can approximate the space as {O(n)}

(NEED HELP ON THIS) Even if it is very dense, the size of the AL is at most the sum of the degrees of the nodes. 

### Tree Properties 
If ${G} is a undirected graph on ${n} nodes, any two of the following statements imply the third. 

- G is connected
- G does not contain a cycle 
- G has ${n - 1} edges

## Breadth First Search 

Explores from start node S. and add layers, one layer at a time.

Each layer ${n}$ is neighbors of layer ${n-1}$ node. 

*Theorem* For each ${i}$, ${L_i}$ consists of all nodes at exactly ${i}$ from ${s}$. and there is a path from ${s}$ to ${t}$ ${IFF}$ ${t}$ appears in some layer 

*Theorem* BFS runs in ${O(m+n)}$ time , if in adjacency list 

- In Adjacency lists, there are ${m}$ nodes and ${n}$ edges representing the node's neighbours.
- when we consider node ${u}$, there are degree(u) incident edges (u,v)
- total time processing edges is sum of of all degress = 2 * number of edges


## Bipartite graph 
short way to remember this is that if all nodes can be colored such that each edge has a blue node on one end and white on the other. 

If a graph is bipartite, then there cannot be an odd length cycle. 

### Bipartite grah and BFS Tree 
to check if something is a bipartite graph, you run BFS to generate a BFS tree, then see if you can color each layer distinct color. 

Exactly one of the following holdes:
1. No edge of G joins two nodes of the same layer, then G is bipartite
2. an edge of G joins two nodes of the same layer, and G has odd-length cycle, so not bipartite

(But dont BFS tree hide edges that are not discovered?)

## Directed Graphs
### Terminologies
Mutually Reachable - if there is a directed path from node ${u} to ${v} and vice versa 
Strongly Connected - if every pair of nodes is mutually reachable, then the graph is *Strongly Connected*
Strong Component - maximal subset of mutually reachable nodes. (cannot add more nodes without breaking 'strong connectness')
Directed Acyclic Graph - a directed graph that contains no directed cycles. 
Topological order 	   - is an ordering of its nodes ${v1, v2, .. vn}$ so that every edge ${(v_i,v_j)}$ we have ${i < j}$

*Theorem* - Can see if ${G} is strongly connected in ${O(m+n)} time

1. Pick any node s 
2. Run BFS from s in G 
3. Run BFS from s in G reverse 
4. if all nodes are reached in both BFS, then G is strongly connected


### Lemma, If G has a topological order, then G is a DAG 

Proof by Contradiction. 

1. Suppose G is not a DAG , then this means there exists a directed cycle
2. let ${v_x}$ be the vertex with the lowest index in the cycle 
so ${v_x...v_{x+1}.. v_{x+2}... v_{j} ... and ... v_x$

3. for ${v_j}$ to go to ${v_x}$, ${j < x}$ , per topological order but ${j > x}$
hence contradiction

### Topological Sort Given a DAG 
- the Topological Sort is just a DFS with an extra temporary stack.

~~~code 
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
~~~

