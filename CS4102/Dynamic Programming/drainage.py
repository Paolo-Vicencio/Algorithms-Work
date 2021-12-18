drainageMatrix = []


# maybe want to initialize each grid spot as unchecked (-1 maybe?)
solutionGrid = [[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]


# this function finds the longest drain that ends at the desired location
def longestDrain(x, y, solutionG, drainageM):
    
    # check if the solution already exists
    # basically, if there is anything else in in the solution grid slot, that is the answer for the longest path ending there
    # print(solutionG[x][y])
    if solutionG[x][y] != 0:
        # print("accessed")
        return solutionG[x][y]

    # length of the grid
    # print(drainageM)
    width = len(drainageM[0])
    # print("width=",width)
    # height of the grid
    height = len(drainageM)
    # print("height=",height)
    # this variable is to keep track of the number to put in the cell
    optimal = 0

    # these are the North, East, South, West directions on the graph (only adjacent cells are considered)
    cardinal = [[0,1], [1,0], [0,-1], [-1,0]]

    # check if those cells exist and don't go off the side of the grid
    for x2, y2 in cardinal:
        if x + x2 < 0 or y + y2 < 0:
            # print("x:",x2,"y2:", y2)
            continue
        if x + x2 >= height or y + y2 >= width:
            # print(x2,y2)
            continue
        if drainageM[x + x2][y + y2] > drainageM[x][y]:
            optimal = max(optimal, longestDrain(x + x2, y + y2, solutionG, drainageM))
    # if, after the whole loop, optimal is still 0, it means that there are no adjacent boxes with
    # a higher value than the target and the longest possible path ending here is just 1 (base case)
    if optimal == 0:
        solutionG[x][y] = 1
        return 1

    solutionG[x][y] = optimal + 1

    return solutionG[x][y]

def drainFinal(drainMatrix, solutionMatrix):
    x_counter = 0
    y_counter = 0
    longest = 0

    x_boundary = len(drainMatrix)
    # print("x-counter=", x_boundary)
    y_boundary = len(drainMatrix[0])
    # print("y-counter=",y_boundary)

    while y_counter < y_boundary:
        # print("accessed")
        drain = longestDrain(x_counter, y_counter, solutionMatrix, drainMatrix)

        if drain > longest:
            longest = drain

        x_counter += 1
        if x_counter == x_boundary:
            x_counter = 0
            y_counter += 1

    return longest





counter = 0
marker = 1
# variables for taking city and grid size input
city = ""
rows = 0
columns = 0
# storing city names and answers to each grid
cityList = []
answerList = []
# necessary matrices
drainageMatrix = []
solutionMatrix = []
# while loop variable
going = False

try:
    while counter <= marker:
        theInput = input("")
        # this if statements basically catches the first input number that defines the number of 
        # test cases in the document
        if " " not in theInput and counter==0:
            marker = int(theInput)
        
        # this statement checks if the input is the city label and grid size
        elif theInput.replace(" ","").isdecimal() == False and "-" not in theInput:
            # print("here!",theInput)
            if counter == 0:
                city, r, c = theInput.split()
                rows = int(r)
                columns = int(c)
                cityList.append(city)
                counter += 1
            else:
                # print("This is the counter: ", counter)
                # print("This is the drainage matrix")
                # print(drainageMatrix)
                # print("This is the solution matrix")
                # print(solutionMatrix)

                answer = drainFinal(drainageMatrix, solutionMatrix)
                answerList.append(answer)

                city, r, c = theInput.split()
                rows = int(r)
                columns = int(c)
                cityList.append(city)
                counter += 1
                    
                drainageMatrix.clear()
                solutionMatrix.clear()

    # this statement checks if the input is a line in a grid
        else:
            # print("there!", theInput)
            interim = []

            splitString = theInput.split()
            obj = map(int, splitString)
            drainageMatrix.append(list(obj))

            # print(drainageMatrix)

            for each in range(columns):
                interim.append(0)
            solutionMatrix.append(interim)
        
        # this statement prints the desired output and then ends the while loop
except EOFError as e:

    answer = drainFinal(drainageMatrix, solutionMatrix)
    answerList.append(answer)

    length = len(cityList)
    for each in range(length):
        print(cityList[each] + ":", answerList[each])





