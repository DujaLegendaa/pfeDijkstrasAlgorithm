import visualizer as viz
import math
import heapq
import sys

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distanca < other.distanca

    distanca = sys.maxsize
    roditelj = None
    pregledan = False
    blokiran = False


horizontalnaVertikalnaDistanca = 1.0
diagonalnaDistanca = 1.4



def dijkatras():
    pozicijeUnetihKvadrata = viz.pozicijeObojenihKvadrata
    pozicijeSvihKvadrata = viz.kvadrati
    brojKvadrata = math.floor(math.sqrt(len(pozicijeSvihKvadrata)))
    
    nodeGrid2d = kreirajGridNoda(brojKvadrata)
    velicina = len(nodeGrid2d)

    (pocetak, kraj) = korisnickiUnetiKvadrati(nodeGrid2d, pozicijeSvihKvadrata, pozicijeUnetihKvadrata, brojKvadrata)
    pocetak.distanca = 0

    priorityQueue = []
    heapq.heapify(priorityQueue)

    heapq.heappush(priorityQueue, pocetak)

    while len(priorityQueue) > 0:
        trenutniNode = heapq.heappop(priorityQueue)
        tempNode = None

        #dole
        if trenutniNode.y + 1 < velicina:

            #dole dole
            tempNode = nodeGrid2d[trenutniNode.x][trenutniNode.y + 1]
            nodeLogic(tempNode, trenutniNode, horizontalnaVertikalnaDistanca, priorityQueue)

            #dole desno
            if trenutniNode.x + 1 < velicina:
                tempNode = nodeGrid2d[trenutniNode.x + 1][trenutniNode.y + 1]
                nodeLogic(tempNode, trenutniNode, diagonalnaDistanca, priorityQueue)

            #dole levo
            if trenutniNode.x - 1 > 0:
                tempNode = nodeGrid2d[trenutniNode.x - 1][trenutniNode.y + 1]
                nodeLogic(tempNode, trenutniNode, diagonalnaDistanca, priorityQueue)

        #gore
        if trenutniNode.y - 1 >= 0:

            #gore gore
            tempNode = nodeGrid2d[trenutniNode.x][trenutniNode.y - 1]
            nodeLogic(tempNode, trenutniNode, horizontalnaVertikalnaDistanca, priorityQueue)

            #gore desno
            if trenutniNode.x + 1 < velicina:
                tempNode = nodeGrid2d[trenutniNode.x + 1][trenutniNode.y - 1]
                nodeLogic(tempNode, trenutniNode, diagonalnaDistanca, priorityQueue)

            #gore levo
            if trenutniNode.x - 1 > 0:
                tempNode = nodeGrid2d[trenutniNode.x - 1][trenutniNode.y - 1]
                nodeLogic(tempNode, trenutniNode, diagonalnaDistanca, priorityQueue)

        #desno
        if trenutniNode.x + 1 < velicina:
            tempNode = nodeGrid2d[trenutniNode.x + 1][trenutniNode.y]
            nodeLogic(tempNode, trenutniNode, horizontalnaVertikalnaDistanca, priorityQueue)

        #levo
        if trenutniNode.x - 1 > 0:
            tempNode = nodeGrid2d[trenutniNode.x - 1][trenutniNode.y]
            nodeLogic(tempNode, trenutniNode, horizontalnaVertikalnaDistanca, priorityQueue)

        trenutniNode.pregledan = True

    return nadjiPut(nodeGrid2d, kraj, pozicijeSvihKvadrata, brojKvadrata)
    


def nodeLogic(tempNode, trenutniNode, distanca, priorityQueue):
    if tempNode.pregledan == False and (tempNode.blokiran == False ) and (tempNode.distanca > trenutniNode.distanca + distanca):
                    tempNode.distanca = trenutniNode.distanca + distanca
                    tempNode.roditelj = trenutniNode
                    heapq.heappush(priorityQueue, tempNode)

def nadjiPut(nodeGrid2d, kraj, pozicijeSvihKvadrata, brojKvadrata):
    put = []
    trenutniNode = nodeGrid2d[kraj.x][kraj.y]
    while trenutniNode.roditelj != None:
        put.append(pozicijeSvihKvadrata[trenutniNode.roditelj.x * brojKvadrata + trenutniNode.roditelj.y])
        trenutniNode = trenutniNode.roditelj
    put.pop()
    return put

def kreirajGridNoda(x):
    nodeGrid1d = []
    nodeGrid2d = []
    
    for col in range(x):
        for row in range(x):
            nodeGrid1d.append(Node(col, row))
        nodeGrid2d.append(list(nodeGrid1d))
        nodeGrid1d.clear()

    return nodeGrid2d

def korisnickiUnetiKvadrati(nodeGrid2d, pozicijeSvihKvadrata, pozicijeUnetihKvadrata, brojKvadrata):
    both = []
    (pocetak, kraj) = (None, None)
    for i in range(len(pozicijeUnetihKvadrata)):
        for j in range(len(pozicijeSvihKvadrata)):
            if pozicijeUnetihKvadrata[i] == pozicijeSvihKvadrata[j]:
                both.append((j, i))
    
    for i in both:
        if both[0] == i:
            pocetak = nodeGrid2d[i[0] // brojKvadrata][i[0] % brojKvadrata]
        elif both[1] == i:
            kraj = nodeGrid2d[i[0] // brojKvadrata][i[0] % brojKvadrata]
        else:
            nodeGrid2d[i[0] // brojKvadrata][i[0] % brojKvadrata].blokiran = True
    
    return (pocetak, kraj)
