from typing import Generator
import time


def generate_streaming_data(
        quantity: int
        ) -> Generator[dict[str, str | int], None, None]:
    player_names = ["Alice", "Bob", "Grace", "Liam"]
    possible_actions = [
        "leveled up", "killed monster", "found treasure",
        "leveled up", "killed monster",
        "died", "completed quest"
        ]
    for i in range(quantity):
        name = player_names[i % 4]
        action = possible_actions[i % 7]
        level = (i % 15) + 1
        yield {
            "name": name,
            "action": action,
            "level": level
        }


def fibonacci_sequence() -> Generator[int, None, None]:
    x = 0
    y = 1
    temp = 0
    while True:
        yield x
        temp = x
        x = y
        y = temp + y


def is_prime(num: int) -> bool:
    factor = 2
    while factor < num:
        if num % factor == 0:
            return False
        factor += 1
    return True


def prime_sequence() -> Generator[int, None, None]:
    prime = 2
    while True:
        if (is_prime(prime)):
            yield prime
        prime += 1


def demonstrate_memory_use() -> Generator[int, None, None]:
    nbr = 0
    for i in range(5):
        nbr += 1
        yield nbr


if __name__ == "__main__":

    print("=== Game Data Stream Processor ===\n")

    num_events = 10000
    print(f"Processing {num_events} game events...\n")
    events = iter(generate_streaming_data(num_events))
    for i in range(5):
        event = next(events)
        print(f"Event {i + 1}: "
              f"Player {event['name']} "
              f"(level {event['level']}) "
              f"{event['action']} "
              )
    print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {num_events}")
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    events = generate_streaming_data(num_events)
    start_time = time.time()
    for _ in range(num_events):
        event = next(events)
        if event["level"] >= 10:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1
    end_time = time.time()
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    num = 10
    fibo_seq = fibonacci_sequence()
    print(f"Fibonacci sequence (first {num}): ", end="")
    for _ in range(num):
        print(f"{next(fibo_seq)}", end=" ")
    num = 5
    prime_seq = prime_sequence()
    print(f"\nPrime numb (first {num}): ", end="")
    for _ in range(num):
        print(f"{next(prime_seq)}", end=" ")

    print("\n")
    print("=== Demonstrating Generators don't store all data in memory ===")

    demo1 = demonstrate_memory_use()
    print(list(demo1))
    demo2 = demonstrate_memory_use()
    next(demo2)
    next(demo2)
    next(demo2)
    print(list(demo2))
