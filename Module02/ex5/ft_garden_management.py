class GardenError(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, water_level: int) -> None:
        if water_level > 10:
            super().__init__(
                f"Water level {water_level} is too high (max 10)"
                )
        if water_level < 1:
            super().__init__(
                f"Water level {water_level} is too low (min 1)"
                )


class SunlightError(GardenError):
    def __init__(self, sunlight_hours: int) -> None:
        if (sunlight_hours > 12):
            super().__init__(
                f"Sunlight hours {sunlight_hours}"
                " is too high (max 12)"
                )
        if (sunlight_hours < 2):
            super().__init__(
                f"Sunlight hours {sunlight_hours}"
                "is too low (min 2)"
                )


class TankError(GardenError):
    def __init__(self) -> None:
        super().__init__("Not enough water in tank")


class Plant:
    def __init__(
            self, name: str, water_level: int, sunlight_hours: int
            ) -> None:
        self.__name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        if name == "" or name is None:
            raise ValueError("Error adding plant: Plant name cannot be empty!")
        else:
            self.__name = name


class GardenManager():
    def __init__(self, tank_level: int) -> None:
        self.plant_list: list[Plant] = []
        self.tank_level = tank_level

    def add_plants(
            self, name: str, water_level: int, sunlight_hours: int
            ) -> None:
        if name == "" or name is None:
            raise ValueError("Error adding plant: Plant name cannot be empty!")
        else:
            plant = Plant(name, water_level, sunlight_hours)
            self.plant_list.append(plant)
            print(f"Added {plant.get_name()} successfully")

    def water_plants(self, plant: Plant) -> None:
        if (self.tank_level <= 0):
            raise TankError
        self.tank_level -= 5
        print(f"Watering {plant.get_name()} - success")

    def check_plant_health(self, plant: Plant):
        if (plant.water_level < 1 or plant.water_level > 10):
            raise WaterError(plant.water_level)
        if (plant.sunlight_hours < 2 or plant.sunlight_hours > 12):
            raise SunlightError(plant.sunlight_hours)


def test_garden_management(manager: GardenManager):
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    plants = [["tomato", 5, 8], ["lettuce", 15, 6], ["", 7, 8]]
    for p in plants:
        try:
            manager.add_plants(p[0], p[1], p[2])
        except ValueError as error:
            print(error)

    print("\nWatering plants...")
    try:
        print("Opening watering system")
        for plant in manager.plant_list:
            manager.water_plants(plant)
    except TankError as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        for plant in manager.plant_list:
            manager.check_plant_health(plant)
            print(
                f"{plant.get_name()}: healthy (water: {plant.water_level}, "
                f"sun: {plant.sunlight_hours})"
            )
    except GardenError as error:
        print(f"Error checking {plant.get_name()}:", error)

    print("\nTesting error recovery...")
    try:
        manager.water_plants(manager.plant_list[0])
    except GardenError as error:
        print("Caught GardenError:", error)
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    manager = GardenManager(10)
    test_garden_management(manager)
