#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import csv

# polySolve will solve any 3rd degree function
# format: ax^3+bx^2+cx+d=0
def polySolve(a, b, c, d):
    coeff = [a, b, c, d] # define list with coefficients
    solution = np.roots(coeff) # use eigenvalues to calculate the solution
    real_valued = solution.real[abs(solution.imag)<1e-5] # calculate real values with treshold
    print(real_valued) # print the solution as an array

# polySolve will solve any 3rd degree function
# format: ax^3+bx^2+cx+d=0
# list should be csv and delimited by ","
# example row: "a, b, c, d"
def polySolveList(file, w=0, path="solutions.csv"):
    try:
        with open(file) as csvFile: # will throw exception(1) if it fails to open or read the csv
            csvReader = csv.reader(csvFile, delimiter=",")
            lineCount = 0 # set line count for debugging and result
            try:
                for row in csvReader:
                    a = np.array(row, dtype=object) # use NumPy array
                    a = a[:4] # slice any unnecessary objects
                    a = list(map(float, a)) # convert from string to float object, if fail exception(2) will create error message
                    coeff = a
                    solution = np.roots(coeff) # use eigenvalues to calculate the solution
                    #print(solution)
                    real_valued = solution.real[abs(solution.imag)<1e-5] # calculate real values with treshold
                    print(real_valued)
                    lineCount += 1
                print("{} lines were processed".format(lineCount))
            except: # exception(2)
                print("Error on line {}: Input was not a float object".format(lineCount))
    except: # exception(1)
        print("Error: Could not read or open the file")

# for testing purposes
# polySolveList("input.csv")
# polySolve(1,1,1,1)
