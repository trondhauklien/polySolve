#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import csv

def solve(a):
    try:
        arr = np.array(a, dtype=object) # use NumPy array
        arr = arr[:4] # slice any unnecessary objects
        arr = list(map(float, arr)) # convert from string to float object, if fail exception(3) will create error message
        coeff = arr
        solution = np.roots(coeff) # use eigenvalues to calculate the solution
        #print(solution) # for debugging
        real_valued = solution.real[abs(solution.imag)<1e-5] # calculate real values with treshold
        return solution, real_valued
    except: # exception(3)
        print("Error: Input was not a float object")

# polySolve will solve any 3rd degree function
# format: ax^3+bx^2+cx+d=0
def polySolve(a, b, c, d):
    coeff = [a, b, c, d] # define list with coefficients
    sol, real = solve(coeff) # solves the equation using the solve() function
    print(real) # print the real value solution as an array

# polySolve will solve any 3rd degree function
# format: ax^3+bx^2+cx+d=0
# list should be csv and delimited by ","
# example row: "a, b, c, d"
def polySolveList(file, w=False, path="solutions.csv"):
    try:
        with open(file) as csvFile: # will throw exception(1) if it fails to open or read the csv
            csvReader = csv.reader(csvFile, delimiter=",")
            lineCount = 0 # set line count for debugging and result
            if w: # check if "write to file" argument is True
                f = open(path, "a+") # open output file
            try:
                for row in csvReader:
                    sol, real = solve(row) # use the solve() function on every row of the input file
                    # will throw exception(3) if there is a problem
                    if w: # check if "write to file" argument is True
                        f.write("{}\r\n".format(real)) # write the real values of the solutions provided by the solve() function
                    else:
                        print(real) # prints the solutions if they're not appended to an output file
                    lineCount += 1
                f.close() # close the output file
                if w:
                    print("Values appended to file")
                print("{} lines were processed".format(lineCount))
            except: # exception(3)
                print("Error: An error occurred")
    except: # exception(1)
        print("Error: Could not read or open the input file")

# for testing purposes
polySolveList("input.csv", True)
# polySolve(1,1,1,1)
