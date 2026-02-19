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
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print(f"Security: Negative height rejected")
            print()
            print(f"Current plant: Rose ({self.get_height()}cm, {self.get_age()} days)")
        else:
            self.__height = new_height

    
    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print(f"Security: Negative age rejected")
            print()
            print(f"Current plant: Rose ({self.get_height()}cm, {self.get_age()} days)")
        else:
            self.__age = new_age        

    def __str__(self) -> str:
        return f"Plant created: {self.__name}\nHeight updated: {self.__height}cm [OK]\nAge updated: {self.__age} days [OK]"
    

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
