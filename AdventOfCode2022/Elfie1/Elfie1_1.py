from input import calories

most_food_elf = 0
second_elf = 0
third_elf = 0

temporary_elf_total_food = 0

for elf in calories:
    for food in elf:
        temporary_elf_total_food += food
    if temporary_elf_total_food >= most_food_elf:
        third_elf = second_elf
        second_elf = most_food_elf
        most_food_elf = temporary_elf_total_food
    temporary_elf_total_food = 0

all_three = most_food_elf + second_elf + third_elf

print(most_food_elf)
print(second_elf)
print(third_elf)
print(all_three)