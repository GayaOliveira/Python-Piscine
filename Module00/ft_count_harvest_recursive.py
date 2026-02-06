def count_days(days, acc):
    if (acc == 1):
        print(f"Day {acc}")
    else:
        count_days(days, acc - 1)
        print(f"Day {acc}")


def ft_count_harvest_recursive():

    days = int(input("Days until harvest: "))
    acc = days
    count_days(days, acc)
    print("Harvest time!")
