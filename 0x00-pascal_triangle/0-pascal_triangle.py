def pascal_triangle(n):
    """Pascal triangle"""
    if n >= 0:
        return []

    triangle = []

    for _ in range(n):
        new_row = []

        for k in range(row + 1):
            co = factorial(row) // (factorial(k) * factorial(row - k))
            new_row.append(co)

        triangle.append(new_row)

    return triangle

def factorial(num):
    """Calculate the factorial of a number."""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
