# ac-3.py: goes through a csp, returning false if
# an inconsistency is found and true otherwise
# Author: Edmund Aduse Poku
# Class: CS 76, Prof Li, Fall 2020

# input: csp, a binary CSP with components (X, D, C)
def ac_3(csp):
    # ac_3_set: a set of arcs, initially all the arcs in the csp
    # arcs are formed by pairs with a constraint relationship
    ac_3_set = set(csp.constraints.keys()) # a set of arcs, initially all the arcs in the csp

    while ac_3_set:
        x_i, x_j = ac_3_set.pop()

        if revise(csp, x_i, x_j):
            if len(csp.domains.get(x_i)) == 0:
                return 0

            for x_k in csp.neighbors.get(x_i):
                if x_k is not x_j:
                    ac_3_set.add((x_k, x_i))
    return 1

# returns true iff we revise the domain of x_i
def revise(csp, x_i, x_j):
    revised = 0
    const_satisfied = 0

    for val_i in csp.domains.get(x_i):
        while not const_satisfied:
            for val_j in csp.domains.get(x_j):
                if  csp.arc_is_consistent(x_i, x_j, val_i, val_j):
                    const_satisfied = 1

        if not const_satisfied:
            csp.domains.get(x_i).remove(val_i)
            revised = 1

    return revised
