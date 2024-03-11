#!/usr/bin/python3
"""
Prime Game module
"""


def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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

    def count_primes(n):
        return sum(1 for i in range(1, n + 1) if is_prime(i))

    def play_round(n):
        for i in range(n, 1, -1):
            if is_prime(i):
                return i

    ben_wins = 0
    for n in nums:
        prime = play_round(n)
        if prime:
            ben_wins += 1

    if ben_wins > x // 2:
        return "Ben"
    elif ben_wins < x // 2:
        return "Maria"
    else:
        return None


if __name__ == "__main__":
    print(isWinner(3, [4, 5, 1]))
    print(isWinner(5, [2, 5, 1, 4, 3]))
