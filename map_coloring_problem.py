# map_coloring_problem.py: class for a Map Coloring Problem
# problem is translated into a csp
# Has specific class for map coloring
# Author: Edmund Aduse Poku
# Class: CS 76, Prof Li, Fall 2020

import csp

class MapColoringCSP(csp.CSP):
    def __init__(self, territory_map, color_domain):
        self.domain_mapping = {}
        self.variable_mapping = {}
        self.convert_to_csp(territory_map, color_domain)

    def convert_to_csp(self, territory_map, color_domain):
        val_count = 0
        for color in color_domain:
            self.domain_mapping[color] = val_count
            val_count += 1

        var_count = 0
        csp.CSP.domains = {}
        csp.CSP.variables = set()
        for variable in territory_map.keys():
            self.variable_mapping[variable] = var_count
            csp.CSP.variables.add(var_count)
            csp.CSP.domains[var_count] =  set(range(val_count))
            var_count += 1

        csp.CSP.constraints = {}
        csp.CSP.neighbors = {}
        for variable in territory_map.keys():
            csp.CSP.neighbors[self.variable_mapping[variable]] = set()
            for adjacent_var in territory_map.get(variable):
                # put variables in the neighbors dictionary
                csp.CSP.neighbors.get(self.variable_mapping[variable]).add(self.variable_mapping[adjacent_var])

                # form an ordered tuple of the variables
                min_var = min(self.variable_mapping[variable], self.variable_mapping[adjacent_var])
                max_var = max(self.variable_mapping[variable], self.variable_mapping[adjacent_var])
                if (min_var, max_var) not in csp.CSP.constraints:
                    csp.CSP.constraints[(min_var, max_var)] = set()
                    for val in csp.CSP.domains.get(min_var):
                        csp.CSP.constraints.get((min_var, max_var)).add((val, val))

    def convert_to_readable(self, ass):
        solution_map = {}
        for var in ass:
            var_territory = None
            for territory in self.variable_mapping:
                if self.variable_mapping.get(territory) == var:
                    var_territory = territory
                    break

            for color in self.domain_mapping:
                if self.domain_mapping.get(color) == ass.get(var):
                    solution_map[var_territory] = color
                    break

        return solution_map

