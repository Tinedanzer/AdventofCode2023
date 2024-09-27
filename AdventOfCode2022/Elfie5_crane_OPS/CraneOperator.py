from get_input import get_input
input_data = get_input("input.txt")

dangitIneedaDict= dict()

formatted_input_data = []

line_counter = 0

# reformatting crane move data
for line in input_data:
    formatted_input_data.append(line.replace("move ", "").replace(" from ",",").replace(" to ", ","))
# checking the first 20 lines for shipping containers, making this 'for' loop a constant.
    if line_counter < 20:
        line_counter += 1
        for index in range(len(line)):
# checks for an open bracket, which denotes that the next index will be a shipping container
# we then take index+1(shipping container's index) and place it within a list within its appropriate key(index)
            if line[index] == "[":
                dangitIneedaDict.setdefault(index+1, [])
                dangitIneedaDict[index+1].append(line[index+1])
                # print(index+1)
#fake indices, making them normalized 1   5   9   13  17  21  25  29  33
dangitIneedaDict[2] = dangitIneedaDict.pop(5)
dangitIneedaDict[3] = dangitIneedaDict.pop(9)
dangitIneedaDict[4] = dangitIneedaDict.pop(13)
dangitIneedaDict[5] = dangitIneedaDict.pop(17)
dangitIneedaDict[6] = dangitIneedaDict.pop(21)
dangitIneedaDict[7] = dangitIneedaDict.pop(25)
dangitIneedaDict[8] = dangitIneedaDict.pop(29)
dangitIneedaDict[9] = dangitIneedaDict.pop(33)

# reformatting data to remove containers and retaining only the instructions.
def dict1():
        for line2 in formatted_input_data:
            if " " in line2 or not line2:
                continue
            else:
                # no_boxes_formatted_input_data.append(line2) 
                amount,start,end = line2.split(',')
                amount = int(amount)
                start  = int(start)
                end    = int(end)
                # print(max(range(amount))+1)
                for iterations in range(amount):
                    # taking the first item of a key value(start) and adding it to the first value of
                    # the designated key value(end)
                    # print(iterations)
                    temp = dangitIneedaDict[start].pop(0)
                    dangitIneedaDict[end].insert(0,temp)
            # temp2 += dangitIneedaDict_part2[start].pop(0)

# uncomment below to run part 1.
# dict1()

#            [Q]     [G]     [M]    
#            [B] [S] [V]     [P] [R]
#    [T]     [C] [F] [L]     [V] [N]
#[Q] [P]     [H] [N] [S]     [W] [C]
#[F] [G] [B] [J] [B] [N]     [Z] [L]
#[L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
#[S] [Z] [M] [G] [H] [C] [C] [H] [Z]
#[R] [N] [S] [T] [P] [P] [W] [Q] [G]
# 1   2   3   4   5   6   7   8   9 
# print(formatted_input_data)
# print(no_boxes_formatted_input_data)
# print(no_boxes_reformatted2)
# print(dangitIneedaDict)
# print(line_counter)
# print(amount)
# 1   5   9   13  17  21  25  29  33

# RIGHT ANSWER - part 1:
# FZCMJCRHZ
# output:
# {1: ['F', 'G', 'N', 'M', 'P', 'W', 'V', 'R'], 
# 2: ['Z', 'Q', 'Z', 'G', 'B', 'S', 'S', 'P', 'L', 'L', 'Q', 'C', 'M', 'N', 'S', 'B', 'Q'], 
# 3: ['C', 'B', 'F', 'N', 'T', 'Q', 'Q'], 
# 4: ['M'], 
# 5: ['J'], 
# 6: ['C', 'F', 'D', 'Z'], 
# 7: ['R', 'P', 'P', 'T', 'H', 'G', 'G', 'V', 'C', 'S', 'H', 'W', 'Q', 'G', 'L'], 
# 8: ['H', 'N'], 
# 9: ['Z']}

# part 2..... this crane now picks up all crates at once, instead of moving them one by one
def dict2():
        for line2 in formatted_input_data:
            if " " in line2 or not line2:
                continue
            else:
                # no_boxes_formatted_input_data.append(line2) 
                amount,start,end = line2.split(',')
                amount = int(amount)
                start  = int(start)
                end    = int(end)
                # print(max(range(amount))+1)
                temp2 = []
                for iterations in range(amount):
                    # taking the first item of a key value(start), storing it in a temp variable
                    # and adding all of temp (from the end of the array first) to
                    # the designated key value(end) after temp has been fully populated.
                    temp2 += dangitIneedaDict[start].pop(0)
                for iterations in range(amount):
                    dangitIneedaDict[end].insert(0,temp2.pop())
dict2()
print(dangitIneedaDict)
# PART 2 ANSWER:
# JSDHQMZG
# {1: ['J', 'P', 'L', 'F', 'C', 'M', 'Q', 'G'], 
# 2: ['S', 'R', 'C', 'N', 'G', 'N', 'B', 'H', 'H', 'B', 'V', 'Q', 'T', 'W', 'V', 'Z', 'N'], 
# 3: ['D', 'P', 'G', 'Q', 'G', 'R', 'P'], 
# 4: ['H'], 
# 5: ['Q'], 
# 6: ['M', 'C', 'F', 'T'], 
# 7: ['Z', 'L', 'Z', 'S', 'L', 'Q', 'B', 'S', 'C', 'M', 'P', 'S', 'Z', 'N', 'Q'], 
# 8: ['G', 'W'], 
# 9: ['F']}