
def evaluate_polynomial(coef: list, x: int) -> int:
    '''
    Given a list of coefficients and a value for x, compute the value of the polynomial:

    Examples:
    >>> evaluate_polynomial([2, 3, 5, 7], 2)
    61.0
    >>> evaluate_polynomial([1, 0, -4], 2)
    -9.0
    >>> evaluate_polynomial([5], 3)
    5.0
    
    Args:
        coef (list): A list of coefficients in descending order
        x (float): The value at which to evaluate the polynomial

    Returns:
        float: The computed value of the polynomial
    '''
    
    return sum(coef * (x ** idx) for idx, coef in enumerate(reversed(coef)))

# #Another Method:

# def evaluate_polynomial(coef: list, x: int) -> int:
   
#     sum=0
#     c=0
#     for i in coef[::-1]:
#         sum=sum+i*x**c
#         c +=1
#     return(sum)

# Compute Polynomial Value
# Write a function evaluate_polynomial(coefficients: list, x: float) -> float that computes the value of a polynomial given its coefficients and a value for x. The coefficients will be provided as a list in descending order, where:

# The first element is the coefficient for the highest degree,
# The last element is the constant term.
# For example, if the polynomial is represented as ( 2x^3 + 3x^2 + 5x + 7 ), the coefficients list would be [2, 3, 5, 7].

# Constraints

# The coefficients list will have at least one element.
# The value of x will be of type int.
# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> evaluate_polynomial([2, 3, 5, 7], 2)
# 45
# >>> evaluate_polynomial([1, 0, -4], 2)
# 0
# >>> evaluate_polynomial([5], 3)
# 5
