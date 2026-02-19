class Plant:
    def __init__(self) -> None:
        self.name = ""
        self.height = 0
        self.age = 0
    

if __name__ == "__main__":
    p1 = Plant()
    p1.name = "Rose"
    p1.height = 25
    p1.age = 30
    p2 = Plant()
    p2.name = "Sunflower"
    p2.height = 80
    p2.age = 45
    p3 = Plant()
    p3.name = "Cactus"
    p3.height = 15
    p3.age = 120

    plants = [p1, p2, p3]

    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
