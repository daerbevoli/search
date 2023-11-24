# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    print("Start:", problem.getStartState())

    stack = util.Stack() # stack used for DFS LIFO
    visited = set() # set -> no repetitions

    stack.push((problem.getStartState(), [])) # push the start position and an empty list

    while not stack.isEmpty():
        node, actions = stack.pop() # get the position in the node and actions
        if problem.isGoalState(node): # if we reached the goal return the actions
            return actions

        if node not in visited: # else check if we already visited the node and add if we didnt
            visited.add(node)
            for successor in problem.getSuccessors(node): # for each of the nodes successors
                stack.push((successor[0], actions + [successor[1]])) # push the position and actions into the stack

    return [] # if we cant get to the goal return empty list


    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # the code below is the same as with the DFS except for the usage of a queue instead of a stack
    # a queue uses FIFO policy used in BFS
    queue = util.Queue()
    visited = set()

    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        node, actions = queue.pop()
        if problem.isGoalState(node):
            return actions

        if node not in visited:
            visited.add(node)
            for successor in problem.getSuccessors(node):
                queue.push((successor[0], actions + [successor[1]]))

    return []

    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # the uniform cost search algorithm takes the least cost path
    # since the cost of all the edges are the same the result in th medium maze remains the same as bfs

    priority_queue = util.PriorityQueue()
    visited = set()

    priority_queue.push((problem.getStartState(), []), 0)
    while not priority_queue.isEmpty():
        node, actions = priority_queue.pop()

        if problem.isGoalState(node):
            return actions

        if node not in visited:
            visited.add(node)
            for successor in problem.getSuccessors(node):
                priority_queue.push((successor[0], actions + [successor[1]]), successor[2])

    return []

    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    priority_queue = util.PriorityQueue()
    visited = set()

    priority_queue.update((problem.getStartState(), []), 0)

    while not priority_queue.isEmpty():
        node, actions = priority_queue.pop()

        if problem.isGoalState(node):
            return actions

        if node not in visited:
            visited.add(node)
            for successor in problem.getSuccessors(node):
                h = heuristic(successor[0], problem)

                # this g is used for question 4
                #g = abs(successor[0][0] - problem.getStartState()[0]) + abs(successor[0][1] - problem.getStartState()[1])

                # this g is used for question 6
                g = abs(successor[0][0][0] - problem.getStartState()[0][0]) + abs(successor[0][0][1] - problem.getStartState()[0][1])

                # the reason being that for question 5 and 6
                # we use a tuple of tuples ad the state
                # instead of just a tuple with the position coordinates

                f = h + g
                priority_queue.update((successor[0], actions + [successor[1]]), f)

    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
