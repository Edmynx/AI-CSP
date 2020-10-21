# circuit_board_layout.py: class for a Circuit Board Problem
# problem is translated into a csp
# Has specific class for map coloring
# Author: Edmund Aduse Poku
# Class: CS 76, Prof Li, Fall 2020

from csp import CSP

class CircuitBoardCSP(CSP):
    def __init__(self, n, m, components):
        self.row = m
        self.column = n
        self.variable_mapping = {}
        self.variable_dimension = {}
        self.convert_to_csp(n, m, components)

    def convert_to_csp(self, n, m, components):
        CSP.domains = {}
        CSP.neighbors = {}

        val_count = 0
        for component in components.keys():
            self.variable_mapping[component] = val_count
            self.variable_dimension[val_count] = components.get(component)

            CSP.domains[val_count] = set()
            for domain_value in range(n * m):
                breadth, height = components.get(component)
                val_col, val_row = self.compute_val_position_coordinates(domain_value)

                # offset of -1 on each side of the inequality cancels out
                # so we don't write it
                if (val_col + breadth <= self.column) and (val_row + height <= self.row):
                    CSP.domains.get(val_count).add(domain_value)

            val_count += 1

        CSP.variables = set(range(val_count))

        for variable in CSP.variables:
            CSP.neighbors[variable] = set(CSP.variables)
            CSP.neighbors.get(variable).remove(variable)

    def convert_to_readable(self, ass):
        solution_map = {}
        solution_string = ""

        # represent the empty circuit
        for i in range(self.row):
            if i > 0:
                solution_string += "\n"
            for j in range(self.column):
                solution_string += "."

        for var in ass:
            var_component = None
            for component in self.variable_mapping:
                if self.variable_mapping.get(component) == var:
                    var_component = component
                    break
            val_col, val_row = self.compute_val_position_coordinates(ass.get(var))
            solution_map[var_component] = (val_col, val_row)

            # put component on the circuit
            var_breadth, var_height = self.variable_dimension.get(var)

            component_row_string = ""
            for i in range(var_breadth):
                component_row_string += var_component

            string_end_col = val_col + var_breadth - 1
            # offsets cancel (-1 to reduce row count and +1 to reduce extra height)
            string_row_begin = self.row - (val_row + var_height)
            for i in range(string_row_begin, string_row_begin + var_height):
                # count for new lines included as string_row_begin
                # ie. number lines before string start
                string_begin_index = self.compute_val_position_index(string_row_begin, val_col) + i
                string_end_index = self.compute_val_position_index(string_row_begin, string_end_col) + i

                solution_string = solution_string[:string_begin_index] +\
                                  component_row_string +\
                                  solution_string[string_end_index+1:]
                string_row_begin += 1


        return solution_map, solution_string

    def compute_val_position_coordinates(self, val):
        val_row = val // self.column  # which row can you find the lower left corner of var
        val_col = val % self.column  # which column can you find the lower left corner of var

        return val_col, val_row

    def compute_val_position_index(self, val_row, val_col):
        return val_row * self.column + val_col

    def arc_is_consistent(self, var1, val1, var2, val2):
        col1, row1 = self.variable_dimension[var1] # provided breadth and height of var 1
        col2, row2 = self.variable_dimension[var2] # provided breadth and height of var 2

        val1_col, val1_row = self.compute_val_position_coordinates(val1)
        val2_col, val2_row = self.compute_val_position_coordinates(val2)
        # if the 2 components are on the same row,
        # they are consistent with each other if
        # their breadths don't run into within each other
        if val1_row == val2_row:
            return (val1_col + col1) < val2_col or (val2_col + col2) < val1_col

        # if the 2 components are on the same column,
        # they are consistent with each other if
        # their heights don't run into within each other
        if val1_col == val2_col:
            return (val1_row + row1) < val2_row or (val2_row + row2) < val1_row

        # if the 2 components are on different rows and columns,
        # they are consistent with each other if both their
        # breadths and heights don't run into within each other

        min_height = row1
        min_breadth = col1
        val_row_min = val1_row
        max_height = row2
        val_row_max = val2_row
        val_col_max = val2_col

        val_col_min = min(val1_col, val2_col)
        if val_col_min == val2_col:
            min_height = row2
            min_breadth = col2
            val_row_min = val2_row
            max_height = row1
            val_row_max = val1_row
            val_col_max = val1_col

        return (val_col_min + min_breadth) < val_col_max or\
               ((val_row_min + min_height) < val_row_max or (val_row_max + max_height) < val_row_min)
