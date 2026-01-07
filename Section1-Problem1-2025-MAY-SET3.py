
def is_decreasing_number(n: int) -> bool:
    '''
    Given a 4-digit number, check if its digits are strictly decreasing 
    from left to right.

    Examples:
    >>> is_decreasing_number(4321)
    True
    >>> is_decreasing_number(4312)
    False
    >>> is_decreasing_number(9876)
    True
    >>> is_decreasing_number(1111)
    False
    >>> is_decreasing_number(3210)
    True

    Args:
        n (int): A 4-digit integer

    Returns:
        bool: True if the number is decreasing, False otherwise
    '''
    
    
    digits = str(n)
    return digits[0] > digits[1] > digits[2] > digits[3]


# #Another Method:

# def is_decreasing_number(n: int) -> bool:
     
#     l=list(str(n))
#     pre=l[0]
    
#     for i in range(1,len(l)):
#         if int(pre)-int(l[i]) <=0:
#             return False
#         else:
#             pre=l[i]
#     return True


# Check If a Number is a Decreasing 4-Digit Number
# Write a function is_decreasing_number(n: int) -> bool that checks if a given 4-digit number is decreasing, meaning each digit is strictly less than the digit before it (from left to right).

# The function should return True if the number meets the criteria and False otherwise.

# Constraints

# The input number will be a 4-digit number, which means it will be in the range of 1000 to 9999.
# Example

# >>> is_decreasing_number(4321)
# True
# >>> is_decreasing_number(4312)
# False
# >>> is_decreasing_number(9876)
# True
# >>> is_decreasing_number(1111)
# False
# >>> is_decreasing_number(3210)
# True
            
