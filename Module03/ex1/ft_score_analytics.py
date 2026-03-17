import sys


def generate_number_list(args: list[str]) -> list[int]:
    numbers: list[int] = []
    for arg in args[1:]:
        try:
            num = int(arg)
            numbers.append(num)
        except ValueError:
            print("Invalid input: arguments must be integer numbers!")
            exit()
    return numbers


def calculate_score_analytics(nums: list[int]) -> None:
    total_players = len(nums)
    print(f"Total players: {total_players}")
    total_score = sum(nums)
    print(f"Total score: {total_score}")
    average = total_score / total_players
    print(f"Average score: {average:.1f}")
    high_score = max(nums)
    print(f"High score: {high_score}")
    low_score = min(nums)
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
    else:
        numbers = generate_number_list(sys.argv)
        print(f"Scores processed: {numbers}")
        calculate_score_analytics(numbers)
