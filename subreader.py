import pyttsx
import pysrt, tkFileDialog
from threading import Timer
from Tkinter import *
from gtts import gTTS
import os





class reader1:
    def __init__(self,root):
        def setreader(num):
            self.readerset = int(num)
            print int(self.readerset)
        self.root = root
        self.currentline = 0
        self.readerset = 0
        self.engine = pyttsx.init()
        
        self.lbl1 = Label(self.root,text=self.currentline)
        self.lbl1.pack()
        
  ### readerButtons Win_TTS and gTTS change setreader value. Win_TTS = windows text to speech. gTTS = Google Text to speech (gTTS uses MP3)
        btn1  = Button(self.root,text='Win_TTS', command = lambda: setreader(1))
        btn1.pack()
        btn2 = Button(self.root,text='gTTS', command = lambda: setreader(0))
        btn2.pack()
  ### readerButtons Win_TTS and gTTS change setreader value. Win_TTS = windows text to speech. gTTS = Google Text to speech (gTTS uses MP3) 
  
  ### SRT Button: Opens selecter window to choose .SRT file  
        btn = Button(self.root,text='Get .SRT', command = self.getsrt)
        btn.pack()
  ### SRT Button: Opens selecter window to choose .SRT file       
        
  ### Displays current SRT line.
        self.lbl0 = Label(self.root,text="",font='Times 15',fg="green",bg='black')
        self.lbl0.pack()
   ### Displays current SRT line.
   
   ### binds Arrow keys triger text to change and pyttsx to process current line.
        self.root.bind('<Right>', self.nextline)
        self.root.bind('<Down>', self.repeatline)
        self.root.bind('<Left>', self.backline)
        self.root.bind('<Control-Right>', self.nextline2)
        self.root.bind('<Control-Left>', self.backline2)
   ### binds Arrow keys triger text to change and pyttsx to process current line.      
        
        self.root.mainloop()
        
    def getsrt(self):
      ### dialog window
        self.dirfile = tkFileDialog.askopenfilename()
      ### dialog window
        print self.dirfile
      ### Opens SRT  
        self.opensrt = pysrt.open(self.dirfile)
      ### Opens SRT
      
      ### Counts Lines
        self.lines = len(self.opensrt)
      ### Counts Lines
        
    def nextline(self,event):
        def readnow():
            self.engine.say(str(self.readcurrent[0:]).replace('<i>','').replace('</i>',''))
            self.engine.runAndWait()
        
        self.currentline += 1
        self.lbl1.configure(text=self.currentline)
        self.getcurrent = str(unicode(self.opensrt[self.currentline]))
        self.readcurrent = self.getcurrent.split('\n')[2:]
#        print self.readcurrent[0:]
        self.lbl0.configure(text=str(self.readcurrent[0:]).replace('[','').replace(']','').replace('\'','').replace('"',''))
        if self.readerset == 0:
            tts = gTTS(text=str(self.readcurrent[0:]).replace('[','').replace(']','').replace('"',''), lang='en')
            tts.save("google.mp3")
            os.system("Start /wait google.mp3")
            os.system('del google.mp3')
        elif self.readerset == 1:            
            t = Timer(0.01, readnow)
            t.start() 

        
    def repeatline(self,event):
        def readnow():
            self.engine.say(self.readcurrent[0:])
            self.engine.runAndWait()
        self.getcurrent = str(unicode(self.opensrt[self.currentline]))
        self.readcurrent = self.getcurrent.split('\n')[2:]
        print self.readcurrent[0:]
        self.lbl0.configure(text=str(self.readcurrent[0:]).replace('[','').replace(']','').replace('\'','').replace('"',''))

        if self.readerset == 0:
            tts = gTTS(text=str(self.readcurrent[0:]).replace('[','').replace(']','').replace('"',''), lang='en')
            tts.save("google.mp3")
            os.system("Start /wait google.mp3")
            os.system('del google.mp3')
        elif self.readerset == 1:
            t = Timer(0.01, readnow)
            t.start() 
        
    def backline(self,event):
        def readnow():
            self.engine.say(self.readcurrent[0:])
            self.engine.runAndWait()        
        self.currentline -= 1
        self.lbl1.configure(text=self.currentline)
        self.getcurrent = str(unicode(self.opensrt[self.currentline]))
        self.readcurrent = self.getcurrent.split('\n')[2:]
        print self.readcurrent[0:]
        self.lbl0.configure(text=str(self.readcurrent[0:]).replace('[','').replace(']','').replace('\'','').replace('"',''))
        if self.readerset == 0:
            tts = gTTS(text=str(self.readcurrent[0:]).replace('[','').replace(']','').replace('"',''), lang='en')
            tts.save("google.mp3")
            os.system("Start /wait google.mp3")
            os.system('del google.mp3')
        elif self.readerset == 1:
            t = Timer(0.01, readnow)
            t.start()
        

        
        ### No read just skim lines
        
    def nextline2(self,event):


        self.currentline += 1
        self.lbl1.configure(text=self.currentline)
        self.getcurrent = str(unicode(self.opensrt[self.currentline]))
        self.readcurrent = self.getcurrent.split('\n')[2:]

        self.lbl0.configure(text=str(self.readcurrent[0:]).replace('[','').replace(']','').replace('\'','').replace('"',''))

        
    def backline2(self,event):
     
        self.currentline -= 1
        self.lbl1.configure(text=self.currentline)
        self.getcurrent = str(unicode(self.opensrt[self.currentline]))
        self.readcurrent = self.getcurrent.split('\n')[2:]

        self.lbl0.configure(text=str(self.readcurrent[0:]).replace('[','').replace(']','').replace('\'','').replace('"',''))

        
        
        
        
        
        
        
        
reader1(Tk())       
