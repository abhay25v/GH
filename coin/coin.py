MOD = 1_000_000

def find_smallest_partition_divisible(divisor: int) -> int:
    if divisor <= 0:
        raise ValueError("Divisor must be positive.")

    partitions = [1]  # p(0) = 1

    number = 1

    while True:

        value = 0
        k = 1

        while True:

            generalized_pentagonal_1 = k * (3 * k - 1) // 2
            generalized_pentagonal_2 = k * (3 * k + 1) // 2

            if generalized_pentagonal_1 > number:
                break

            sign = 1 if k % 2 == 1 else -1

            value += sign * partitions[number - generalized_pentagonal_1]

            if generalized_pentagonal_2 <= number:
                value += sign * partitions[number - generalized_pentagonal_2]

            k += 1

        value %= divisor

        partitions.append(value)

        if value == 0:
            return number

        number += 1


def main():

    try:
        result = find_smallest_partition_divisible(MOD)

        print(
            "Smallest number with partition divisible "
            f"by {MOD}: {result}"
        )

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()