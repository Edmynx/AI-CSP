# @Author: Edmund Aduse Poku

class CSPSolution:
    def __init__(self, csp, csp_name, search_method, solution, time, circ=True, inf=True, lcv=True, mrv=True, degree_heuristic=True):
        self.csp = csp
        self.csp_name = str(csp_name)
        self.search_method = search_method
        self.solution = solution
        self.runtime = time
        self.circ = circ
        self.inf = inf
        self.lcv = lcv
        self.mrv = mrv
        self.degree_heuristic = degree_heuristic
        self.no_heuristic = True

    def __str__(self):
        string = "\n-------------------------------\n"
        string += "{:s}\n"
        string += "solved by {:s} in runtime: {:f} seconds\n"
        string += "using the following: {:s} heuristics and {:s} inference\n"

        heuristic = ""
        if self.degree_heuristic:
            heuristic += "degree_heuristics"
            self.no_heuristic = False

        if self.mrv:
            if len(heuristic) > 0:
                heuristic += ", 'MRV'"

            else:
                heuristic += "'MRV'"

            self.no_heuristic = False

        if self.lcv:
            if len(heuristic) > 0:
                heuristic += ", 'LCV'"

            else:
                heuristic += "'LCV'"
            self.no_heuristic = False

        if self.no_heuristic:
            heuristic += "no"
            self.no_heuristic = False

        inference = ""
        if self.inf:
            inference += "'forward checking'"

        else:
            inference += "no"



        string = string.format(self.csp_name, self.search_method, self.runtime, heuristic, inference)

        if self.solution != "failure":
            if self.csp_name == "CircuitBoardCSP":
                string += "the components should be laid out as:\n\n"
                string += self.csp.convert_to_readable(self.solution)[1] + "\n\n"
                string += "using the coordinates: \n"
                string += str(self.csp.convert_to_readable(self.solution)[0]) + "\n"

            elif self.csp_name == "MapColoringCSP":
                string += "the solution suggests that the colors be assigned in the manner:\n"
                string += str(self.csp.convert_to_readable(self.solution)) + "\n"

        else:
            string += "the csp has no solution\n"

        return string