from collections.abc import Callable
from functools import wraps
import time
# from operator import add, mul
# from typing import Any


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


def main() -> None:

    print("\nTESTING SPELL TIMER...\n")
    test_function()
    print()


if __name__ == "__main__":
    main()
