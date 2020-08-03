import pygame as pg

### Korisnicke Promenjive ###
(visina, sirina) = (600, 600)
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
kvadrati = []
pozicijeObojenihKvadrata = []
nacrtanPocetak = False
nacrtanKraj = False
pg.init()
ekran = pg.display.set_mode((visina, sirina))
ekran.fill(pg.Color("white"))

def reset():
    global nacrtanPocetak, nacrtanKraj
    ekran.fill(pg.Color("white"))
    kvadrati.clear()
    pozicijeObojenihKvadrata.clear()
    nacrtanPocetak = False
    nacrtanKraj = False
    nacrtajGrid()

def nacrtajGrid():
    global pozicijeKvadrata
    for x in range(sirina // velicinaKvadrata):
        for y in range(visina // velicinaKvadrata):
            rect = pg.Rect(x * velicinaKvadrata, y * velicinaKvadrata,
                           velicinaKvadrata, velicinaKvadrata)
            kvadrati.append(rect)
            pg.draw.rect(ekran, boje["bojaGrida"], rect, 1)



def obojKvadrat():
    global  nacrtanPocetak, nacrtanKraj, pozicijeObojenihKvadrata
    posMisa = pg.mouse.get_pos()

    for kvadrat in kvadrati:
        if kvadrat.collidepoint(posMisa):
            if nacrtanPocetak == False:
                bojaKvadrata = boje["bojaPKvadrata"]
                nacrtanPocetak = True
            elif nacrtanKraj == False:
                bojaKvadrata = boje["bojaKKvadrata"]
                nacrtanKraj = True
            else:
                bojaKvadrata = boje["bojaPrepreke"]
            pg.draw.rect(ekran, bojaKvadrata, kvadrat, 0)
            pozicijeObojenihKvadrata.append(kvadrat)


def obojiPut(put, i, bPut):
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

