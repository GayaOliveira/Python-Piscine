from ex1 import HealingCreatureFactory, TransformCreatureFactory

if __name__ == "__main__":

    print("Testing Creature with healing capability")

    healing_factory = HealingCreatureFactory()

    sproutling = healing_factory.create_base()
    print(" base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    bloomelle = healing_factory.create_evolved()
    print(" evolved:")
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())

    print("\nTesting Creature with transform capability")

    transform_factory = TransformCreatureFactory()

    shiftling = transform_factory.create_base()
    print(" base:")
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())

    torragon = transform_factory.create_evolved()
    print(" evolved:")
    print(torragon.describe())
    print(torragon.attack())
    print(torragon.transform())
    print(torragon.attack())
    print(torragon.revert())
