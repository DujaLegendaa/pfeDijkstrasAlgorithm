import pygame as pg

### Korisnicke Promenjive ###
boje = { "bojaPKvadrata": (50, 168, 82),
         "bojaKKvadrata": (168, 64, 50),
         "bojaGrida": (0, 0, 0),
         "bojaPrepreke": (0, 0, 0),
         "bojaPuta": (212, 203, 30),
         "radnaBoja": (66, 147, 245),
         "bojaTrenutna": (245, 47, 50)}
velicinaKvadrata = 20
##############################

running = True

def reset():
    global nacrtanPocetak, nacrtanKraj
    ekran.fill(pg.Color("white"))
    kvadrati.clear()
    pozicijeObojenihKvadrata.clear()
    nacrtanPocetak = False
    nacrtanKraj = False
    nacrtajGrid()


def obojiPut(put, i, bPut, ekran):
    if(bPut == True):
        boja = boje["radnaBoja"]
    else:
        boja = boje["bojaPuta"]
    if(i < len(put)):
        pg.draw.rect(ekran, boja, put[i - 1], 0)
        pg.draw.rect(ekran, boje["bojaGrida"], put[i - 1], 1)
        pg.draw.rect(ekran, boje["bojaTrenutna"], put[i], 0)
        return i + 1
    else:
        if(bPut == False):
            pg.draw.rect(ekran, boja, put[i-1],0)
            pg.draw.rect(ekran, boje["bojaGrida"], put[i - 1], 1)
        return -1

