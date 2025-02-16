def factorial_recursive(n):
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Input must be a positive integer")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
