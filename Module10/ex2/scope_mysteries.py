from collections.abc import Callable


def mage_counter() -> Callable:

    count = 0

    def call_counter() -> int:
        nonlocal count
        count += 1
        return count

    return call_counter


def spell_accumulator(initial_power: int) -> Callable:

    if not initial_power:
        raise TypeError("Missing argument(s)")
    power = initial_power

    def accumulate_power(increment: int) -> int:
        if not increment:
            raise TypeError("Missing argument(s)")
        nonlocal power
        power += increment
        return power

    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:

    if not enchantment_type:
        raise TypeError("Missing argument(s)")

    return lambda name: f"{enchantment_type.capitalize()} {name}"


def memory_vault() -> dict[str, Callable]:

    vault_manipulation: dict[str, Callable] = {}
    memory: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        memory.update({key: value})

    def recall(key: str) -> str:
        return memory.get(key, "Memory not found")

    vault_manipulation.update({"store": store})
    vault_manipulation.update({"recall": recall})

    return vault_manipulation


# def memory_vault2() -> dict[str, Callable]:

#     memory: dict[str, str] = {}

#     return {
#         "store": lambda key, value: memory.update(key, value),
#         "recall": lambda key: memory.get(key, "Memory not found")
#     }


def main() -> None:

    print("\n==> MAGE COUNTER:\n")

    print("Call counter 1")
    call_counter1 = mage_counter()
    print(call_counter1())
    print(call_counter1())
    print(call_counter1())
    print(call_counter1())

    print("\nCall counter 2")
    call_counter2 = mage_counter()
    print(call_counter2())
    print(call_counter2())
    print(call_counter2())
    print("-----------------------------")

    print("\n==> SPELL ACCUMULATOR:\n")

    print("Accumulator 1 - intial power = 20")
    try:
        accumulator1 = spell_accumulator(20)
        print("(+5)", accumulator1(5))
        print("(+2)", accumulator1(2))
        print("(+3)", accumulator1(3))
    except TypeError as err:
        print(err)

    print("\nAccumulator 2 - intial power = 50")
    try:
        accumulator2 = spell_accumulator(50)
        print("(+8)", accumulator2(8))
        print("(+6)", accumulator2(6))
        print("(+6)", accumulator2(6))
    except TypeError as err:
        print(err)
    print("-----------------------------")

    print("\n==> ENCHANTMENT FACTORY:\n")

    print("Type: 'flaming', Name: 'sword'")
    try:
        create_enchantment = enchantment_factory("flaming")
        print("Enchantment created:", create_enchantment("sword"))
    except TypeError as err:
        print(err)
    print("-----------------------------")

    print("\n==> MEMORY VAULT:\n")

    try:
        vault = memory_vault()
        print("Saving 'secret' with value '42'...")
        vault["store"]("secret", "42")
        print("Recovering 'secret' value:", vault["recall"]("secret"))
        print("Recovering 'no_secret' value:", vault["recall"]("no_secret"))
    except TypeError as err:
        print(err)
    print()


if __name__ == "__main__":
    main()
