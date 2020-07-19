import visualizer as viz
import algoritam as alg
import pygame as pg

def main():
    viz.nacrtajGrid()
    izvrsen = False
    while viz.running == True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                viz.running = False
            if ev.type == pg.MOUSEBUTTONUP:
                viz.obojKvadrat()
            if ev.type==pg.KEYDOWN:
                if ev.key==pg.K_RETURN:
                        if izvrsen == False:
                            viz.obojiPut(alg.dijkatras())
                            izvrsen = True
                        else:
                            viz.reset()
                            izvrsen = False
        pg.display.update()

main()
    
