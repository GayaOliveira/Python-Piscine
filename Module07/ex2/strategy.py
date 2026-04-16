from abc import ABC, abstractmethod
from ex0._product import Creature
from ex1._product import (
    TransformCapability,
    HealCapability,
    Shiftling,
    Sproutling,
    Bloomelle,
    Morphagon
)


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Shiftling | Morphagon) -> None:
        if not self.is_valid(creature):
            raise Exception(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.__class__.__name__}' "
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Sproutling | Bloomelle) -> None:
        if not self.is_valid(creature):
            raise Exception(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.__class__.__name__}' "
                "for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
