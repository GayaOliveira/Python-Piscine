class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.__name = name
        if height >= 0:
            self.__height = height
        else:
            self.__height = 0

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def set_height(self, new_height: int) -> None:
        if new_height >= 0:
            self.__height = new_height

    def grow(self, cm: int) -> None:
        self.__height = self.__height + cm
        print(f"{self.get_name()} grew {cm}cm")

    def __str__(self) -> str:
        return f"- {self.get_name()}: {self.get_height()}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.__color = color

    def get_color(self) -> str:
        return self.__color

    def set_color(self, new_color: str) -> None:
        self.__color = new_color

    def __str__(self) -> str:
        info = f"- {self.get_name()}: {self.get_height()}cm, "
        info += f"{self.get_color()} flowers (blooming)"
        return info


class PrizeFlower(FloweringPlant):
    def __init__(
            self, name: str, height: int, color: str, points: int
            ) -> None:
        super().__init__(name, height, color)
        self.__prize_points = points

    def get_prize_points(self) -> int:
        return self.__prize_points

    def set_prize_points(self, new_points: int) -> None:
        if new_points < 0:
            info = "Invalid operation attempted: prize points"
            info += f" {new_points} [REJECTED]\n"
            info += "Security: Negative points rejected\n\n"
            info += f"Current plant: {self.get_name()} "
            info += f"({self.get_prize_points()} prize points)"
            print(info)
        else:
            self.__prize_points = new_points

    def __str__(self) -> str:
        info = f"- {self.get_name()}: {self.get_height()}cm, "
        info += f"{self.get_color()} flowers (blooming), "
        info += f"Prize points: {self.get_prize_points()}"
        return info


class Garden:

    def __init__(self) -> None:
        self.__plants = []
        self.__total_growth = 0
        self.__manager = None

    def get_plants(self) -> list[Plant]:
        return self.__plants

    def get_total_growth(self) -> int:
        return self.__total_growth

    def get_manager(self) -> "GardenManager":
        return self.__manager

    def set_total_growth(self, cm: int) -> None:
        self.__total_growth += cm

    def set_manager(self, manager: "GardenManager") -> None:
        self.__manager = manager

    def include_plant(self, plant: Plant) -> None:
        if plant not in self.__plants:
            self.__plants.append(plant)
        info = f"Added {plant.get_name()}"
        info += f" to {self.get_manager().get_manager()}'s garden"
        print(info)

    def count_plants(self) -> int:
        return len(self.__plants)

    def list_plants(self) -> None:
        print("Plants in garden:")
        for plant in self.__plants:
            print(plant)

    def classify_plants(self) -> list[int]:
        types = [0, 0, 0]
        for plant in self.__plants:
            if plant.__class__.__name__ == "PrizeFlower":
                types[2] += 1
            elif plant.__class__.__name__ == "FloweringPlant":
                types[1] += 1
            elif plant.__class__.__name__ == "Plant":
                types[0] += 1
            else:
                print("Tipo inexistente")
        return types


class GardenManager:
    __managers: list["GardenManager"] = []

    def __init__(self, manager: str) -> None:
        self.__manager = manager
        self.__garden = None

    class GardenStats:

        @staticmethod
        def validate_height() -> bool:
            plant = Plant("teste", -1)
            if plant.get_height() < 0:
                return False
            return True

        @staticmethod
        def calculate_scores(types: list[int]) -> None:
            return types[0] * 5 + types[1] * 10 + types[2] * 20

        @staticmethod
        def calculate_gardens_managed(gardens: list[Garden]) -> int:
            return len(gardens)

    def get_manager(self) -> str:
        return self.__manager

    def set_manager(self, new_manager: str) -> None:
        self.__manager = new_manager

    def get_garden(self) -> Garden:
        return self.__garden

    def set_garden(self, garden: Garden) -> None:
        self.__garden = garden
        garden.set_manager(self)

    def get_managers(self) -> list["GardenManager"]:
        return self.__managers

    def create_garden_network(cls, name: str) -> "GardenManager":
        manager = cls(name)
        cls.__managers.append(manager)
        return manager

    def add_plant(self, plant: Plant) -> None:
        self.get_garden().include_plant(plant)

    def manage_garden(self) -> None:
        print(f"{self.get_manager()} is helping all plants grow...")
        for plant in self.get_garden().get_plants():
            plant.grow(1)
            self.get_garden().set_total_growth(1)

    def produce_report(self) -> None:
        print(f"=== {self.get_manager()}'s Garden Report ===")
        self.get_garden().list_plants()
        print()
        print(f"Plants added: {self.get_garden().count_plants()}, ", end="")
        print(f"Total growth: {self.get_garden().get_total_growth()}")
        print("Plant types: ", end="")
        print(f"{self.get_garden().classify_plants()[0]} regular, ", end="")
        print(f"{self.get_garden().classify_plants()[1]} flowering, ", end="")
        print(f"{self.get_garden().classify_plants()[2]} prize flowers")

    @classmethod
    def show_analytics(cls) -> None:
        print("Height validation test: ", end="")
        print(cls.GardenStats.validate_height())
        print("Garden scores - ", end="")
        for manager in cls.__managers:
            types = manager.get_garden().classify_plants()
            score = cls.GardenStats.calculate_scores(types)
            print(f"{manager.get_manager()}: {score}", end=" ")
        print()
        print("Total gardens managed: ", end="")
        print(len(cls.__managers))


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    rose = FloweringPlant("Rose", 25, "red")
    daisy = FloweringPlant("Daisy", 20, "white")
    oak = Plant("Oak Tree", 1500)
    sunflower = PrizeFlower("Sunflower", 100, "yellow", 10)
    orchid = PrizeFlower("Orchid", 30, "pink", 20)

    alice = GardenManager.create_garden_network(GardenManager, "Alice")

    garden1 = Garden()
    alice.set_garden(garden1)
    alice.add_plant(rose)
    alice.add_plant(oak)
    alice.add_plant(orchid)
    alice.add_plant(sunflower)
    print()

    bob = GardenManager.create_garden_network(GardenManager, "Bob")
    garden2 = Garden()
    bob.set_garden(garden2)
    bob.add_plant(sunflower)
    bob.add_plant(daisy)
    print()
    alice.manage_garden()
    print()
    alice.produce_report()
    print()
    GardenManager.show_analytics()
