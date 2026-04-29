from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} inflicting {power} of damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined(
            target1: str,
            power1: int,
            target2: str,
            power2: int
            ) -> tuple[str, str]:
        return spell1(target1, power1), spell2(target2, power2)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    pass


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass


def spell_sequence(spells: list[Callable]) -> Callable:
    pass


if __name__ == "__main__":

    combined = spell_combiner(heal, fireball)
    str1, str2 = combined("Dragon", "Goblin", 20, 50)
    print(f"{str1}, {str2}")


# test_values = [12, 23, 17]
# test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
