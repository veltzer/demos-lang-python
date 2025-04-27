""" demo of very small numbers using the decimal module """


from decimal import Decimal, getcontext


def main():
    # First, let's compare regular float vs Decimal
    print("COMPARING FLOAT VS DECIMAL")
    print("-" * 40)

    # Regular float calculation of 0.1 + 0.2
    float_sum = 0.1 + 0.2
    print(f"Using float: 0.1 + 0.2 = {float_sum}")
    print(f"Is float_sum exactly 0.3? {float_sum == 0.3}")

    # Decimal calculation of 0.1 + 0.2
    decimal_sum = Decimal('0.1') + Decimal('0.2')
    print(f"Using Decimal: 0.1 + 0.2 = {decimal_sum}")
    print(f"Is decimal_sum exactly 0.3? {decimal_sum == Decimal('0.3')}")

    print("\nVERY SMALL NUMBERS")
    print("-" * 40)

    # Setting precision for our calculations
    # Default is usually 28 digits, but we need more for very small numbers
    getcontext().prec = 1000  # Set precision to 1000 digits

    # Calculate 0.1^1000 using float
    float_result = 0.1 ** 1000
    print(f"Float 0.1^1000 = {float_result}")

    # Calculate 0.1^1000 using Decimal
    decimal_result = Decimal('0.1') ** 1000

    print(f"Decimal 0.1^1000 = {decimal_result}")
    print(f"Number of digits in result: {len(str(decimal_result)) - 2}")  # -2 for "0." prefix

    # Scientific notation of the result
    print(f"Scientific notation: {decimal_result:.6e}")


if __name__ == "__main__":
    main()
