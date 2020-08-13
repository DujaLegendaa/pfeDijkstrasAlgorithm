import visualizer as viz
import algoritam as alg
import pygame as pg
import GUI

def handleButtonPress(ekran, pozicijeiIDDugmica, obojiAktivnoDugmeFunc):
    brojAlgoritma = -1
    brojOpcije = -1
    brojCetkice = -1
    def handleButtonPressInternal():
        nonlocal brojAlgoritma, brojOpcije, brojCetkice
        posMisa = pg.mouse.get_pos()
        for pozicijaiID in pozicijeiIDDugmica:
            if pozicijaiID["pozicija"].collidepoint(posMisa):
                if pozicijaiID["id"] < 100:
                    brojAlgoritma = pozicijaiID["id"]
                elif pozicijaiID["id"] >= 100 and pozicijaiID["id"] < 200:
                    brojOpcije = pozicijaiID["id"]
                elif pozicijaiID["id"] >= 200:
                    brojCetkice = pozicijaiID["id"]
                else:
                    raise NameError("pogresan id dugmeta")
                obojiAktivnoDugmeFunc(pozicijaiID["id"], pozicijaiID["pozicija"])
        return (brojAlgoritma, brojOpcije, brojCetkice)
    return handleButtonPressInternal

def main():
    FPS = 100;

    visina = 600
    GUIdodatak = 400
    sirina = visina + GUIdodatak
    velicinaKvadrata = 20

    nacrtanPut = False
    nacrtanNajkraciPut = False

    (najkraciPut, predjeniNodeovi) = (None, None)
    (brojAlgoritma, brojOpcije) = (-1, -1)
    (ekran, kvadrati, pozicijeiIDDugmica) = GUI.main(sirina, visina, GUIdodatak, velicinaKvadrata)

    obojKvadratFunc = GUI.obojKvadrat(kvadrati, ekran)
    obojAktivnoDugmeFunc = GUI.obojiAktivnoDugme(ekran)
    handleButtonPressFunc = handleButtonPress(ekran, pozicijeiIDDugmica, obojAktivnoDugmeFunc)
    obojPutRadaFunc = viz.obojiPut(True, ekran, alg.nadjiKvadratUGridu)
    obojNajkraciPut = viz.obojiPut(False, ekran, alg.nadjiKvadratUGridu)

    running = True

    while running == True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False
            if ev.type == pg.MOUSEBUTTONUP:
                (brojAlgoritma, brojOpcije, brojCetkice) = handleButtonPressFunc()
                pozicijeObojenihKvadrata = obojKvadratFunc(brojCetkice)

        if brojAlgoritma != -1 and brojOpcije == 100:
            (najkraciPut, predjeniNodeovi, nodeGrid2d) = alg.switchAlgoritma(brojAlgoritma, pozicijeObojenihKvadrata, kvadrati)
            brojOpcije = -1
        if brojOpcije == 101:
            return main()

        if predjeniNodeovi != None and nacrtanPut == False and nacrtanNajkraciPut == False:
            nacrtanPut = obojPutRadaFunc(predjeniNodeovi, nodeGrid2d)
        if najkraciPut != None and nacrtanPut == True and nacrtanNajkraciPut == False:
            nacrtanNajkraciPut = obojNajkraciPut(najkraciPut)

        pg.time.Clock().tick(FPS)
        pg.display.update()


main()
    
