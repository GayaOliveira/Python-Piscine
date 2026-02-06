def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != "grams" and unit != "area":
        print("Unknown unit type")
    else:
        answer = f"{seed_type.capitalize()} seeds: "
        if unit == "packets":
            answer += f"{quantity} packets available"
        elif unit == "grams":
            answer += f"{quantity} grams total"
        elif unit == "area":
            answer += f"covers {quantity} squares meters"
        print(answer)
