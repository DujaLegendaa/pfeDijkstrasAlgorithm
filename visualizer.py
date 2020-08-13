import pygame as pg


### Korisnicke Promenjive ###
boje = { "bojaPKvadrata": (50, 168, 82),
         "bojaKKvadrata": (168, 64, 50),
         "bojaGrida": (0, 0, 0),
         "bojaPrepreke": (0, 0, 0),
         "bojaPuta": (212, 203, 30),
         "radnaBoja": (66, 147, 245),
         "bojaTrenutna": (245, 47, 50)}
##############################

def obojiPut(bPut, ekran, nadjiKvadratUGridu):
    i = 0
    def obojiPutInternal(put, nodeGrid2d = None):
        nonlocal i
        if nodeGrid2d != None:
            nadjiKvadratUGriduFunc = nadjiKvadratUGridu(nodeGrid2d)

            if nadjiKvadratUGriduFunc(put[i]).distanca != 1.0:
                i += 1
                return False
            

            if i == len(put) - 1:
                return True
            boja = boje["radnaBoja"]
            pg.draw.rect(ekran, boja, put[i], 0)
            pg.draw.rect(ekran, boje["bojaGrida"], put[i], 1)
            if nadjiKvadratUGriduFunc(put[i + 1]).distanca == 1.0:
                pg.draw.rect(ekran, boje["bojaTrenutna"], put[i + 1], 0)
            

        else:
            if i == len(put):
                return True
            boja = boje["bojaPuta"]
            pg.draw.rect(ekran, boja, put[i],0)
            pg.draw.rect(ekran, boje["bojaGrida"], put[i], 1)
        
        i += 1
        return False
    return obojiPutInternal

