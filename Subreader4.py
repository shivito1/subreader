import pysrt,pyttsx,time
from threading import Thread
from Tkinter import *
from idlelib.idle_test.mock_tk import Event



set1 = 0
set2 = 0
subcount = 0 
interupt = 0

settozero = 0

subs = pysrt.open(r"C:\Users\admin\Desktop\Python-files\Deskinfo\eternal-loveSUBS\Eternal.Love_E19.srt")
compsrt = []

def speechafter(subit,x):
    try:
        engine = pyttsx.init()
        engine.setProperty('rate',x)
        engine.say(subit.replace('[','').replace(']','').replace('\'','').replace('"','').replace('<i>','').replace('</i>',''))
        engine.runAndWait()
    except RuntimeError:
        print str(set2) + 'FAILD here\n' + subit[:10] + '\n'
def get_ms(t): 
    return (t.hours*60*60 + t.minutes*60 + t.seconds)*1000 + t.milliseconds 

#start speaking
def start_speak1(event):
    
    Thread(target=start_speak).start()
    
def curset2(val):
    global set2
    set2 = val
    
    
def start_speak():
    global set2
    try:
        inter
        if inter == 'asdf':
            pass
        else:
            set2 = subcount
    except:
        set2 = subcount

        

    for item in range(len(subs)):
        if interupt == 5:
            while interupt == 5:
                pass
        else:
            start = get_ms(subs[set2].start)
            start2 = get_ms(subs[(set2 - 1)].start)
            if set2 == 0:
                newtime = get_ms(subs[0].start)
                print newtime
                x = 200
            else:
                newtime = start - start2  
                print str(float(newtime) / 1000) + " - Place:" + str(item) + " --- " + (subs[set2].text).replace('\n',' ')
                if subs[set2].text.endswith(' zz$'):
                    x=250
                    subs[set2].text = subs[set2].text.replace(' zz$', '') 
                else:
                    x = 200
            curset2(set2)
            global settozero
            if settozero == 5:
                newtime = 0
                settozero = 0
            else:
                pass

            time.sleep(float(newtime) / 1000)
            lblsub.config(text=(subs[set2].text))
            var.set(set2 +1)
            Thread(target=speechafter,args=(subs[set2].text, x)).start()
            set2 += 1
        

        

for sub in subs:
    
    start = get_ms(sub.start)

    char = len(sub.text)
    time_need = int((char / 3.0) / (200.0/60.0) * 1000.0) 
    if (sub.end - sub.start) > int(time_need):
        pass
    else:
        time_need = int((char / 3.0) / (250.0/60.0) * 1000.0)
        subs[set1].end = (subs[set1].start + time_need + 100)
        subs[set1].text = subs[set1].text + ' zz$'
        try:
            if subs[set1].end >= subs[(set1 +1)].start:
                subs[(set1 +1)].start = (subs[set1].end)
            
            else:
                pass
        except IndexError:
            pass
    set1 +=1
    compsrt.append(str(set1) + '\n' + str(sub.start) + " - " + str(sub.end) + '\n' + str(sub.text) + '\n\n')
    
    
    
ed = open('compsrt.txt', 'w')
for i in compsrt:
    ed.write(i)
ed.close()
            
            
            
            
            
            
            
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

root.wm_minsize(root.winfo_screenwidth() - 25, 200)

var = StringVar()


def nextline(event):
    global inter
    inter = 'asdf'
    global set2
    set2 = set2 + 1
    print set2
    print subs[set2].text
    lblsub.config(text=(subs[set2].text))
def pause(event):
    global settozero
    settozero = 5
    global interupt
    if interupt == 5:
        interupt = 0
    else:
        interupt = 5
def backline(event):
    global inter
    inter = 'asdf'
    global set2
    set2 = set2 - 1
    print subs[set2].text
    lblsub.config(text=(subs[set2].text))
    
def enterline(line):
    global inter
    inter = 'asdf'
    global set2
    set2 = int(line)-1
    print line

root.attributes("-topmost", True)
lblsub = Label(root,text='',font='comic 45',height=2,bg='gray')
lblsub.pack(fill=X)
lblcount = Label(root,textvariable=var)
lblcount.pack(fill=X)
ent = Entry(root)
ent.pack(fill=X)
ent.bind('<Return>', lambda e: enterline(ent.get()))
lbl = Label(root,text="start")
lbl.pack(fill=X)
lbl.bind("<Button-1>",start_speak1)
root.bind('<Right>', nextline)
root.bind('<Down>', pause)
root.bind('<Left>', backline)
root.mainloop()
 
    

