import sys


def ft_score_analytics() -> list[int]:
    scores = []
    if len(sys.argv) == 1:
        print("No scores provided. ", end="")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        for i in range(1, len(sys.argv)):
            try:
                data = int(sys.argv[i])
                scores.append(data)
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
        if len(scores) == 0:
            print("No scores provided. ", end="")
            print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    return scores


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = ft_score_analytics()
    if len(scores) >= 1:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        return


if __name__ == "__main__":
    main()
