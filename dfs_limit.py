# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:38:50 2020

@author: gojea
ABHIGNYA GOJE
700703549
Certificate of Authenticity: “I certify that the codes/answers of this assignment are
entirely my own work.”
"""

from Puzzle8 import *

def depth_first_search_limit(problem,g):
        queue =deque([])  #LIFO for depth first search
        a = HashTable()
        root=TreeNode(problem,problem.initial_state,0,0)
        queue.append(root)
        a.add_hash(root.state,0)
        next=root
        nodes_generated = 1 
        nodes_expanded = 1
        que_len=1         #variable to store the max length of queue for dfs
        while (len(queue)>0):
            new_nodes=next.generate_new_tree_nodes()
            nodes_expanded += 1
            #Remove the nodes that are not visited
            for new_node in new_nodes:
                if (not check_cyclic_repeats(new_node,a) and new_node.g<=g):
                    queue.append(new_node)
                    que_len+=1
                    nodes_generated += 1
                    x = a.get_hash_value(new_node.state)
                    if (x == -1 or x > new_node.g):
                        a.add_hash(new_node.state,new_node.g)

            #Check if this node is Goal state 
            #if yes, print the stats
            #else, check for children and break out of loop        
            while (len(queue)>0):
                new_node=queue.pop()
                if (new_node.goalp()):
                    print("Maximum length of queue   : ",que_len)
                    print("Number of nodes generated : ",nodes_generated)
                    print("Number of nodes expanded  : ",nodes_expanded)
                    print("Number of moves           : ",a.get_hash_value(new_node.state))
                    del(queue)
                    a.delete_hash()
                    return new_node.path()
                else:
                    if new_node.g > g:
                        next=queue.pop()
                    else:
                        next=new_node
                    break
        print("No Solution or goal not couldn't be reached with in the limit.")
        return root.path()

    
    
def check_cyclic_repeats(new_node,a):
    return (a.in_hashp(new_node.state))


problem=Puzzle8_Problem(Example1) 
print('Solution Example 1:')
output=depth_first_search_limit(problem,10)
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2) 
output=  depth_first_search_limit(problem,10)
print('Solution Example 2:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example3) 
output=  depth_first_search_limit(problem,10)
print('Solution Example 3:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")


problem=Puzzle8_Problem(Example4) 
output=  depth_first_search_limit(problem,10)
print('Solution Example 4:')
print_path(output)