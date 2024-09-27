from get_input import get_input
input_data = get_input("input.txt")
# How many characters need to be processed before the first start-of-packet marker is detected?
# start of packet = the last of the index of the first 4 unique characters + 1.
def first_four():
    index = 0
    counter1 = input_data[0][0]
    counter2 = input_data[0][1]
    counter3 = input_data[0][2]
    counter4 = input_data[0][3]
    for list in input_data:
        for char in list:
            if index < 4:
                index += 1 
                continue
            if counter1 in counter2 or counter1 in counter3 or counter1 in counter4:
                counter1=counter2
                counter2=counter3
                counter3=counter4
                counter4 = char
                index += 1
                continue
            elif counter2 in counter3 or counter2 in counter4:
                counter1=counter2
                counter2=counter3
                counter3=counter4
                counter4 = char
                index += 1
                continue
            elif counter3 in counter4:
                counter1=counter2
                counter2=counter3
                counter3=counter4
                counter4 = char
                index += 1
                continue
            else:
                exit
    # print(counter1,counter2,counter3,counter4)
    print(index)
first_four()
# 1300 right answer part 1

# part 2, first 14 unique characters now, gonna do this a lil better this time.
def first_fourteen():
    index = 0
    current_sequence= []
    counter = 0
    for line in input_data:
        for x in range(len(line)):
            index += 1
            counter += 1
            if line[x] in current_sequence:
                current_sequence = []
                index = 0
            
            current_sequence.append(line[x])
            
            if index == 13:
                print(current_sequence)
                print(counter)
                return current_sequence

first_fourteen()
# correct answer is 3986 characters needed to be counted until we were able 
# to populate a unique list of 14.

# think about using sets next time - ak
# if youre using something like if list[x] in current_sequence: (checking for an item in a list), use sets.
# using sets is a lot better for checking if something is in something, as sets cannot have duplicates.