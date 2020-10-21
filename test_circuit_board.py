from circuit_board_problem import CircuitBoardCSP
from CSPSolution import CSPSolution
from search import *
from time import time

#####
# CircuitBoardCSP test on a 7 by 8 circuit
n = 7
m = 8

# circuit components and dimensions (breadth by height)
components = {'a' : (2, 5), 'b' : (6, 1), 'e' : (4, 2), 'g' : (2, 2)}
c_csp = CircuitBoardCSP(n, m, components)

# print variable mapping
print("\nVariable mapping: component -> variables\n", c_csp.variable_mapping)

# print domains
print("\nCSP Domains:\n", c_csp.domains)

######
# run backtracking search on the csp without heuristics and inferences
t_0 = time()
c_result0 = backtracking_search(c_csp, inf=False, lcv=False, mrv=False, degree_heuristic=False)
t_1 = time()

# display solution
c_solution0 = CSPSolution(c_csp, "CircuitBoardCSP", "backtracking", c_result0, t_1-t_0, inf=False, lcv=False, mrv=False, degree_heuristic=False)
print(c_solution0)

######
# run backtracking search on the csp with just mrv and no inferences
t_2 = time()
c_result1 = backtracking_search(c_csp, inf=False, lcv=False, mrv=True, degree_heuristic=False)
t_3 = time()

# display solution
c_solution1 = CSPSolution(c_csp, "CircuitBoardCSP", "backtracking", c_result1, t_3-t_2, inf=False, lcv=False, mrv=True, degree_heuristic=False)
print(c_solution1)

######
# run backtracking search on the csp with just mrv, lcv and no inferences
t_4 = time()
c_result2 = backtracking_search(c_csp, inf=False, lcv=True, mrv=True, degree_heuristic=False)
t_5 = time()

# display solution
c_solution2 = CSPSolution(c_csp, "CircuitBoardCSP", "backtracking", c_result2, t_5-t_4, inf=False, lcv=True, mrv=True, degree_heuristic=False)
print(c_solution2)

######
# run backtracking search on the csp with just mrv, lcv, degree_heuristics and no inferences
t_6 = time()
c_result3 = backtracking_search(c_csp, inf=False, lcv=True, mrv=True, degree_heuristic=True)
t_7 = time()

# display solution
c_solution3 = CSPSolution(c_csp, "CircuitBoardCSP", "backtracking", c_result3, t_7-t_6, inf=False, lcv=True, mrv=True, degree_heuristic=True)
print(c_solution3)

######
# run backtracking search on the csp with just mrv, lcv, degree_heuristics and forward checking inferences
t_8 = time()
c_result4 = backtracking_search(c_csp, inf=True, lcv=True, mrv=True, degree_heuristic=True)
t_9 = time()

# display solution
c_solution4 = CSPSolution(c_csp, "CircuitBoardCSP", "backtracking", c_result4, t_9-t_8, inf=True, lcv=True, mrv=True, degree_heuristic=True)
print(c_solution4)
