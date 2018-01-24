title: "AI Survey"
date: 2018-01-05
code: "CMPT 310"
semester: "Spring 2018"


Pancake Flipping Robot -> close world, only one action 

AI falls in four categories

__Think Humanly__
comparing with thinking in humans, construct the working of human mind.


__Think Rationally__
what are correct arguments, and various logics


__Acting Humanly__
like google home, siri, etc. parsing answers from voice


__Acting Rationally__
rational behaviour -- doing the right thing.

the Mars rover had autnomous planning and scheduling 

thinking vs acting, bacterias, are reacting from stimulus, and then act, but its hard to claim they are thinking. 

so acting does not always require thinking
	- instinct
	- reflexs like blinking
	- insects, Siri, Watson? 

what are the advantages of thinking? why thinking animal have evolved? 
- so we can deal with new situations. (maybe stimulus is preprogrammed) so flexibility
- planning vs reacting 
- inventions
- Flexibility
- Robustness



### What is intelligent system
anything that can be viewed as preceiving its environment through sensors, and acting upon the environment through actuators.

our human agents are : eyes ears for sensors, and our actuators are our limbs

robot agents are : cameras, range finders for snesors, and wheels motor for actuators.

agent function maps from percept histories to actions

the agent program runs on the physical architecture to produce the behaviour f

agent = architecture + program

in the case of self driving car -> the __agent__ function says if theres person in front of you, (__percept__) then maps to the __action__  of stopping the car. 



### The PEAS model

stands for performance measure environment, actuator, sensor

this defines the task for the agent. 

in a Interactive Spanish Tutor
1. The Performant Measurement - student success, 
3. Environment  - the set of students
3. The Actuator - the lessons themselves
4. Sensor      - the keyboard, speakers. 

Self Driving Car
1. Performance Measure - Safety record, traffice rules, on time performance, 
2. Environment - the road 
3. Actuator - 
4. Sensor -  

### Environment Types
- Fully Observable (vs partially observable) does the agent know everything relevant for its environment (chess robot knows all of its playing area), if not a robot has to make a decision, using probability
- Deterministics(vs stochastic), is there something in the environment beyond the control (chess is deterministic, poker is stochastic) 
- Episodic (vs sequential) are we in an environemnt where we can break down the tasks in sequence, (do i need to remember the past to make my choice) , anyting with a budget is sequential, if we dont need to remember anything in the past its episodic. 
- Static(vs dynamic), agent should/consult the world when choosing action for dynamic. (Taxi driver robot has dynamic world) poker robot is static. anything where its turn based is static environment
- Discrete (vs continous) clearly defined percepts and actions, or range of value (continous). 
- Single Agent (vs Multi agent) are you the only entity in this environment. Cross Word (single agent), Poker ( multi agent) 

some of these distinctions are not cut and dry. 


### Simple Reflex State  Agents ###
simple but very limited intelligence, does not depend on percept history, only on current percept
(thermostat), no memory requirements, so it can lead to infinite loop


### State Based Reflex Agents ###
opposite of simple reflex agent, has history, 

### Model Based Reflex Agent ###
has a sense of modelling the world.  one level higher than the previous two examples

### Goal Based Agent
uses knowledge about a goal to guide its action (use knowledge, search and planning)

monkeys and banana problem - (monkey can use a stick to strike at the banana to get the banana from tree)

### Utility Based Agent
Goals are not always enough, - many actions sequence gets car to destination, but others include how fast, how safe. Utility measure a degree of "happiness", "goodness", "success" , so utility base is built on multiple goal based agents.


### What is control theory:
about how robots control themself, such as using sensors like thermostat,

## Game Theory

the previous section was an introduction of AI, now we will drill down to decision theory

### Rational Choice Theory:

make decisions base on the value some decision provides. 

sunk cost fallacy - 

make a decision matrix
	utility
go	-200 + -10
stay	0 + -10

but, the -10 pay a ticket, 


### Uncertainty

here it is defined as the `set` of all possible outcome 

expected value is - possibility * outcome

if we know the probability of each outcome, then single agent decision making is straight forward. 


### Multi agent setting

each player has a set of options or strategies, and choose __independently__ off the other player. each player gets a payoff (AKA Utility), they would want to max the utility
