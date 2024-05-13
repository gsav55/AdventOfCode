"""
https://adventofcode.com/2022/day/3
"""

EXAMPLE = "2022\\03\\example.txt"
INPUT = "2022\\03\\input.txt"
ALPHABET = "2022\\03\\alph.txt"
FILE = INPUT


def get_alfa() -> list[str]:
    alfa = []
    with open(ALPHABET, "r") as f:
        for letter in f.readlines():
            alfa.append(letter.replace("\n", ""))
    return alfa


alfa = get_alfa()
value = 0
with open(FILE, "r") as f:
    for sack in f.readlines():
        print(sack)
        num_items = len(sack)
        compartment1 = sack[0 : int(num_items / 2)]
        compartment2 = sack[int(num_items / 2) : num_items]
        print(compartment1)
        print(compartment2)
        for item in compartment1:
            if item in compartment2:
                print(item)
                print(alfa.index(item) + 1)
                value += alfa.index(item) + 1
                break

print(f"Final Score: {value}")
