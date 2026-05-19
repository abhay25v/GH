def kaprekar_step(number: int, digits: int) -> int:
    number_str = str(number).zfill(digits)

    ascending = ''.join(sorted(number_str))
    descending = ''.join(sorted(number_str, reverse=True))

    return int(descending) - int(ascending)


def find_kaprekar_result(number: int):
    digits = len(str(number))

    if digits < 1 or digits > 10:
        raise ValueError("Number length must be between 1 and 10 digits.")

    if len(set(str(number).zfill(digits))) == 1:
        raise ValueError("All digits cannot be identical.")

    visited = set()

    current = number
    iteration = 0

    while True:

        next_number = kaprekar_step(current, digits)

        iteration += 1

        # Fixed point detected
        if next_number == current:
            return {
                "type": "constant",
                "value": current,
                "iterations": iteration
            }

        # Cycle detected
        if next_number in visited:
            return {
                "type": "cycle",
                "value": next_number,
                "iterations": iteration
            }

        visited.add(next_number)

        current = next_number


def main():

    try:
        number = int(input("Enter a number (1 to 10 digits): "))

        result = find_kaprekar_result(number)

        if result["type"] == "constant":
            print(
                f"Kaprekar Constant: {result['value']} "
                f"(found in {result['iterations']} iterations)"
            )

        else:
            print(
                f"Repeating cycle detected at {result['value']} "
                f"after {result['iterations']} iterations"
            )

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()