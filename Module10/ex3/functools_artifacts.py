from functools import reduce


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        raise ValueError("Invalid list")

    if not all(isinstance(spell, int) for spell in spells):
        raise ValueError("List must contain only integers")

    operations = ['add', 'multiply', 'max', 'min']

    if operation.lower() not in operations:
        raise ValueError("Invalid operation")

    if operation.lower() == "add":
        result = reduce(lambda x, y: x + y, spells)

    if operation.lower() == "multiply":
        result = reduce(lambda x, y: x * y, spells)

    if operation.lower() == "max":
        result = reduce(lambda x, y: x if x > y else y, spells)

    if operation.lower() == "min":
        result = reduce(lambda x, y: x if x < y else y, spells)

    return result


def main() -> None:

    print("\n==> SPELL REDUCER:\n")

    spell_powers = [1, 2, 3, 4, 5]
    print(f"List: {spell_powers}")
    try:
        print(f"Sum: {spell_reducer(spell_powers, "add")}")
        print(f"Product: {spell_reducer(spell_powers, "multiply")}")
        print(f"Max: {spell_reducer(spell_powers, "max")}")
        print(f"Min: {spell_reducer(spell_powers, "min")}")
        print(f"Adding: {spell_reducer(spell_powers, "adding")}")
    except ValueError as err:
        print(err)
    print("-----------------------------------------------------------------")

    print("\n==> PARTIAL ENCHANTER:\n")


if __name__ == "__main__":
    main()

# operations = ['add', 'multiply', 'max', 'min']
# fibonacci_tests = [20, 8, 13]
