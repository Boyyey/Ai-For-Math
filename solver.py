from sympy import symbols, Eq, solve, sympify
import re

def solve_equation(equation_str):
    x = symbols('x')
    # If the input contains '=', split into left and right and create Eq
    if '=' in equation_str:
        left, right = equation_str.split('=', 1)
        eq = Eq(sympify(left.strip()), sympify(right.strip()))
    else:
        eq = sympify(equation_str)
    solution = solve(eq, x)
    return solution
