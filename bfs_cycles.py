# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:07:03 2020

@author: gojea

from Puzzle8 import *
from collections import deque

def breadth_first_search_cycles(problem):
    a = HashTable()
    queue =deque([])
    nodes_generated, nodes_expanded,que_len = 0, 0, 0
    root=TreeNode(problem,problem.initial_state)
    queue.append(root)
    que_len+=1
    a.add_hash(root.state)
    while len(queue)>0:
        next=queue.popleft()
        if next.goalp():
            print("Total number of moves  :",next.g)
            print("Maximum length of queue:",que_len)
            print("No.of nodes generated  :",nodes_generated)
            print("No.of nodes expanded   :",nodes_expanded)
            del(queue)
            return next.path()
        else:
            new_nodes=next.generate_new_tree_nodes()
            nodes_expanded+=1
            for new_node in new_nodes:
                if (check_cyclic_repeats(new_node,a)!=True):
                    queue.append(new_node)
                    que_len+=1
                    a.add_hash(new_node)
                    nodes_generated+=1
                
    print("No Solution")
    return NULL


def check_cyclic_repeats(new_node,a):
    return(a.in_hashp(new_node.state))

problem=Puzzle8_Problem(Example1) 
output=breadth_first_search_cycles(problem)
print('Solution Example 1:')
print_path(output)

problem=Puzzle8_Problem(Example2) 
output=breadth_first_search_cycles(problem)
print('Solution Example 2:')
print_path(output)

problem=Puzzle8_Problem(Example3) 
output=breadth_first_search_cycles(problem)
print('Solution Example 3:')
print_path(output)

problem=Puzzle8_Problem(Example4) 
output=  breadth_first_search_cycles(problem)
print('Solution Example 4:')
print_path(output)
