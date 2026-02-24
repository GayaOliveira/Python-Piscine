class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        if height >= 0:
            self.__height = height
        else:
            self.__height = 0
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

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


class Garden:

        def __init__(self, owner: str) -> None:
            self.__owner = owner
            self.__plants = []
            self.__total_growth = 0

        def get_owner(self) -> str:
            return self.__owner

        def get_plants(self) -> list[Plant]:
            return self.__plants

        def get_total_growth(self) -> int:
            return self.__total_growth
        
        def set_total_growth(self, cm: int) -> None:
            self.__total_growth += cm

        def include_plant(self, plant: Plant) -> None:
            if plant not in self.__plants:
                self.__plants.append(plant)
            info = f"Added {plant.get_name()}"
            info += f" to {self.get_owner()}'s garden"
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
    __managers = []

    def __init__(self, manager: str) -> None:
        self.__manager = manager
        self.__garden = []
        # self.internal = self.GardenStats(self)

    class GardenStats:

        @staticmethod
        def validate_height() -> bool:
            plant = Plant("teste", -5)

        @staticmethod
        def calculate_scores():
            pass

        @staticmethod
        def calculate_gardens_managed(gardens: list[Garden]) -> int:
            pass

    def get_manager(self) -> str:
        return self.__manager

    def set_manager(self, new_manager: str) -> None:
        self.__manager = new_manager

    # @classmethod
    def create_garden_network(cls, name: str) -> "GardenManager":
        manager = cls(name)
        cls.__managers.append(manager)
        return manager
    
    def assign_garden_to_manager(self, garden: Garden) -> None:
        self.__garden.append(garden)

    def add_plant(self, plant: Plant, garden: Garden) -> None:
        for gard in self.__garden:
            if gard == garden:
                garden.include_plant(plant)

    def manage_garden(self, garden: Garden) -> None:
        print(f"{garden.get_owner()} is helping all plants grow...")
        for plant in garden.get_plants():
            plant.grow(1)
            garden.set_total_growth(1)
    
    def produce_report(self, garden: Garden) -> None:
        print(f"=== {garden.get_owner()}'s Garden Report ===")
        garden.list_plants()
        print()
        print(f"Plants added: {garden.count_plants()}, ", end = "")
        print(f"Total growth: {garden.get_total_growth()}")
        print("Plant types: ", end = "")
        print(f"{garden.classify_plants()[0]} regular, ", end = "")
        print(f"{garden.classify_plants()[1]} flowering, ", end = "")
        print(f"{garden.classify_plants()[2]} prize flowers")

    def show_analytics() -> None:
        pass


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    rose = FloweringPlant("Rose", 25, "red")
    daisy = FloweringPlant("Daisy", 20, "white")
    oak = Plant("Oak Tree", 1500)
    sunflower = PrizeFlower("Sunflower", 100, "yellow", 10)
    orchid = PrizeFlower("Orchid", 30, "pink", 20)

    # alice = GardenManager("Alice")
    m1 = GardenManager.create_garden_network(GardenManager, "Manager1")
    alice_garden = Garden("Alice")
    m1.assign_garden_to_manager(alice_garden)
    bob_garden = Garden("Bob")
    m1.assign_garden_to_manager(bob_garden)

    m1.add_plant(rose, alice_garden)
    m1.add_plant(oak, alice_garden)
    m1.add_plant(orchid, alice_garden)
    m1.add_plant(sunflower, alice_garden)
    m1.add_plant(sunflower, bob_garden)
    m1.add_plant(daisy, bob_garden)
    print()

    m1.manage_garden(alice_garden)
    print()

    m1.produce_report(alice_garden)
    print()
    m1.produce_report(bob_garden)

    # for i in GardenManager.managers:
    #     print(i.get_name())

    # print(alice.internal.count_plants([1, 2, 3]))

    
