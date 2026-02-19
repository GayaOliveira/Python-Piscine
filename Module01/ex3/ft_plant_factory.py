class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow_higher(self, cm: int) -> None:
        self.height = self.height + cm

    def grow_older(self, days: int) -> None:
        self.age = self.age + days

    def grow_a_week(self) -> None:
        self.grow_higher(6)
        self.grow_older(6)

    def get_info(self) -> str:
        info = f"""=== Day 1 ===
        {self.name}: {self.height}cm, {self.age} days old\n"""
        self.grow_a_week()
        info = info + f"""=== Day 7 ===
        {self.name}: {self.height}cm, {self.age} days old
        Growth this week: +6cm"""
        return info

    def __str__(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)

    plants = [p1, p2, p3, p4, p5]
    
    i = 0

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant}")
        i += 1
    print()
    print(f"Total plants created: {i}")
