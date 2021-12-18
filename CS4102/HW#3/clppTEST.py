import math
import copy

theAnswers = []

def sortByX(points):
    points.sort()

def splitList(points):
    mid = len(points)//2
    return points[:mid], points[mid:]

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

tupList = [[-6.47, 2.24], [8.90, 6.53], [-1.45, 5.05]]
tupList2 = [(-0.19, 4.85), (1.38, 9.05), (2.77, -9.81)]

# sort the ordered pairs by the x value
sortByX(tupList)
sortByX(tupList2)

# create two lists separated at the mid point of the original list
left,right = splitList(tupList)

# create delta out of the two lowest distances in the left and the right lists
deltaLeft = closestOG(left)
deltaRight = closestOG(right)

delta = min(deltaLeft, deltaRight)

print(delta)

# create a strip using delta and the original list
theStrip = createStrip(tupList, delta)

# sort the strip by its y value
theStrip.sort(key=lambda point:point[1])

print(theStrip)
# finding the closest distance between the strip points
stripMin = stripDistance(theStrip, delta)

print(stripMin)
# finding the closest pair of points from all 3: deltaLeft, deltaRight, and stripDistance
answerUnrounded = min(deltaLeft, deltaRight, stripMin)

# if the final answer is greater than 10,000 just set it equal to "infinity". If not, round it to 4
if answerUnrounded >= 10000:
    finalAnswer = "infinity"
else:
    finalAnswer = round(answerUnrounded, 4)

# appendingt the final answer to the list of total answers for the input
theAnswers.append(finalAnswer)

print(theAnswers)