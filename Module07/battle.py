import ex0

if __name__ == "__main__":

    print("Testing factory\n")

    flame_factory = ex0.FlameFactory()

    flameling = flame_factory.create_base()
    print(flameling.describe())
    print(flameling.attack())

    pyrodon = flame_factory.create_evolved()
    print(pyrodon.describe())
    print(pyrodon.attack())
    print()

    aqua_factory = ex0.AquaFactory()

    aquabub = aqua_factory.create_base()
    print(aquabub.describe())
    print(aquabub.attack())

    torragon = aqua_factory.create_evolved()
    print(torragon.describe())
    print(torragon.attack())
    print()

    print("Testing battle\n")
    print(flameling.describe())
    print(" vs.")
    print(aquabub.describe())
    print(" fight!")
    print(flameling.attack())
    print(aquabub.attack())
