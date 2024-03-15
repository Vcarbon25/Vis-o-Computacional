import cv2
import time
import tkinter as TK
from PIL import Image, ImageTk

raiz = TK.Tk()

ECamera =TK.Label(raiz)
ECamera.grid(row=1, column=0)

ptime=0
ctime=0
cap= cv2.VideoCapture(0)

def show_frames():  #Não sei porque no arquivo novo funciona e no velho não
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   ctime = time.time()
   global ptime
   fps=1/(ctime-ptime)
   nfps = int(fps)
   txtfps=str(nfps)
   cv2.putText(cv2image, txtfps,(10,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(20,80,255))
   ptime=ctime #ele conseguiu fazer a contagem de fps aqui no tkinter tbm
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   ECamera.imgtk = imgtk
   ECamera.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   ECamera.after(20, show_frames)

show_frames()
raiz.mainloop()
