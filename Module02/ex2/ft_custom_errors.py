class GardenError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def raise_errors(error):
    if error == "PlantError":
        raise PlantError
    if error == "WaterError":
        raise WaterError
    if error == "GardenError":
        raise GardenError


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    errors = ["PlantError", "WaterError"]
    for error in errors:
        try:
            print(f"Testing {error}...")
            raise_errors(error)
        except PlantError as err:
            print("Caught PlantError: ", err)
        except WaterError as err:
            print("Caught PlantError: ", err)
        print()
    print("Testing catching all garden errors...")
    for error in errors:
        try:
            raise_errors(error)
        except GardenError as err:
            print("Caught PlantError: ", err)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()