from input import cheat_sheet 

# Opponent:
# rock(A) = 1 point
# Paper(B) = 2 points
# Scissors(C) = 3 points

# THE CHOSEN ELFIE:
# Rock(X) = 1 point
# Paper(Y) = 2 points
# Scissors(Z) = 3 points

total_points = 0

for list in cheat_sheet:
# these first three If statements give us points for throwing certain signs regardless of winner. 3 for scissors, 2 for paper, 1 for rock. 
    if list[1] == 'X':
        total_points += 1
    if list[1] == 'Y':
        total_points += 2
    if list[1] == 'Z':
        total_points += 3

# begins the comparing, 6 points for winning, 3 for tie, 0 for losing
# handling the ties.
    if list[0] == "A" and list[1] == "X":
        total_points += 3
    if list[0] == "B" and list[1] == "Y":
        total_points += 3
    if list[0] == "C" and list[1] == "Z":
        total_points += 3

# handling the winning.
    if list[0] == "A" and list[1] == "Y":
        total_points += 6
    if list[0] == "B" and list[1] == "Z":
        total_points += 6
    if list[0] == "C" and list[1] == "X":
        total_points += 6

print(total_points)

# 8890 is my answer for this game.