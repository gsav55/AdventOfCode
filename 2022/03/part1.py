'''
https://adventofcode.com/2022/day/3
'''
EXAMPLE = "./example.txt"

FILE = EXAMPLE

with open(FILE, "r") as f:
    for sack in f.readlines():
        print(sack)
        num_items = len(sack)
        compartment1 = sack[0:int(num_items/2)]
        compartment2 = sack[int(num_items/2):num_items]
        print(compartment1)
        print(compartment2)
        for item in compartment1:
            if item in compartment2:

