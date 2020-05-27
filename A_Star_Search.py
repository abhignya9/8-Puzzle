#!/usr/bin/env python
# coding: utf-8

from Puzzle8 import *
from collections import deque

def A_Star_Search(problem):
    queue = deque([]) #fringe
    visited = HashTable() #hash table to keep a track of all the nodes expanded and their f values
    root=TreeNode(problem,problem.initial_state)
    #add the root to the visited list 
    visited.add_hash(root.state,0)
    #expand the root
    new_nodes=root.generate_new_tree_nodes()
    #initialize the counters
    nodes_generated, nodes_expanded,que_len = 0, 1, 0
    for new_node in new_nodes:
        #add all nodes expanded from the root to the queue
        nodes_generated+=1
        queue.append(new_node)
        que_len+=1
    while len(queue)>0:
        next = min(queue, key=lambda node: node.f)  #picks the node from the queue that has the lowest f value
        #if the node is a goal node, print the stats
        if(next.goalp()):
            print("Number of nodes expanded including root node = " ,(nodes_expanded))
            print("Number of nodes generated = ",(nodes_generated))
            print("Maximum length of queue = ",que_len)
            print("Number of moves = ",(next.g))
            del(queue)
            visited.delete_hash()
            return next.path()
        #else check if its already present in the visited list
        #if not,add it to visited list and expand further
        else:
            queue.remove(next)
            if (not visited.in_hashp(next.state)):
                visited.add_hash(next.state,next.f)
                new_nodes=next.generate_new_tree_nodes()
                nodes_expanded +=1
                for new_node in new_nodes:
                    #add all generated nodes to the queue
                    queue.append(new_node) 
                    que_len+=1
                    nodes_generated+=1
            else:
                #if already present in visited, check if the new h value is lesser,
                #if yes, update the visited list with lower h value
                #if not, expand no further and move on to next minimum node in the queue(goes back to while loop)
                if(next.f < visited.get_hash_value(next.state)):
                    visited.add_hash(next.state,next.f)
                        
    print('No solution')
    return NULL


problem=Puzzle8_Problem(Example1) 
output=A_Star_Search(problem)
print('Solution Example 1:')
print_path(output)


wait = input("PRESS ENTER TO CONTINUE.")


problem=Puzzle8_Problem(Example2) 
output=A_Star_Search(problem)
print('Solution Example 2:')
print_path(output)
wait = input("PRESS ENTER TO CONTINUE.")


problem=Puzzle8_Problem(Example3) 
output=A_Star_Search(problem)
print('Solution Example 3:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")


problem=Puzzle8_Problem(Example4) 
output=A_Star_Search(problem)
print('Solution Example 4:')
print_path(output)
