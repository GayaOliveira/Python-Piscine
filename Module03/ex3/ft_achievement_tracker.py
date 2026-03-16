if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = set([
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon'
    ])
    bob = set([
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector'
    ])
    charlie = set([
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    ])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    union = alice.union(bob, charlie)
    print(f"All unique achievements: {union}")
    print(f"Total unique achievements: {len(union)}\n")

    intersection = alice.intersection(bob, charlie)
    print(f"Common to all players: {intersection}")

    alice_only = alice.difference(bob, charlie)
    bob_only = bob.difference(alice, charlie)
    charlie_only = charlie.difference(alice, bob)
    difference = alice_only.union(bob_only, charlie_only)
    print(f"Rare achievements (1 player): {difference}\n")

    alice_n_bob = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_n_bob}")
    alice_without_bob = alice.difference(bob)
    print(f"Alice unique: {alice_without_bob}")
    bob_without_alice = bob.difference(alice)
    print(f"Bob unique: {bob_without_alice}")
