import math
def isExistsTriangle(a, b, c):

    return (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0)

def triangleType(a, b, c):

    if not isExistsTriangle(a, b, c):
        return "Not a triangle"

    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
    

def trianglePerimeter(a, b, c):

    if not isExistsTriangle(a, b, c):
        return 0

    return a + b + c

def triangleArea(a, b, c):
    if not isExistsTriangle(a, b, c):
        return 0

    s = trianglePerimeter(a, b, c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c)) 
    return area

def triangleAreaA_Ha(a, ha):
    if a <= 0 or ha <= 0:
        return 0
    return (a * ha) / 2

