import math
import heapq
import sys
import queue

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        self.distanca = 1.0
        self.diagonalnaDistanca = math.sqrt(self.distanca * self.distanca + self.distanca * self.distanca)

    roditelj = None
    pregledan = False
    blokiran = False

    def setDistanca(self, novaDistanca):
        self.distanca = novaDistanca
        self.diagonalnaDistanca = math.sqrt(novaDistanca * novaDistanca + novaDistanca * novaDistanca)
    
    def __lt__(self, other):
        return self.f < other.f

X = [ 0, 1, 1, 1, 0, -1, -1, -1];
Y = [ 1, 1, 0, -1, -1, -1, 0, 1];
#X = [0, 1, 0, -1]
#Y = [1, 0, -1, 0]
''' 
     |     |
-1 1 | 0 1 | 1 1
     |     |
-----|-----|-----
-1 0 | 0 0 | 1 0
     |     |
-----|-----|-----
     |     |
-1 -1| 0 -1| 1 -1
     |     |
'''


def switchAlgoritma(index, pozicijeUnetihKvadrata, kvadrati):
    brojKvadrataUOsi = math.floor(math.sqrt(len(kvadrati)))

    nodeGrid2d = kreirajGridNoda(brojKvadrataUOsi)
    velicina = len(nodeGrid2d)

    pronalazacFunc = nadjiKvadratUGridu(nodeGrid2d)
    (pocetak, kraj) = resiPozicijeUnetihKvadrata(pozicijeUnetihKvadrata, pronalazacFunc)

    if pocetak == None or kraj == None:
        return (None, None)

    if index == 0:
        return bfs(pocetak, kraj, nodeGrid2d, kvadrati)
    elif index == 1:
        return dfs(pocetak, kraj, nodeGrid2d, kvadrati)
    elif index == 2:
        return dijakstra(pocetak, kraj, nodeGrid2d, kvadrati)
    elif index == 3:
        return aStar(pocetak, kraj, nodeGrid2d, kvadrati)
    else:
        raise NameError("bad algoritam index")
        return -1

def resiPozicijeUnetihKvadrata(pozicijeUnetihKvadrata, pronalazacFunc):
    pocetak = pronalazacFunc(pozicijeUnetihKvadrata["pocetak"])
    kraj = pronalazacFunc(pozicijeUnetihKvadrata["kraj"])
    for blokiranKvadrat in pozicijeUnetihKvadrata["blokirane"]:
        pronalazacFunc(blokiranKvadrat).blokiran = True

    for vodaKvadrat in pozicijeUnetihKvadrata["voda"]:
        pronalazacFunc(vodaKvadrat).setDistanca(2)
    for planinaKvadrat in pozicijeUnetihKvadrata["planine"]:
        pronalazacFunc(planinaKvadrat).setDistanca(4)
    for brdoKvadrat in pozicijeUnetihKvadrata["brda"]:
        pronalazacFunc(brdoKvadrat).setDistanca(3)
    for ledKvadrat in pozicijeUnetihKvadrata["led"]:
        pronalazacFunc(ledKvadrat).setDistanca(0.3)


    return (pocetak, kraj)

def nadjiKvadratUGridu(nodeGrid2d):

    def internal(kvadrat):
        x = kvadrat.x // kvadrat.width
        y = kvadrat.y // kvadrat.width

        return nodeGrid2d[x][y]
    return internal

def pregledajObliznjeNode(trenutniNode, nodeGrid2d, kraj, pregledaniNodeovi, kju):
    tempNode = None
    for k in range(0, len(X)):
        dx = trenutniNode.x + X[k]
        dy = trenutniNode.y + Y[k]

        if(dx >= 0 and dx < len(nodeGrid2d) and dy >= 0 and dy < len(nodeGrid2d)):
            tempNode = nodeGrid2d[dx][dy]
            if tempNode.pregledan == False and tempNode.blokiran == False:
                tempNode.pregledan = True
                tempNode.roditelj = trenutniNode
                pregledaniNodeovi.append(tempNode)
                kju.put(tempNode)

            if tempNode is kraj:
                return -1

def pregledajObliznjeNodeHeapQ(trenutniNode, nodeGrid2d, pocetak, kraj, pregledaniNodeovi, kju, dijkstra):
    tempNode = None

    for k in range(len(X)):
        dx = trenutniNode.x + X[k]
        dy = trenutniNode.y + Y[k]

        if(dx >= 0 and dx < len(nodeGrid2d) and dy >= 0 and dy < len(nodeGrid2d)):
            tempNode = nodeGrid2d[dx][dy]
            if tempNode.pregledan == False and tempNode.blokiran == False:
                distanca = tempNode.diagonalnaDistanca if X[k] != 0 and Y[k] != 0 else tempNode.distanca

                if dijkstra == True: 
                    tempNode.h = 0 
                    tempNode.g = trenutniNode.g + distanca
                else:
                    tempNode.h = max(abs(tempNode.x - pocetak.x), abs(tempNode.y - pocetak.y))
                    tempNode.g = abs(tempNode.x - kraj.x) + abs(tempNode.y - kraj.y)
                
                tempNode.f = tempNode.g + tempNode.h
                tempNode.pregledan = True
                tempNode.roditelj = trenutniNode
                pregledaniNodeovi.append(tempNode)

                heapq.heappush(kju, tempNode)

            if tempNode is kraj:
                return -1

def nodeToRect(nodeArr, kvadrati, brojKvadrataUOsi):
    rectArr = []
    for node in nodeArr:
        rectArr.append(kvadrati[node.x * brojKvadrataUOsi + node.y])
    return rectArr

def nadjiPut(nodeGrid2d, pocetak, kraj, kvadrati, brojKvadrataUOsi):
    put = []
    trenutniNode = nodeGrid2d[kraj.x][kraj.y]
    while trenutniNode != pocetak and trenutniNode.roditelj != None:
        put.append(kvadrati[trenutniNode.roditelj.x * brojKvadrataUOsi + trenutniNode.roditelj.y])
        trenutniNode = trenutniNode.roditelj
    put.pop()
    put.reverse()
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

def bfs(pocetak, kraj, nodeGrid2d, kvadrati):
    brojKvadrata = math.floor(math.sqrt(len(kvadrati)))
    pregledaniNodeovi = []

    kju = queue.Queue(0)
    kju.put(pocetak)
    trenutniNode = Node(-1, -1)

    while kju.qsize() > 0:
        trenutniNode = kju.get()
        
        if pregledajObliznjeNode(trenutniNode, nodeGrid2d, kraj, pregledaniNodeovi, kju) == -1:
            break

    return (nadjiPut(nodeGrid2d, pocetak, kraj, kvadrati, brojKvadrata), nodeToRect(pregledaniNodeovi, kvadrati, brojKvadrata), nodeGrid2d)

def dfs(pocetak, kraj, nodeGrid2d, kvadrati):
    brojKvadrata = math.floor(math.sqrt(len(kvadrati)))
    pregledaniNodeovi = []

    kju = queue.LifoQueue(0)
    kju.put(pocetak)
    trenutniNode = Node(-1, -1)

    while kju.qsize() > 0:
        trenutniNode = kju.get()

        if pregledajObliznjeNode(trenutniNode, nodeGrid2d, kraj, pregledaniNodeovi, kju) == -1:
            break

    return (nadjiPut(nodeGrid2d, pocetak, kraj, kvadrati, brojKvadrata), nodeToRect(pregledaniNodeovi, kvadrati, brojKvadrata), nodeGrid2d)

def dijakstra(pocetak, kraj, nodeGrid2d, kvadrati):
    brojKvadrata = math.floor(math.sqrt(len(kvadrati)))
    velicina = len(nodeGrid2d)

    pregledaniNodeovi = []

    priorityQueue = []
    heapq.heapify(priorityQueue)

    heapq.heappush(priorityQueue, pocetak)
    trenutniNode = Node(-1, -1)

    while len(priorityQueue) > 0:
        trenutniNode = heapq.heappop(priorityQueue)
        tempNode = None

        if pregledajObliznjeNodeHeapQ(trenutniNode, nodeGrid2d, pocetak, kraj, pregledaniNodeovi, priorityQueue, True) == -1:
            break

    return (nadjiPut(nodeGrid2d, pocetak, kraj, kvadrati, brojKvadrata), nodeToRect(pregledaniNodeovi, kvadrati, brojKvadrata), nodeGrid2d)

def aStar(pocetak, kraj, nodeGrid2d, kvadrati):
    brojKvadrata = math.floor(math.sqrt(len(kvadrati)))
    pregledaniNodeovi = []

    otvoreneNodeQ = []
    heapq.heapify(otvoreneNodeQ)
    heapq.heappush(otvoreneNodeQ, pocetak)

    while len(otvoreneNodeQ) > 0:
        trenutniNode = heapq.heappop(otvoreneNodeQ)

        if pregledajObliznjeNodeHeapQ(trenutniNode, nodeGrid2d, pocetak, kraj, pregledaniNodeovi, otvoreneNodeQ, False) == -1:
            break

    return (nadjiPut(nodeGrid2d, pocetak, kraj, kvadrati, brojKvadrata), nodeToRect(pregledaniNodeovi, kvadrati, brojKvadrata), nodeGrid2d)