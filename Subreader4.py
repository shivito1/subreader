import pysrt,pyttsx,time
from threading import Timer
from Tkinter import Label,Tk
from idlelib.idle_test.mock_tk import Event


set1 = 0
set2 = 0
subs = pysrt.open(r"C:\Users\admin\Desktop\Python-files\Deskinfo\eternal-loveSUBS\Eternal.Love.E14.srt")

def speechafter(sub):
    engine = pyttsx.init()
    engine.setProperty('rate',200)
    engine.say(sub.replace('[','').replace(']','').replace('\'','').replace('"','').replace('<i>','').replace('</i>',''))
    
    engine.runAndWait()
def get_ms(t): 
    return (t.hours*60*60 + t.minutes*60 + t.seconds)*1000 + t.milliseconds 

#start speaking
def start_speak1(event):
    engine = pyttsx.init()
    engine.setProperty('rate',200)
    engine.say('start')
    
    engine.runAndWait()
    start_speak()    
    
def start_speak():
    set2 = 0

    for sub in subs:
        start = get_ms(subs[set2].start)
        start2 = get_ms(subs[(set2 - 1)].start)
        if set2 == 0:
            newtime = get_ms(sub.start)
        else:
            newtime = start - start2
            print newtime / 1000


        
        set2 += 1
        time.sleep(newtime / 1000)
        speechafter(sub.text)

        

        

for sub in subs:
    
    start = get_ms(sub.start)

    char = len(sub.text)
    time_need = int((char / 3.0) / (200.0/60.0) * 1000.0)
    
    if (sub.end - sub.start) > int(time_need):
            pass
    else:
        subs[set1].end = (subs[set1].start + time_need)
    try:
        if subs[set1].end >= subs[(set1 +1)].start:
            subs[(set1 +1)].start = (subs[set1].end)
        else:
            pass
    except IndexError:
        pass
    
    set1 +=1
            
            
            
            
            
            
            
#            print sub.end,sub.start
#            print (sub.end - sub.start)
#            print int(time_need)
#            print sub.text
#            if (sub.end - sub.start) < int(time_need):
#                pass
                #    set2 += 1
#            else:
#                    pass
root = Tk()

lbl = Label(text="start")
lbl.pack()
lbl.bind("<Button-1>",start_speak1)
root.mainloop()
 
    
