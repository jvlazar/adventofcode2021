# Day 3: Binary Diagnostic

# read the command prompt
import sys

 
# setup; manipulating the input file to a format that's easy to work with
# converting all text in the file to an array
def toArray(fileName):
    lines = fileName.read()
    lines = lines.split('\n')
    return lines

# converting the array with values in string format to int format (easy to compare later)
def toInt(stringListName,intListName):
    for i in stringListName:
        intListName.append(int(i))
    return intListName

# convert from binary to decimal
def toDecimal(number):
    decimal = 0
    pos = 0
    while (pos < len(number)):
       # print(pos)
        if (number[pos] == '1'):
            decimal = decimal + (2**(len(number) - pos - 1))
        pos += 1
    return decimal

# removes from list
def removeNumber(bit, list, pos):
    # cycle through list, remove the entries without the most common bit at the position
    position = 0
    isBit = True
    while (position < len(list)):
        listValue = list[position]

        if (listValue[pos] != bit):
           list.remove(listValue)
        else:  
            position += 1
        
        
    return list

# count how many leading 0s and 1s there are in each position
def getGamma(list):
    data = list
    gamma = ''
    
    pos = 0
    while (pos < len(data[0])):
        count0 = 0
        count1 = 0
        for str in data:      
            if str[pos] == '0':
                count0 += 1
            else: 
                count1 += 1     
        if (count0 > count1):
            gamma = gamma + '0'
            #print("The leading bit is 0 for position %d" %(pos))
            
        else:
            gamma = gamma + '1' 
            #print("The leading bit is 1 for position %d" %(pos))
        pos += 1
        #print("The gamma is %s" %(gamma))

    return (toDecimal(gamma), getEpsilon(gamma))


# get the epsilon rate 
def getEpsilon(gamma):
    pos = 0
    epsilon = ''
    while (pos < len(gamma)):
        if gamma[pos] == '0':
            epsilon = epsilon + '1'
        else:
            epsilon = epsilon + '0'
        pos += 1
    return toDecimal(epsilon)



# gets the oxygen generator rating
def getOxygen(list):
    # go through and check to see what the most common bit for each index
    pos = 0
    mostCommon = list[:]
    commonBit = []

   
   # iterating through each character in one entry
    while (pos < len(mostCommon[0])):
        count0 = 0
        count1 = 0
        # commonBit = "0"

        # iterates through each entry to see the most common bit
        for str in mostCommon:      
            if str[pos] == "0":
                count0 += 1
            else: 
                count1 += 1    

        # append the commonBit to an array
        if (count0 > count1):
            commonBit.append("0")
        # set commonBit to 0 if count0 > count1 or count0 == count1
        else:
            commonBit.append("1")
        
        # remove all items that do not have the common bit
        mostCommon = removeNumber(commonBit[pos], mostCommon, pos)
        
        pos += 1
    
    return toDecimal(mostCommon[0])
       
# gets the CO2 scrubber rating
def getCO2(list):
    leastCommon = list[:]
    leastCommonBit = []
    pos = 0
    while (pos < len(leastCommon[0]) and len(leastCommon) > 1):
        count0 = 0
        count1 = 0
       

        # iterates through each entry to see the most common bit
        for str in leastCommon:      
            if str[pos] == "0":
                count0 += 1
            else: 
                count1 += 1    

        # append the commonBit to an array
        if (count0 > count1):
            leastCommonBit.append("1")
        # set commonBit to 0 if count0 > count1 or count0 == count1
        else:
            leastCommonBit.append("0")

        leastCommon = removeNumber(leastCommonBit[pos], leastCommon, pos)
        
        pos += 1

    return(toDecimal(leastCommon[0]))




def viewData(data):
    print("The data is ", data)

# takes the part number from the AoC.py file and sets it
def setPart(set_part):
    global part
    part = set_part

# returns the part
def getPart():
    return part
   
# define the main function
def main():
   # input = []
    part = getPart()
    # read the input file
    data = open("D3.txt", 'r')
    data = toArray(data)
   
    

    if (part == "1"):
       # cycle through the data to get the gamma rate for each data
       gamma, epsilon = getGamma(data)
       power = gamma * epsilon
       print("The gamma is %d, the epsilon is %d, and the power is %d" %(gamma, epsilon, power))
        

    elif (part == "2"):
       oxygen = (getOxygen(data[:]))
       CO2 = getCO2(data)
       print("The oxygen generator rating multiplied with the CO2 scrubbing rating is: ", oxygen * CO2)
       exit()

    else:
        print("There is no valid part number. Clossing program")
        exit()

    

# running the function
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide valid arguments (python [nameOfFile.py] [nameOfPart] [inputFile.txt])")
        exit()
    main()  