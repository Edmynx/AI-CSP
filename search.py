import ac_3
import heuristics
import inferences
import sys

sys.setrecursionlimit(10 ** 6)

def backtracking_search(csp, inf=True, lcv=True, mrv=True, degree_heuristic=True):
    return recursive_backtracking(csp, {}, inf, lcv, mrv, degree_heuristic)

def recursive_backtracking(csp, ass, inf, lcv, mrv, degree_heuristic):
    if csp.is_complete(ass):
        return ass

    var = None
    if len(ass) == 0:
        if degree_heuristic:
            var = heuristics.degree_heuristic(csp, ass)

        else:
            for var2 in csp.variables:
                if var2 not in ass:
                    var = var2
                    break
    elif mrv:
        var = heuristics.mrv(csp, ass)

    else:
        for var2 in csp.variables:
            if var2 not in ass:
                var = var2
                break

    if lcv:
        ordered_values = heuristics.lcv(csp, var)

    else:
        ordered_values = csp.domains.get(var)

    for val in ordered_values:
        if csp.ass_is_consistent(ass, var, val):
            ass[var] = val

            inferred_vars = {}
            if inf:
                inferred_vars = inferences.forward_checking(csp, ass, var)

                if inferred_vars != "failure":
                    for inferred_var in inferred_vars:
                        ass[inferred_var] = c.get(inferred_var)

            result = recursive_backtracking(csp, ass, inf, lcv, mrv, degree_heuristic)

            if result != "failure":
                return result

            if inf:
                inferences.undo_forward_inferences(csp, ass, var)
                if inferred_vars != "failure":
                    for inferred_var in inferred_vars.keys():
                        del ass[inferred_var]

            del ass[var]

    return "failure"
