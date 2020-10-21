from map_coloring_problem import MapColoringCSP
from CSPSolution import CSPSolution
from search import *
from time import time

#####
# MapColoringCSP test on territories
territory_map = {"WA" : {"SA", "NT"},
                 "NT" : {"SA", "Q", "WA"},
                 "Q" : {"SA", "NSW", "NT"},
                 "NSW" : {"Q", "V", "SA"},
                 "SA" : {"Q", "NT", "V", "WA", "NSW"},
                 "V" : {"NSW", "SA" },
                 "T" : ""}

territory_color_domain = {'r', 'g', 'b'}
t_csp = MapColoringCSP(territory_map, territory_color_domain)

# print variable mapping
print("\nVariable mapping: territory -> variables:\n", t_csp.variable_mapping)

# print domain mapping
print("\nDomain mapping: color -> domain:\n", t_csp.domain_mapping)

# print constraints
print("\nConstraints:\n", t_csp.constraints, "\n")

######
# run backtracking search on the csp without heuristics and inferences
t_0 = time()
t_result0 = backtracking_search(t_csp, inf=False, lcv=False, mrv=False, degree_heuristic=False)
t_1 = time()

# display solution
t_solution0 = CSPSolution(t_csp, "MapColoringCSP", "backtracking", t_result0, t_1-t_0, inf=False, lcv=False, mrv=False, degree_heuristic=False)
print(t_solution0)

######
# run backtracking search on the csp with just mrv and no inferences
t_2 = time()
t_result1 = backtracking_search(t_csp, inf=False, lcv=False, mrv=True, degree_heuristic=False)
t_3 = time()

# display solution
t_solution1 = CSPSolution(t_csp, "MapColoringCSP", "backtracking", t_result1, t_3-t_2, inf=False, lcv=False, mrv=True, degree_heuristic=False)
print(t_solution1)

######
# run backtracking search on the csp with just mrv, lcv and no inferences
t_4 = time()
t_result2 = backtracking_search(t_csp, inf=False, lcv=True, mrv=True, degree_heuristic=False)
t_5 = time()

# display solution
t_solution2 = CSPSolution(t_csp, "MapColoringCSP", "backtracking", t_result2, t_5-t_4, inf=False, lcv=True, mrv=True, degree_heuristic=False)
print(t_solution2)

######
# run backtracking search on the csp with just mrv, lcv, degree_heuristics and no inferences
t_6 = time()
t_result3 = backtracking_search(t_csp, inf=False, lcv=True, mrv=True, degree_heuristic=True)
t_7 = time()

# display solution
t_solution3 = CSPSolution(t_csp, "MapColoringCSP", "backtracking", t_result3, t_7-t_6, inf=False, lcv=True, mrv=True, degree_heuristic=True)
print(t_solution3)

######
# run backtracking search on the csp with just mrv, lcv, degree_heuristics and forward checking inferences
t_8 = time()
t_result4 = backtracking_search(t_csp, inf=True, lcv=True, mrv=True, degree_heuristic=True)
t_9 = time()

# display solution
t_solution4 = CSPSolution(t_csp, "MapColoringCSP", "backtracking", t_result4, t_9-t_8, inf=True, lcv=True, mrv=True, degree_heuristic=True)
print(t_solution4)

#####
# Test case not used
# MapColoringCSP test on courses
course_map = {"COSC" : {"MATH"},
                 "ENGS" : {"MATH", "PHYS", "CHEM"},
                 "PHY" : {"MATH"},
                 "CHEM" : {},
                 "BIOL" : {"MATH"},
                 "PSYC" : {"BIOL" },
                 "HUMA" : {}}








