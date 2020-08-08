import pygame as pg

boje = { "bojaPKvadrata": (50, 168, 82),
         "bojaKKvadrata": (168, 64, 50),
         "bojaGrida": (0, 0, 0),
         "bojaPrepreke": (0, 0, 0),
         "bojaPuta": (212, 203, 30),
         "radnaBoja": (66, 147, 245),
         "bojaTrenutna": (245, 47, 50)}

dugmiciZaGui = [{"id": 0, "fontVelicina": 40, "text": "BFS", "boja": (0, 0, 0), "backgroundBoja": (67, 183, 250), "veliki": False},
                {"id": 1, "fontVelicina": 40, "text": "DFS", "boja": (0, 0, 0), "backgroundBoja": (67, 183, 250), "veliki": False},
                {"id": 2, "fontVelicina": 40, "text": "Dijkstra", "boja": (0, 0, 0), "backgroundBoja": (67, 183, 250), "veliki": False},
                {"id": 3, "fontVelicina": 40, "text": "A*", "boja": (0, 0, 0), "backgroundBoja": (67, 183, 250), "veliki": False},

                {"id": 100, "fontVelicina": 52, "text": "Start", "boja": (0, 0, 0), "backgroundBoja": (67, 183, 250), "veliki": True},
                {"id": 101, "fontVelicina": 52, "text": "Reset", "boja": (0, 0, 0), "backgroundBoja": (67, 183, 250), "veliki": True}
]

def main(sirina, visina, GUIdodatak, velicinaKvadrata):
    brojKvadrataUOsi = visina // velicinaKvadrata
    pg.init()
    ekran = pg.display.set_mode((sirina, visina))
    ekran.fill(pg.Color("white"))

    kvadrati = nacrtajGrid(ekran, brojKvadrataUOsi, velicinaKvadrata)

    dugmiciZaCrtanjeArr = dobijDugmiceZaCrtanje(GUIdodatak, visina, dugmiciZaGui, "Roboto-Regular.ttf", 20, 20)

    nacrtajDugmice(ekran, dugmiciZaCrtanjeArr)

    pozicijeDugmica = []
    for i in range(len(dugmiciZaCrtanjeArr)):
        pozicijeDugmica.append({"pozicija": dugmiciZaCrtanjeArr[i][1].copy(), "id": dugmiciZaGui[i]["id"]})

    return (ekran, kvadrati, pozicijeDugmica)

def nacrtajDugmice(ekran, dugmiciZaCrtanjeArr):
    for dugme in dugmiciZaCrtanjeArr:
        internalRect = dugme[0].get_rect()
        internalRect.center = (dugme[1].centerx, dugme[1].centery)
        pg.draw.rect(ekran, (67, 183, 250), dugme[1])
        pg.draw.rect(ekran, (0,0,0), dugme[1], 1)
        ekran.blit(dugme[0], internalRect)

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
    pozicijeObojenihKvadrata = []
    nacrtanPocetak = False
    nacrtanKraj = False
    def obojKvadratInternal():
        nonlocal nacrtanKraj, nacrtanPocetak, pozicijeObojenihKvadrata
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
        return pozicijeObojenihKvadrata
    return obojKvadratInternal

def dobijDugmiceZaCrtanje(GUIdodatak, visina, dugmiciList, fontIme, topPadding, leftPadding):
    dugmiciRectArr = []
    textRect = pg.Rect((0, 0, 0, 0))
    odrediMestoDugmetaFunc = odrediMestoDugmeta(GUIdodatak, visina, topPadding, leftPadding)
    for i in range (0, len(dugmiciList)):
        temp = dugmiciList[i]
        textSurface = dobijDugme(fontIme, temp["fontVelicina"], temp["text"], temp["boja"], temp["backgroundBoja"])
        mestoDugmeta = odrediMestoDugmetaFunc(temp["veliki"])
        textRect.width = mestoDugmeta[1][0]
        textRect.height = mestoDugmeta[1][1]
        textRect.topleft = mestoDugmeta[0]
        dugmiciRectArr.append((textSurface, textRect.copy()))

    return dugmiciRectArr

def odrediMestoDugmeta(GUIdodatak, visina, topPadding, leftPadding, visinaVelikog = 100, visinaMalog = 75):
    ostaloVisine = visina
    ostaloSirine = GUIdodatak
    def odrediMestoDugmetaInternal(veliki):
        nonlocal ostaloVisine, ostaloSirine
        ###
        sirinaMalog = GUIdodatak // 2 - leftPadding * 2
        ###

        (x, y) = (None, None)
        (sirina, visinaInternal) = (None, None)

        if veliki == True:
            if visina - ostaloVisine + visinaVelikog < 0:
                raise NameError("nema mesta u visina za crtanje velikog dugmeta")

            (sirina, visinaInternal) = (GUIdodatak - leftPadding * 2, visinaVelikog)
            (x, y) = (visina + leftPadding, visina - ostaloVisine + topPadding)

            ostaloVisine -= (visinaVelikog + topPadding)
            #ostaloSirine -= (GUIdodatak - leftPadding * 2)
            ostaloSirine = GUIdodatak
        else:
            if visina - ostaloVisine + visinaMalog < 0:
                raise NameError("nema mesta u visini za crtanje malog dugmeta")

            (sirina, visinaInternal) = (GUIdodatak // 2 - leftPadding * 2, visinaMalog)
            (x, y) = (visina + leftPadding if ostaloSirine != (GUIdodatak // 2) else visina + ostaloSirine + leftPadding, visina - ostaloVisine + topPadding)
            

            ###
            #ostaloSirine -= GUIdodatak // 2
            ostaloSirine = GUIdodatak if ostaloSirine == (GUIdodatak // 2) else (GUIdodatak // 2)
            ostaloVisine = (ostaloVisine - (visinaMalog + topPadding)) if ostaloSirine == GUIdodatak else ostaloVisine
            ###
        return ((x, y),(sirina, visinaInternal))
    return odrediMestoDugmetaInternal

def dobijDugme(fontIme, fontVelicina, text, boja, backgroundBoja):
    font = pg.font.Font(fontIme, fontVelicina)

    textSurface = font.render(text, True, boja)

    return textSurface

def obojiAktivnoDugme(ekran):
    indexObojenogDumeta = -1
    oldDugme = None
    oldPozicija = None
    def obojiAktivnoDugmeInternal(dugmeID, dugmePozicija):
        nonlocal indexObojenogDumeta, oldDugme, oldPozicija
        def find(lst, key, value):
            for i, dic in enumerate(lst):
                if dic[key] == value:
                    return i
            return -1

        if oldDugme != None:
            textSurface = dobijDugme("Roboto-Regular.ttf", oldDugme["fontVelicina"], oldDugme["text"], oldDugme["boja"], oldDugme["backgroundBoja"])
            internalRect = textSurface.get_rect()
            internalRect.center = (oldPozicija.centerx, oldPozicija.centery)
            pg.draw.rect(ekran, (67, 183, 250), oldPozicija)
            pg.draw.rect(ekran, (0,0,0), oldPozicija, 1)
            ekran.blit(textSurface, internalRect)
        
        indexObojenogDumeta = find(dugmiciZaGui, "id", dugmeID)
        dugme = dugmiciZaGui[indexObojenogDumeta]

        textSurface = dobijDugme("Roboto-Regular.ttf", dugme["fontVelicina"], dugme["text"], dugme["boja"], dugme["backgroundBoja"])
        internalRect = textSurface.get_rect()
        internalRect.center = (dugmePozicija.centerx, dugmePozicija.centery)
        pg.draw.rect(ekran, (242, 75, 41), dugmePozicija)
        pg.draw.rect(ekran, (0,0,0), dugmePozicija, 1)
        ekran.blit(textSurface, internalRect)

        oldDugme = dugme
        oldPozicija = dugmePozicija

    return obojiAktivnoDugmeInternal



