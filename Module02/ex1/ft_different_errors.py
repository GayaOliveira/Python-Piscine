def garden_operations(error: str) -> dict[str, str]:
    if (error == "value"):
        int("abc")
    elif (error == "zero"):
        1 / 0
    elif (error == "file"):
        open("missing.txt")
    else:
        dictionary = {"flower": "rose", "tree": "oak"}
        dictionary["plant"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    try:
        print("\nTesting ValueError...")
        garden_operations("value")
    except ValueError as error:
        error = str(error)[:25]
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
        error = str(error)[10:]
        print(f"Caught FileNotFoundError: {error}")
    try:
        print("\nTesting KeyError...")
        garden_operations("key")
    except KeyError as error:
        error = str(error)[1:]
        print(fr"Caught KeyError: 'missing/_{error}")
    try:
        print("\nTesting multiple errors togheter...")
        garden_operations("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues")
    print("\nAll error types tested successfully!")


if (__name__ == "__main__"):
    test_error_types()
