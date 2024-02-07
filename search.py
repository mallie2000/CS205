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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    #Check if goal State
    if problem.isGoalState(problem.getStartState()):
        return []
    
    path = []
    visited = dict()
    stack = util.Stack()
    stack.push((problem.getStartState(),[]))

    while True:
        #All states were explored and no path was found
        if stack.isEmpty():
            return False
        
        state,path = stack.pop()
        visited[str(state)] = 1

        if problem.isGoalState(state):
            return path
        
        children = problem.getSuccessors(state)

        #check that there are potential paths
        if children:
            for state,direction,cost in children:
                if(str(state) not in visited):
                    new_path = path + [direction]
                    stack.push((state,new_path))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # check if goal state is the start state
    if problem.isGoalState(problem.getStartState()):
        return []

    path = []
    queue = util.Queue()
    visited = dict()

    # starting state
    queue.push((problem.getStartState(), []))
    visited[str(problem.getStartState())] = 1

    while True:
        if queue.isEmpty():
            return False

        # next state and path
        state, path = queue.pop()

        if problem.isGoalState(state):
            return path

        children = problem.getSuccessors(state)
        for state, direction, cost in children:
            if str(state) not in visited:
                new_path = path + [direction]
                queue.push((state, new_path))
                visited[str(state)] = 1

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # check if start state is goal state
    if problem.isGoalState(problem.getStartState()):
        return []

    pq = util.PriorityQueue()
    visited = set()
    cost = 0
    item = (problem.getStartState(), [], cost)
    pq.push(item, cost)

    while not pq.isEmpty():
        state, path, old_cost = pq.pop()

        # Mark the state as visited only if it's not the goal state
        if state not in visited:
            visited.add(state)

            if problem.isGoalState(state):
                return path

            children = problem.getSuccessors(state)

            if children:
                for child_state, direction, child_cost in children:
                    if child_state not in visited:
                        new_path = path + [direction]
                        new_cost = child_cost + old_cost
                        new_item = (child_state, new_path, new_cost)
                        pq.push(new_item, new_cost)

    return False



    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
