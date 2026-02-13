class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"
    

plants = []

p1 = Plant("Rose", 25, 30)
p2 = Plant("Sunflower", 80, 45)
p3 = Plant("Cactus", 15, 120)

plants.append(p1)
plants.append(p2)
plants.append(p3)

for i in range (0, 3):
    print(plants[i])
