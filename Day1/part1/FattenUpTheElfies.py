# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") 
# and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") 
# when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) 
# has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration 
# value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit 
# and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?
import re
from get_input import get_input

# getting our data
input_data = get_input("input.txt")

def letTheFunBegin(input):
    number1 = ''
    counter = 0
    number2 = ''
    finalSum = 0
    for string in input:
        cleanedString = re.findall("\d", string)
        # print(cleanedString)
        for character in cleanedString:
           if counter == 1:
                number2= character
                if cleanedString[-1] == character:
                    finalSum += int(number1)*10 + int(number2)
                    print(int(number1)*10 + int(number2))
                    break
           if counter == 0 :
                number1=character
                # counter is used to move on to the 'digits' number
                counter += 1
                # checks to see if this is the only number in the string, and even checks if the last number is the same number. 2 for 1 !
                if cleanedString[-1] == character:
                    number2= character
                    finalSum += int(number1)*10 + int(number2)
                    print(int(number1)*10 + int(number2))
                    break
        # resetting the variables.
        number1 = ''
        counter= 0
        number2= ''

    print(finalSum)
    return(finalSum)
letTheFunBegin(input_data)