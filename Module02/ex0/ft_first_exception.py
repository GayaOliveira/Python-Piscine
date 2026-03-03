def check_temperature(temp_str):
    try:
        temperature = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        if temperature > 40:
            raise ValueError(
                f"Error: {temperature}°C is too hot for plants (max 40°C)"
                )
        if temperature < 0:
            raise ValueError(
                f"Error: {temperature}°C is too cold for plants (min 0°C)"
                )
        print(f"Temperature {temperature}°C is perfect for plants!")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    temperatures = [25, "abc", 100, -50]
    for temp in temperatures:
        print(f"Testing temperature: {temp}")
        try:
            check_temperature(temp)
        except ValueError as error:
            print(error)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
