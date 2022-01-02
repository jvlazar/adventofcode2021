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

# convert to decimal
def toDecimal(number):
    decimal = 0
    pos = 0
    while (pos < len(number)):
       # print(pos)
        if (number[pos] == '1'):
            #print("The digit at position %d is %s" %(len(number) - pos - 1, number[pos]))
            decimal = decimal + (2**(len(number) - pos - 1))
            #print(decimal)
        pos += 1

    return decimal

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

    

# define the main function
def main():
    input = []
    # read the input file
    data = open("D3.txt", 'r')
    data = toArray(data)
   
    

    if (sys.argv[1] == "P1"):
       # cycle through the data to get the gamma rate for each data
       gamma, epsilon = getGamma(data)
       power = gamma * epsilon
       print("The gamma is %d, the epsilon is %d, and the power is %d" %(gamma, epsilon, power))
        

    elif (sys.argv[1] == "P2"):
       print("This is a work in progress")
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