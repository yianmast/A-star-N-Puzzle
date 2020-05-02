#----------------------------------------------------------------------------------
# Name:      astar puzzle.py                              
#
# Purpose:   This .py file takes the list of steps from solver.py, and prints out
#            the the steps and the state after each step
#
#IMPORTANT! It must be in the same folder with solver.py!
#
#Author:    Ioannis Mastoras
#
#Created:   4 April 2020
#
#----------------------------------------------------------------------------------
from solver import astar, state, goal_state, n
#from solver.py import the function astar, and the variables state, goal_state, and n (see solver.py for documentation)

 
steps = astar(state,goal_state) #a list with all the steps

if not steps and state!= goal_state:  #if there are no steps, then the algorithm did not find a solution
    print('\n No Solution Could Be Found')
    
elif not steps and state == goal_state: #in case initial and final states are the same
    print('\n There is Nothing to Solve')

else:
    print('\n','----Initial State----','\n')

    k = 1 #count
    
    while k<n+1:  #loop to print the list as a NxN board
         print('',*state[n*(k-1):n*k]) #prints it row by row
         k += 1
    print('\n','----------------')
    print('\n','Solution')
    print('\n','----------------')

    for a in steps:  #traces the list with the steps
        
        t = list(state).index(0) #finds the index/position of zero for that state

        print('\n',a,'\n')  #prints the step
                
        if a == 'Up':
            state[t], state[t-n] = state[t-n], state[t]
        elif a == 'Down':
            state[t], state[t+n] = state[t+n], state[t]
        elif a == 'Left':
            state[t], state[t-1] = state[t-1], state[t]
        elif a == 'Right':
            state[t], state[t+1] = state[t+1], state[t]

        l=1  #count
        while l<n+1: #loop to print the state as matrix
              
            print('',*state[n*(l-1):n*l]) #prints it row by row
            l += 1

###################################################
#
#End of puzzle.py
#
###################################################
