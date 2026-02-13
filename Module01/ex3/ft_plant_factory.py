class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


plants = []

p1 = Plant("Rose", 25, 30)
p2 = Plant("Oak", 200, 365)
p3 = Plant("Cactus", 5, 90)
p4 = Plant("Sunflower", 80, 45)
p5 = Plant("Fern", 15, 120)

plants.append(p1)
plants.append(p2)
plants.append(p3)
plants.append(p4)
plants.append(p5)

print("=== Plant Factory Output ===")
for i in range (0, len(plants)):
    print(f"Created: {plants[i]}")
print("")
print(f"Total plants created: {len(plants)}")
