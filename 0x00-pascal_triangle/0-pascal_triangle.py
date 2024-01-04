def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []

    triangle = []

    for _ in range(n):
        new_row = []
        for k in range(_ + 1):
            co = factorial(_) // (factorial(k) * factorial(_ - k))
            new_row.append(co)

        triangle.append(new_row)

    return triangle

def factorial(num):
    """Calculate the factorial of a number."""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
