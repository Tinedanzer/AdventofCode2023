import re
from get_input import get_input
input_data = get_input("input.txt")


# this problem requires you to sometimes double count the storage amount. Which directories have under 100,000
# space? Add those directories and give us the total. Sometimes a child of a directory will get double counted.

# isnumeric()
# isalpha()
dict_directories = {}
directories = []
activated = 0
index_of_directories = 0
child = 0
child2 = 0
child3 = 0
child4 = 0
total = 0
temptotal = 0
temptotal2 = 0
temptotal3 = 0
temptotal4 = 0
noGood = False
# print(input_data)
for line in input_data:
    # print(line[0:4])
    # need to remove cd .. from the next line and add a reaction for when it is called. update: removed it.
    if line == "$ ls" or "dir " in line or line == '$ cd /':
        continue
# essentially starting the program once we receive the first legit change directory command.
# i do not want to count cd / as a command.
    # is_activated(line)
    if activated == 0:
        if "$ cd" == line[0:4]:
            activated = 1
        else:
            # print(line)
            continue
# lets start over:
# can move the 2nd part of the 'if' statement to later... keeping it here now while deving.
    if "cd" in line and line != "$ cd ..":
        dict_directories[line[5:]] = {line[5:]}
        index_of_directories += 1
        continue

    if "cd .." in line:
# step logic needs to be inspected here.
        if index_of_directories == 1:
            if temptotal <= 100000:
                total += temptotal
                temptotal = 0
        if index_of_directories == 2:
            if temptotal2 <= 100000:
                total += temptotal2 + temptotal
                total += temptotal2
        if index_of_directories == 3:
            if temptotal3 + temptotal4 <= 100000:
                total += temptotal3 + temptotal4
                temptotal4 = 0
        if index_of_directories == 4:
            if temptotal4 <= 100000:
                total += temptotal4
        #         if temptotal4 + temptotal3 <= 100000:
        #             total += temptotal4 + temptotal3
        #             if temptotal4 + temptotal3 + temptotal2 <= 100000:
        #                 total += temptotal4 + temptotal3 + temptotal2
        #                 if temptotal4 + temptotal3 + temptotal2 + temptotal <= 100000:
        #                     total += temptotal4 + temptotal3 + temptotal2 + temptotal
        index_of_directories -= 1
        noGood = False
        continue

# checks to see if the first character is an integer(this is how we know this line is a file size)
    if line[0].isdigit():
        # if noGood == True:
        if noGood:
            continue

        getDigits = [int(n) for n in line.split(" ") if n.isdigit()]
        # if index_of_directories == 0:
        #     continue
        if index_of_directories == 1:
            temptotal += getDigits[0]
            if temptotal >= 100000:
                noGood = True

        elif index_of_directories == 2:
            temptotal2 += getDigits[0]
            if temptotal + temptotal2 >= 100000:
                noGood = True
                continue
                
        elif index_of_directories == 3:
            temptotal3 += getDigits[0]
        elif index_of_directories == 4: 
            temptotal4 += getDigits[0]
        # aroo3 = print(nums_from_string.get_nums(line))
        # print(int(line[0]))
        # print(getDigits[0])

dict_directories["bqm"] = 20
# print(directories)
# print(dict_directories.values())
# print(next(iter(dict_directories)))
# print(dict_directories)
# print(index_of_directories)
print(temptotal)
# print(temptotal2)
# print(temptotal3)
# print(temptotal4)
print(total) 
