import visualizer as viz
import math
import heapq
import sys
import queue

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

def jeValidna(i, j, brojKvadrata, pregledan):
    return (not pregledan and i >= 0 and i < brojKvadrata and j>=0 and j < brojKvadrata)

X = [0,1,0,-1];
Y = [-1,0,1,0];

def bfs(pocetak, kraj, nodeGrid2d, brojKvadrata, pozicijeSvihKvadrata):
    pregledaniNodeovi = []

    kju = queue.Queue(0)

    kju.put(pocetak)
    trenutniNode = Node(-1, -1)
    tempNode = None

    while kju.qsize() > 0:
        trenutniNode = kju.get()

        if trenutniNode is kraj or tempNode is kraj:
            break
        

        for k in range(0, 4):
            dx = trenutniNode.x + X[k]
            dy = trenutniNode.y + Y[k]

            if(dx >= 0 and dx < len(nodeGrid2d) and dy >= 0 and dy < len(nodeGrid2d)):
                tempNode = nodeGrid2d[dx][dy]
                if(tempNode.pregledan == False and tempNode.blokiran == False and '''tempNode.distanca > trenutniNode.distanca + horizontalnaVertikalnaDistanca'''):
                    '''tempNode.distanca = trenutniNode.distanca + horizontalnaVertikalnaDistanca'''
                    tempNode.pregledan = True
                    tempNode.roditelj = trenutniNode
                    pregledaniNodeovi.append(tempNode)
                    kju.put(tempNode)

                    

    return (nadjiPut(nodeGrid2d, pocetak, kraj, pozicijeSvihKvadrata, brojKvadrata), nodeToRect(pregledaniNodeovi, pozicijeSvihKvadrata, brojKvadrata))


def main():
    pozicijeUnetihKvadrata = viz.pozicijeObojenihKvadrata
    pozicijeSvihKvadrata = viz.kvadrati
    brojKvadrata = math.floor(math.sqrt(len(pozicijeSvihKvadrata)))

    nodeGrid2d = kreirajGridNoda(brojKvadrata)
    velicina = len(nodeGrid2d)

    (pocetak, kraj) = korisnickiUnetiKvadrati(nodeGrid2d, pozicijeSvihKvadrata, pozicijeUnetihKvadrata, brojKvadrata)
    pocetak.distanca = 0

    #return dijakstra(pocetak, kraj, nodeGrid2d, pozicijeSvihKvadrata)
    return bfs(pocetak, kraj, nodeGrid2d, brojKvadrata, pozicijeSvihKvadrata)




def dijakstra(pocetak, kraj, nodeGrid2d, pozicijeSvihKvadrata):
    brojKvadrata = math.floor(math.sqrt(len(pozicijeSvihKvadrata)))
    velicina = len(nodeGrid2d)

    pregeledaniNodeovi = []

    priorityQueue = []
    heapq.heapify(priorityQueue)

    heapq.heappush(priorityQueue, pocetak)
    trenutniNode = Node(-1, -1)

    while (len(priorityQueue) > 0) and (trenutniNode != kraj):
        trenutniNode = heapq.heappop(priorityQueue)
        tempNode = None

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
            if trenutniNode.x - 1 >= 0:
                tempNode = nodeGrid2d[trenutniNode.x - 1][trenutniNode.y - 1]
                nodeLogic(tempNode, trenutniNode, diagonalnaDistanca, priorityQueue)
            
        #desno
        if trenutniNode.x + 1 < velicina:
            tempNode = nodeGrid2d[trenutniNode.x + 1][trenutniNode.y]
            nodeLogic(tempNode, trenutniNode, horizontalnaVertikalnaDistanca, priorityQueue)

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
            if trenutniNode.x - 1 >= 0:
                tempNode = nodeGrid2d[trenutniNode.x - 1][trenutniNode.y + 1]
                nodeLogic(tempNode, trenutniNode, diagonalnaDistanca, priorityQueue)
            
        #levo
        if trenutniNode.x - 1 >= 0:
            tempNode = nodeGrid2d[trenutniNode.x - 1][trenutniNode.y]
            nodeLogic(tempNode, trenutniNode, horizontalnaVertikalnaDistanca, priorityQueue)

        trenutniNode.pregledan = True
        pregeledaniNodeovi.append(trenutniNode)

    return (nadjiPut(nodeGrid2d, pocetak, kraj, pozicijeSvihKvadrata, brojKvadrata), nodeToRect(pregeledaniNodeovi, pozicijeSvihKvadrata, brojKvadrata))

def nodeLogic(tempNode, trenutniNode, distanca, priorityQueue):
    if tempNode.pregledan == False and (tempNode.blokiran == False ) and (tempNode.distanca > trenutniNode.distanca + distanca):
                    tempNode.distanca = trenutniNode.distanca + distanca
                    tempNode.roditelj = trenutniNode
                    heapq.heappush(priorityQueue, tempNode)

def nodeToRect(nodeArr, pozicijeSvihKvadrata, brojKvadrata):
    rectArr = []
    for node in nodeArr:
        rectArr.append(pozicijeSvihKvadrata[node.x * brojKvadrata + node.y])
    return rectArr

def nadjiPut(nodeGrid2d, pocetak, kraj, pozicijeSvihKvadrata, brojKvadrata):
    put = []
    trenutniNode = nodeGrid2d[kraj.x][kraj.y]
    while trenutniNode != pocetak and trenutniNode.roditelj != None:
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
