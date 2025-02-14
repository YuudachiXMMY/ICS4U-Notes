def multiply(a, b):
    # Base case: if b is 1, the result is a
    if b == 1:
        return a
    # Recursive case: add a to the result of multiplying a and (b-1)
    else:
        return a + multiply(a, b - 1)
