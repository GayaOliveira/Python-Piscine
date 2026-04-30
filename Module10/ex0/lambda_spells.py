
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda item: item["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"*{spell}*", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        raise ValueError("Mage list cannot be empty")
    stats: dict = {}
    most_powerful = max(mages, key=lambda item: item["power"])
    stats["max_power"] = most_powerful["power"]
    least_powerful = min(mages, key=lambda item: item["power"])
    stats["min_power"] = least_powerful["power"]
    average = round(sum(item["power"] for item in mages)/len(mages), 2)
    stats["avg_power"] = average
    return stats


def main() -> None:

    try:
        artifacts = [
            {'name': 'Storm Crown', 'power': 82, 'type': 'armor'},
            {'name': 'Akasha Grimoire', 'power': 87, 'type': 'relic'},
            {'name': 'Earth Shield', 'power': 67, 'type': 'weapon'},
            {'name': 'Wind Cloak', 'power': 86, 'type': 'accessory'}
        ]
    except Exception:
        print("Invalid artifact list")

    try:
        mages = [
            {'name': 'Riley', 'power': 71, 'element': 'shadow'},
            {'name': 'Kai', 'power': 57, 'element': 'shadow'},
            {'name': 'Ember', 'power': 68, 'element': 'wind'},
            {'name': 'River', 'power': 92, 'element': 'fire'},
            {'name': 'Jordan', 'power': 86, 'element': 'fire'}
        ]
    except Exception:
        print("Invalid mage list")

    try:
        spells = ['lightning', 'tsunami', 'fireball', 'darkness']
    except Exception:
        print("Invalid spell list")

    print("\nTESTING ARTIFACT SORTER...")

    try:
        result = artifact_sorter(artifacts)
        print("\nBefore:")
        print(artifacts)
        print("\nAfter:")
        print(result)
    except Exception:
        print("Invalid artifact list")

    print("\nTESTING MAGE FILTER...")

    try:
        print("\nBefore:")
        print(mages)
        print("\nAfter:")
        print(power_filter(mages, 70))
    except Exception:
        print("Invalid mage list")

    print("\nTESTING SPELL TRANSFORMER...")

    try:
        print("\nBefore:")
        print(spells)
        print("\nAfter:")
        print(spell_transformer(spells))
    except Exception:
        print("Invalid spell list")

    print("\nTESTING MAGE STAT CALCULATOR...")

    try:
        print("\nMage list:")
        for mage in mages:
            print(f"Name: {mage["name"]} - Power: {mage["power"]}")
        print("\nStatistics:")
        stats = mage_stats(mages)
        print(f"Most powerful mage's power level: {stats["max_power"]}")
        print(f"Least powerful mage's power level: {stats["min_power"]}")
        print(f"Average mages's power level: {stats["avg_power"]}")
    except Exception:
        print("Invalid mage list")


if __name__ == "__main__":
    main()
