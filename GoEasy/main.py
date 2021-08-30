import webbrowser
from time import sleep
import datetime
from tkinter import *
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from win10toast import ToastNotifier
  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#speak(voices[1].id)
engine.setProperty('voice', voices[0].id)


       
bum = Tk()
bum.title("GoEasy Version 1.3 - 11B ")
bum.geometry("300x190")


MatAYT = ('https://meet.google.com/lesson')
Matbrk = ('https://meet.google.com/lesson')
BiyAYT = ('https://meet.google.com/lesson')
TRTYT = ('https://meet.google.com/lesson')
Fizik = ('https://meet.google.com/lesson')
TarihAyt =('https://meet.google.com/lesson')
KimyaAyt = ('https://meet.google.com/lesson')
Din = ('https://meet.google.com/lesson')
Felsefe = ('https://meet.google.com/lesson')
KimyaTYT = ('https://meet.google.com/lesson')
BiyTYT =('https://meet.google.com/lesson')
ing = ('https://meet.google.com/lesson')
Cografya = ('https://meet.google.com/lesson')
Alm = ('https://meet.google.com/lesson')

saymatayt = ('Your lesson is Math AYT')
saymatyt = ('Your lesson is Math TYT')
saybioayt = ('Your lesson is Biology AYT')
saytr = ('Your lesson is Turkish')
sayfizikayt = ('Your lesson is Physics AYT')
saykimyaayt = ('Your lesson is Chemistry AYT')
saydin = ('Your lesson is about Religions')
saytarih = ('Your lesson is History')
saybiotyt = ('Your lesson is Biology TYT')
saykimyatyt = ('Your lesson is Chemistry TYT')
saying =('Your lesson is English')
sayfelsefe =('Your lesson is Philosophy')

dersbaslıyor = ('Your lesson will start soon.')




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def joinmonday():
    hour = int(datetime.datetime.now().hour)
   
    if hour>=7.55 and hour<8.40:
        webbrowser.open(MatAYT)
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatayt, duration = 60)
        speak(dersbaslıyor)
        speak(saymatayt)
        


    elif hour>=8.55 and hour<9.40:
        webbrowser.open(MatAYT)
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatayt, duration = 60)
        speak(dersbaslıyor)
        speak(saymatayt)
    
    elif hour>=9.50 and hour<10.30:
        webbrowser.open(Matbrk)
        speak(dersbaslıyor)
        speak(saymatyt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatyt, duration = 60)
    
    elif hour>=10.40 and hour<11.20:
        webbrowser.open(BiyAYT)
        speak(dersbaslıyor)
        speak(saybioayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saybiotyt, duration = 60)
   
    elif hour>=11.25 and hour<12.10:
        webbrowser.open(TRTYT) 
        speak(dersbaslıyor)
        speak(saytr)
        n = ToastNotifier()
        n.show_toast("GoEasy", saytr, duration = 60)
   
    elif hour>=12.05 and hour<13.40:
        webbrowser.open(Fizik)
        speak(dersbaslıyor)
        speak(sayfizikayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", sayfizikayt, duration = 60)
        
    elif hour>=13.35 and hour<14.30:
        webbrowser.open(TarihAyt)
        speak(dersbaslıyor)
        speak(saytarih)
        n = ToastNotifier()
        n.show_toast("GoEasy", saytarih, duration = 60)
   
    elif hour>=14.35 and hour<15.20:
        webbrowser.open(KimyaAyt)
        speak(dersbaslıyor)
        speak(saykimyaayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saykimyaayt, duration = 60)
    
    elif hour>=15.25 and hour<16.10:
        webbrowser.open(Din)
        speak(dersbaslıyor)
        speak(saydin)
        n = ToastNotifier()
        n.show_toast("GoEasy", saydin, duration = 60)
  
    else:
        speak("You haven't got a lesson right now.")
        n = ToastNotifier()
        n.show_toast("GoEasy", "You haven't got a lesson right now.", duration = 60)

def jointuesday():
    hour = int(datetime.datetime.now().hour)
   
    if hour>=7.55 and hour<8.40:
        webbrowser.open(Matbrk)
        speak(dersbaslıyor)
        speak(saymatyt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatyt, duration = 60)

    elif hour>=8.55 and hour<9.40:
        webbrowser.open(Matbrk)
        speak(dersbaslıyor)
        speak(saymatyt)  
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatyt, duration = 60)

    elif hour>=9.50 and hour<10.30:
        webbrowser.open(MatAYT)
        speak(dersbaslıyor)
        speak(saymatayt)  
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatayt, duration = 60)
   
    elif hour>=10.40 and hour<11.20:
        webbrowser.open(MatAYT)
        speak(dersbaslıyor)
        speak(saymatayt)  
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatayt, duration = 60)
   
    elif hour>=11.25 and hour<12.10:
        webbrowser.open(Felsefe) 
        speak(dersbaslıyor)
        speak(sayfelsefe)
        n = ToastNotifier()
        n.show_toast("GoEasy", sayfelsefe, duration = 60)
   
    elif hour>=12.05 and hour<13.40:
        webbrowser.open(KimyaTYT)
        speak(dersbaslıyor)
        speak(saykimyatyt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saykimyatyt, duration = 60)
        
    elif hour>=13.35 and hour<14.30:
        webbrowser.open(BiyTYT)
        speak(dersbaslıyor)
        speak(saybiotyt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saybiotyt, duration = 60)
   
    elif hour>=14.35 and hour<15.20:
        webbrowser.open(KimyaAyt)
        speak(dersbaslıyor)
        speak(saykimyaayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saykimyaayt, duration = 60)
    
    elif hour>=15.25 and hour<16.10:
        webbrowser.open(ing)
        speak(dersbaslıyor)
        speak(saying)
        n = ToastNotifier()
        n.show_toast("GoEasy", saying, duration = 60)
    else:
        speak("You haven't got a lesson right now.")
        n = ToastNotifier()
        n.show_toast("GoEasy", "You haven't got a lesson right now.", duration = 60)

def joinwednesday():
    hour = int(datetime.datetime.now().hour )
   
    if hour>=7.55 and hour<8.40:
        webbrowser.open(TRTYT)
        speak(dersbaslıyor)
        speak(saytr)
        n = ToastNotifier()
        n.show_toast("GoEasy", saytr, duration = 60)

    elif hour>=8.55 and hour<9.40:
        webbrowser.open(TRTYT)
        speak(dersbaslıyor)
        speak(saytr)
        n = ToastNotifier()
        n.show_toast("GoEasy", saytr, duration = 60)
    
    elif hour>=9.50 and hour<10.30:
        webbrowser.open(Fizik)
        speak(dersbaslıyor)
        speak(sayfizikayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", sayfizikayt, duration = 60)
   
    elif hour>=10.40 and hour<11.20:
        webbrowser.open(Fizik)
        speak(dersbaslıyor)
        speak(sayfizikayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", sayfizikayt, duration = 60)
   
    elif hour>=11.25 and hour<12.10:
        webbrowser.open(BiyTYT) 
        speak(dersbaslıyor)
        speak(saybiotyt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saybiotyt, duration = 60)
   
    elif hour>=12.05 and hour<13.40:
        webbrowser.open(ing)
        speak(dersbaslıyor)
        speak(saying)
        n = ToastNotifier()
        n.show_toast("GoEasy", saying, duration = 60)
        
    elif hour>=13.35 and hour<14.30:
        webbrowser.open(Cografya)
        speak(dersbaslıyor)
        speak('Your lesson is geography')
        n = ToastNotifier()
        n.show_toast("GoEasy", 'Your lesson is Geography', duration = 60)

    elif hour>=15.35 and hour<16.20:
        webbrowser.open(KimyaTYT)
        speak(dersbaslıyor)
        speak(saykimyatyt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saykimyatyt, duration = 60)
    
    else:
        speak("You haven't got a lesson right now.")
        n = ToastNotifier()
        n.show_toast("GoEasy", "You haven't got a lesson right now.", duration = 60) 

def jointhursday():
    hour = int(datetime.datetime.now().hour )
   
    if hour>=7.55 and hour<8.40:
        webbrowser.open(MatAYT)
        speak(dersbaslıyor)
        speak(saymatayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatayt, duration = 60)

    elif hour>=8.55 and hour<9.40:
        webbrowser.open(MatAYT)
        speak(dersbaslıyor)
        speak(saymatayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatayt, duration = 60)
    
    elif hour>=9.50 and hour<10.30:
        webbrowser.open(Matbrk)
        speak(dersbaslıyor)
        speak(saymatyt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatyt, duration = 60)
   
    elif hour>=10.40 and hour<11.20:
        webbrowser.open(Matbrk)
        speak(dersbaslıyor)
        speak(saymatyt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatyt, duration = 60)
   
    elif hour>=11.25 and hour<12.10:
        webbrowser.open(Fizik) 
        speak(dersbaslıyor)
        speak(sayfizikayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", sayfizikayt, duration = 60)
   
    elif hour>=12.05 and hour<13.40:
        webbrowser.open(Fizik)
        speak(dersbaslıyor)
        speak(sayfizikayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", sayfizikayt, duration = 60)
        
    elif hour>=13.35 and hour<14.30:
        webbrowser.open(BiyAYT)
        speak(dersbaslıyor)
        speak(saybioayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saybioayt, duration = 60)
   
    elif hour>=14.35 and hour<15.20:
        webbrowser.open(BiyAYT)
        speak(dersbaslıyor)
        speak(saybioayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saybioayt, duration = 60)
    
    elif hour>=15.25 and hour<16.10:
        webbrowser.open(Felsefe)
        speak(dersbaslıyor)
        speak(sayfelsefe)
        n = ToastNotifier()
        n.show_toast("GoEasy", sayfelsefe, duration = 60)
  
    else:
        speak("You haven't got a lesson right now.")
        n = ToastNotifier()
        n.show_toast("GoEasy", "You haven't got a lesson right now.", duration = 60) 

def joinfriday():
    hour = int(datetime.datetime.now().hour )
   
    if hour>=7.55 and hour<8.40:
        webbrowser.open(Fizik)
        speak(dersbaslıyor)
        speak(sayfizikayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", sayfizikayt, duration = 60)

    elif hour>=8.55 and hour<9.40:
        webbrowser.open(BiyAYT)
        speak(dersbaslıyor)
        speak(saybioayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saybioayt, duration = 60)
    
    elif hour>=9.50 and hour<10.30:
        webbrowser.open(TRTYT)
        speak(dersbaslıyor)
        speak(saytr)
        n = ToastNotifier()
        n.show_toast("GoEasy", saytr, duration = 60)
   
    elif hour>=10.40 and hour<11.20:
        webbrowser.open(TRTYT)
        speak(dersbaslıyor)
        speak(saytr)
        n = ToastNotifier()
        n.show_toast("GoEasy", saytr, duration = 60)
   
    elif hour>=11.25 and hour<12.10:
        webbrowser.open(MatAYT) 
        speak(dersbaslıyor)
        speak(saymatayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saymatayt, duration = 60)
   
    elif hour>=12.05 and hour<13.40:
        webbrowser.open(KimyaAyt)
        speak(dersbaslıyor)
        speak(saykimyaayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saykimyaayt, duration = 60)
        
    elif hour>=13.35 and hour<14.30:
        webbrowser.open(KimyaAyt)
        speak(dersbaslıyor)
        speak(saykimyaayt)
        n = ToastNotifier()
        n.show_toast("GoEasy", saykimyaayt, duration = 60)
   
    elif hour>=14.35 and hour<15.20:
        webbrowser.open(TarihAyt)
        speak(dersbaslıyor)
        speak(saytarih)
        n = ToastNotifier()
        n.show_toast("GoEasy", saytarih, duration = 60)
    
    elif hour>=15.25 and hour<16.10:
        webbrowser.open(Alm)
        speak(dersbaslıyor)
        speak('Your lesson is German')
        n = ToastNotifier()
        n.show_toast("GoEasy", "Your lesson is German", duration = 60)
  
    else:
        speak("You haven't got a lesson right now.")
        n = ToastNotifier()
        n.show_toast("GoEasy", "You haven't got a lesson right now.", duration = 60) 
 
label1 = Label(bum,text="Choose Day For Join Your Online Class",font="helvatica")
label1.pack()
Monday = Button(bum, text="Monday",font="helvatica-bold", width = 20,bg = "#DE52AF",fg ="white",command=joinmonday).pack()
Tuesday = Button(bum, text="Tuesday",font="helvatica-bold", width = 20,bg= '#007aff',fg ="white" ,command=jointuesday).pack()
Wednesday = Button(bum, text="Wednesday",font="helvatica-bold", width = 20,bg = "#ffd60a",fg ="white" , command=joinwednesday).pack()
Thursday = Button(bum, text="Thursday",font="helvatica-bold", width = 20,bg = "#ff3b30",fg ="white" ,command=jointhursday).pack()
Friday = Button(bum, text="Friday",font="helvatica-bold", width = 20,bg = "#8fd158",fg ="white" ,command=joinfriday).pack()

bum.mainloop()
