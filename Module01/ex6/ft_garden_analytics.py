class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.__name = name
        self.__height = height

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            info = "Invalid operation attempted: height"
            info += f" {new_height}cm [REJECTED]\n"
            info += "Security: Negative height rejected\n\n"
            info += f"Current plant: {self.get_name()} "
            info += f"({self.get_height()}cm"
            print(info)
        else:
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


class GardenManager:
    managers = []     # Encapsular??

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__garden = []
        # self.internal = self.GardenStats(self)
        self.__total_growth = 0

    class GardenStats:

        # @staticmethod
        # def count_plants(lst: list["GardenManager"]) -> int:
        #     return len(lst)

        # @staticmethod
        # def count_plants(lst: list["GardenManager"]) -> int:
        #     return len(lst)
        pass

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    # @classmethod
    def create_garden_network(cls, name: str) -> None:
        manager = cls(name)
        cls.managers.append(manager)
        return manager

    def include_plant(self, plant: Plant) -> None:
        if plant not in self.__garden:
            self.__garden.append(plant)
            info = f"Added {plant.get_name()}"
            info += f" to {self.get_name()}'s garden"
            print(info)

    def remove_plant(self, plant: Plant) -> None:
        if plant in self.__garden:
            self.__garden.pop(plant)
            info = f"Removed {plant.get_name()}"
            info += f" from {self.get_name()}'s garden"
            print(info)

    def list_plants_garden(self):
        print("Plants in garden:")
        for plant in self.__garden:
            print(plant)

    def manage_garden(self):
        print(f"{self.get_name()} is helping all plants grow...")
        for plant in self.__garden:
            plant.grow(1)
            self.__total_growth += 1
    
    def count_plants(self) -> int:
        return len(self.__garden)
    
    def total_growth(self) -> int:
        return self.__total_growth

    def classify_plants(self) -> list[int]:
        types = [0, 0, 0]
        for plant in self.__garden:
            if plant.__class__.__name__ == "PrizeFlower":
                types[2] += 1
            elif plant.__class__.__name__ == "FloweringPlant":
                types[1] += 1
            elif plant.__class__.__name__ == "Plant":
                types[0] += 1
            else:
                print("Deu ruim")
        return types


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    rose = FloweringPlant("Rose", 25, "red")
    daisy = FloweringPlant("Daisy", 20, "white")
    oak = Plant("Oak Tree", 1500)
    sunflower = PrizeFlower("Sunflower", 100, "yellow", 10)

    # alice = GardenManager("Alice")
    alice = GardenManager.create_garden_network(GardenManager, "Alice")
    alice.include_plant(rose)
    alice.include_plant(oak)
    alice.include_plant(sunflower)
    alice.include_plant(daisy)
    print()

    alice.manage_garden()
    print()

    alice.list_plants_garden()

    for i in GardenManager.managers:
        print(i.get_name())

    # print(alice.internal.count_plants([1, 2, 3]))

    lista = alice.classify_plants()
    for i in lista:
        print(i)
