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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):

    frontier = util.Stack()
    frontier.push((problem.getStartState(), []))
    return dfs_help(frontier, problem, [])


def dfs_help(frontier, problem, visitedNodes):

    while not frontier.isEmpty():
        curr_state, action_state = frontier.pop()

        if problem.isGoalState(curr_state):
            return action_state

        if curr_state not in visitedNodes:
            visitedNodes.append(curr_state)

            for successor_state, successor_action, successor_cost in problem.getSuccessors(curr_state):
                if successor_state not in visitedNodes:
                    new_action_state = []
                    for moves in action_state:
                        new_action_state.append(moves)
                    new_action_state.append(successor_action)
                    new_state = (successor_state, new_action_state)
                    frontier.push(new_state)


def breadthFirstSearch(problem):

    frontier = util.Queue()
    frontier.push((problem.getStartState(), []))
    return bfs_help(frontier, problem, [])


def bfs_help(frontier, problem, visitedNodes):

    while not frontier.isEmpty():
        curr_state, action_state = frontier.pop()

        if curr_state not in visitedNodes:
            visitedNodes.append(curr_state)

            if problem.isGoalState(curr_state):
                print(action_state)
                return action_state

            successor_states = problem.getSuccessors(curr_state)

            for successor_state, successor_action, successor_cost in successor_states:
                print("In BFS", successor_state)
                new_action_state = []
                for moves in action_state:
                    new_action_state.append(moves)
                new_action_state.append(successor_action)
                new_state = (successor_state, new_action_state)
                frontier.push(new_state)

    return action_state


def uniformCostSearch(problem):

    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), [], 0), 0)
    return ucs_help(frontier, problem, [])


def ucs_help(frontier, problem, visitedNodes):

    while not frontier.isEmpty():
        curr_state, action_state, curr_cost = frontier.pop()

        if curr_state not in visitedNodes:
            visitedNodes.append(curr_state)

            if problem.isGoalState(curr_state):
                return action_state

            successor_states = problem.getSuccessors(curr_state)

            for successor_state, successor_action, successor_cost in successor_states:
                new_action_state = []
                for moves in action_state:
                    new_action_state.append(moves)
                new_action_state.append(successor_action)
                new_state = (successor_state, new_action_state,
                             curr_cost + successor_cost)
                frontier.push(new_state, curr_cost + successor_cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):

    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), [], 0), 0)
    return astar_help(frontier, problem, [], heuristic)


def astar_help(frontier, problem, visitedNodes, heuristic):

    while not frontier.isEmpty():
        curr_state, action_state, curr_cost = frontier.pop()

        if curr_state not in visitedNodes:
            visitedNodes.append(curr_state)

            if problem.isGoalState(curr_state):
                print(action_state)
                return action_state

            successor_states = problem.getSuccessors(curr_state)

            for successor_state, successor_action, successor_cost in successor_states:
                if successor_state not in visitedNodes:
                    new_action_state = []
                    for moves in action_state:
                        new_action_state.append(moves)
                    new_action_state.append(successor_action)
                    new_state = (successor_state, new_action_state,
                                 successor_cost + curr_cost)
                    frontier.push(new_state, successor_cost +
                                  curr_cost + heuristic(successor_state, problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
