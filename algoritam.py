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

    distanca = sys.maxsize
    roditelj = None
    pregledan = False
    blokiran = False
    GHF = False
    
    def __lt__(self, other):
        if self.GHF == False:
            return self.distanca < other.distanca
        else:
            return self.f < other.f

horizontalnaVertikalnaDistanca = 1.0
diagonalnaDistanca = 1.4
X = [-1,0,1,0];
Y = [0 ,1,0,-1];

def switchAlgoritma(index, pozicijeObojenihKvadrata, kvadrati):
    pozicijeUnetihKvadrata = pozicijeObojenihKvadrata
    pozicijeSvihKvadrata = kvadrati
    brojKvadrataUOsi = math.floor(math.sqrt(len(pozicijeSvihKvadrata)))

    nodeGrid2d = kreirajGridNoda(brojKvadrataUOsi)
    velicina = len(nodeGrid2d)

    (pocetak, kraj) = korisnickiUnetiKvadrati(nodeGrid2d, pozicijeSvihKvadrata, pozicijeUnetihKvadrata, brojKvadrataUOsi)
    pocetak.distanca = 0

    if index == 0:
        return bfs(pocetak, kraj, nodeGrid2d, pozicijeSvihKvadrata)
    elif index == 1:
        return dfs(pocetak, kraj, nodeGrid2d, pozicijeSvihKvadrata)
    elif index == 2:
        return dijakstra(pocetak, kraj, nodeGrid2d, pozicijeSvihKvadrata)
    elif index == 3:
        return aStar(pocetak, kraj, nodeGrid2d, pozicijeSvihKvadrata)
    else:
        print("bad algorithm index")
        return -1

def dijakstra(pocetak, kraj, nodeGrid2d, brojKvadrataUOsi, pozicijeSvihKvadrata):
    velicina = len(nodeGrid2d)

    pregledaniNodeovi = []

    priorityQueue = []
    heapq.heapify(priorityQueue)

    heapq.heappush(priorityQueue, pocetak)
    trenutniNode = Node(-1, -1)

    while len(priorityQueue) > 0:
        trenutniNode = heapq.heappop(priorityQueue)
        tempNode = None

        if pregledajObliznjeNodeHeapQ(trenutniNode, nodeGrid2d, pocetak, kraj, pregledaniNodeovi, priorityQueue, False) == -1:
            break

    return (nadjiPut(nodeGrid2d, pocetak, kraj, pozicijeSvihKvadrata, brojKvadrataUOsi), nodeToRect(pregledaniNodeovi, pozicijeSvihKvadrata, brojKvadrataUOsi))

def bfs(pocetak, kraj, nodeGrid2d, pozicijeSvihKvadrata):
    brojKvadrata = math.floor(math.sqrt(len(pozicijeSvihKvadrata)))
    pregledaniNodeovi = []

    kju = queue.Queue(0)
    kju.put(pocetak)
    trenutniNode = Node(-1, -1)

    while kju.qsize() > 0:
        trenutniNode = kju.get()
        
        if pregledajObliznjeNode(trenutniNode, nodeGrid2d, kraj, pregledaniNodeovi, kju) == -1:
            break

    return (nadjiPut(nodeGrid2d, pocetak, kraj, pozicijeSvihKvadrata, brojKvadrata), nodeToRect(pregledaniNodeovi, pozicijeSvihKvadrata, brojKvadrata))

def pregledajObliznjeNode(trenutniNode, nodeGrid2d, kraj, pregledaniNodeovi, kju):
    tempNode = None
    for k in range(0, 4):
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


def dfs(pocetak, kraj, nodeGrid2d, pozicijeSvihKvadrata):
    brojKvadrata = math.floor(math.sqrt(len(pozicijeSvihKvadrata)))
    pregledaniNodeovi = []

    kju = queue.LifoQueue(0)
    kju.put(pocetak)
    trenutniNode = Node(-1, -1)

    while kju.qsize() > 0:
        trenutniNode = kju.get()

        if pregledajObliznjeNode(trenutniNode, nodeGrid2d, kraj, pregledaniNodeovi, kju) == -1:
            break

    return (nadjiPut(nodeGrid2d, pocetak, kraj, pozicijeSvihKvadrata, brojKvadrata), nodeToRect(pregledaniNodeovi, pozicijeSvihKvadrata, brojKvadrata))
        
def aStar(pocetak, kraj, nodeGrid2d, pozicijeSvihKvadrata):
    brojKvadrata = math.floor(math.sqrt(len(pozicijeSvihKvadrata)))
    pregledaniNodeovi = []

    otvoreneNodeQ = []
    heapq.heapify(otvoreneNodeQ)
    heapq.heappush(otvoreneNodeQ, pocetak)

    while len(otvoreneNodeQ) > 0:
        trenutniNode = heapq.heappop(otvoreneNodeQ)

        if pregledajObliznjeNodeHeapQ(trenutniNode, nodeGrid2d, pocetak, kraj, pregledaniNodeovi, otvoreneNodeQ, True) == -1:
            break

    return (nadjiPut(nodeGrid2d, pocetak, kraj, pozicijeSvihKvadrata, brojKvadrata), nodeToRect(pregledaniNodeovi, pozicijeSvihKvadrata, brojKvadrata))

def trebaDodati(tempNode, otvoreneNodeQ):
    for noda in otvoreneNodeQ:
        if noda == tempNode and tempNode.f >= noda.f:
            return False
    return True

def pregledajObliznjeNodeHeapQ(trenutniNode, nodeGrid2d, pocetak, kraj, pregledaniNodeovi, kju, GHF):
    tempNode = None

    for k in range(0, 4):
        dx = trenutniNode.x + X[k]
        dy = trenutniNode.y + Y[k]

        if(dx >= 0 and dx < len(nodeGrid2d) and dy >= 0 and dy < len(nodeGrid2d)):
            tempNode = nodeGrid2d[dx][dy]
            if tempNode.pregledan == False and tempNode.blokiran == False:
                if GHF == False:
                    if tempNode.distanca > trenutniNode.distanca + horizontalnaVertikalnaDistanca:
                        tempNode.distanca = trenutniNode.distanca + horizontalnaVertikalnaDistanca
                        tempNode.pregledan = True
                        tempNode.roditelj = trenutniNode
                        pregledaniNodeovi.append(tempNode)
                        heapq.heappush(kju, tempNode)

                if GHF == True:
                    tempNode.GHF = True
                    tempNode.pregledan = True
                    tempNode.roditelj = trenutniNode
                    pregledaniNodeovi.append(tempNode)
                    tempNode.g = abs(tempNode.x - pocetak.x) + abs(tempNode.y - pocetak.y)
                    tempNode.h = abs(tempNode.x - kraj.x) + abs(tempNode.y - kraj.y)
                    tempNode.f = tempNode.g + tempNode.h

                    if trebaDodati(tempNode, kju):
                        heapq.heappush(kju, tempNode)

            if tempNode is kraj:
                return -1




def nodeToRect(nodeArr, pozicijeSvihKvadrata, brojKvadrataUOsi):
    rectArr = []
    for node in nodeArr:
        rectArr.append(pozicijeSvihKvadrata[node.x * brojKvadrataUOsi + node.y])
    return rectArr

def nadjiPut(nodeGrid2d, pocetak, kraj, pozicijeSvihKvadrata, brojKvadrataUOsi):
    put = []
    trenutniNode = nodeGrid2d[kraj.x][kraj.y]
    while trenutniNode != pocetak and trenutniNode.roditelj != None:
        put.append(pozicijeSvihKvadrata[trenutniNode.roditelj.x * brojKvadrataUOsi + trenutniNode.roditelj.y])
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
            pocetak.pregledan = True
        elif both[1] == i:
            kraj = nodeGrid2d[i[0] // brojKvadrata][i[0] % brojKvadrata]
        else:
            nodeGrid2d[i[0] // brojKvadrata][i[0] % brojKvadrata].blokiran = True
    
    return (pocetak, kraj)
