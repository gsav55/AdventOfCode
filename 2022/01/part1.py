'''
https://adventofcode.com/2022/day/1
'''

party = []
elf = []

with open('2022/01/input.txt', 'r') as f:
	for line in f.readlines():
		if not line == "\n":
			elf.append(int(line.replace("\n", "")))
		else:
			party.append(elf)
			elf = []
	party.append(elf)
		

#print(party)

fat_elf: int = 0
fat_pack: int = 0
party_total: int = 0

for i, elf in enumerate(party):
	holding = sum(elf)
	party_total += holding
	if holding > fat_pack:
		fat_elf = i
		fat_pack = sum(elf)

print(f"Party has {party_total} calories between {len(party)} elfs.  Elf {fat_elf +1} has the most with {fat_pack} calories.")