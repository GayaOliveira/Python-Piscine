from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    valid_ingredients = validate_ingredients(ingredients)
    if "INVALID" in valid_ingredients:
        return f"Spell rejected: {spell_name} ({valid_ingredients})"
    return f"Spell recorded: {spell_name} ({valid_ingredients})"
