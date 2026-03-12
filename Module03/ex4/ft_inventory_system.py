import sys

# dicionário com itens do tipo "item: quantidade"
# dicionário com itens que têm quantidade >= 5
# dicionário com itens que têm quantidade < 5

def create_dict(args: list[str]) -> dict[str, int]:
    invent_dict = dict()
    for arg in args:
        separator_index = arg.index(":")
        item = arg[:separator_index]
        quantity = int(arg[separator_index + 1:])
        invent_dict[item] = quantity
    return invent_dict


def calculate_total_items(invent_dict: dict[str, int]) -> int:
    total_items = 0
    for qtty in invent_dict.values():
        total_items += qtty
    return total_items


if __name__ == "__main__":

    print("=== Inventory System Analysis ===")
    inventory = create_dict(sys.argv[1:])
    total_items = calculate_total_items(inventory)
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")


# def my_split(string: str) -> list[str | str]:
# 	str_list = []
# 	key = ""
# 	i = 0
# 	while (i < len(string)):
# 		if string[i] == ":":
# 			i += 1
# 			value = string[i:]
# 			str_list.append([key, value])
# 			key = ""
# 		else:
# 			key = key + string[i]
# 			i += 1
# 	return str_list