from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        raise ValueError("Invalid list")

    if not all(isinstance(spell, int) for spell in spells):
        raise ValueError("List must contain only integers")

    operations = {
        'add': add,
        'multiply': mul,
        'max': max,
        'min': min
    }

    if not operations.get(operation.lower()):
        raise ValueError("Invalid operation")

    result = reduce(operations[operation], spells)

    return result


# This function should not be called directly
def spear(power: int, element: str, target: str) -> str:
    if not target or not element or power is None:
        raise TypeError("Invalid/missing argument(s)")
    return f"{element} spear hits {target} inflicting {power} of damage"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    if base_enchantment is None:
        raise ValueError("Invalid enchantmente")

    power = 50
    elements: list[str] = ["Ice", "Flaming", "Water", "Eletric", "Acid"]

    spell_book: dict[str, Callable] = {}

    for element in elements:
        spell = partial(base_enchantment, power=power, element=element)
        spell_book.update({element: spell})

    return spell_book


@lru_cache(maxsize=None)
def memoized_fibonacci(n):
    if n < 0:
        raise ValueError("Invalid argument")
    if n == 0 or n == 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("Invalid argument")
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def spell(data: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(data: str) -> str:
        return f"Damage spell: {data} damage"

    @spell.register(str)
    def _(data: str) -> str:
        return f"Enchantment: {data}"

    @spell.register(list)
    def _(data: list) -> str:
        return f"Multi-cast: {len(data)} spells"

    return spell


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

    print("Creating spear spells...\n")
    try:
        spear_spells = partial_enchanter(spear)
    except TypeError:
        print("Invalid argument")
    ice_spear = spear_spells.get("Ice")
    if ice_spear:
        print(ice_spear(target="Knight"))
    else:
        print("Invalid element")

    print("-----------------------------------------------------------------")

    print("\n==> MEMOIZED FIBONACCI:\n")

    print("Testing memoized fibonacci...\n")
    try:
        print("Memoized Fib(36):", memoized_fibonacci(36))
        # print(memoized_fibonacci.cache_info())
        print("Normal Fib(36):", fibonacci_recursive(36))
    except (TypeError, ValueError):
        print("Invalid argument")
    except RecursionError:
        print("Maximum recursion depth exceeded")

    print("-----------------------------------------------------------------")

    print("\n==> SPELL DISPATCHER:\n")

    print("Testing spell dispatcher...\n")
    try:
        print(spell_dispatcher()(42))
        print(spell_dispatcher()("fireball"))
        print(spell_dispatcher()(["heal", "fireball", "revive"]))
        print(spell_dispatcher()({"heal": 30}))
        print("With no argument: ", end="")
        print(spell_dispatcher()())
    except TypeError as err:
        print(err)

    print()


if __name__ == "__main__":
    main()
