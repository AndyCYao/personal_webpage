title: CMPT 307 Cheat Sheet
date: 2017-12-09

Course summary for 307 DS/Algorithm II with Valentine Kabanet

***Breadth First Search***

- has property that each layer is one edge distance away from the previous layer

- runs in O() time when in adjacency list

- can be used to see if a graph is 2 colorable / bipartite, by creating a tree G' and see if theres an edge in original graph that connects two nodes of same level in G'. if there is, there is a odd cycle, and cannot be 2 colorable

    
***Depth First Search***

- useful for direct acyclic graphs DAGS. (checking if there is a cycle)

- has property that an edge in original graph G  a DFS tree 


***DAG and Topological ordering***

- uses DFS to find the topo. ordering, repeatly traceback a starting node until a node without entering edge is found, then pop that, and repeat

***Dijkstra's Algorithm***

- finds the shortest path to any node from starting node s.
- can't be used for edges with negative weight.
- uses BFS to find nodes to add to the set of explored nodes. 
- use min heap to order nodes of different weight

***Kruskal Algorithm***

- finds the minimum spanning tree by repeatly adding min weight edges that does not create cycle
- when running this algo we should sort the edges from low to high weight


***Prim's Algorithm***

- think modified Dijkstras Algorithm. finds the minimum spanning tree by repeatly adding min weight unexplored vertex to the set of explored vertex - that does not create a cycle

???***Disjoint Data Structure***

- this is used for kruskal algo to find edges that do not create cycle.
- we group all the "connected" edges in independent sets. so in kruskal if we are checking if two edges u, v create a cycle, we simply look for the set with u, and see if v is in it.

???***Link By Size***

***Interval Scheduling***
- to minimize lateness, we do greedy algorithm (GA) by selecting jobs with earliest deadline first
- to get the maximum size of job in a schedule, we do GA by selecting earliest finish time first
- Interval Partitioning...

***Divide and conquer***
- refers to algorithm that divide the problem into subproblems, so smaller chunks that is easier to solve (like merge sort)

- the run time of divide and conquer are usually logarithic , because we can visualize the calls in a tree structure, and each level is dividing the input size by some factor, and there are k such levels.

???***Counting Inversions*** 
Inversions have to do with job scheduling as well

???***Integer Multiplication / Karatsuba**

***Weighted Interval Scheduling***
- is a type of dynamic programming (DP)
- need to use an array that stores the max weight at n number of jobs. 

***Knapsack problem***
- given weight n of a knapsack, find the max value of items to put in the knapsack.
- the array will be a table with i items as rows, and n number as columns.

***Floyd Warshall (All Shortest Path)***
- the intuition is that if a path from \\(s\\) to \\(t\\) has intermediate nodes, let \\(a\\) be one of those nodes.  so we can breakdown the question into subproblems

1. shortest path from \\(s\\) to \\(a\\) , plus 
2. shortest path from \\(a\\) to \\(t\\) 

the DP array will have the value of shortest path from S to any node n

***Bellman Ford***
- this is a DP algorithm that accomodates for negative edge cycles 
- initialize distance from \\(s\\) to all nodes as infinity.
- it runs in n-1 time, (because a path has at most n-1 edges)
- each time we update the distance from s to i node by looking every edge (u,i) (relaxing the edge)
    :::code 
    if d(v) > d(u) + w(v):
        d(v) = d(u) + w(v)

- the algo ends at n-1, if we want to check for negative cycles, we run the algo one more time, and see if there are any changes, if there is, that means theres negative cycle

***Longest Common Subsequence***

***Longest Increasing Subsequence***

***Min Cut Max Flow***
is a network flow idea that in an s t cut, where graph is separated in two sides where s is on oneside and t is on another. the minimum cut's capacity = the max flow from s to t. 

***Ford Fulkerson Algorithm***
Residual Graph -> a \\(graph_f\\) that has exact same nodes as G, but have added "back edges" to accomodate for unused capacity.

Augment Path ->  a path in the residual graph you can add flow to

takes the idea of residual graphs, the algo keeps iterating while there is an augmenting path in \\(G_f\\) 

***Choosing Better Path - Capacity Scaling***

***matching in a bipartite graph***
network flow can help with finding out match in a graph, connect left side with s, and rightside with t. the edges connected to s will each have 1 capacity. 

then run ford fulkerson algo, if the max flow equals to size of L then there is perfect matching, otherwise it shows the max number of matching possible.

this works because of __conservation of flow__ which says for all nodes except s, t, what goes in = what goes out. and __integrality invariant__ which says the flow values are integer, you can't subdivide an integer (if in edge is 1, and theres two out edge, you can't say .5 and .5 for both outflow, only 1 out edge is used)


***project selection***
network flow can solve project selection questions too, given a set of projects with their revenue, a set of components and their cost, and a list of dependencies between project and component, we can create a network to solve the optimum set of projects to take on.

1. connect s to components, each edge (s,c) will have weight of the cost of the component
2. connect t to projects, each edge (p,t) will have weight of the revenue of the component
3. connect components and projects by the list of dependencies , each (c,p) will have weight infinity

then run ford fulkerson algorithm, which will create a graph that has some edges used, and some not.

take a min cut such that the capacity is finite, this will be the optimum project selected

the intuition is that the finite min cut will contain outgoing edges that are either

- revenue on missing project
- cost of selected project

And then the max profit is just Total possible revenue less those edges

***Edge Disjoint Path***
number of paths from s to t that does not have overlap edges

Menger's theorem says max number of edge disjoint paths is the same as min cut from s to t, assuming each edge has capacity 1


***Konig-Egervary Theorem***
this theorem says the maximum size of matching is <= the minimum size of vertex cover

***Approximation***

theres an \\(O(n)\\) way of finding vertex covers, the result is approximately

\\(S = 2S_{optimal}\\)

    :::code
    findVC(graph G):
        init S <- {}  //our vertex cover
        while there are edges in G:
            take an edge (u,v)
            add both u and v into set S
            remove all edges related to u, v
        return S

this is using the idea that S really contains set of pairs of independent nodes, 




### Proofing strategy
***Greedy Algorithm***

think in terms of promising solutions, for each round of iteration, the invariant is that
\\(S_{greedy} \subseteq S_{promising} \subseteq S_{greedy} +\\)some future choices 

the greedy algorithm chooses something that belongs to the \\(S_{promising}\\)

***Dynamic Programming***

- describe an array \\(A(n)\\) that stores the answer at \\(n\\) , this will be the max, or min of the question, or true/false etc.

- build a recurrence that uses the \\(A(n)\\), this is call memoization

- build the algorithm that populates \\(A(n)\\) based on the recurrence.

- retrieve the answer by looking at \\(A(n)\\), depending on the problem, the answer can be at the last spot of the array (for things like max number of something). or we need to build the answers from the array by iterating through it. 

*** NP Completeness ***

- first show that the problem z is NP , this involves checking if there is a certifier that can validate an answer in polytime

- find a NP Complete problem X that can reduce to z. this involves converting an instance of X to have the properties z. lets call this new converted instance Y

- we then need to proof that Y Is true if and only if z is true, and vice versa. 

