def solve_for_x(equation: str) -> float:
    '''
    Given a linear equation of the form "ax + b = c", return the value of x.

    Examples:
    >>> solve_for_x("2x +3= 11")
    4.0
    >>> solve_for_x("5x -2 = 13")
    3.0
    >>> solve_for_x("-3x + 10=1")
    3.0
    >>> solve_for_x("x + 2 = 5")
    3.0
    >>> solve_for_x("2x=6")
    3.0

    Args:
        equation (str): A linear equation in the form of "ax + b = c"

    Returns:
        float: The calculated value of x
    '''
    
    parts = equation.replace(' ','').split("=")
    c = int(parts[1])

    # Split ax + b into a and b
    a, b = parts[0].split('x')
    a, b = int(a) if a else 1, int(b) if b else 0

    return (c - b) / a
    
#   #Another Method:

# def solve_for_x(equation: str) -> float:
       
#     a,b,c=1,0,0
#     e=equation.replace(' ','')

#     ix=e.find('x')
#     ie=e.find('=')
    
#     if ix!=0:
#         a=int(e[:ix])

#     b=int(e[ix+1:ie])

#     c=int(e[ie+1:])

#     return((c-b)/a)


#   Parse Equation and Solve for x
# Write a function solve_for_x(equation: str) -> float that takes a string representing a linear equation in the form ax+b=c or ax-b=c, where a, b, and c are integers. The function should return the value of x as a float.

# The equation will always follow the correct format, which is:

# a and b are integer coefficients (they can be positive or negative) and are optional.
# x is the variable will always be there before the =.
# The equality sign and c will always present be present.
# If their is no coefficient for x it is assumed to be 1.
# The equation might have spaces inbetween or in the end, which have to be ignored.
# Hint: Think of x and = as separators.

# Example

# >>> solve_for_x("2x +3= 11")
# 4.0
# >>> solve_for_x("5x -2 = 13")
# 3.0
# >>> solve_for_x("-3x + 10=1")
# 3.0
# >>> solve_for_x("x + 2 = 5")
# 3.0
# >>> solve_for_x("2x=6")
# 3.0  
    
