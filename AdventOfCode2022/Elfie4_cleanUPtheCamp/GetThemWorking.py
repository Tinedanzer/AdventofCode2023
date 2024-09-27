from get_input import get_input

input_data = get_input("input.txt")

how_bad_is_the_overseer = 0

for duties in input_data:
    range1, range2 = duties.split(",")
    starting_area_elf1, ending_area_elf1 = range1.split("-")
    starting_area_elf2, ending_area_elf2 = range2.split("-")
    # making them all ints.
    starting_area_elf1,ending_area_elf1, starting_area_elf2, ending_area_elf2 = int(starting_area_elf1), int(ending_area_elf1), int(starting_area_elf2), int(ending_area_elf2)

# commenting part 1 out, so part 2 can be performed. Alternatively i could break this into functions

    # counting how many elves have completely overlapping cleaning duties
    # if starting_area_elf1 >= starting_area_elf2 and ending_area_elf1 <= ending_area_elf2 or starting_area_elf2 >= starting_area_elf1 and ending_area_elf2 <= ending_area_elf1:
    #     how_bad_is_the_overseer += 1
    
# received correct answer of 595

# part 2, count how many things overlap at all
    if starting_area_elf2 <= starting_area_elf1 <= ending_area_elf2:
        how_bad_is_the_overseer += 1
        continue
    elif starting_area_elf1 <= starting_area_elf2 <= ending_area_elf1:
        how_bad_is_the_overseer += 1
# received correct answer of 952

print(how_bad_is_the_overseer)