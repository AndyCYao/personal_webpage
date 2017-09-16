---
layout: page
title: "Data Structure and Algorithm II"
code: "CMPT 307"
semester: "Fall 2017"
---

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

### Does G.S always produce the same matches?
Yes, because G.S produces man (porposer) - optimal matches.
And man-optimal match are subset of all stable matches



