from tkinter import *
import random
import time

class Spiel:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Herr Wichssohn rennt bis er verreckt")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg = PhotoImage(file="Hintergrund.gif")
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        self.sprites = []
        self.rennen = True

    def Hauptschleife(self):
        while 1:
            if self.rennen == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

class Koordinaten:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def innerhalb_x(co1, co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
        return True
    else:
        return False

def innerhalb_y(co1, co2):
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y1):
        return True
    else:
        return False


def angestoßen_links(co1, co2):
    if innerhalb_y(co1, co2):
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False


def angestoßen_rechts(co1, co2):
    if innerhalb_y(co1, co2):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False


def angestoßen_oben(co1, co2):
    if innerhalb_x(co1, co2):
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
            return True
    return False


def angestoßen_unten(y, co1, co2):
    if innerhalb_x(co1, co2):
        y_calc = co1.y2 + y
        if y_calc >= co2.y1 and y_calc <= co2.y2:
            return True
    return False


class Sprite:
    def __init__(self, spiel):
        self.spiel = spiel
        self.spielende = False
        self.koordinaten = None
    def move(self):
        pass
    def coords(self):
        return self.koordinaten


class EbenenSprite(Sprite):
    def __init__(self, spiel, photo_image, x, y, width, height):
        Sprite.__init__(self, spiel)
        self.photo_image = photo_image
        self.bild = spiel.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.koordinaten = Koordinaten(x, y, x + width, y + height)


class StickFigureSprite(Sprite):
    def __init__(self, spiel):
        Sprite.__init__(self, spiel)
        self.bilder_links = [
            PhotoImage(file="Figur-L1.gif"),
            PhotoImage(file="Figur-L2.gif"),
            PhotoImage(file="Figur-L3.gif")
        ]
        self.bilder_rechts = [
            PhotoImage(file="Figur-R1.gif"),
            PhotoImage(file="Figur-R2.gif"),
            PhotoImage(file="Figur-R3.gif")
        ]
        self.bild = spiel.canvas.create_image(200, 470, image=self.bilder_links[0], anchor='nw')
        self.x = -2
        self.y = 0
        self.aktuelles_bild = 0
        self.aktuelles_bild_plus = 1
        self.springen_zähler = 0
        self.letzte_zeit = time.time()
        self.koordinaten = Koordinaten()
        spiel.canvas.bind_all('<KeyPress-Left>', self.turn_links)
        spiel.canvas.bind_all('<KeyPress-Right>', self.turn_rechts)
        spiel.canvas.bind_all('<space>', self.springen)

    def turn_links(self, evt):
        if self.y == 0:
            self.x = -2

    def turn_rechts(self, evt):
        if self.y == 0:
            self.x = 2

    def springen(self, evt):
        if self.y == 0:
            self.y = -4
            self.springen_zähler = 0
            
    def animieren(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.letzte_zeit > 0.1:
                self.letzte_zeit = time.time()
                self.aktuelles_bild += self.aktuelles_bild_plus
                if self.aktuelles_bild >= 2:
                    self.aktuelles_bild_plus = -1
                if self.aktuelles_bild <= 0:
                    self.aktuelles_bild_plus = 1
        if self.x < 0:
            if self.y != 0:
                self.spiel.canvas.itemconfig(self.bild, image=self.bilder_links[2])
            else:
                self.spiel.canvas.itemconfig(self.bild, image=self.bilder_links[self.aktuelles_bild])
        elif self.x > 0:
            if self.y != 0:
                self.spiel.canvas.itemconfig(self.bild, image=self.bilder_rechts[2])
            else:
                self.spiel.canvas.itemconfig(self.bild, image=self.bilder_rechts[self.aktuelles_bild])

    def coords(self):
        xy = list(self.spiel.canvas.coords(self.bild))
        self.koordinaten.x1 = xy[0]
        self.koordinaten.y1 = xy[1]
        self.koordinaten.x2 = xy[0] + 27
        self.koordinaten.y2 = xy[1] + 30
        return self.koordinaten
        
    def move(self):
        self.animieren()
        if self.y < 0:
            self.springen_zähler += 1
            if self.springen_zähler > 20:
                self.y = 4
        if self.y > 0:
            self.springen_zähler -= 1
            
        co = self.coords()
        links = True
        rechts = True
        oben = True
        unten = True
        fallen = True
        
        if self.y > 0 and co.y2 >= self.spiel.canvas_height:
            self.y = 0
            unten = False
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            oben = False

        if self.x > 0 and co.x2 >= self.spiel.canvas_width:
            self.x = 0
            rechts = False
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            links = False

        for sprite in self.spiel.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if oben and self.y < 0 and angestoßen_oben(co, sprite_co):
                self.y = -self.y
                oben = False
                
            if unten and self.y > 0 and angestoßen_unten(self.y, co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                unten = False
                oben = False

            if unten and fallen and self.y == 0 and co.y2 < self.spiel.canvas_height and angestoßen_unten(1, co, sprite_co):
                fallen = False
                
            if links and self.x < 0 and angestoßen_links(co, sprite_co):
                self.x = 0
                links = False

            if rechts and self.x > 0 and angestoßen_rechts(co, sprite_co):
                self.x = 0
                rechts = False
            
        if fallen and unten and self.y == 0 and co.y2 < self.spiel.canvas_height:
            self.y = 4
        
        self.spiel.canvas.move(self.bild, self.x, self.y)

s = Spiel()
Ebene1 = EbenenSprite(s, PhotoImage(file="Ebene1.gif"), 0, 480, 100, 10)
Ebene2 = EbenenSprite(s, PhotoImage(file="Ebene1.gif"), 150, 440, 100, 10)
Ebene3 = EbenenSprite(s, PhotoImage(file="Ebene1.gif"), 300, 400, 100, 10)
Ebene4 = EbenenSprite(s, PhotoImage(file="Ebene1.gif"), 300, 160, 100, 10)
Ebene5 = EbenenSprite(s, PhotoImage(file="Ebene2.gif"), 175, 350, 66, 10)
Ebene6 = EbenenSprite(s, PhotoImage(file="Ebene2.gif"), 50, 300, 66, 10)
Ebene7 = EbenenSprite(s, PhotoImage(file="Ebene2.gif"), 170, 120, 66, 10)
Ebene8 = EbenenSprite(s, PhotoImage(file="Ebene2.gif"), 45, 60, 66, 10)
Ebene9 = EbenenSprite(s, PhotoImage(file="Ebene3.gif"), 170, 250, 32, 10)
Ebene10 = EbenenSprite(s, PhotoImage(file="Ebene3.gif"), 230, 200, 32, 10)
s.sprites.append(Ebene1)
s.sprites.append(Ebene2)
s.sprites.append(Ebene3)
s.sprites.append(Ebene4)
s.sprites.append(Ebene5)
s.sprites.append(Ebene6)
s.sprites.append(Ebene7)
s.sprites.append(Ebene8)
s.sprites.append(Ebene9)
s.sprites.append(Ebene10)
sf = StickFigureSprite(s)
s.sprites.append(sf)
s.Hauptschleife()
