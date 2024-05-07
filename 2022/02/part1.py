"""
Advent of Code Day 2
Part 1

https://adventofcode.com/2022/day/2

The score for a single round is the score for the shape you selected
(1 for Rock,
 2 for Paper, and
 3 for Scissors)
plus the score for the outcome of the round
(0 if you lost,
 3 if the round was a draw, and
 6 if you won).
----------------------
A = Rock
B = Paper
C = Scissors

X = Rock
Y = Paper
Z = Scissors
"""

EXAMPLE = "2022/02/example.txt"
INPUT = "2022/02/input.txt"
FILE = INPUT

score = 0
opponent_score = 0
ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
DRAW = 3
WIN = 6


# score += shape_val + win/lose/tie
def opponent_rock(my_throw):
    global score, opponent_score, ROCK, PAPER, SCISSORS, LOSE, DRAW, WIN
    match my_throw:
        case "X":
            score += ROCK + DRAW
            opponent_score += ROCK + DRAW
        case "Y":
            score += PAPER + WIN
            opponent_score += ROCK + LOSE
        case "Z":
            score += SCISSORS + LOSE
            opponent_score += ROCK + WIN


def oppenent_paper(my_throw):
    global score, opponent_score, ROCK, PAPER, SCISSORS, LOSE, DRAW, WIN
    match my_throw:
        case "X":
            score += ROCK + LOSE
            opponent_score += PAPER + WIN
        case "Y":
            score += PAPER + DRAW
            opponent_score += PAPER + DRAW
        case "Z":
            score += SCISSORS + WIN
            opponent_score += PAPER + LOSE


def opponent_scissors(my_throw):
    global score, opponent_score, ROCK, PAPER, SCISSORS, LOSE, DRAW, WIN
    match my_throw:
        case "X":
            score += ROCK + WIN
            opponent_score += SCISSORS + LOSE
        case "Y":
            score += PAPER + LOSE
            opponent_score += SCISSORS + WIN
        case "Z":
            score += SCISSORS + DRAW
            opponent_score += SCISSORS + DRAW


with open(FILE, "r") as f:
    for line in f.readlines():
        print(f"{line[0]} vs {line[2]}")
        match line[0]:
            case "A":
                opponent_rock(line[2])
            case "B":
                oppenent_paper(line[2])
            case "C":
                opponent_scissors(line[2])

print(f"My Score: {score : >10}")
print(f"Their Score: {opponent_score : >7}")
