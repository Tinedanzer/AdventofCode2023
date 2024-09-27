from input import i_Refuse_To_Fold_My_Laundry

values = 0

def half_it_up(putItInHere):
    string1, string2 = putItInHere[:len(putItInHere)//2], putItInHere[len(putItInHere)//2:]
    # search and compare both sides of the string for 1 common character.
    for item in string1:
        if item in string2:
             # using ascii to convert to something more manageable
            #  convert_to_ascii(item)
            if item == item.lower():
                return ord(item)-96
            else:
                return ord(item)-38

# looping and adding modified ascii number values to the variable 'values'
commonItem = 0
temp1 = ""
temp2 = ""
temp3 = ""
counter = 0

def step2(findTheSameItem):
    # print(findTheSameItem)
    counter = 0
    if counter == 0:
        temp1 = set(findTheSameItem)
        counter = 1
    if counter == 1:
        temp2 = set(findTheSameItem)
        counter = 2
    if counter == 2: 
        temp3 = set(findTheSameItem)
        ultimate = temp1.intersection(temp2).intersection(temp3).pop()
        counter = 0
        if ultimate == ultimate.lower():
            return ord(ultimate)-96
        else:
            return ord(ultimate)-38
        # print(ultimate)


for inventory in i_Refuse_To_Fold_My_Laundry:
    values += half_it_up(inventory)
    commonItem += step2(inventory)

# here we need to group the first 3 lines together and find the common character and
# then output a number value to be added to a total.
    
# why didnt this work AK?

# def convert_to_ascii(item):
#     if item == item.lower():
#         return ord(item)-96
#     else:
#         return ord(item)-38

print(values)
print(commonItem)