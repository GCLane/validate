#validate program that validates a persons credentials
#Author: Grant Lane
#Date: 2-17-22
import sys

#validates the ID of the person
def validateID(id):
    isValid = len(id) == 6
    if(isValid):
        counter = 0
        while counter < len(id):
            if(counter <=2):
                isValid = id[counter] >= '0' and id[counter] <= '9'
            else:
                isValid = id[counter] >= 'A' and id[counter] <= 'Z'
            counter += 1
    return isValid

#Checks if the name of the person is valid
def validateName(word):
    name_list = word.split(" ")
    isName = False
    check_suffix = False
    for name in name_list:
        isName = False
        counter = 0
        while counter < len(name) and isLetter(name[counter]):
            counter += 1
        if(counter == len(name)):
            isName = True
        elif(counter == (len(name) - 1) and name[-1] == ',' and name == name_list[-2]):
            isName = True
            check_suffix = True
        elif(check_suffix):
            isName = isSuffix(name)
            check_suffix = False
        if(isName == False):
            return isName
    return isName

    
#quick helper method for validate name to check if a letter is actually a letter
def isLetter(letter):
    if(letter <= 'Z' and letter >= "A"):
        return True
    elif(letter <= 'z' and letter >= 'a'):
        return True
    else:
        return False
#helper method for checking suffixes on names to see if they are valid
def isSuffix(word):
    isValid = False
    for char in word: isValid = char == "V" or char == "I"
    if(word == "Jr." or word == "Sr."):
        isValid = True
    return isValid

#method for checking if the zipcode is valid
def validateZip(code):
    isValid = len(code) == 5 or len(code) == 10
    if(isValid):
        if(len(code) == 5):
            for i in code: 
                isValid = i >= '0' and i <= '9'
                if(not(isValid)):
                    return isValid
        else:
            for i in code:
                if(i != code[5]):
                    isValid = i >= '0' and i <= '9'
                else:
                    isValid = i == '-'
                if(not(isValid)):
                    return isValid
    return isValid

#simple method for checking if the number is positive
def validateItem(numStr):
    counter = 0 
    isValid = True
    while counter < len(numStr) and isValid:
        isValid = numStr[counter] >= "0" and numStr[counter] <= "9"):
        counter += 1

#method for checking for a valid amount of purchase
def validateAmt(amt):
    amt = amt[0:-1] #accounting for the "\n"
    isValid = amt[0] == '$' and amt[-3] == '.'
    if(isValid):
        amt = amt[1:len(amt)]
    isValid = not(amt[0] == '.')
    if(isValid):
        counter = 0
        while counter < len(amt) and isValid:
            isValid = False
            if(amt[counter] >= '0' and amt[counter] <= '9' or amt[counter] == amt[-3]):
                isValid = True
            counter += 1
    return isValid


infile_name = sys.argv[1]
outfile_name = sys.argv[2]

infile = open(infile_name, 'r')
the_file = infile.readlines()
infile.close()
line_num = 1
the_string = ''
for line in the_file: 
    line = line.split('\t')
    for item in line:
        if(item == line[0] and not(validateID(item))):
            the_string += "Error in ID field of record" + str(line_num) + ": " + item + "\n"
        elif(item == line[1] and not(validateName(item))):
            the_string += "Error in Name field of record" + str(line_num) + ": " + item + "\n"
        elif(item == line[2] and not(validateZip(item))):
            the_string += "Error in Zip code field of record" + str(line_num) + ": " + item + "\n"
        elif(item == line[3] and not(validateItem(item))):
            the_string += "Error in Number purchased field of record" + str(line_num) + ": " + item + "\n"
        elif(item == line[4] and not(validateAmt(item))):
            the_string += "Error in Purchase amount field of record" + str(line_num) + ": " + item + "\n"
    line_num += 1


outfile = open(outfile_name, "w")
outfile.write(the_string)
outfile.close()





