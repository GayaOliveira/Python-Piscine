import sys

def my_split(string: str) -> list[str | str]:
	str_list = []
	key = ""
	i = 0
	while (i < len(string)):
		if string[i] == ":":
			i += 1
			value = string[i:]
			str_list.append([key, value])
			key = ""
		else:
			key = key + string[i]
			i += 1
	return str_list

# dicionário com itens do tipo "item: quantidade"
# dicionário com itens que têm quantidade >= 5
# dicionário com itens que têm quantidade < 5


if __name__ == "__main__":

	entry_list = sys.argv[1:].copy()
	# print(entry_list)
	splitted_entry_list = []
	for entry in entry_list:
		splitted_entry_list.append(my_split(entry))
	print(splitted_entry_list)
	# print("=== Inventory System Analysis ===")
