import math
import copy
import time

# Note: got the minimum as 'inf' idea from geeksforgeeks in the closestOG function

theAnswers = []

def sortByX(points):
    points.sort()

# def splitList(points):
#     mid = len(points)//2
#     return points[:mid], points[mid:]

def distance(point1, point2):
    val1 = (point2[0] - point1[0]) ** 2
    val2 = (point2[1] - point1[1]) ** 2
    val3 = val1 + val2
    finalVal = val3 ** (1/2)
    return finalVal

def closestOG(pointArray):
    minimum = float('inf')
    for i in range(len(pointArray)):
        for j in range(i + 1, len(pointArray)):
            dist = distance(pointArray[i], pointArray[j])
            if dist < minimum:
                minimum = dist
    return minimum

def createStrip(theArray, delta):
    theStrip = []
    mid = len(theArray) // 2
    for i in range(len(theArray)):
        if abs(theArray[i][0] - theArray[mid][0]) < delta:
            theStrip.append(theArray[i])
    return theStrip

def stripDistance(stripArray, delta):
    minimum = delta
    for i in range(len(stripArray)):
        for j in range(i + 1, len(stripArray)):
            while j < len(stripArray) and (stripArray[j][1] - stripArray[i][1]) < minimum:
                minimum = distance(stripArray[i], stripArray[j])
                j+=1
    return minimum

def closestFinal(theArray, theArrayY, size):

    # brute force base case to allow recursion to work
    # if size <= 3:
    #     return closestOG(theArray)
    
    # finding the mid point of the array
    mid = size // 2

    # establishing the left and right arrays
    left = theArray[:mid]
    right = theArray[mid:]

    # find the delta values for the left and right respectively
    deltaLeft = closestOG(left)
    deltaRight = closestOG(right)

    # find the smaller of the two values
    deltaFinal = min(deltaLeft, deltaRight)
    

    # create the strip
    theStrip = createStrip(theArray, deltaFinal)

    # sorting the strip
    theStrip.sort(key=lambda point:point[1])
    # find the closest value in the strip
    stripMin = stripDistance(theStrip, deltaFinal)

    # return the smallest of the 3 minimum values
    return min(deltaFinal, stripMin)



# working on taking input
isZero = False
pointList = []
# t0 = time.time()
while isZero == False:
    # reading the input
    theInput = input("")

    # if the input is equal to 0 and the loop is over
    if theInput == "0":
        isZero = True

        # sort the points by their x-values
        pointList.sort()

        # create an identical list but sorted by the y-value instead (for the strip)
        pointListY = copy.deepcopy(pointList)
        pointListY.sort(key=lambda point:point[1])

        # run the function closestFinal() on the two lists and the size of the initial list
        answerUnrounded = closestFinal(pointList, pointListY, len(pointList))

        # transforming the answer to the proper format
        if answerUnrounded >= 10000:
            finalAnswer = "infinity"
        else:
            finalAnswer = "%.4f" % answerUnrounded

        # adding the final answer to the final list then print the list
        theAnswers.append(finalAnswer)
        print(*theAnswers, sep = "\n")
    else:
        if " " not in theInput:

            if len(pointList) == 0:
                pointList.clear()

            else:
                # sort the points by their x-values
                pointList.sort()

                # create an identical list but sorted by the y-value instead (for the strip)
                pointListY = copy.deepcopy(pointList)
                pointListY.sort(key=lambda point:point[1])

                # run the function closestFinal() on the two lists and the size of the initial list
                answerUnrounded = closestFinal(pointList, pointListY, len(pointList))

                # transforming the answer to the proper format
                if answerUnrounded >= 10000:
                    finalAnswer = "infinity"
                else:
                    finalAnswer = "%.4f" % answerUnrounded

                # adding the final answer to the final list then clear the list
                theAnswers.append(finalAnswer)
                pointList.clear()
                pointListY.clear()
        else:
            # taking the input and storing it in representative points x and y 
            x, y = theInput.split()
                    
            # converting the two chars into floats
            x = float(x)
            y = float(y)

            # creating a new tuple that represents an ordered pair
            newTup = (x,y)

            # adding new tup to list to create 2D tup
            pointList.append(newTup)
# t1 = time.time()
# total=t1-t0
# print(total)
