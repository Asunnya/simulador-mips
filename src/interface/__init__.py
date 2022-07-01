from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame as pg


class Info:
    DISPLAY: pg.Surface
    REGS = dict()
    DATA = dict()

    @staticmethod
    def set_values(display: pg.Surface):
        Info.DISPLAY = display
        for line in open("base/registers.txt", "r").readlines():
            Info.REGS[line[:-1]] = 0


class Colors:
    WHITE = (255, 255, 255)
    GRAY = (100, 100, 100)
    LIGHT_GRAY = (192, 192, 192)
    DARK_GRAY = (51, 51, 51)
