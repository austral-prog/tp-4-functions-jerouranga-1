# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):

    determinante = float((b**2)-4*a*c)

    if determinante > 0:
     r1 = float((-b+(determinante)**0.5)/2*a)
     r2 = float((-b-(determinante)**0.5)/2*a)
     return f"({r1}, {r2})"
    elif determinante == 0:
     r12 = float((-b)/(2*a))
     return f"({r12})"
    else:
        return "( )"

def value_y(a, b, c, x):
    y = a*(x**2) + b*x + c
    return y


def to_string(a, b, c):
    A = a
    B = b
    C = c

    if A == 0 and B == 0 and C == 0:
        return "f(x) = 0"
    elif A == 0 and B == 0 and C != 0:
        return f"f(x) = {C}"
    elif A == 0 and B != 0 and C == 0:
        return f"f(x) = {B} * X"
    elif A == 0 and B != 0 and C != 0:
        return f"f(x) = {B} * X + {C}"
    elif A != 0 and B == 0 and C == 0:
        return f"f(x) = {A} * X^2"
    elif A != 0 and B != 0 and C == 0:
        return f"f(x) = {A} * X^2 + {B} * X"
    elif A != 0 and B != 0 and C != 0:
        return f"f(x) = {A} * X^2 + {B} * X + {C}"
    elif A != 0 and B == 0 and C != 0:
        return f"f(x) = {A} * X^2 + {C}"


def derivation(a, b, c):
    nuevo_a = a * 2
    nuevo_b = b
    if nuevo_a != 0 and nuevo_b != 0:
        return f"f'(x) = {nuevo_a} * X + {nuevo_b}"
    elif nuevo_a == 0 and nuevo_b == 0:
        return f"f'(x) = 0"
    elif nuevo_a != 0 and nuevo_b == 0:
        return f"f'(x) = {nuevo_a} * X"
    elif nuevo_a == 0 and nuevo_b != 0:
        return f"f'(x) = {nuevo_b}"


