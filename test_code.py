# -*- coding: utf-8 -*-

from task import Task
from buchi_parse import Buchi
from workspace import Workspace

import datetime
from collections import OrderedDict
import numpy as np


import matplotlib.pyplot as plt
import pyvisgraph as vg
from termcolor import colored
import networkx as nx



if __name__ == "__main__":
    # task
    
    start = datetime.datetime.now()
    task = Task()
    buchi = Buchi(task)
    buchi.construct_buchi_graph()
    buchi.get_minimal_length()
    buchi.get_feasible_accepting_state()
    buchi_graph = buchi.buchi_graph
    NBA_time = (datetime.datetime.now() - start).total_seconds()
    print('Time for constructing the NBA: {0:.4f} s'.format(NBA_time))
    
    
    '''
    Following code shows implementation of the functions in the class:
        
        buchi.update_alternate_transition(currentNBAState, nextNBAState) # command provides alternate 'truth' value that enables transition 
        
        buchi.delete_transition(currentNBAState, nextNBAState) # deletes edge in NBA if none of the actions are possible.
        
        buchi.get_next_NBA_state(currentNBAState, acceptingNBAState)  # command computes and returns next NBA state
        
        buchi.get_next_action(currentNBAState, nextNBAState) # "command to generate next action so that the above transition is enabled"
                
    '''
    flagFeasible = 1
    
    currentNBAState = "T0_init"
    #currentNBAState = buchi.buchi_graph.graph['init'][0]
    acceptingNBAState = buchi.buchi_graph.graph['accept'][0]
    
    nextNBAState = buchi.get_next_NBA_state(currentNBAState, acceptingNBAState)
    nextAction = buchi.get_next_action(currentNBAState, nextNBAState)
    print("\ncurrentNBAState: ",currentNBAState)
    print("nextNBAState: ",nextNBAState)
    print("nextAction: ",nextAction)
    
    
    #Suppose above action cannot be taken i.e. if we get flagFeasible=0. We will select the alternative action
    flagAlternate = buchi.update_alternate_transition(currentNBAState, nextNBAState) # update alternate action 
    nextAction = buchi.get_next_action(currentNBAState, nextNBAState)
    print("\nAfter updating action... \ncurrentNBAState: ",currentNBAState)
    print("nextNBAState: ",nextNBAState)
    print("nextAction: ",nextAction)
    
    
    # Suppose the action is again infeasible, i.e. flafFeasible = 0
    flagAlternate = buchi.update_alternate_transition(currentNBAState, nextNBAState)
    # flagAlternate will be False as both actions are not possible and thus we delete this edge in the NBA
    buchi.delete_transition(currentNBAState, nextNBAState)
    
    
    
    nextNBAState = buchi.get_next_NBA_state(currentNBAState, acceptingNBAState)
    nextAction = buchi.get_next_action(currentNBAState, nextNBAState)
    print("\nT0_init to accept_all edge is removed from NBA")
    print("currentNBAState: ",currentNBAState)
    print("nextNBAState: ",nextNBAState)
    print("nextAction: ",nextAction)
    
    currentNBAState = nextNBAState
    nextNBAState = buchi.get_next_NBA_state(currentNBAState, acceptingNBAState)
    nextAction = buchi.get_next_action(currentNBAState, nextNBAState)
    print("\ncurrentNBAState is updated")
    print("currentNBAState: ",currentNBAState)
    print("nextNBAState: ",nextNBAState)
    print("nextAction: ",nextAction)
    
    
    '''
    NBA graph of current task for reference
    T0_init :    /* init */
    	if
    	:: (1) -> goto T0_init
    	:: (l8_1) || (l12_1) -> goto T0_S2
    	:: (l4_2) -> goto T1_S3
    	:: (l4_2 && l8_1) || (l4_2 && l12_1) -> goto accept_all
    	fi;
    T0_S2 :    /* 1 */
    	if
    	:: (1) -> goto T0_S2
    	:: (l4_2) -> goto accept_all
    	fi;
    T1_S3 :    /* 2 */
    	if
    	:: (1) -> goto T1_S3
    	:: (l8_1) || (l12_1) -> goto accept_all
    	fi;
    accept_all :    /* 3 */
    '''
