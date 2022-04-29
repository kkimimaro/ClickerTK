from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

gold = 0
dmg = 1

def saveData():
  f = open("data.txt",'w')
  f.write(str(gold)+"."+str(dmg))
  f.close()

def loadData():
  global gold
  global dmg
  f = open("data.txt", 'r')
  data = f.read()
  data = data.split(".")
  gold = int(data[0])
  dmg = int(data[1])
  f.close()

def closePrevious(previous):
  if previous != "null":
    previous.destroy()

def menuWindow(previous):
  
  closePrevious(previous)
  menu = Tk()
  menu.geometry("500x500")
  
  img = Image.open("bb.png")
  img = img.resize((500, 500))
  bg = ImageTk.PhotoImage(img)
  
  label1 = Label(image = bg)
  label1.place(x = 0,y = 0)
  
  but1 = Button( text='PLAY', font='Arial 22', 
    command= lambda:gameWindow(menu))
  but1.place(relx=0.3, rely=0.3,height=80, width=200)
  
  but2 = Button( text='SHOP', font='Arial 22',
    command= lambda:shopWindow(menu))
  but2.place(relx=0.3, rely=0.5,height=80, width=200)
  menu.mainloop()

def gameWindow(previous):
  
  def increaseGold():
    global gold
    global dmg
    gold+=dmg
    goldAmountGame["text"]= str(gold)
    saveData()
 
  closePrevious(previous)
  game = Tk()
  game.geometry("500x500")
  
  img = Image.open("bb.png")
  img = img.resize((500, 500))
  bg = ImageTk.PhotoImage(img)
  
  label1 = Label(image = bg)
  label1.place(x = 0,y = 0)
  
  goldAmountGame = Label(text=gold, font='Arial 25')
  goldAmountGame.place(relx=0.45, rely=0.3)
  
  butI = Button( text='Click', font='Arial 21',
    command=increaseGold)
  butI.place(relx=0.3, rely=0.4,height=80, width=200)
  
  butM = Button( text='Menu', font='Arial 21',
    command= lambda:menuWindow(game))
  butM.place(relx=0.3, rely=0.6,height=80, width=200)
  
  game.mainloop()

def shopWindow(previous):
  global gold
  closePrevious(previous)
  shop = Tk()

  img = Image.open("bb.png")
  img = img.resize((500, 500))
  bg = ImageTk.PhotoImage(img)
  
  label1 = Label(image = bg)
  label1.place(x = 0,y = 0)
     
  shop.geometry("500x500")
  
  def rollCharacter():
    characters = ["bubus", "makar", "ivanzol2004"]
    character= random.choice(characters)
    print(character)
  
  def buy(price):
    global gold
    global dmg
    if gold >= price:
      rollCharacter()
      gold = gold - price
      dmg = dmg + 1
      label["text"] = gold
      saveData()
    else:
      messagebox.showwarning(message="Not enough money")
  
  
  imgd = Image.open("b.png")
  imgd = imgd.resize((50, 50))
  imgd = ImageTk.PhotoImage(imgd)
  
  label = Label(image = imgd, width = 60, height = 60)
  label.place(relx=0.3, rely=0.3)
  
  label = Label(text = gold, width = 8, height = 3, font=("Arial", 17))
  label.place(relx=0.5, rely=0.3)
  
  #Чтение и изменение размера изображения
  img = Image.open("v.png")
  img = img.resize((70, 50))
  img = ImageTk.PhotoImage(img)
  
  btn2 = Button(image = img, text=80, width = 70, height = 50)
  
  btn2["command"] = lambda: buy(100)
  btn2.place(relx=0.23, rely=0.6)
  
  btn3 = Button(image = img, text=80, width = 70, height = 50)
  btn3["command"] = lambda: buy(200)
  btn3.place(relx=0.43, rely=0.6)
  
  btn4 = Button(image = img, text=80, width = 70, height = 50)
  btn4["command"] = lambda: buy(400)
  btn4.place(relx=0.63, rely=0.6)
  
  butM = Button( text='Menu', font='Arial 15',
    command= lambda:menuWindow(shop))
  butM.place(relx=0.35, rely=0.9,height=50, width=150)
  
  shop.mainloop()

loadData()
menuWindow("null")