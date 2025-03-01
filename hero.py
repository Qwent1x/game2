class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = loader.loadModel('hero.model.obj')
        self.hero.setColor(0,0,0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        self.mode = True

    def accept_events(self):
        base.accept('k', self.land.saveMap)
        base.accept('l', self.land.loadMap)

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 4.5)
        self.cameraOn = True

    def cameraUp(self):
        base.mouseInterfaceNode.setPos(-12.5, -12.5, -4)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False


    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def forward(self):
        pass

    def back(self):
        pass

    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('a', self.turn_left)
        base.accept('a' + '-repeat', self.turn_left)
        base.accept('d', self.turn_right)
        base.accept('d' + '-repeat', self.turn_right)
        base.accept('s', self.back)
        base.accept('s' + '-repeat' , self.back)
        base.accept('w', self.forward)
        base.accept('w' + '-repeat' , self.forward)
        base.accept('e', self.up)
        base.accept('e' + '-repeat' , self.up)
        base.accept('q', self.down)
        base.accept('q' + '-repeat' , self.down)
        base.accept('z', self.changeMode)
        base.accept('b', self.build)
        base.accept('1', self.build1)
        base.accept('2', self.build2)
        base.accept('3', self.build3)
        base.accept('v', self.destroy)



    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return from_x + dx,from_y + dy, from_z

    def check_dir(self, angle):
        if angle >=0 and angle <= 20:
            return 0, -1
        elif angle >= 20 and angle <= 65:
            return +1, -1
        elif angle >= 65 and angle <= 110:
            return +1, 0
        elif angle >= 110 and angle <= 155:
            return +1, +1
        elif angle >= 155 and angle <= 200:
            return 0, +1
        elif angle >= 200 and angle <= 245:
            return -1, +1
        elif angle >= 245 and angle <= 290:
            return -1, 0
        elif angle >= 290 and angle <= 335:
            return -1, -1
        elif angle >= 335:
            return 0, -1

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def back(self):
        angle =(self.hero.getH()+180) % 360
        self.move_to(angle)

    def forward(self):
        angle =(self.hero.getH()+0) % 360
        self.move_to(angle)

    def left(self):
        angle =(self.hero.getH()+90) % 360
        self.move_to(angle)

    def right(self):
        angle =(self.hero.getH()+270) % 360
        self.move_to(angle)

    def up(self):
        self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        self.hero.setZ(self.hero.getZ() - 1)

    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)
    
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.landmfindHighestEmpty(pos)
            self.hero,setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def build1(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addFloor(pos)
        else:
            self.land.buildFloor(pos)

    def build2(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock2(pos)
        else:
            self.land.buildBlock2(pos)

    def build3(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addWhite(pos)
        else:
            self.land.buildWhite(pos)    

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)