# polySolve
*By Trond Hauklien*

The main use of this script is to easily calculate the roots of third degree equations or functions. I made this because I wanted to revert an polynomial model applied to a dataset. I knew the coefficients, and had an calculated value for every input, but I needed the raw data. I had no chance of calculating the data manually, because the list was a csv file consisting of over 40,000 datapoints.

## How to use
There is two ways to use this script. The first class, `polySolve()`, uses `np.roots()` to solve a single third degree equation. The other class, `polySolveList()`, takes input from a csv file and processes it with the `np.roots()` function.

### polySolve
The required input format is `polySolve(a, b, c, d)` where the arguments are equal to the coefficients of your equation. Just like this: `ax^3+bx^2+cx+d=0`. The solution will be printed as an array.

### polySolveList
This script need an input csv file to process. It takes each row as an equation, and uses the same format as in `polySolve()`. The script will process up to four coefficients per equation (i.e. will be able to handle 3rd degree equations) and provide you with the solutions to your list of equations. The solutions are printed as arrays.

If there is any problems regarding your inputs, the code will prompt you with an error message telling you what line the error lies within.

**NEW!** You are now able to output the solutions of your equations (from the input file) to an separate output file. The syntax of the function is `polySolveList(file, w=True, path="solutions.csv")`, where `file` is the path to your input file, `w` is wether or not you'd like to output the solutions to a separate csv file (default `False`) and `path` is the path to your output file (default `solutions.csv`). The output list will consist of one array of solutions per row, with the following format: `[x1 x2 x3]`, where the objects are float elements.

## To do
A list of what has been done, and where to go next.
- [x] Make the script solve up to third degree equations
- [x] Make it possible to output the results to a csv
- [ ] Expand to solve equations of a higher degree
