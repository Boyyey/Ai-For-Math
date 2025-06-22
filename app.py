import streamlit as st
from solver import solve_equation
from explain import explain_solution
from plotter import plot_equation
import re

st.title("AI Math Solver")

st.write("Enter your math problem below:")
equation_input = st.text_area("Math Problem or Question (e.g., x**2 - 5*x + 6 = 0 or 'Solve x squared minus 5x plus 6 equals 0')")

def extract_equation(text):
    # Try to extract a math expression from the input
    # Look for patterns like y = ... or ... = ...
    match = re.search(r'([\w\s\^\*\+\-/=\.]+=[\w\s\^\*\+\-/=\.]+)', text)
    if match:
        return match.group(1)
    # If not found, try to extract numbers and math words
    # (very basic fallback, can be improved)
    math_words = re.sub(r'[^\dxX\+\-\*/=\^\s]', '', text)
    if any(char.isdigit() for char in math_words):
        return math_words.strip()
    return None

if st.button("Solve") and equation_input.strip():
    eq = extract_equation(equation_input)
    if not eq:
        st.write("Could not extract a valid equation. Please enter a clear math expression or equation.")
    else:
        try:
            solution = solve_equation(eq)
            st.write("Solution:", solution)
            explanation = explain_solution(eq)
            st.write("Explanation:", explanation)
            # Optional: plot if equation is suitable
        except Exception as e:
            st.write("Could not solve:", e)
