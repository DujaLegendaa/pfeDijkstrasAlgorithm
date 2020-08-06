import visualizer as viz
import algoritam as alg
import pygame as pg
import GUI

visina = 600
GUIdodatak = 400
sirina = visina + GUIdodatak
velicinaKvadrata = 20

def handleButtonPress(pozicijeiTextDugmica):
    brojAlgoritma = -1
    brojOpcije = -1
    def handleButtonPressInternal():
        nonlocal brojAlgoritma, brojOpcije
        posMisa = pg.mouse.get_pos()
        for pozicijaiText in pozicijeiTextDugmica:
            if pozicijaiText["pozicija"].collidepoint(posMisa):
                if pozicijaiText["text"] == "BFS":
                    brojAlgoritma = 0
                if pozicijaiText["text"] == "DFS":
                    brojAlgoritma = 1
                if pozicijaiText["text"] == "Dijkstra":
                    brojAlgoritma = 2
                if pozicijaiText["text"] == "A*":
                    brojAlgoritma = 3
                if pozicijaiText["text"] == "Start":
                    brojOpcije = 100
                if pozicijaiText["text"] == "Resset":
                    brojOpcije = 101
        return (brojAlgoritma, brojOpcije)
    return handleButtonPressInternal
def main():
    FPS = 30;
    i = 2
    k = 0
    (put, predjeniNodeovi) = (None, None)
    (brojAlgoritma, brojOpcije) = (-1, -1)
    (ekran, kvadrati, pozicijeiTextDugmica) = GUI.main(sirina, visina, GUIdodatak, velicinaKvadrata)
    obojKvadratFunc = GUI.obojKvadrat(kvadrati, ekran)
    handleButtonPressFunc = handleButtonPress(pozicijeiTextDugmica)
    izvrsen = False
    while viz.running == True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                viz.running = False
            if ev.type == pg.MOUSEBUTTONUP and izvrsen == False:
                pozicijeObojenihKvadrata = obojKvadratFunc()
                (brojAlgoritma, brojOpcije) = handleButtonPressFunc()
            if ev.type==pg.KEYDOWN:
                if ev.key==pg.K_RETURN:
                        if izvrsen == False:
                            (put, predjeniNodeovi) = alg.switchAlgoritma(brojAlgoritma, pozicijeObojenihKvadrata, kvadrati)
                            izvrsen = True
                        else:
                            viz.reset()
                            i = 2
                            k = 1
                            (put, predjeniNodeovi) = (None, None)
                            izvrsen = False
            
        if brojAlgoritma != -1 and brojOpcije == 100:
            (put, predjeniNodeovi) = alg.switchAlgoritma(brojAlgoritma, pozicijeObojenihKvadrata, kvadrati)
            brojOpcije = -1
        if((predjeniNodeovi != None) and (i == 1 or i != -1)):
            i = viz.obojiPut(predjeniNodeovi, i, True, ekran)
        if(i == -1 and put != None and (k == 0 or k!= -1)):
            k = viz.obojiPut(put, k, False, ekran)
        pg.time.Clock().tick(FPS)
        pg.display.update()


main()
    
