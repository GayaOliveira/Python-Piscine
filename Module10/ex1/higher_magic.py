from collections.abc import Callable


def heal(target: str, power: int) -> str:
    if not target or power is None:
        raise TypeError("Invalid/missing argument(s)")
    if power <= 0:
        raise ValueError("HP increment must be positive")
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    if not target or power is None:
        raise TypeError("Invalid/missing argument(s)")
    if power <= 0:
        raise ValueError("Damage must be positive")
    return f"Fireball hits {target} inflicting {power} of damage"


def hidropump(target: str, power: int) -> str:
    if not target or power is None:
        raise TypeError("Invalid/missing argument(s)")
    if power <= 0:
        raise ValueError("Damage must be positive")
    return f"Hidropump hits {target} inflicting {power} of damage"


# Como padrão, essa função revive o alvo.
# Para fazer sentido, deve ser combinada com a is_dead
# por meio da conditional_caster.
def revive(target: str, power: int) -> str:
    if not target or power is None:
        raise TypeError("Invalid/missing argument(s)")
    if power < 0:
        raise ValueError("HP cannot be negative")
    return f"{target} has been revived"


def is_dead(target: str, power: int) -> bool:
    if not target or power is None:
        raise TypeError("Invalid/missing argument(s)")
    if power < 0:
        raise ValueError("HP cannot be negative")
    if power == 0:
        return True
    return False


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    if spell1 is None or spell2 is None:
        raise TypeError("Missing argument(s)")

    if not callable(spell1) or not callable(spell2):
        raise TypeError("Spells must be callable objects")

    def combine(
            target: str,
            power: int
            ) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    if base_spell is None or multiplier is None:
        raise TypeError("Missing argument(s)")

    if not callable(base_spell):
        raise TypeError("The spell must be a callable object")

    def amplify(target: str, power: int) -> str:
        return f"Original: {base_spell(target, power)}, " \
               f"Amplified: {base_spell(target, power * multiplier)}"

    return amplify


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    if condition is None or spell is None:
        raise TypeError("Missing argument(s)")

    if not callable(condition) or not callable(spell):
        raise TypeError("Spell/condition must be a callable object")

    def cast_if(target: str, power: int) -> str:

        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return cast_if


def spell_sequence(spells: list[Callable]) -> Callable:

    if not spells:
        raise TypeError("Missing argument(s)")

    for spell in spells:
        if spell is None:
            raise TypeError("Missing argument(s)")
        if not callable(spell):
            raise TypeError("Spell/condition must be a callable object")

    def cast_in_sequence(target: str, power: int) -> list[str]:

        spell_results: list[str] = []
        for spell in spells:
            spell_results.append(spell(target, power))

        return spell_results

    return cast_in_sequence


def main() -> None:

    print("\n ==> SPELL COMBINER:\n")

    print("Test 1:")
    try:
        combined = spell_combiner(heal, fireball)
        result1, result2 = combined("Goblin", 10)
        print(f"Combined spell result: {result1}, {result2}")
    except Exception as err:
        print(f"Error: {err}")

    print("\nTest 2:")
    try:
        combined = spell_combiner("heal", fireball)   # type: ignore
        result1, result2 = combined("Goblin", 10)
        print(f"Combined spell result: {result1}, {result2}")
    except Exception as err:
        print(f"Error: {err}")

    print("\nTest 3:")
    try:
        combined = spell_combiner(heal, fireball)
        result1, result2 = combined("Goblin", -10)    # exemplo com erro
        print(f"Combined spell result: {result1}, {result2}")
    except Exception as err:
        print(f"Error: {err}")

    print("-----------------------------------------------------------------")
    print("\n ==> POWER AMPLIFIER:\n")

    print("Test 1:")
    try:
        mega_hidropump = power_amplifier(hidropump, 50)
        print(mega_hidropump("Turtle", 20))
    except Exception as err:
        print(f"Error: {err}")

    print("\nTest 2:")
    try:
        mega_hidropump = power_amplifier(hidropump, 50)    # exemplo com erro
        print(mega_hidropump("Turtle", None))
    except Exception as err:
        print(f"Error: {err}")

    print("-----------------------------------------------------------------")
    print("\n ==> CONDITIONAL CASTER:\n")

    print("Test 1:")
    try:
        reviver = conditional_caster(is_dead, revive)
        print(reviver("Dragon", 10))
    except Exception as err:
        print(f"Error: {err}")

    print("\nTest 2:")
    try:
        reviver = conditional_caster(is_dead, revive)
        print(reviver("Knight", 0))
    except Exception as err:
        print(f"Error: {err}")

    print("-----------------------------------------------------------------")
    print("\n ==> SPELL SEQUENCE:\n")

    print("Test 1:")
    try:
        spells = [heal, fireball, hidropump, revive]
        sequence_caster = spell_sequence(spells)
        print(sequence_caster("Lion", 20))
    except Exception as err:
        print(f"Error: {err}")

    print("\nTest 2:")
    try:
        spells = []
        sequence_caster = spell_sequence(spells)
        print(sequence_caster("Sorcerer", 20))
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
