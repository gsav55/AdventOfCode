'''
https://adventofcode.com/2022/day/1
'''

party = []
elf = []

test = '2022/01/example.txt'
real = '2022/01/input.txt'

with open(real, 'r') as f:
	for line in f.readlines():
		if not line == "\n":
			elf.append(int(line.replace("\n", "")))
		else:
			party.append(elf)
			elf = []
	party.append(elf)
		

#print(party)

fat_elf: list[int] = [0,0,0]
fat_pack: list[int] = [0,0,0]
party_total: int = 0

for i, load in enumerate(party):
	party[i] = sum(load)
party.sort(reverse=True)

#print(party)

t3 = 0
for i in range(0,3):
	print(i)
	t3 += party[i]


print(f"Top 3 total = {t3}")