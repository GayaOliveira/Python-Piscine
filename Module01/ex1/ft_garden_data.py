class Plant:
    def __init__(self):
        self.name = ""
        self.height = 0
        self.age = 0
    

plants = []

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

plants.append(p1)
plants.append(p2)
plants.append(p3)

for i in range (0, len(plants)):
    print(f"{plants[i].name}: {plants[i].height}cm, {plants[i].age} days old")
