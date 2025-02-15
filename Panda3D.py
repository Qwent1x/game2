from direct.showbase.ShowBase import ShowBase
from Mapmanager import Mapmanager
from hero import Hero
import  pickle
pos = (0, 0, 3.5)

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager(self)  # Передаємо об'єкт ShowBase до Mapmanager
        self.camLens.setFov(90)  # Встановлюємо поле огляду камери
        self.land.addBlock((0, 0, 0))
        self.land.loadLand("land.txt")
        self.hero = Hero(pos, self.land)

game = Game()
game.run()
