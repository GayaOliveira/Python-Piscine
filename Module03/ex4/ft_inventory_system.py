import sys


def create_dict(args: list[str]) -> dict[str, int]:
    invent_dict = dict()
    for arg in args:
        separator_index = arg.index(":")
        item = arg[:separator_index]
        try:
            quantity = int(arg[separator_index + 1:])
        except ValueError as err:
            print(err)
        else:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative!")
            invent_dict[item] = quantity
    return invent_dict


def calculate_total_items(invent_dict: dict[str, int]) -> int:
    total_items = 0
    for qtty in invent_dict.values():
        total_items += qtty
    return total_items


def show_inventory(invent_dict: dict[str, int]) -> None:
    total_items = calculate_total_items(invent_dict)
    for name, qtty in invent_dict.items():
        percentage = qtty / total_items * 100
        print(f"{name}: {qtty} units ({percentage:.1f}%)")


def find_most_abundant(invent_dict: dict[str, int]) -> tuple[str, int]:
    most_qtty = 0
    most_name = ""
    for name, qtty in invent_dict.items():
        if qtty > most_qtty:
            most_qtty = qtty
            most_name = name
    return most_name, most_qtty


def find_max(invent_dict: dict[str, int]) -> int:
    biggest = None
    for value in invent_dict.values():
        if biggest is None or biggest < value:
            biggest = value
    return biggest


def find_least_abundant(invent_dict: dict[str, int]) -> tuple[str, int]:
    least_qtty = find_max(invent_dict.values())
    least_name = ""
    for name, qtty in invent_dict.items():
        if qtty < least_qtty:
            least_qtty = qtty
            least_name = name
    return least_name, least_qtty


def analyze_frequency(
        invent_dict: dict[str, int]
        ) -> list[dict[str, int] | dict[str, int] | dict[str, int]]:
    frequent: dict[str, int] = {}
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}
    for name, qtty in invent_dict.items():
        if qtty <= 3:
            scarce[name] = qtty
        elif qtty > 4 and qtty < 10:
            moderate[name] = qtty
        else:
            frequent[name] = qtty
    return [scarce, moderate, frequent]


def check_restock(invent_dict: dict[str, int]) -> list[str]:
    need_restock: list[str] = []
    for name, qtty in invent_dict.items():
        if qtty == 1:
            need_restock.append(name)
    return need_restock


def list_to_str(list_to_print: list) -> str:
    str_to_print = ""
    for i, item in enumerate(list_to_print):
        if i < len(list_to_print) - 1:
            str_to_print += f"{item}, "
        else:
            str_to_print += f"{item}"
    return str_to_print


def find_item(item: str, invent_dict: dict[str, int]) -> bool:
    if item in invent_dict:
        return True
    else:
        return False


if __name__ == "__main__":

    print("=== Inventory System Analysis ===")
    try:
        inventory = create_dict(sys.argv[1:])
    except ValueError as err:
        print(err)
    else:
        total_items = calculate_total_items(inventory)
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {len(inventory)}")

        print("\n=== Current Inventory ===")
        show_inventory(inventory)

        print("\n=== Inventory Statistics ===")
        most_abundant_name, most_abundant_qtty = find_most_abundant(inventory)
        print(
            f"Most abundant: {most_abundant_name} ({most_abundant_qtty} units)"
            )
        least_abund_name, least_abund_qtty = find_least_abundant(inventory)
        print(
            f"Least abundant: {least_abund_name} ({least_abund_qtty}"
            f" {'units' if least_abund_qtty > 1 else 'unit'})"
            )

        print("\n=== Item Categories ===")
        scarce, moderate, frequent = analyze_frequency(inventory)
        if (len(frequent) != 0):
            print(f"Frequent: {frequent}")
        if (len(moderate) != 0):
            print(f"Moderate: {moderate}")
        if (len(scarce) != 0):
            print(f"Scarce: {scarce}")

        print("\n=== Management Suggestions ===")
        need_restock = check_restock(inventory)
        print(f"Restock needed: {list_to_str(need_restock)}")

        print("\n=== Dictionary Properties Demo ===")
        keys = [*inventory.keys()]
        print(f"Dictionary keys: {list_to_str(keys)}")
        values = [*inventory.values()]
        print(f"Dictionary values: {list_to_str(values)}")
        print(
            "Sample lookup - 'sword' in inventory: "
            f"{find_item('sword', inventory)}"
            )


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
