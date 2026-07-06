import random


def main() -> None:
    initial_list = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_list}")

    all_caps = [name.capitalize() for name in initial_list]
    print(f"New list with all names capitalized: {all_caps}")

    only_caps = [name for name in initial_list if name.istitle()]
    print(f"New list of capitalized names only: {only_caps}")

    score_dict = {name: random.randint(0, 1000) for name in all_caps}
    print(f"Score dict: {score_dict}")

    score_average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {score_average}")

    high_score_dict = {
        name: score
        for name, score in score_dict.items()
        if score > score_average
    }
    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    main()
