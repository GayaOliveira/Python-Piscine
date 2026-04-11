from . import light_spellbook as spe


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = spe.light_spell_allowed_ingredients()
    ingredients_list = ingredients.split(", ")
    is_valid = "VALID"
    for element in ingredients_list:
        if element not in allowed_ingredients:
            is_valid = "INVALID"
    ingredients_str = ""
    for i in range(len(ingredients_list)):
        if i == 0:
            ingredients_str += f"{ingredients_list[i].capitalize()}, "
        elif i == len(ingredients_list) - 2:
            ingredients_str += f"{ingredients_list[i]} and "
        elif i == len(ingredients_list) - 1:
            ingredients_str += f"{ingredients_list[i]}"
        else:
            ingredients_str += f"{ingredients_list[i]}, "
    return f"{ingredients_str} - {is_valid}"
