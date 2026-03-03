def garden_operations(error):
    if error == "ValueError":
        raise ValueError("invalid literal for int()")
    if error == "ZeroDivisionError":
        raise ZeroDivisionError("division by zero")
    if error == "FileNotFoundError":
        raise FileNotFoundError("No such file 'missing.txt'")
    if error == "KeyError":
        raise KeyError("missing_plant")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    errors = [
        "ValueError",
        "ZeroDivisionError",
        "FileNotFoundError",
        "KeyError"
        ]
    for error in errors:
        print(f"Testing {error}...")
        try:
            garden_operations(error)
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as err:
            print(f"Caught {error}: {err}\n")
    print("Testing multiple errors together...")
    try:
        garden_operations()
    except Exception:
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()


# Usar exemplos reais? Open? Close? ?????