def factorial_recursive(n):
    if n < 0:
        raise ValueError("Input must be a positive integer")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
