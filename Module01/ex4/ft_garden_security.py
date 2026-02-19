class SecurePlant:
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
            to_print = "Invalid operation attempted: height"
            to_print += f" {new_height}cm [REJECTED]\n"
            to_print += "Security: Negative height rejected\n\n"
            to_print += f"Current plant: {self.get_name()} "
            to_print += f"({self.get_height()}cm, {self.get_age()} days)"
            print(to_print)
        else:
            self.__height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            to_print = "Invalid operation attempted: age"
            to_print += f" {new_age}cm [REJECTED]\n"
            to_print += "Security: Negative height rejected\n\n"
            to_print += f"Current plant: {self.get_name()} "
            to_print += f"({self.get_height()}cm, {self.get_age()} days)"
            print(to_print)
        else:
            self.__age = new_age

    def __str__(self) -> str:
        ret = f"Plant created: {self.__name}\nHeight updated: {self.__height}"
        ret += f"cm [OK]\nAge updated: {self.__age} days [OK]"
        return ret


if __name__ == "__main__":
    rose = SecurePlant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(rose)
    print()
    rose.set_height(-5)
    print()
    rose.set_age(-12)
    print()
    rose.set_height(26)
    print(rose)
