CS 7641 Assignment 4: Reinforcement Learning

This project seeks to understand the computational and predictive qualities of two MDPs applying three reinforcement learning algorithms.

	- Value Iteration
	- Policy Iteration
	- Q-Learning


## Getting Started & Prerequisites
	- Download code of this project from Github: https://github.com/yinuomvp/Reinforcement-Learning
	- Open the entire folder as a project in IntelliJ IDEA to run EasyGridWorldLauncher.java and HardGridWorldLauncher.java by setting the MAX_ITERATIONS (line32) and NUM_INTERVALS (line33) 
	- Run analysis.py in PyCharm, with matplotlib installed


##Important Notes
	- Code in this assignment was changed from reference: https://github.com/juanjose49/omscs-cs7641-machine-learning-assignment-4


## Running the Code

Code is downloadable at https://github.com/yinuomvp/Reinforcement-Learning

The code consists of the following main sections:

Running codes:
	- EasyGridWorldLauncher.java and HardGridWorldLauncher.java. 
	- analysis.py is built to making plots analysis through the output arrays generated in EasyGridWorldLauncher.java and HardGridWorldLauncher.java. 

Supportive codes:
	- AgentPainter.java, MapPrinter.java, LocationPainter.java and WallPainter.java are built to construct the background and styles for the agent and maze. 
	- AnalysisAggregator.java is built to collect all the values from reward functions and perform computations. 
	- AnalysisRunner.java is built to run the algorithms of Policy Iteration, Value Iteration, Q-Learning. 
	- AtLocation.java, BasicRewardFunction.java, BasicTerminalFunction.java are built to control the location at which the agent is on the grid world, and assign the appropriate reward for the agent. 
	- Movement.java is built to manipulate the action performed by the agent.
