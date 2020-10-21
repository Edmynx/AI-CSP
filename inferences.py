from ac_3 import ac_3
def forward_checking(csp, ass, var):
    inferences = {}
    for var2 in csp.neighbors.get(var):
        if var2 not in ass:
            var2_domain = csp.domains.get(var2).copy()
            for val in var2_domain:
                if val == ass.get(var):
                    csp.domains.get(var2).remove(val)
                    if len(csp.domains.get(var2)) == 0:
                        return "failure"
                    if len(csp.domains.get(var2)) == 1:
                        for inferred_val in csp.domains.get(var2):
                            inferences[var2] = inferred_val

    return inferences

def undo_forward_inferences(csp, ass, var):
    for var2 in csp.neighbors.get(var):
        csp.domains.get(var2).add(ass.get(var))

def mac(csp, ass, var):
    inferences = {}

    ac_3_set = set()
    for var2 in csp.variables:
        if var2 not in ass:
            ac_3_set.add(var2)

    ac_3_result = ac_3(csp, ac_3_set)

    if ac_3_result:
        for var2 in ac_3_set:
        if len(csp.domains.get(var2)) == 1:
            for inferred_val in csp.domains.get(var2):
                inferences[var2] = inferred_val

    return inferences

def undo_forward_inferences(csp, ass, var):
    for var2 in csp.neighbors.get(var):
        csp.domains.get(var2).add(ass.get(var))





