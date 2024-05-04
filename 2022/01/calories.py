'''
https://adventofcode.com/2022/day/1
'''

class elf:
	party = []

	def __new__(cls) -> Self:
		pass

	def __init__(self) -> None:
		pass

with open('example.txt', 'r') as f:
	for i in f.readlines():
		if i == "\n":
			print("skip")
		else:
			print(i)