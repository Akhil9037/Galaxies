from numpy import*
# Function to integrate
def f(theta):
    return sqrt(cos(theta))

# Interval
a, b = 0, pi/2
n = 60   # number of subintervals (must be even for Simpson's rule)
h = (b - a) / n

# Nodes
x = linspace(a, b, n+1)
y = f(x)

# Trapezoidal rule
trap = (h/2) * (y[0] + 2*sum(y[1:-1]) + y[-1])

# Simpson's 1/3 rule
simpson = (h/3) * (y[0] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-2:2]) + y[-1])

# Exact value using Beta/Gamma functions
'''import mpmath as mp
exact = 0.5 * mp.beta(0.5, 0.75)'''

print("Trapezoidal rule (n=60):", trap)
print("Simpson's 1/3 rule (n=60):", simpson)
'''print("Exact value:", exact)
print("Trapezoidal error:", abs(trap - exact))
print("Simpson error:", abs(simpson - exact))'''

