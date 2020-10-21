# heuristics.py: includes various heuristic functions
# that can be used on a csp
# Author: Edmund Aduse Poku
# Class: CS 76, Prof Li, Fall 2020

import csp
from math import inf

# attempts to reduce the branching factor on future choices by selecting the variable
# that is involved in the largest number of constraints on other unassigned variables
def degree_heuristic(csp, ass):
    best_heuristic_var = None
    best_heuristic_val = 0

    # if no assignment has been made yet, then the degree_heuristic
    # value of each variable is just the number of variables it is in arc with
    if len(ass) == 0:
        for var in csp.neighbors.keys():
            heuristic_val = len(csp.neighbors.get(var))
            if heuristic_val > best_heuristic_val:
                best_heuristic_var = var
                best_heuristic_val = heuristic_val

    # if an assignment has been made, then the degree_heuristic value is calculated for
    # each unassigned variable based on the number of unassigned variables it is in arc with
    else:
        for var in csp.neighbors.keys():
            if var not in ass:
                heuristic_val = 0
                for adjacent_var in csp.neighbors.get(var):
                    if adjacent_var not in ass:
                        heuristic_val += 1

                if heuristic_val > best_heuristic_val:
                    best_heuristic_var = var

    return best_heuristic_var


# chooses the variable with the fewest “legal” values
def mrv(csp, ass):
    mrv_val = inf
    mrv_var = None
    for var in csp.domains.keys():
        if var not in ass and len(csp.domains.get(var)) < mrv_val:
            mrv_var = var
            mrv_val = len(csp.domains.get(var))

    return mrv_var


def lcv(csp, var):
    vars_map = {}
    for value in csp.domains.get(var):
        value_heuristic = 0
        for var2 in csp.neighbors.get(var):
            if value in csp.domains.get(var2):
                value_heuristic += 1

        vars_map[value] = value_heuristic

    return [ordered_var for ordered_var in sorted(vars_map, key=vars_map.get)]


