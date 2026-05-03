from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


@spell_timer
def test_function():
    time.sleep(1)


def power_validator(min_power: int) -> Callable:
    def validator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[-1]

            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper
    return validator


@power_validator(80)
def earthquake(power: int) -> str:
    return f"Earthquake unleashed with power {power}!"


def retry_spell(max_attempts: int) -> Callable:
    def retry(func: Callable) -> Callable:

        @wraps(func)
        def wrapper() -> str:
            for i in range(max_attempts):
                try:
                    return func()
                except Exception:
                    if i < max_attempts - 1:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {i + 1}/{max_attempts})"
                        )
            return (
                f"Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper
    return retry


@retry_spell(3)
def heal() -> str:
    raise Exception()


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        for char in name:
            if not (char.isalpha() or char.isspace()):
                return False

        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    print("\nTESTING SPELL TIMER...\n")
    test_function()
    print()

    try:
        print("\nTESTING POWER VALIDATOR...\n")
        print(f"Valid: {earthquake(80)}")
        print(f"Invalid: {earthquake(70)}")
    except TypeError as err:
        print(err)

    print("\nTESTING RETRYING SPELL\n...")
    print(heal())
    print("Waaaaaaagh spelled !")

    print("\nTESTING MAGEGUILD...")
    print(MageGuild().validate_mage_name("Gandalf"))
    print(MageGuild().validate_mage_name("Saruman*"))
    print(MageGuild().cast_spell("Lightning", 15))
    print(MageGuild().cast_spell("Lightning", 8))


if __name__ == "__main__":
    main()
