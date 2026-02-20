class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_name(self, new_name: int) -> None:
        self.__name = new_name

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            info = "Invalid operation attempted: height"
            info += f" {new_height}cm [REJECTED]\n"
            info += "Security: Negative height rejected\n\n"
            info += f"Current plant: {self.get_name()} "
            info += f"({self.get_height()}cm, {self.get_age()} days)"
            print(info)
        else:
            self.__height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            info = "Invalid operation attempted: age"
            info += f" {new_age}cm [REJECTED]\n"
            info += "Security: Negative height rejected\n\n"
            info += f"Current plant: {self.get_name()} "
            info += f"({self.get_height()}cm, {self.get_age()} days)"
            print(info)
        else:
            self.__age = new_age

    def __str__(self) -> str:
        info = f"Plant created: {self.get_name()}\nHeight updated: "
        info += f"{self.get_height()}cm [OK]\nAge updated: {self.get_age} days [OK]"
        return info


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.__color = color

    def get_color(self) -> str:
        return self.__color

    def set_color(self, new_color: str) -> None:
        self.__color = new_color

    def bloom(self) -> str:
        return f"{self.get_name()} is blooming beautifully!"

    def __str__(self) -> str:
        info = f"{self.get_name()} (Flower): {self.get_height()}cm, "
        info = f"{self.get_age()} days, {self.get_color()} color\n"
        info += self.bloom()
        return info


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 trunk_diameter: int,
                 shade: int
                 ) -> None:
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter
        self.__shade = shade

    def get_trunk_diameter(self) -> int:
        return self.__trunk_diameter

    def set_trunk_diameter(self, new_trunk_diameter: int) -> None:
        if new_trunk_diameter < 0:
            info = "Invalid operation attempted: trunk diameter"
            info += f" {new_trunk_diameter}cm [REJECTED]\n"
            info += "Security: Negative trunk diameter rejected\n\n"
            info += f"Current plant: {self.get_name()} "
            info += f"({self.get_trunk_diameter()}cm diameter)"
            print(info)
        else:
            self.__trunk_diameter = new_trunk_diameter

    def get_shade(self) -> int:
        return self.__shade

    def set_shade(self, new_shade: int) -> None:
        if new_shade < 0:
            info = "Invalid operation attempted: shade area of"
            info += f" {new_shade} square meters [REJECTED]\n"
            info += "Security: Negative trunk diameter rejected\n\n"
            info += f"Current plant: {self.get_name()} "
            info += f"({self.get_shade()} square meters)"
            print(info)
        else:
            self.__shade = new_shade

    def produce_shade(self) -> str:
        info = f"{self.get_name()} provides "
        info += f"{self.get_shade()} square meters of shade"
        return info

    def __str__(self) -> str:
        info = f"{self.get_name()} (Tree): {self.get_height()}cm, "
        info = f"{self.get_age()} days, "
        info = f"{self.get_trunk_diameter()}cm diameter\n"
        info += self.produce_shade()
        return info


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str
                 ) -> None:
        super().__init__(name, height, age)
        self.__harvest_season = harvest_season
        self.__nutritional_value = nutritional_value

    def get_harvest_season(self) -> str:
        return self.__harvest_season

    def set_harvest_season(self, new_harvest_season: str) -> None:
        self.__harvest_season = new_harvest_season

    def get_nutritional_value(self) -> str:
        return self.__nutritional_value

    def set_nutritional_value(self, new_nutritional_value: str) -> None:
        self.__nutritional_value = new_nutritional_value

    def __str__(self) -> str:
        info = f"{self.get_name()} (Vegetable): {self.get_height()}cm, "
        info += f"{self.get_age()} days, "
        info += f"{self.get_harvest_season()} harvest\n"
        info += f"{self.get_name()} is rich in {self.get_nutritional_value()}"
        return info


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    daisy = Flower("Daisy", 20, 60, "white")
    oak = Tree("Oak", 500, 2280, 80, 78)
    pine = Tree("Pine", 1500, 1600, 50, 5)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    spinach = Vegetable("Spinach", 60, 120, "autumn", "iron")

    plants = [rose, daisy, oak, pine, tomato, spinach]

    print("=== Garden Plant Types ===")
    for plant in plants:
        print(plant)
        print()
