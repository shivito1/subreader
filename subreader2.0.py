import Tkinter as tk 
import sys 
import pysrt 
from time import sleep 

import pyttsx
import tkFileDialog
from threading import Timer
from Tkinter import *
from gtts import gTTS
import os


class Application(tk.Frame): 
    def __init__(self, root=None, subs=[]): 
        tk.Frame.__init__(self, root) 
        self.root = root
        self.subs = subs 
        self.pack() 
        self.tick = 0
        root.attributes("-topmost", True) 
        root.lift() 
        self.font = ("Roboto", "32", "bold")  
        
        self.currentline = 0
        self.current_time = 0
        self.engine = pyttsx.init()
        
        self.root.bind('<Right>', self.oneforward)
        self.root.bind('<Left>', self.onebackward)
        
        self.createWidgets() 

    def oneforward(self,event):
        self.current_time += 10000
        
            
    def onebackward(self,event):
        self.current_time -= 1000
    
    def createWidgets(self): 
        self.sub_var = tk.StringVar() 
        self.sub_label = tk.Label(self, textvariable=self.sub_var, font=self.font) 
        self.sub_label.pack() 
        


        def get_ms(t): 
            return (t.hours*60*60 + t.minutes*60 + t.seconds)*1000 + t.milliseconds 
            if self.tick == 0:
                self.slidstart = self.Start
            else:
                pass
        
        self.slidend = 20000
        
        self.w = Scale(self.root, from_=0, to=self.slidend,length=900, orient=HORIZONTAL)
        self.w.pack() 
        
        for sub in subs: 
            self.start = get_ms(sub.start)
            
            duration =  get_ms(sub.end) - get_ms(sub.start) 
            self.current_time = get_ms(sub.end) 
            self.sub_label.after(self.start, self.update, self.start, duration, sub.text) 
            self.sub_label.after(self.start + duration, self.update, self.start, duration, "") 
        
        
        self.w.configure(to=self.current_time)
        
        
       
        

    def updateText(self, val, verbose=""): 
        if verbose: 
            print(verbose) 
        self.sub_var.set(val) 


    def update(self, start, duration, text): 
        self.updateText(text, verbose="%i (%i): %s" % (start, duration, text)) 




if __name__ == "__main__": 
    filename = r"C:\Users\admin\Desktop\Python-files\Deskinfo\eternal-loveSUBS\Eternal.Love.E13.srt"
    print('Starting %s' % filename) 


    filename = r"C:\Users\admin\Desktop\Python-files\Deskinfo\eternal-loveSUBS\Eternal.Love.E13.srt"
    subs = pysrt.open(filename) 


    root = tk.Tk() 
    app = Application(root=root, subs=subs) 
    app.mainloop() 


    
