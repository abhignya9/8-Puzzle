# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:10:02 2020

@author: gojea
"""

#from IPython.core.debugger import set_trace
from Puzzle8 import *
from collections import deque
def breadth_first_search_stats(problem):
    nodes_generated = 0
    nodes_expanded=0
    que_len=0
    queue =deque([])
    root=TreeNode(problem,problem.initial_state)
    queue.append(root)
    que_len+=1
    while len(queue)>0:
        next=queue.popleft()
        if next.goalp():
            print("Total no.of moves      :",next.g)
            print("Maximum length of queue:",que_len)
            print("No.of nodes generated  :", nodes_generated)
            print("No.of nodes expanded   :", nodes_expanded)
            del(queue)
            return next.path()
        else:
            new_nodes=next.generate_new_tree_nodes()
            nodes_expanded+=1
            for new_node in new_nodes:
                que_len+=1
                queue.append(new_node)
                nodes_generated+=1
                
    print("No Solution")
    return NULL

problem=Puzzle8_Problem(Example1) 
output=breadth_first_search_stats(problem)
print('Solution Example 1:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2) 
output=  breadth_first_search_stats(problem)
print('Solution Example 2:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example3) 
output=  breadth_first_search_stats(problem)
print('Solution Example 3:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example4) 
output=  breadth_first_search_stats(problem)
print('Solution Example 4:')
print_path(output)
