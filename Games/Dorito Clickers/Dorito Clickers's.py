from tkinter import *
import time
import random

class field:
    def __init__(self):
        self.text_ver()
        doritos_amount_plus = 1
        self.doritos_amount_plus = doritos_amount_plus
        doritos_amount = 0
        self.doritos_amount = doritos_amount
        cheat_mode_ = []
        self.cheat_mode_ = cheat_mode_
        dorito_text = canvas.create_text(400, 20, text=self.doritos_amount, fill='black', font=('Courier', 20))
        self.dorito_text = dorito_text
        canvas.bind_all('<Button-1>', self.click_doritos)
        canvas.bind_all('<KeyPress-Up>', self.cheat_mode)
        
        
        
    def click_doritos(self, event):
        random_doritos_amount = [20, 1, 1, 1, 4, 6, 3, 6, 1, 5, 8, 8, 4]
        self.random_doritos_amount = random_doritos_amount
        doritos_rndm_ch = random.choice(self.random_doritos_amount)
        self.doritos_rndm_ch = doritos_rndm_ch
        if self.doritos_amount >= 0 and self.doritos_amount <= 99:
            self.doritos_amount = self.doritos_amount + 1
        if self.doritos_amount >= 100 and self.doritos_amount <= 199:
            self.doritos_amount = self.doritos_amount + 2
        if self.doritos_amount >= 200 and self.doritos_amount <= 299:
            self.doritos_amount = self.doritos_amount + 3
        if self.doritos_amount >= 300 and self.doritos_amount <= 399:
            self.doritos_amount = self.doritos_amount + 4
        if self.doritos_amount == 400 and self.doritos_amount <= 410 :
            self.doritos_amount = self.doritos_amount + 4
        if self.doritos_amount >= 411 and self.doritos_amount <= 499:
            self.doritos_amount = self.doritos_amount + 5
        if self.doritos_amount >= 500 :
            self.doritos_amount = self.doritos_amount + self.doritos_rndm_ch
                
        
    def dorito_number(self):
        canvas.itemconfig(self.dorito_text, text=self.doritos_amount)


    def cheat_mode(self, event):
        cheat = ['key100',]
        self.cheat = cheat
        if 'key100' in self.cheat :
            self.doritos_amount = self.doritos_amount + 60
        else:
            self.doritos_amount = self.doritos_amount + 0

    def cheat_loop(self, event):
        for x in range(self.doritos_amount, 1000000000001):
            time.sleep(0.4)
            if self.cheat_loop_stop :
                break
            

    def cheat_loop_stop(self, event):
        pass

    def text_ver(self):
        canvas.create_text(410, 470, text='Dorito Clickers / Alpha 0.1', font=('System', 1), fill='black')
        canvas.create_text(400, 490, text='All rights reserved', font=('System', 1), fill='black')

    
        
        
        




        
        

            





            
tk = Tk()
doritos_background = PhotoImage(file='c:\\Users\\alexv\\Desktop\\Alex\\Programmierung\\Projekte\\Python\\Dorito Clickers\\Background.gif')
dorito_pic_chip = PhotoImage(file='c:\\Users\\alexv\\Desktop\\Alex\\Programmierung\\Projekte\\Python\\Dorito Clickers\\dorito_chip.gif')
doritos_pic_1 = PhotoImage(file='c:\\Users\\alexv\\Desktop\\Alex\\Programmierung\\Projekte\\Python\\Dorito Clickers\\doritos.gif')
dorito_pic_2 = PhotoImage(file='c:\\Users\\alexv\\Desktop\\Alex\\Programmierung\\Projekte\\Python\\Dorito Clickers\\dorito_chip.gif')
fat_kid = PhotoImage(file='c:\\Users\\alexv\\Desktop\\Alex\\Programmierung\\Projekte\\Python\\Dorito Clickers\\fat_kid.gif')
tk.title('Dorito Clicker\'s')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, height=500, width=500, bd=0)
canvas.pack()
canvas.create_image(0, 0, anchor =NW, image=doritos_background)
canvas.create_image(380, 25, image=dorito_pic_2)
canvas.create_image(230, 230, image=doritos_pic_1)
canvas.create_image(410, 25, image=dorito_pic_chip)
tk.update()




field1 = field()


while 1:
    field1.dorito_number()
    tk.update()
    tk.update_idletasks()





# for later (dump)

# loops

# for x in range(0, 2):
            #fat_kid_ID = canvas.create_image(360, 250, image=fat_kid)
            #canvas.move(fat_kid_ID, -4, 0)
            #canvas.move(fat_kid_ID, 2, 0)


# bindings

# canvas.bind_all('<KeyPress-Up>' + '<KeyPress-Down>', self.cheat_mode_actv)

#canvas.bind_all('<KeyPress-Left>', self.cheat_loop)
#canvas.bind_all('<KeyPress-Right>', self.cheat_loop_stop)



# lost projects


#def cheat_loop(self, event):
        #for x in range(self.doritos_amount, 1000000000001):
            #time.sleep(0.4)
            #if self.cheat_loop_stop :
                #break
            

    #def cheat_loop_stop(self, event):
        #pass
    
