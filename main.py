import visualizer as viz
import algoritam as alg
import pygame as pg

def main():
    FPS = 60;
    i = 2
    k = 0
    (put, predjeniNodeovi) = (None, None)
    viz.nacrtajGrid()
    izvrsen = False
    while viz.running == True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                viz.running = False
            if ev.type == pg.MOUSEBUTTONUP and izvrsen == False:
                viz.obojKvadrat()
            if ev.type==pg.KEYDOWN:
                if ev.key==pg.K_RETURN:
                        if izvrsen == False:
                            (put, predjeniNodeovi) = alg.main()
                            izvrsen = True
                        else:
                            viz.reset()
                            i = 2
                            k = 1
                            (put, predjeniNodeovi) = (None, None)
                            izvrsen = False
        if((predjeniNodeovi != None) and (i == 1 or i != -1)):
            i = viz.obojiPut(predjeniNodeovi, i, True)
        if(i == -1 and put != None and (k == 0 or k!= -1)):
            k = viz.obojiPut(put, k, False)
        pg.time.Clock().tick(FPS)
        pg.display.update()


main()
    
