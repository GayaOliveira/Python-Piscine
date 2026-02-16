class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: int) -> None:
        self._name = new_name

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print(f"Security: Negative height rejected")
            print()
            print(f"Current plant: Rose ({self.height}cm, {self.age} days)")
        else:
            self._height = new_height

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print(f"Security: Negative age rejected")
            print()
            print(f"Current plant: Rose ({self.height}cm, {self.age} days)")
        else:
            self._age = new_age
        
    def __str__(self) -> str:
        return f"Plant created: {self.name}\nHeight updated: {self.height}cm [OK]\nAge updated: {self.age} days [OK]"
    

rose = Plant("Rose", 25, 30)
print("=== Garden Security System ===")
print(rose)
print()
rose.height = -5
print()
rose.age = -12
print()
rose.height = 26
print(rose)
