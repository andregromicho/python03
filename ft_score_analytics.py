import sys


def ft_score_analytics() -> None:
    arguments = sys.argv[1:]

    if not arguments:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    valid_scores: list[int] = []
    for arg in arguments:
        try:
            score = int(arg)
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not valid_scores:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    total_players = len(valid_scores)
    total_score = sum(valid_scores)
    average_score = total_score / total_players
    high_score = max(valid_scores)
    low_score = min(valid_scores)
    range_score = high_score - low_score

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {range_score}")


if __name__ == "__main__":
    ft_score_analytics()
