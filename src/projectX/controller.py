import bge
from bge import events, render
from mouse import *

scene = bge.logic.getCurrentScene()


class Controller():

    def __init__(self):
        self.frame = 0
        self.mouse = Mouse(self)
        self.x = 0  # is used for testing purpose in addO()
        self.y = 0  # is used for testing purpose in addO()
        self.selectedUnits = []
        self.movingUnits = []

    def addO(cont):
        """ Temporary fonction used to test the controller, the spawn point move,
        the subclassing of blender game objects and spawning them, well, it actually test everything ^^"""
        scene = bge.logic.getCurrentScene()
        scene.objects['SpawnP'].worldPosition.x = bge.c.x
        scene.objects['SpawnP'].worldPosition.y = bge.c.y
        scene.addObject('Unit', scene.objects['SpawnP'])
        bge.c.x += 1
        bge.c.y += 1


def main():
    """called once by the "Always" sensor named InitGame,
    will remove sensors if we have timeits kinda complicated"""
    bge.c = Controller()


def update(cont):
    """called every frame by the "Always" sensor named Update
    this is the main loop"""
    bge.c.frame += 1
    render.showMouse(True)
    if bge.logic.mouse.events:
        bge.c.mouse.select(cont)
    if logic.keyboard.events[events.XKEY] == logic.KX_INPUT_JUST_ACTIVATED:
        bge.c.addO()
    if logic.keyboard.events[events.ZKEY] == logic.KX_INPUT_JUST_ACTIVATED:
        print(bge.c.selectedUnits)
    if bge.c.movingUnits:
        for obj in bge.c.movingUnits:
            x = obj.worldPosition[0]
            y = obj.worldPosition[1]
            obj.move(x, y)
