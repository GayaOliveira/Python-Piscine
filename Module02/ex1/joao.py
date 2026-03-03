def garden_operations(error: str) -> None:
    if (error == "value"):
        int("abc")
    elif (error == "zero"):
        1 / 0
    elif (error == "file"):
        open("missing.txt")
    else:
        dictionary = {"flower": "rose", "tree": "oak"}
        return (dictionary["plant"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    try:
        print("\nTesting ValueError...")
        garden_operations("value")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    try:
        print("\nTesting ZeroDivisionError...")
        garden_operations("zero")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    try:
        print("\nTesting FileNotFoundError...")
        garden_operations("file")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    try:
        print("\nTesting KeyError...")
        garden_operations("key")
    except KeyError as error:
        print(f"Caught KeyError: {error}")
    try:
        print("\nTesting multiple errors togheter...")
        garden_operations("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues")
    print("\nAll error types tested successfully!")


if (__name__ == "__main__"):
    test_error_types()
