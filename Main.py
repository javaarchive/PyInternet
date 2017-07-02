from tkinter import *
from tkinter.ttk import *
from urllib.request import *
import time
from time import sleep
try:
    import pygame
    pygame_enabled=True
except:
    pygame_enabled=False
try:
    import urllib.request as urllib
    import platform
except:
    print("Warning:Module load error will affect loading pages")
try:
    mainwindow=Tk()
    win=mainwindow
except:
    print("Window make error:Error Code 001")
    
win.grid()
win.title("Pyinternet")
url=Entry(win,width=100)
url.grid(row=1,column=1)

start=Button(win,text=">>>")
start.grid(row=1,column=2)
def enter(key=None):
    start.invoke()
win.bind("<Return>",enter)
display=Text(win)
out=display
out.grid(row=2,column=1,columnspan=2)
def heading(w):
    
    out.insert(END,w+"\n")

def p(w):
    
    out.insert(END,w+"\n")
def getweb():
    get=url.get()
    get="https://raw.githubusercontent.com/javaarchive/PyInternet/master/web/"+get+"/index.txt"
    out.delete("0.0",END)
    load=urlopen(get).read().decode()
    print("Loading")
    exec(load)
start["command"]=getweb
def btn1():
    print("Not set 1")
    
def btn2():
    print("Not set 2")

def btn3():
    print("Not set 3")

def redirect(url):
    url.delete("0",END)
    url.insert(END,url)
    getweb()
linkpress=redirect
    
b1=Button(win,text="Web Button 1",command=btn1)
b1.grid(row=3,column=1)
b2=Button(win,text="Web Button 2",command=btn2)
b2.grid(row=3,column=2)
b3=Button(win,text="Web Button 3",command=btn3)
b3.grid(row=3,column=3)

    


    


    

