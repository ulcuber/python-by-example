"""
Must print and return sum of two numbers
Ask user to input number one by one
"""


def main() -> int:
    """
    Prints result of num1 + num2 taken from input
    """
    num1 = int(input("Please enter first number:"))
    num2 = int(input("Please enter second number:"))
    result = num1 + num2
    print(result)
    return result


if __name__ == "__main__":
    main()
