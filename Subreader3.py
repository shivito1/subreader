import Tkinter as tk 
import sys 
import pysrt,time
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
        self.pause = 2
        self.collisioncheck = []
        self.collend = [] 
        self.store_subs = []
        
        
        self.currentline = 0
        self.current_time = 0
        self.engine = pyttsx.init()
        self.engine.setProperty('rate',200)
        
        self.root.bind('<Right>', self.oneforward)
        self.root.bind('<Left>', self.onebackward)
        
        ti = Timer(0.3,self.createWidgets)
        ti.start()

    def oneforward(self,event):
        ## Pause (1) Play (2)
        if self.pause == 1:
            self.pause = 2
        elif self.pause == 2:
            self.pause = 1
        
            
    def onebackward(self,event):
        self.current_time -= 1000
    
    def speechafter(self,sub):
#        while True:
 #           try:
        self.engine.say(sub.replace('[','').replace(']','').replace('\'','').replace('"','').replace('<i>','').replace('</i>',''))
        
        self.engine.runAndWait()
  #          except RuntimeError:
   #             continue
    #        break
        
    
    def get_ms(self,t): 
        return (t.hours*60*60 + t.minutes*60 + t.seconds)*1000 + t.milliseconds 
        if self.tick == 0:
            self.slidstart = self.Start
        else:
            pass    
    def createWidgets(self): 
        self.sub_var = tk.StringVar() 
        self.sub_label = tk.Label(self, textvariable=self.sub_var, font=self.font) 
        self.sub_label.pack() 
        



        

        self.i = 0   
            
        for sub in subs: 
            
            if self.pause == 2:
            
                self.start = self.get_ms(sub.start)
                self.end = self.get_ms(sub.end)
                
                self.collisioncheck.append(self.start)
                self.collend.append(self.end)
                self.store_subs.append(sub.text)
                line = len(self.collisioncheck)
                pre_sub = self.store_subs[(line - 2)]
                lineget = self.collisioncheck[(line - 2)] ## previous sub start time
                lineget2 = self.collend[(line - 2)]  ## previous sub end time
                check = self.collisioncheck[(line - 1)]  ## current sub start time
                check2 = self.collend[(line - 1)]  ## current sub end time
                settime = ((self.start) - lineget)
                print settime, '#########start'
                char = len((pre_sub).replace('[','').replace(']','').replace('\'','').replace('"','').replace('<i>','').replace('</i>',''))
                
                addthis = (((char / 5) / 3) * 1000)
                print addthis,'##added'
                
#                print lineget, check                
#                print self.collisioncheck
#                print self.collend
                
                if lineget + addthis > check:
                    print settime
                    settime += addthis
                    print 'here'
                else:
                    print 'not there'
                
    
                duration =  self.get_ms(sub.end) - self.get_ms(sub.start) 
                self.current_time = self.get_ms(sub.end) 
                self.sub_label.after(settime - 10, self.update, settime - 10, duration, sub.text) 

                

                
                print settime / 1000
                
                time.sleep(settime / 1000)
                
                self.tb = Timer(0, self.speechafter, [sub.text])
                self.tb.start() 
            else:
                print 'here'
                pass
            

            
        
        self.slidend = self.start
        
        self.w = Scale(self.root, from_=0, to=self.slidend / 1000,length=900, orient=HORIZONTAL)
        self.w.pack()
        
        
        
       
        

    def updateText(self, val, verbose=""): 
        if verbose: 
            print(verbose) 
        self.sub_var.set(val) 


    def update(self, start, duration, text): 
        self.updateText(text, verbose="%i (%i): %s" % (start, duration, text)) 




if __name__ == "__main__": 
    filename = r"C:\Users\admin\Desktop\Python-files\Deskinfo\eternal-loveSUBS\Eternal.Love.E14.srt"
    print('Starting %s' % filename) 


    filename = r"C:\Users\admin\Desktop\Python-files\Deskinfo\eternal-loveSUBS\Eternal.Love.E14.srt"
    subs = pysrt.open(filename) 


    root = tk.Tk() 
    app = Application(root=root, subs=subs) 
    app.mainloop() 


    
