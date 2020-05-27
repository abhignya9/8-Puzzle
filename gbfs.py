#!/usr/bin/env python
# coding: utf-8

from Puzzle8 import *
from collections import deque

def Greedy_Best_First_Search(problem):
    queue = deque([]) #fringe
    visited = HashTable() #hash table to keep a track of all the nodes expanded and their h values
    root=TreeNode(problem,problem.initial_state)
    visited.add_hash(root.state,0)
    #expand root node
    new_nodes=root.generate_new_tree_nodes()
    #initialize counters
    nodes_generated, nodes_expanded,que_len = 0, 1, 0
    #add the generated nodes to queue
    for new_node in new_nodes:                                    
        nodes_generated+=1
        queue.append(new_node)
        que_len+=1
    while len(queue)>0:
        #pick the node from queue with minimum h value
        next = min(queue, key=lambda node: node.h)
        #if goal node, print the stats
        if(next.goalp()):                                         
            print("Number of nodes expanded including root node = " ,(nodes_expanded))
            print("Number of nodes generated = ",(nodes_generated))
            print("Maximum length of queue:",que_len)
            print("Number of moves = ",(next.g))
            del(queue)
            visited.delete_hash()
            return next.path()
        else:
            #else, add it to the visited list if not already present in it
            queue.remove(next)                                    
            if (not visited.in_hashp(next.state)):
                visited.add_hash(next.state,next.h)
                new_nodes=next.generate_new_tree_nodes()
                nodes_expanded +=1
                for new_node in new_nodes:
                    nodes_generated+=1
                    #since the h value of a state doesn't change with number of moves,
                    #we don't have to expand it anymore if done once already(avoiding repetition)
                    #hence add to the queue only if its not expanded earlier
                    if(not visited.in_hashp(new_node.state)):
                        queue.append(new_node) 
                        que_len+=1
                        
    print('No solution')
    return NULL

problem=Puzzle8_Problem(Example1) 
output=Greedy_Best_First_Search(problem)
print('Solution Example 1:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2) 
output=Greedy_Best_First_Search(problem)
print('Solution Example 2:')
print_path(output)


wait = input("PRESS ENTER TO CONTINUE.")


problem=Puzzle8_Problem(Example3) 
output=Greedy_Best_First_Search(problem)
print('Solution Example 3:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example4) 
output=Greedy_Best_First_Search(problem)
print('Solution Example 4:')
print_path(output)
