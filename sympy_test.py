from sympy import Symbol, solve
x = Symbol('x')
expr = (x + 2) ** 3
sol = solve(expr, x)
print(sol)