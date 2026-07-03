import random

ALL_ACHIEVEMENTS = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    num_achievements = random.randint(5, 9)

    player_list = random.sample(ALL_ACHIEVEMENTS, num_achievements)
    return set(player_list)


def main():
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_sets = list(players.values())
    all_distinct = set.union(*all_sets)
    print(f"All distinct achievements: {all_distinct}")

    common_achievements = set.intersection(*all_sets)
    print(f"Common achievements: {common_achievements}")

    for name, current_set in players.items():
        others_combined = set().union(
            *[s for s in all_sets if s is not current_set]
        )
        unique_to_player = current_set.difference(others_combined)
        print(f"Only {name} has: {unique_to_player}")

    full_catalog = set(ALL_ACHIEVEMENTS)
    for name, current_set in players.items():
        missing_achievements = full_catalog.difference(current_set)
        print(f"{name} is missing: {missing_achievements}")


if __name__ == "__main__":
    main()
