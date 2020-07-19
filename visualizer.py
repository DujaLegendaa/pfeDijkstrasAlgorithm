import pygame as pg

(visina, sirina) = (600, 600)
running = True
kvadrati = []
pozicijeObojenihKvadrata = []
nacrtanPocetak = False
nacrtanKraj = False
pg.init()
ekran = pg.display.set_mode((visina, sirina))
ekran.fill(pg.Color("white"))


def nacrtajGrid():
    global pozicijeKvadrata
    velicinaKvadrata = 20
    bojaKvadrata = (0, 0, 0)
    for x in range(sirina // velicinaKvadrata):
        for y in range(visina // velicinaKvadrata):
            rect = pg.Rect(x * velicinaKvadrata, y * velicinaKvadrata,
                           velicinaKvadrata, velicinaKvadrata)
            kvadrati.append(rect)
            pg.draw.rect(ekran, bojaKvadrata, rect, 1)



def obojKvadrat():
    global  nacrtanPocetak, nacrtanKraj, pozicijeObojenihKvadrata
    bojaPKvadrata = (0,255,0)
    bojaKKvadrata = (0,0,255)
    posMisa = pg.mouse.get_pos()

    for kvadrat in kvadrati:
        if kvadrat.collidepoint(posMisa):
            if nacrtanPocetak == False:
                bojaKvadrata = bojaPKvadrata
                nacrtanPocetak = True
            elif nacrtanKraj == False:
                bojaKvadrata = bojaKKvadrata
                nacrtanKraj = True
            else:
                bojaKvadrata = (0,0,0)
            pg.draw.rect(ekran, bojaKvadrata, kvadrat, 0)
            pozicijeObojenihKvadrata.append(kvadrat)

def obojiNode(rect, color):
    pg.draw.rect(ekran, color, rect, 0)  

