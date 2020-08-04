import pygame as pg

boje = { "bojaPKvadrata": (50, 168, 82),
         "bojaKKvadrata": (168, 64, 50),
         "bojaGrida": (0, 0, 0),
         "bojaPrepreke": (0, 0, 0),
         "bojaPuta": (212, 203, 30),
         "radnaBoja": (66, 147, 245),
         "bojaTrenutna": (245, 47, 50)}

nacrtanPocetak = False
nacrtanKraj = False
pozicijeObojenihKvadrata = []

def main(sirina, visina, velicinaKvadrata):
    brojKvadrataUOsi = visina // velicinaKvadrata
    pg.init()
    ekran = pg.display.set_mode((sirina, visina))
    ekran.fill(pg.Color("white"))

    kvadrati = nacrtajGrid(ekran, brojKvadrataUOsi, velicinaKvadrata)

    return (ekran, kvadrati)

def nacrtajGrid(ekran, brojKvadrataUOsi, velicinaKvadrata):
    kvadrati = []
    for x in range(brojKvadrataUOsi):
        for y in range(brojKvadrataUOsi):
            rect = pg.Rect(x * velicinaKvadrata, y * velicinaKvadrata,
                           velicinaKvadrata, velicinaKvadrata)
            kvadrati.append(rect)
            pg.draw.rect(ekran, boje["bojaGrida"], rect, 1)

    return kvadrati

def obojKvadrat(kvadrati, ekran):
    global nacrtanPocetak, nacrtanKraj, pozicijeObojenihKvadrata 
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

    if len(pozicijeObojenihKvadrata) >= 2:
        return pozicijeObojenihKvadrata
    else:
        return False

