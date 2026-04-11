from . import light_validator as val


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    valid_ingredients = val.validate_ingredients(ingredients)
    if "INVALID" in valid_ingredients:
        return f"Spell rejected: {spell_name} ({valid_ingredients})"
    return f"Spell recorded: {spell_name} ({valid_ingredients})"
