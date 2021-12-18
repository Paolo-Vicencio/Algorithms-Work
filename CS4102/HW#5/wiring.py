# Class for defining a node with both a name field and a number field 
class node:
    def __init__(self, junction, number):
        self.junction = junction
        self.number = number

# These are the find and union data functions
def find(node):
    if  nodeSet[node.number].number == node.number:
        return node.number
    else:
        return find(nodeSet[node.number])

def union(node1, node2):
    label1 = find(node1)
    label2 = find(node2)
    if label1 != label2:
        nodeSet[label2].number = label1

finalEdges = []
# This is the basic kruskals algorithm
def kruskals(edges, nodes, switchID):
    # Managing Edges counted and total weights
    edgesAccepted = 0
    edgeTotal = 0
    count = 0

    while (edgesAccepted <= nodes):
        # print(len(edges))
        edge_check = False
        if len(edges) == 0:
            return edgeTotal
        else:
            e = edges[0]
            edges.pop(0)
        # this block if statements ensures that the lights and switches being connected are in the correct order
        # and that they are compatible with each other before forming the union
        while edge_check == False:
            if e[0].junction[0] == 's' or e[0].junction[0] == 'l':
                if e[1].junction[0] == 's' or e[1].junction[0] == 'l':
                    if switchID[e[0].junction] != switchID[e[1].junction]:
                        if len(edges) == 0:
                            return edgeTotal
                        e = edges[0]
                        edges.pop(0)
                    else:
                        edge_check = True
            else:
                edge_check = True

        
        aSet = find(e[0])
        bSet = find(e[1])
        if aSet != bSet:
            edgesAccepted+=1
            edgeTotal+=e[2]
            union(e[0], e[1])
        else:

            if len(edges) == 0:
                return edgeTotal
            # else:
            #     edges.pop(0)
    return edgeTotal


# this is the kruskals algorithm specifically for the set of overlapping wires
# from group 1 to group 2
def kruskals3(edges, nodes, switchID):
    # Managing Edges counted and total weights
    edgesAccepted = 0
    edgeTotal = 0


    while (edgesAccepted <= nodes):
        if len(edges) == 0:
            return edgeTotal
        switch_check = False

        e = edges[0]
        edges.pop(0)

        # this is to ensure that only the lowest cost wire connects each switch group
        # to the non-switch and non-light nodes
        while switch_check == False:
            if e[0].junction[0] == 's':
                if switchID[e[0].junction] == "checked":
                    edgesAccepted+=1
                    if len(edges) == 0:
                        return edgeTotal
                    e = edges[0]
                    edges.pop(0)
                else:
                    switchID[e[0].junction] = "checked"
                    switch_check = True
            elif e[1].junction[0] == 's':
                if switchID[e[1].junction] == "checked":
                    edgesAccepted+=1
                    if len(edges) == 0:
                        return edgeTotal
                    e = edges[0]
                    edges.pop(0)
                else:
                    switchID[e[1].junction] = "checked"
                    switch_check = True
            elif e[0].junction[0] == 'l' or e[1].junction[0] == 'l':
                    edgesAccepted += 1
                    if len(edges) == 0:
                        return edgeTotal
                    e = edges[0]
                    edges.pop(0)
            else:
                light_check = True

        aSet = find(e[0])
        bSet = find(e[1])
        if aSet != bSet:

            # print("edge accepted: ", "(", e[0].junction, " ", e[1].junction, " ", e[2], ")" )

            edgesAccepted+=1
            edgeTotal+=e[2]
            union(e[0], e[1])
        else:
            if len(edges) == 0:
                return edgeTotal
            else:
                edges.pop(0)
    return edgeTotal



nodeDict = {}
room_counter = -1
junctionSet = []
nodeSet = []
daEdges = []
lineCounter = 0
nodeCounter = 0
count = 0
is_zero = 1
while is_zero != 0:
    theInput = input("")

    # reading the first line of input
    if lineCounter == 0:
        nodeLength, edgeLength = theInput.split()
    
    # reading the junctions
    elif theInput.count(' ') == 1:
        # reading the input
        junc, type = theInput.split()
        junctionSet.append(junc)
        
        # creating switch room ID's with dictionary
        if junc[0] == 's':
            room_counter += 1
        if junc[0] == 's' or junc[0] == 'l':
            nodeDict[junc] = room_counter

        # creating node with unique ID and adding it to nodeSet
        newNode = node(junc, count)
        nodeSet.append(newNode)
        nodeCounter += 1
        count += 1

    # reading the edges in
    if theInput.count(' ') == 2:
        firstNode, secondNode, weight = theInput.split()

    # taking that input and matching it with the provided junctions in the set
        for each in nodeSet:
            if each.junction == firstNode:
                firstNode = each
            if each.junction == secondNode:
                secondNode = each
    # adding those edges to the overall edge list
        daEdges.append([firstNode, secondNode, int(weight)])

    lineCounter += 1

    if lineCounter == int(nodeLength) + int(edgeLength) + 1:
        is_zero = 0


# # sorting the edges by the edge weight provided
daEdges.sort(key=lambda tup: tup[2])
# for each in range(len(daEdges)):
#     print("[", "(", daEdges[each][0].junction, daEdges[each][0].number, ")", "(", daEdges[each][1].junction,
#     daEdges[each][1].number, ")", daEdges[each][2], "]")

# creating 3 lists:
# for holding all edges between everything but lights and switches
g1 = []
# for holding all edges between only lights and switches
g2 = []
# for holding all other edges that cross over
g3 = []

# adding appropriate edges to each list
for each in daEdges:
    if each[0].junction[0] == 'b' or each[0].junction[0] == 'j' or each[0].junction[0] == 'o':
        if each[1].junction[0] == 'b' or each[1].junction[0] == 'j' or each[1].junction[0] == 'o':
            g1.append(each)
        else:
            g3.append(each)
    elif each[0].junction[0] == 's' or each[0].junction[0] == 'l' :
        if each[1].junction[0] == 's' or each[1].junction[0] == 'l':
            g2.append(each)
        else:
            g3.append(each)
  


# creating sets of node lengths for each of the edge sets
g1Nodes = []
g2Nodes = []
g3Nodes = []


# filling the unique node sets
for each in g1:
    if each[0].junction not in g1Nodes:
        g1Nodes.append(each[0].junction)
    if each[1].junction not in g1Nodes:
        g1Nodes.append(each[1].junction)
        
for each in g2:
    if each[0].junction not in g2Nodes:
        g2Nodes.append(each[0].junction)
    if each[1].junction not in g2Nodes:
        g2Nodes.append(each[1].junction)



        
for each in g3:
    if each[0].junction not in g3Nodes:
        g3Nodes.append(each[0].junction)
    if each[1].junction not in g3Nodes:
        g3Nodes.append(each[1].junction)

# print(len(g2Nodes))
# print(len(g2))
# calculate kruskals for each piece
g1Kruskals = kruskals(g1, len(g1Nodes) , nodeDict)
g2Kruskals = kruskals(g2, len(g2Nodes), nodeDict)
g3Kruskals = kruskals3(g3, len(g3Nodes), nodeDict)

# adding all three pieces together to create the final answer
# make sure to include g3kruskals later
final = g1Kruskals + g2Kruskals + g3Kruskals
print(final)

