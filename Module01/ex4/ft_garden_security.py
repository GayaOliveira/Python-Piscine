class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print(f"Security: Negative height rejected")
            print()
            print(f"Current plant: Rose ({self.height}cm, {self.age} days)")
        else:
            self._height = new_height

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print(f"Security: Negative age rejected")
            print()
            print(f"Current plant: Rose ({self.height}cm, {self.age} days)")
        else:
            self._age = new_age
        
    def __str__(self):
        return f"""Plant created: {self.name}
Height updated: {self.height}cm [OK]
Age updated: {self.age} days [OK]"""
    

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
