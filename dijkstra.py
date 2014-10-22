import heapq # Binary heap structure, to keep paths in order

def dijkstra(graph, node):
    shortestPaths = list()
    pathsInMaking = list()
    knownPaths = list()

    # This list keeps the list of shortest paths. We initialize it here.
    shortestPaths.append((0,[node]))
    # This list is to remember which nodes we already have shortest paths for
    knownPaths.append(node) 

    while len(shortestPaths) < len(graph):
        newPath = shortestPaths[-1][1]
        newPathLen = shortestPaths[-1][0]
        newNode = newPath[-1]
        # The last node on the latest path is the new node that we added,
        # so we look at the new paths that it brings
        neighbors = graph[newNode].keys()
        for elm in neighbors:
            heapq.heappush(pathsInMaking,
                           (newPathLen+graph[newNode][elm],newPath+[elm]))

        # We remove all paths that go to nodes that we already have
        # shortest paths for
        while pathsInMaking[0][1][-1] in knownPaths:
            heapq.heappop(pathsInMaking)

        newPath = heapq.heappop(pathsInMaking)
        shortestPaths.append(newPath)
        knownPaths.append(newPath[1][-1])
    return shortestPaths

theGraph = dict()
for i in range(20): # Creating the graph, as specified:
    indI = i+1
    theGraph[indI] = dict()
    for j in range(20):
        indJ = j+1
        if abs(indJ-indI) in [1,2,19]:
            theGraph[indI][indJ] = (-1)**indJ+abs(2*indI-indJ)+5
print str(dijkstra(theGraph,1))
"""
OUTPUT: (distance, [path])

>dijkstra(theGraph,1)
[(0, [1]),
 (5, [1, 3]),
 (6, [1, 2]),
 (10, [1, 3, 5]),
 (12, [1, 2, 4]),
 (17, [1, 3, 5, 7]),
 (20, [1, 2, 4, 6]),
 (24, [1, 20]),
 (26, [1, 3, 5, 7, 9]),
 (29, [1, 3, 5, 7, 8]),
 (37, [1, 3, 5, 7, 9, 11]),
 (40, [1, 3, 5, 7, 9, 10]),
 (49, [1, 20, 19]),
 (50, [1, 3, 5, 7, 9, 11, 13]),
 (52, [1, 20, 18]),
 (53, [1, 3, 5, 7, 9, 11, 12]),
 (65, [1, 3, 5, 7, 9, 11, 13, 15]),
 (68, [1, 3, 5, 7, 9, 11, 13, 14]),
 (74, [1, 20, 19, 17]),
 (78, [1, 20, 18, 16])]
"""
