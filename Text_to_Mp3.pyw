import os
import tkinter
from tkinter.tix import ButtonBox
from tkinter.ttk import Style
import keyboard
from pygame import mixer
from gtts import gTTS
from tkinter import*
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox
from mutagen.mp3 import MP3
import time
# import profit
# import loss
class Main:

    def __init__(self, root):
        self.root = root
        photo = PhotoImage(file = "icon.png")
        photo2=Image.open("icon.png").resize([50,50])
        
        self.root.iconphoto(False, photo)
        self.root.geometry("600x400+500+200")
        self.root.resizable(False,False)
        self.root.title("Text To Mp3")
        


       
        

        
        self.text=Text(self.root,bg='lightblue',width=70,height=15)
        self.text.place(x=20 , y=50)


        
        self.L1=Label(self.root,text="Enter Your Text Below:",font=("New Times Roman",15),bg="white")
        self.L1.place(x=200,y=8)


        self.intry=Entry(self.root,width=70,bg="cyan",fg="black")
        self.intry.place(x=10,y=320)


        # Buttons

        self.BU=Button(self.root,text="OutPut Folder",bg="#00FFFF",fg="red",command=self.output)
        self.BU.place(x=460,y=320)


        # <<<<<-------Button Submit----------->>>>>>>>
        self.Bs=Button(self.root,text="Submit",bg="black",fg="white",command=self.text_to_speech)
        self.Bs.place(x=300,y=365)

        # <<<<<-------Button Clear----------->>>>>>>>
        # Style.configure('Style1',font='Times New Roman',background="gradient-linar(green,red)")
        self.Bc=Button(self.root,text="Clear",bg="red",fg="white",command=self.clear)
        self.Bc.place(x=380,y=365)

        self.Bp=Button(self.root,text="Play",bg="purple",fg="white",command=self.play)
        self.Bp.place(x=550,y=8)
        

  

    def text_to_speech(self):
        # try:
          
            self.data=self.text.get("1.0",END)
            self.path=self.intry.get()
            
            
            
                
            tts=gTTS(self.data,)
            self.filename=f'{self.path}/text_to_speech.mp3'
            tts.save(self.filename)
           
            if os.path.exists(self.filename):
                messagebox.showinfo(title="Success",message="Congratulations Your Text Has Been \n Convert Into Mp3")
            else:
                messagebox.showerror(title="Failed",message="Some Error Occured.\n Retry Again")
        # except:
            # messagebox.showerror(title="Error",message=f"Some Error Occured.\n 1.Check Your Internet\n2.The Input Fields Can't be blank\n ")


    
    def clear(self):
        self.text.delete("1.0",END)
        self.intry.delete(0,END)

    def output(self):
        self.intry.delete(0,END)

        path=str(filedialog.askdirectory())

        self.intry.insert(0,path)

    def play(self):
        try:

            if os.path.exists(self.filename):
                mixer.init()
                mixer.music.load(self.filename)
                mixer.music.play()
                if keyboard.read_key()=='s':
                    mixer.music.stop()
                    mixer.music.unload()
                
                else:
                    audio = MP3(self.filename)
                    length=audio.info.length
                    time.sleep(length)
                    mixer.music.unload()
        except:
           messagebox.showerror(title="Error", message="Generate the audio first then play")
            
        
       


      
            

       

        
root = Tk()
obj = Main(root)
root.mainloop()