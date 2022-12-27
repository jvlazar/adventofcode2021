# read input from the terminal and run the appropriate file

# read input


# check to see what Advent of Code day 
def findDate(day_result):
    match day_result:
        case "1":
            import D1
            return D1, 1
        case "2":
            import D2
            return D2, 2
        case "3":
            import D3
            return D3, 3
        case _:
         return None

def run(day, part):
        day.setPart(part)
        day.main()

# switch control to the appropriate file
def main():
    day_result = input("Please say what day you want to do ('X'): \n")
    day, number = findDate(day_result)
    part = input("Please insert which part: (1 or 2) ")
    run(day, part)


main()