# day 1 - count the number of times a depth measurement increases from the previous measurement

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


### PART 1 - find the number of measurements that are larger than the previous one
def getCount(input):
    count = 0
    i = 1
    # for each input (on a new line), compare with previous input
    # if current (i) > past (i-1), then add to counter
    while (i<len(input)):
        if (input[i] > input[i-1]):
            count +=  1
        i += 1
   
    return count



### Part 2 - find the number of 3-measurement sets that are larger than the previous 3-measurement set
def getCount2(input):
    count = 0
    start = 0
    end = start + 2
    OGsum = 0
  
   # initialize OG sum
    for i in range(start, end+1):
       OGsum += input[i]
    start +=1
    end +=1

    # iterate until the upper limit 
    while (end < (len(input))):
       # re-initialize the sum at each new iteration
        sum = 0
        
        # get the new sum
        for i in range(start, end+1):
            sum += input[i] 
        
        # check if the new sum is bigger than original
        if (sum > OGsum):
            count += 1
        start +=1
        end += 1
        # re-initialize original sum to the new sum
        OGsum = sum

    return(count)


# define the main function
def main():
    input = []
    # read the input file
    data = open("D1.txt", 'r')
    data = toArray(data)
    input = toInt(data, input)
    

    if (sys.argv[1] == "P1"):
     
        print(getCount(input))

    elif (sys.argv[1] == "P2"):
        print("There are %d number of increased 3-set measurements than the previous set" %(getCount2(input)))

    else:
        print("There is no valid part number. Clossing program")
        exit()

    

# running the function
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide valid arguments (python [nameOfFile.py] [nameOfPart] [inputFile.txt])")
        exit()
    main()  