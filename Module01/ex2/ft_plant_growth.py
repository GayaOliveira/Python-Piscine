class Plant:
    def __init__(self):
        self.name = ""
        self.height = 0
        self.age = 0


    def grow_higher(self, cm):
        self.height = self.height + cm


    def grow_older(self, days):
        self.age = self.age + days


    def grow_a_week(self):
        self.grow_higher(6)
        self.grow_older(6)


    def get_info(self):
        info = f"""=== Day 1 ===
        {self.name}: {self.height}cm, {self.age} days old\n"""
        self.grow_a_week()
        info = info + f"""=== Day 7 ===
        {self.name}: {self.height}cm, {self.age} days old
        Growth this week: +6cm"""
        return info


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
    print(plants[i].get_info())
    print("\n")
