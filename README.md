## An invincible AI Agent

<img src="https://t3rmit4nk.github.io/TicTacToeAIAgent/TicTacToeAI.png" width="300" height="auto" />

I made this agent using the cycle:
* Plan
* Execute
* Perceive

This type of games, with an enemy, are more complicated than the other and it's similar to real problems.

To resolve this kind of problems the important think is to manage them like a searching problems where:

* States: are the configuration of the game
* Player(s): which player should play in the state 's'
* Result(s,a): the result state after an action
* Terminal-Test(s): determ if the game is ended
* Utility(s,p): utility function to evaluate the ending states of the game for the user p


### Two types of algorithm solve this problem

* Min-Max algorithm
* Alpha-Beta algorithm

Both are implemented in the code.

## Min-Max

<img src="https://t3rmit4nk.github.io/TicTacToeAIAgent/minMax.png" widht="400" height="auto">

It's very useful for simpler games, it generate all the possible configuration for the current state. Choosing the action that maximize your chance of victory and minimize the enemy one. If you want to read more [MinMax](https://en.wikipedia.org/wiki/Minimax).

## Alpha-beta

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/AB_pruning.svg/1920px-AB_pruning.svg.png" widht="400" height="auto">

It's similar to Min-Max algorithm but it take less time and space beacause it didn't generate all the possible permutations. Instead it cut the leaves of the permutation tree, visiting a minor number of state. If you want to read more [AlphaBeta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
