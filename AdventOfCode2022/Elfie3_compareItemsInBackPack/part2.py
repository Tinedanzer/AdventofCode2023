from input import i_Refuse_To_Fold_My_Laundry

commonItem = 0
temp1 = ""
temp2 = ""
temp3 = ""
counter = 0
for line in i_Refuse_To_Fold_My_Laundry:
    if counter == 0:
        temp1 = line
        # print(counter)
        counter += 1
        continue
    if counter == 1:
        temp2 = line
        counter += 1
        print(counter)
        continue
    if counter == 2: 
        temp3 = line
        ultimate = set(temp1).intersection(set((temp2))).intersection(set(temp3)).pop()
        counter = 0
        if ultimate == ultimate.lower():
            commonItem += ord(ultimate)-96
        else:
            commonItem += ord(ultimate)-38
        print(ultimate)

    # print(temp1,temp2,temp3)


print(commonItem)
# "DddBHCmfWCBTDBHTHfMpzhzpJJMJsFrGrz",
# "tPVPmbnttjPnZvSvSbnmZPZPNpNGMpJNzzNrGJpvhsshMpFs",
# "mwnZcbmmStbVtVjbZVlcLTBlcLCRHRDWCWWW