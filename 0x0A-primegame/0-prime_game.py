#!/usr/bin/python3
"""
Prime Game module
"""


def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determine winner of each round of prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing n for each round.

    Returns:
        str: Name of player that won most rounds.
             If winner cannot be determined, returns None.
    """
    if not nums or x <= 0:
        return None

    # Function to determine the winner of each round
    def play_round(n):
        largest_prime_factor = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0 and is_prime(i):
                largest_prime_factor = max(largest_prime_factor, i)
                quotient = n // i
                if is_prime(quotient):
                    largest_prime_factor = max(largest_prime_factor, quotient)
        return largest_prime_factor

    # Counting wins for each player
    ben_wins = sum(1 for n in nums if play_round(n) == 1)

    # Determining the winner based on the number of wins
    if ben_wins > x // 2:
        return "Ben"
    elif ben_wins < x // 2:
        return "Maria"
    else:
        return None


if __name__ == "__main__":
    print(isWinner(3, [4, 5, 1]))
    print(isWinner(5, [2, 5, 1, 4, 3]))
