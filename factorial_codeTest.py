from factorial_code import factorial_recursive

if __name__ == "__main__":
    number = input("Enter a number: ")
    print(f"The factorial of {number} is {factorial_recursive(number)}")