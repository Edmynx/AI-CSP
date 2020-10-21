# csp.py: generic class for a Constraint Search Problem
# Author: Edmund Aduse Poku
# Class: CS 76, Prof Li, Fall 2020


class CSP:
    def __init__(self, variables=None, domains=None, constraints=None):
     self.variables = variables
     self.domains = domains
     self.constraints = constraints
     self.neighbors = None

    def is_complete(self, ass):
        return len(ass) == len(self.variables)

    def arc_is_consistent(self, var1, val1, var2, val2):
        # initialize variables and guess which is bigger
        max_var = var2
        max_val = val2
        min_var = var1
        min_val = val1

        if min(var1, var2) == var2:
            max_var = var1
            max_val = val1
            min_var = var2
            min_val = val2

        if (min_var, max_var) in self.constraints.keys():
            return (min_val, max_val) not in self.constraints.get((min_var, max_var))

        return 1

    def ass_is_consistent(self, ass, var, val):
        if len(ass) == 0:
            return 1
        for ass_var in ass.keys():
            is_consistent = self.arc_is_consistent(ass_var, ass.get(ass_var), var, val)
            if not is_consistent:
                return 0
        return 1
