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



def main():
    hVDistanca = 1.0
    dDistanca = 1.4

    pozicijeObojenihKvadrata = viz.pozicijeObojenihKvadrata
    pozicijeSvihKvadrata = viz.kvadrati
    brojKvadrata = math.floor(math.sqrt(len(pozicijeSvihKvadrata)))

    pocetak = viz.pozicijeObojenihKvadrata[0]
    kraj = viz.pozicijeObojenihKvadrata[2]

    nodeGrid1d = []
    nodeGrid2d = []
    
    for col in range(brojKvadrata):
        for row in range(brojKvadrata):
            nodeGrid1d.append(Node(col, row))
        nodeGrid2d.append(list(nodeGrid1d))
        nodeGrid1d.clear()

    both = []
    for i in range(len(pozicijeObojenihKvadrata)):
        for j in range(len(pozicijeSvihKvadrata)):
            if pozicijeObojenihKvadrata[i] == pozicijeSvihKvadrata[j]:
                both.append((j, i))
    
    print(both)
    for i in both:
        if both[0] == i:
            pocetak = nodeGrid2d[i[0] // brojKvadrata][i[0] % brojKvadrata]
        elif both[1] == i:
            kraj = nodeGrid2d[i[0] // brojKvadrata][i[0] % brojKvadrata]
        else:
            nodeGrid2d[i[0] // brojKvadrata][i[0] % brojKvadrata].blokiran = True
    
    pocetak.distanca = 0
    velicina = len(nodeGrid2d)
    
    for col in range(brojKvadrata):
        for row in range(brojKvadrata):
            print(nodeGrid2d[col][row].blokiran)


    priorityQueue = []
    heapq.heapify(priorityQueue)

    heapq.heappush(priorityQueue, pocetak)

    while len(priorityQueue) > 0:
        trenutniNode = heapq.heappop(priorityQueue)
        viz.obojiNode(pozicijeSvihKvadrata[trenutniNode.x * brojKvadrata + trenutniNode.y], (100, 0, 0))
        tempNode = None

        #dole
        if trenutniNode.y + 1 < velicina:

            #dole dole
            tempNode = nodeGrid2d[trenutniNode.x][trenutniNode.y + 1]
            if tempNode.pregledan == False and (tempNode.blokiran == False ) and (tempNode.distanca > trenutniNode.distanca + hVDistanca):
                tempNode.distanca = trenutniNode.distanca + hVDistanca
                tempNode.roditelj = trenutniNode
                heapq.heappush(priorityQueue, tempNode)

            #dole desno
            if trenutniNode.x + 1 < velicina:
                tempNode = nodeGrid2d[trenutniNode.x + 1][trenutniNode.y + 1]
                if tempNode.pregledan == False and (tempNode.blokiran == False) and (tempNode.distanca > trenutniNode.distanca + dDistanca):
                    tempNode.distanca = trenutniNode.distanca + dDistanca
                    tempNode.roditelj = trenutniNode
                    heapq.heappush(priorityQueue, tempNode)

            #dole levo
            if trenutniNode.x - 1 > 0:
                tempNode = nodeGrid2d[trenutniNode.x - 1][trenutniNode.y + 1]
                if tempNode.pregledan == False and (tempNode.blokiran == False) and (tempNode.distanca > trenutniNode.distanca + dDistanca):
                    tempNode.distanca = trenutniNode.distanca + dDistanca
                    tempNode.roditelj = trenutniNode
                    heapq.heappush(priorityQueue, tempNode)

        #gore
        if trenutniNode.y - 1 >= 0:

            #gore gore
            tempNode = nodeGrid2d[trenutniNode.x][trenutniNode.y - 1]
            if tempNode.pregledan == False and (tempNode.blokiran == False) and (tempNode.distanca > trenutniNode.distanca + hVDistanca):
                tempNode.distanca = trenutniNode.distanca + hVDistanca
                tempNode.roditelj = trenutniNode
                heapq.heappush(priorityQueue, tempNode)

            #gore desno
            if trenutniNode.x + 1 < velicina:
                tempNode = nodeGrid2d[trenutniNode.x + 1][trenutniNode.y - 1]
                if tempNode.pregledan == False and (tempNode.blokiran == False) and (tempNode.distanca > trenutniNode.distanca + dDistanca):
                    tempNode.distanca = trenutniNode.distanca + dDistanca
                    tempNode.roditelj = trenutniNode
                    heapq.heappush(priorityQueue, tempNode)

            #gore levo
            if trenutniNode.x - 1 > 0:
                tempNode = nodeGrid2d[trenutniNode.x - 1][trenutniNode.y - 1]
                if tempNode.pregledan == False and (tempNode.blokiran == False) and (tempNode.distanca > trenutniNode.distanca + dDistanca):
                    tempNode.distanca = trenutniNode.distanca + dDistanca
                    tempNode.roditelj = trenutniNode
                    heapq.heappush(priorityQueue, tempNode)

        #desno
        if trenutniNode.x + 1 < velicina:
            tempNode = nodeGrid2d[trenutniNode.x + 1][trenutniNode.y]
            if tempNode.pregledan == False and (tempNode.blokiran == False) and (tempNode.distanca > trenutniNode.distanca + hVDistanca):
                tempNode.distanca = trenutniNode.distanca + hVDistanca
                tempNode.roditelj = trenutniNode
                heapq.heappush(priorityQueue, tempNode)

        #levo
        if trenutniNode.x - 1 > 0:
            tempNode = nodeGrid2d[trenutniNode.x - 1][trenutniNode.y]
            if tempNode.pregledan == False and (tempNode.blokiran == False) and (tempNode.distanca > trenutniNode.distanca + hVDistanca):
                tempNode.distanca = trenutniNode.distanca + hVDistanca
                tempNode.roditelj = trenutniNode
                heapq.heappush(priorityQueue, tempNode)

        trenutniNode.pregledan = True

    put = []

    trenutniNode = nodeGrid2d[kraj.x][kraj.y]

    while trenutniNode.roditelj != None:
        put.append(trenutniNode.roditelj)
        trenutniNode = trenutniNode.roditelj

    for item in put:
        viz.obojiNode(pozicijeSvihKvadrata[item.x * brojKvadrata + item.y], (200, 200, 0))

    



 


    


