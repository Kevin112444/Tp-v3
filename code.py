from cmu_112_graphics import *
import os

class MyApp(App):
    
    def appStarted(self):
        self.timerDelay = 10
        self.background = self.loadImage('Assets/Backgrounds/background.png')
        self.xd= 0
        self.age = 0
        self.alive = []
        self.sprites = []
        self.spriteCounters = []
        self.absSpriteLocation = []
        self.relSpriteLocation= []
        self.icons = []
        self.iconLoader()
        allyBase = self.Base()
        enemyBase = self.Base()
        self.baseSprites = []
        self.baseCounter = 0
        self.baseAnimate()
        self.money = 1000

    class Units(object):
        def __init__(self,health,attack,movespd,range,cost):
            self.health = health
            self.attack = attack
            self.moveSpeed = movespd
            self.range = range
            self.cost = cost
            self.state = 'walk'
            self.spriteCounter = 0
        
        def __eq__(self, other):
            return (isinstance(other, A) and (self.x == other.x))
    
    class Base(Units):
        def __init__(self):
            self.health = 10000
     
    class Bat(Units):
        spritesheet = 'Assets/Sprites/Age0/Bat.png'
        def __init__(self):
            super().__init__(10,1,10,0,10)
            
        def action(self):
            if self.state == 'walk':
                return (0,4)
            elif self.state == 'fight':
                return (30,42)

    class Owl(Units):
        spritesheet = 'Assets/Sprites/Age0/Owl.png'
        def __init__(self): 
            super().__init__(10,1,15,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,9)
            elif self.state == 'fight':
                return (9,18)
                    
    class Peacock(Units):
        spritesheet = 'Assets/Sprites/Age0/Peacock.png'
        def __init__(self):
            super().__init__(10,1,10,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (9,18)
                
    class Rat(Units):
        spritesheet = 'Assets/Sprites/Age0/Rat.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (9,18)
            elif self.state == 'fight':
                return (0,9)

    class Anubis(Units):
        spritesheet = 'Assets/Sprites/Age1/Anubis.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (42,48)
            elif self.state == 'fight':
                return (2,5)
    
    class Knight(Units):
        spritesheet = 'Assets/Sprites/Age1/Knight.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,5)
            elif self.state == 'fight':
                return (11,13)
    
    class Slime(Units):
        spritesheet = 'Assets/Sprites/Age1/Slime.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (9,14)
            elif self.state == 'fight':
                return (21,26)

    class Spore(Units):
        spritesheet = 'Assets/Sprites/Age1/Spore.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (0,5)
    
    class EarthWorm(Units):
        spritesheet = 'Assets/Sprites/Age2/EarthWorm.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (18,27)
            elif self.state == 'fight':
                return (3,5)
    
    class Golem(Units):
        spritesheet = 'Assets/Sprites/Age2/Golem.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (6,11)
            elif self.state == 'fight':
                return (18,26)
    
    class Phoenix(Units):
        spritesheet = 'Assets/Sprites/Age2/Phoenix.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (9,18)
    
    class WereWolf(Units):
        spritesheet = 'Assets/Sprites/Age2/WereWolf.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,6)
            elif self.state == 'fight':
                return (12,14)
    
    class DoppelSlime(Units):
        spritesheet = 'Assets/Sprites/Age3/DoppelSlime.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
            
        def action(self):
            if self.state == 'walk':
                return (15,21)
            elif self.state == 'fight':
                return (9,18)
    
    class Slayer(Units):
        spritesheet = 'Assets/Sprites/Age3/Slayer.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,35)
            elif self.state == 'fight':
                return (11,14)
    
    class Whale(Units):
        spritesheet = 'Assets/Sprites/Age3/Whale.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (36,45)
            elif self.state == 'fight':
                return (2,7)

    class Wyvern(Units):
        spritesheet = 'Assets/Sprites/Age3/Wyvern.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,8)
            elif self.state == 'fight':
                return (36,42)

    class Angel(Units):
        spritesheet = 'Assets/Sprites/Age4/Angel.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (0,9)
    
    class Boss(Units):
        spritesheet = 'Assets/Sprites/Age4/Boss.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (0,7)
    
    class Overmind(Units):
        spritesheet = 'Assets/Sprites/Age4/Overmind.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (5,13)
            elif self.state == 'fight':
                return (4,7)
    
    class Spike(Units):
        spritesheet = 'Assets/Sprites/Age4/Spike.png'
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,9)
            elif self.state == 'fight':
                return (9,15)

    #def keyPressed(self,event):
        
    def spawn(self,unit):
        self.alive.append(unit)
        self.spriteCounters.append(0)
        self.spriteLocation.append(.05 * self.width)
        self.money -= unit.cost
        self.Animate()

    def mousePressed(self,event):
        if (.75 * self.width <= event.x <= .85 * self.width) and (.05 * self.height <= event.y <= .15 * self.height): 
            self.age += 1
        if (.85 * self.height) <= event.y <= (.99 * self.height):
            if (.01 * self.width) <= event.x <= (.09 * self.width):
                if self.age == 0:
                    newBat = 'bat' + str(len(self.sprites))
                    newBat = self.Bat()
                    self.spawn(newBat)
                elif self.age == 1:
                    newAnubis = 'anubis'+ str(len(self.sprites))
                    newAnubis = self.Anubis()
                    self.spawn(newAnubis)
                elif self.age == 2:
                    newEarthworm = 'earthworm'+ str(len(self.sprites))
                    newEarthworm = self.EarthWorm()
                    self.spawn(newEarthworm)
                elif self.age == 3:
                    newDoppelSlime = 'doppelslime'+ str(len(self.sprites))
                    newDoppelSlime = self.DoppelSlime()
                    self.spawn(newDoppelSlime)
                elif self.age == 4:
                    newAngel = 'angel'+ str(len(self.sprites))
                    newAngel = self.Angel()
                    self.spawn(newAngel)
            elif (.12 * self.width) <= event.x <= (.2 * self.width):
                if self.age == 0:
                    newOwl = 'owl' + str(len(self.sprites))
                    newOwl = self.Owl()
                    self.spawn(newOwl)
                elif self.age == 1:
                    newKnight = 'knight'+ str(len(self.sprites))
                    newKnight = self.Knight()
                    self.spawn(newKnight)
                elif self.age == 2:
                    newGolem = 'golem'+ str(len(self.sprites))
                    newGolem = self.Golem()
                    self.spawn(newGolem)
                elif self.age == 3:
                    newSlayer = 'slayer'+ str(len(self.sprites))
                    newSlayer = self.Slayer()
                    self.spawn(newSlayer)
                elif self.age == 4:
                    newBoss = 'boss'+ str(len(self.sprites))
                    newBoss = self.Boss()
                    self.spawn(newBoss)
            elif (.23 * self.width) <= event.x <= (.31 * self.width):
                if self.age == 0:
                    newPeacock = 'peacock' + str(len(self.sprites))
                    newPeacock = self.Peacock()
                    self.spawn(newPeacock)
                elif self.age == 1:
                    newSlime = 'slime'+ str(len(self.sprites))
                    newSlime = self.Slime()
                    self.spawn(newSlime)
                elif self.age == 2:
                    newPhoenix = 'phoenix'+ str(len(self.sprites))
                    newPhoenix = self.Phoenix()
                    self.spawn(newPhoenix)
                elif self.age == 3:
                    newWhale = 'whale'+ str(len(self.sprites))
                    newWhale = self.Whale()
                    self.spawn(newWhale)
                elif self.age == 4:
                    newOvermind = 'overmind'+ str(len(self.sprites))
                    newOvermind = self.Overmind()
                    self.spawn(newOvermind)
            elif (.34 * self.width) <= event.x <= (.42 * self.width):
                if self.age == 0:
                    newRat = 'rat' + str(len(self.sprites))
                    newRat = self.Rat()
                    self.spawn(newRat)
                elif self.age == 1:
                    newSpore = 'spore ' + str(len(self.sprites))
                    newSpore = self.Spore()
                    self.spawn(newSpore)
                elif self.age == 2:
                    newWerewolf = 'werewolf'+ str(len(self.sprites))
                    newWerewolf = self.WereWolf()
                    self.spawn(newWerewolf)
                elif self.age == 3:
                    newWyvern = 'wyvern'+ str(len(self.sprites))
                    newWyvern = self.Wyvern()
                    self.spawn(newWyvern)
                elif self.age == 4:
                    newSpike = 'spike'+ str(len(self.sprites))
                    newSpike = self.Spike()
                    self.spawn(newSpike)

    def Animate(self):
        for count in range(len(self.alive)):
            unit = self.alive[count]
            pic = self.loadImage(unit.spritesheet)
            (start,end) = unit.action()
            unitSprite = []
            for i in range(start,end):
                sprite = pic.crop((0 + 512 * (i % 9) , 0 + 512 * (i // 9),\
                    512 + 512 * (i % 9), 512 + 512 * (i //9 ) ))
                sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 6)
                sprite = sprite.transpose(Image.FLIP_LEFT_RIGHT)
                unitSprite.append(sprite)
            if count >= len(self.sprites):
                self.sprites.append(unitSprite)
            else:
                self.sprites[count] = unitSprite

    def baseAnimate(self):
        pic = self.loadImage("Assets/Backgrounds/allyPortal.png") 
        allyBaseSprites = []
        for i in range(4):
            sprite = pic.crop((0 + 512 * i  , 0 + 512 * (i//3), 512 + 512 * i , 512 + 512 * (i//3) ))
            sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 4)
            sprite = sprite.transpose(Image.FLIP_LEFT_RIGHT) 
            allyBaseSprites.append(sprite)   
        self.baseSprites.append(allybaseSprites)    
        pic2 = self.loadImage("Assets/Backgrounds/enemyPortal.png")     
        enemyBaseSprites = []   
        for i in range(4):
            sprite = pic.crop((0 + 512 * i  , 0 + 512 * (i//3), 512 + 512 * i , 512 + 512 * (i//3) ))
            sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 4)   
            enemyBaseSprites.append(sprite)
        self.baseSprites.append(enemyBaseSprites)

    def iconLoader(self):
        path = 'Assets/Sprites'
        for folder in os.listdir(path):
            images = os.listdir(path + '/' + folder)
            for spritesheets in images:
                sheet = self.loadImage(path + '/' + folder + '/' + spritesheets)
                icon = sheet.crop((0,0,512,512))
                icon = sprite = self.scaleImage(icon, (self.height / 700 + self.width / 1400) / 12)
                self.icons.append(icon)

    def dist(self,x1,x2):
        return (x1 - 512 * ((self.height / 700 + self.width / 1400) / 12) - \
            x2 - 512 * ((self.height / 700 + self.width / 1400) / 12))

    def timerFired(self):
        self.background = self.background.resize((self.width,self.height))
        for unit in range(len(self.alive)):
            self.spriteCounters[unit] = (1 + self.spriteCounters[unit]) % len(self.sprites[unit])
            if unit == 0 or (self.dist(self.spriteLocation[unit-1],self.spriteLocation[unit]) > self.alive[unit].moveSpeed):
                self.spriteLocation[unit] += self.alive[unit].moveSpeed
        self.baseCounter = (1 + self.baseCounter) % 3
        self.xd += 1
        self.money += 1

    def interface(self,canvas): 
        canvas.create_image(self.width/2, self.height/2, image=ImageTk.PhotoImage(self.background))
        for unit in range(4):
            canvas.create_rectangle((.01 + .11 * unit) * self.width, .85 * self.height, (.09 + .11 * unit) * self.width, .99 * self.height, fill = "Teal")
            canvas.create_image((.05 + .11 * unit) * self.width, .88 * self.height, image = ImageTk.PhotoImage(self.icons[4 * self.age + unit]))
            canvas.create_rectangle((.01  + .11 * unit) * self.width, .95 * self.height, (.09 + .11 * unit) * self.width, .99 * self.height, fill = "White")
        if self.age < 5:
            canvas.create_rectangle(.75 * self.width, .05 * self.height, .85 * self.width, .15 * self.height, fill = "White" )
        canvas.create_text(.05 * self.width, .1 * self.height, text = f'${self.money}', font = "Helvetica 25 bold")

    def redrawAll(self,canvas):
        self.interface(canvas)
        for base in self.baseSprites:
            canvas.create_image(.05 * self.width, .68 * self.height, \
                image=ImageTk.PhotoImage(base[self.baseCounter]))
        for sprite in range(len(self.sprites)):
            unit = self.sprites[sprite]
            canvas.create_image(self.spriteLocation[sprite], .72 * self.height, \
                image=ImageTk.PhotoImage(unit[self.spriteCounters[sprite]]))
        
        
        
            
MyApp(width=1400, height=700)