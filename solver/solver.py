from typing import Callable


def solve(input: Callable[[], str], output: Callable[[str], None]) -> None:
    """
    Use "input" and "output" just like "input" and "print" functions:
    -> inp = input().strip().split()
    -> out: list[str] = run(inp)
    -> print(*out, sep=" ", end=" ")
    """
    ...


""" -------------------- EXAMPLE --------------------
    N = int(input().strip())

    for _ in range(N):
        ships = [int(x) for x in input().split()]
        res = run(ships)
        print(res)


def run(ships: list[int]) -> str:
    shipCount = [0, 4, 3, 2, 1]

    for ship in ships:
        shipCount[ship] -= 1

    for i in range(len(shipCount)):
        if shipCount[i] != 0:
            return "NO"

    return "YES"
"""
