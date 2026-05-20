def build_divisor_sums(limit: int) -> list[int]:
    divisor_sums = [0] * limit

    for divisor in range(1, limit):

        for multiple in range(2 * divisor, limit, divisor):
            divisor_sums[multiple] += divisor

    return divisor_sums


def is_amicable(number: int, divisor_sums: list[int], limit: int) -> bool:
    partner = divisor_sums[number]

    if partner == number:
        return False

    if partner < limit and divisor_sums[partner] == number:
        return True

    return False


def sum_amicable_numbers(limit: int) -> int:
    if limit < 1:
        raise ValueError("Limit must be positive.")

    divisor_sums = build_divisor_sums(limit)

    total_sum = 0

    for number in range(2, limit):

        if is_amicable(number, divisor_sums, limit):
            total_sum += number

    return total_sum


def main():

    try:
        limit = int(input("Enter the upper limit: "))

        result = sum_amicable_numbers(limit)

        print(f"Sum of amicable numbers: {result}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()