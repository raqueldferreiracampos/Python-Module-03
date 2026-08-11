import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    new_cap_players = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {new_cap_players}")
    cap_players = [player for player in players if player[0].isupper()]
    print(f"New list of capitalized names only: {cap_players}")


if __name__ == "__main__":
    main()