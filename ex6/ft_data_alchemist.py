import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()

    players = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]

    new_cap_players = [player.capitalize() for player in players]
    cap_players = [player for player in players if player[0].isupper()]

    score_dict = {
        player: random.randint(0, 1000)
        for player in new_cap_players
    }

    average = sum(score_dict.values()) / len(score_dict)

    high_scores = {
        player: score
        for player, score in score_dict.items()
        if score > average
    }

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {new_cap_players}")
    print(f"New list of capitalized names only: {cap_players}")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {average:.2f}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
