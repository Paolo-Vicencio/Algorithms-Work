workingLeest = [[6,6], [1,7], [3,5], [3,5]]
# workingList2 = [[2,2], [3,3], [5,1], [5,10]]
# workingList3 = [[9,7], [9,2], [9,13], [7,14], [11,11]]
# workingList4 = [[11,7], [1,9], [11,10], [4,6], [11,3], [13,12], [7,5], [14,7], [7,12]]

def daycare(rooms):
    t = 0
    e = 0

    for each in rooms:
        # print(each[0])
        # base case (if it is the first )
        if each[0] == rooms[0][0] and each[1] == rooms[0][1]:
            t = each[0]
            if each[1] - t < 0:
                e = 0
            else:
                e = each[1] - t
            # print("t: ", t, "e: ", e)

        # if the amount of kids can fit into the total space currently alotted
        elif each[0] <= t + e:
            # print("yes")
            # just adjust the room count
            e = e + (each[1] - each[0])
            # print("t: ", t, "e: ", e)

        # if the amount of kids CANT fit into the total space currenly alotted
        elif each[0] > t + e:
            # print("no")
            # adjust the trailer amount to just enough to handle then move on
            t = (t + (each[0] - (t + e)))
            e = e + (each[1] - each[0])
            # print("t: ", t, "e: ", e)
        

    return t

def room_sorting(rooms):
    # setting up the 3 different categories to save the rooms in
    extraSpace = []
    sameSpace = []
    loseSpace = []

    # sifting through all rooms and placing them in proper category
    for each in rooms:
        if each[0] - each[1] < 0:
            extraSpace.append(each)
        elif each[0] - each[1] == 0:
            sameSpace.append(each)
        elif each[0] - each[1] > 0:
            loseSpace.append(each)

    # sort the extra space rooms least to greatest by before value
    extraSpace.sort()
    # sort the same space rooms greatest to least
    sameSpace.sort(reverse=True)
    # sort the lost space rooms greatest to least
    loseSpace.sort(key=lambda point:point[1], reverse=True)

    finalList = extraSpace + sameSpace + loseSpace
    
    return finalList

workingList = []
finalAnswers = []
counter = 0
marker = 1
try:
    while counter <= marker:
        theInput = input("")

        if " " not in theInput:
            workingList.clear()
            marker = int(theInput)
            counter = 0

        else:
            old, new = theInput.split()
            old = int(old)
            new = int(new)
            room = [old, new]
            workingList.append(room)
            counter += 1

        if counter == marker:
            # print("accessed")
            newRooms = room_sorting(workingList)
            # print(newRooms)
            trailerSize = daycare(newRooms)
            finalAnswers.append(trailerSize)
except EOFError as e:      
    for each in finalAnswers:
        print(each)

