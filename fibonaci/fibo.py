def sum_even_fibonacci(limit: int) -> int:

    if limit < 0:
        raise ValueError("Limit must be non-negative.")

    first = 1
    second = 2

    total_sum = 0

    while second <= limit:

        if second % 2 == 0:
            total_sum += second

        next_term = first + second

        first = second
        second = next_term

    return total_sum


def main():

    try:
        limit = int(input("Enter the upper limit: "))

        result = sum_even_fibonacci(limit)

        print(f"Sum of even Fibonacci numbers: {result}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()