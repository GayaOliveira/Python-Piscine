from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy
)
from typing import List, Tuple


def create_combat_list(
        raw_list: List[Tuple[CreatureFactory, BattleStrategy]]
) -> List[Tuple]:

    battle_list = []

    for creature_factory, bat_str in raw_list:
        creature = creature_factory.create_base()
        battle_list.append((creature, bat_str))

    combat_list: List[Tuple] = []

    for adversary1 in battle_list:
        for adversary2 in battle_list:
            if (
                    adversary1 is not adversary2
                    and (adversary2, adversary1) not in combat_list
            ):
                combat_list.append((adversary1, adversary2))

    return combat_list


def battle(
        raw_list: List[Tuple[CreatureFactory, BattleStrategy]]
        ) -> None:

    combat_list: List[Tuple] = create_combat_list(raw_list)

    for pair1, pair2 in combat_list:
        print("* Battle *")
        adversary1 = pair1[0]
        strategy1 = pair1[1]
        adversary2 = pair2[0]
        strategy2 = pair2[1]
        print(adversary1.describe())
        print(" vs.")
        print(adversary2.describe())
        print(" now fight!")
        try:
            strategy1.act(adversary1)
            strategy2.act(adversary2)
        except Exception as err:
            print(err)
        finally:
            print()


if __name__ == "__main__":

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    agressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    battle_list0 = [
            (flame_factory, normal_strategy),
            (healing_factory, defensive_strategy)
        ]
    print(f"{len(battle_list0)} opponents involved\n")
    battle(battle_list0)

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    battle_list1 = [
            (flame_factory, agressive_strategy),
            (healing_factory, defensive_strategy)
        ]
    print(f"{len(battle_list1)} opponents involved\n")
    battle(battle_list1)

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    battle_list2 = [
            (aqua_factory, normal_strategy),
            (healing_factory, defensive_strategy),
            (transform_factory, agressive_strategy)
        ]
    print(f"{len(battle_list2)} opponents involved\n")
    battle(battle_list2)
