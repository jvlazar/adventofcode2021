# day 2: DIVE - figuring out how to pilot the submarine

# read the command prompt
import sys
 
# setup; manipulating the input file to a format that's easy to work with
# converting all text in the file to an array
def toArray(fileName):
    lines = fileName.read()
    lines = lines.split('\n')
    return lines



### PART 1 & 2 - multiply the final horizontal and depth positions
# get the directions for the submarine
def getDirections(input):
    data = input
    depth = 0
    horizontal = 0

    # extra variable needed for PART 2
    aim = 0
    # for every value in the array
    for str in data:
        # split the current data
        info = str.split(' ')
        direction = int(info[1])
        # manipulate the variables according to the input
        if info[0] == "forward":
            horizontal += direction
            # for PART 2
            if sys.argv[1] == "P2":
                increase = (aim * direction)
                depth += increase
        elif info[0] == "up":
            aim -= direction
        elif info[0] == "down":
            aim += direction
        else:
            print("There is no valid direction")
       
    return (depth * horizontal)
        
    
  


# define the main function
def main():
    input = []
    # read the input file
    data = open("D2.txt", 'r')
    # gives the data as an array with instructions and coordinates afterwards
    data = toArray(data)
    

    if (sys.argv[1] == "P1"):
        print("The multiplied final horizontal and final depth position is %d" %(getDirections(data)))
       
    elif (sys.argv[1] == "P2"):
        print("The multiplied final horizontal and final depth position is %d" %(getDirections(data)))
       
    else:
        print("There is no valid part number (P1 or P2). Clossing program")
        exit()

    

# running the function
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide valid arguments (python [nameOfFile.py] [nameOfPart] [inputFile.txt])")
        exit()
    main()  
