#--------------------------------------------------------------------------------
# Name:      astar solver.py
#
# Purpose:   This .py file contains all required functions except the function that prints
#            the solution. This can be find in the puzzle.py file.

#   legal_moves function: creates a list with all the moves 0 is allowed to do given its
#   coordinates in the form (row,column)
#
#   generate_child function: it generates children for every node, where node is a state and
#   ech child is a possible next state.
#
#   find_path function: return a list with the steps.
#
#   manhattan function: return the heuristic of a state using manhattan distance
#
#   f function: state-evaluation function
#
#   astar function: astar search algorithm.
#
#Required libs: heapq (should not need installation)
#
#Author:    Ioannis Mastoras
#
#Created:   4 April 2020
#
#-----------------------------------------------------------------------------------

import heapq

#------USER INPUT--------------------
n = int(input("Enter size of tile puzzle (integer greater that 0): "))  

state = []  #store the state as a list
print("\n Enter start state row by row (numbers delimited by white space): \n")

for i in range(0,n):
    s = list(map(int,input("Enter Start state: row %a : " % str(i+1)).strip().split()))[:n**2]  #strip() add a comma, and split() deletes the space
    for k in s:
        state.append(k) #adds everynumber in the list
print("\n Enter goal state row by row (numbers delimited by white space): \n")
goal_state = []
for i in range(0,n):
    s = list(map(int,input("Enter Goal state: row %a : " % str(i+1)).strip().split()))[:n**2]  
    for k in s:
        goal_state.append(k)
#########################################################

######--returns a list with legal moves of 0 for a given state--####
def legal_moves(row,col):
            
    legal_action = ['Down', 'Left', 'Up','Right'] #list with all possible moves
    
    if row == 0:  # up is not not allowed at the top row
        legal_action.remove('Up')
    elif row == n-1:  # down is not allowed at the bottom row
        legal_action.remove('Down')
    if col == 0:      #Left is not allowed at the leftost column
        legal_action.remove('Left')
    elif col == n-1:  #Right is not allowed at the rightmost column
        legal_action.remove('Right')
    return legal_action #list with moves 0 can make
#########################################################

####--retuns the children, i.e. next states, for a given node/state, based on the legal moves---##
def generate_child(node,g):
    
    children = []  #list of children    
        
    x = node.index(0)  #index of zero in the list, i.e. where is the zero. 
                       #Note that the NxN matrix has been converted to 1D matix, i.e. a list
   
    i = int(x / n)  #row coordinate
    j = int(x % n)   #column coordinate
    
    legal_actions=legal_moves(i,j) #calls the function legal_moves

    for action in legal_actions:

        new_state = node.copy()     #loop always starts with the curent state, and then find the child
            
        if action == 'Down':
            new_state[x], new_state[x+n] = new_state[x+n], new_state[x]
            
        elif action == 'Left':
            new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
                                                                            #for each move in the list, it changes the index of 0 accordingly
        elif action == 'Up':
            new_state[x], new_state[x-n] = new_state[x-n], new_state[x]
            
        elif action == 'Right':
            new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            
            
        children.append([f(g,manhattan(new_state)),new_state,action]) #puts in the chidren list the child, the action that resulted to that state, and the cost
        
   
    return children #a list of children, i.e. next states
#########################################################

##--returns the heuristic for a state using manhattan distance--##
def manhattan(mstate):

    manhattan = 0 

    for i in mstate: #for tile in the board

        if i != 0: #we need only calculate it for n-1 tiles, so I exlcluded 0
            t = mstate.index(i) #index of the tile in the current state
            s = goal_state.index(i) #index of the tile in the goal state
            
            drow = abs(int(t/n)-int(s/n)) #difference in row
            dcol = abs(int(t%n)-int(s%n)) #difference in columns

            manhattan += drow + dcol #add the difs. to get the manhattan distance

    return manhattan #the heuristic of the state
#########################################################

##--State-Evaluation Function--##
def f(g,h): 
    f = g+h #g is the distance for the current state back to start and h is the heuristic/manhattan
    return f
#########################################################

##--A*--##
def astar(initialState,goalState):
    
    openList = [] #list of states, their cost, and step to creat them
    closedList = [] #list of states with lowest cost

    openList.append([0,initialState,''])
    
    g = 1 #g is the distance for the current state back to start
    while openList:

        heapq.heapify(openList) #prioritizes the open list according to the cost of the states
                                #from lowest to highest

        node = heapq.heappop(openList) #chooses the swallowest node in frontier; the one at the front
        closedList.append(node) #puts node in the closedList since it has the smallest cost value

        if node[1] == goalState: #test if the node is the goal node
            
            return find_path(closedList) #calls find_path function to return the path
            break #stops the loop

        ch = generate_child(node[1],g) #calls the generate_child function to return a list of children of the node

        for child in ch: #child has the form [cost,child node],'action']

            if child not in openList: #puts all chilren on the openlist
                openList.append(child)
        g += 1 

    return 
#########################################################                
   
###--returns a list with the moves 0 needs to make for the puzzle to be solved
def find_path(lst): #lst is a list with all nodes, actions, and cost

#it has the form [ [0,[start node],None],...[cost,[node],'action'],..[cost,[goal node],'action']]

    steps = []
    for i in range(1,len(lst)): #exclude initial state
        steps.append(lst[i][2]) #put all steps in a list
    return steps #return the list

###################################################
#
#End of solver.py
#You shoud run puzzle.py to see the output
#
###################################################
