from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy
)
from typing import List, Tuple


def battle(
        battle_list: List[Tuple[CreatureFactory, BattleStrategy]]
        ) -> None:

    combat_list = []

    for creature_factory, bat_str in battle_list:
        creature = creature_factory.create_base()
        combat_list.append((creature, bat_str))

    combat_set = set()

    for adversary1 in combat_list:
        for adversary2 in combat_list:
            combat_set.add({adversary1, adversary2})


    # [(flame_factory, normal_strategy), (healing_factory, defensive_strategy)]
    # [(flameling, normal_strategy), (sprouting, defensive_strategy)]

    print("* Battle *")
    print(creature.describe())
    print(" vs.")
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
    print(f"{len(battle_list0)} opponents involved")
    battle(battle_list0)
