def pythagoras(perpendicular, base):
    """this is the classic function of
    pythagoras theorem
    perpendicualr : should be numeric value
    base : should be numeric value
    usage :

    h = pythagoras(2,3)
    """
    from math import sqrt
    hyp = sqrt(perpendicular**2 + base** 2)
    return hyp

h = pythagoras(3,4)
print(f'hypotenuse={h}')

