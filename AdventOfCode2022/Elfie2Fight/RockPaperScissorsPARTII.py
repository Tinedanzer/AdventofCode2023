from input import cheat_sheet 

# Each thrown sign gets you different points,
# Opponent throws a,b, or c:
# rock(A) = 1 point
# Paper(B) = 2 points
# Scissors(C) = 3 points

# THE CHOSEN ELFIE:
# XYZ NOW designates what you should do, not what signal to throw. 
# X = you need to lose!  (in order to not be caught for cheating, smart immoral elfie)
# Y = DRAW! this round.
# Z = WIN IT, WIN IT ALL
total_points = 0

for list in cheat_sheet:
# handling the intentional losses
    if list[1] == 'X':
        total_points += 0 #losing getcha 0
        if list[0] == "A":
            total_points +=3
        if list[0] == "B":
            total_points +=1
        if list[0] == "C":
            total_points +=2

# handling ties
    if list[1] == 'Y':
        total_points += 3
        if list[0] == "A":
            total_points +=1
        if list[0] == "B":
            total_points +=2
        if list[0] == "C":
            total_points +=3

# handling the weiners
    if list[1] == 'Z':
        total_points += 6
        if list[0] == "A":
            total_points +=2
        if list[0] == "B":
            total_points +=3
        if list[0] == "C":
            total_points +=1

print(total_points)

#  is my answer for this game.