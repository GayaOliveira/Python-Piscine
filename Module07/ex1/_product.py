from abc import ABC, abstractmethod
from ex0._product import Creature


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):

    def __init__(self):
        super().__init__()
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if not self.transformed:
            return f"{self.name} attacks normally."
        return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} attacks normally."
        return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."
