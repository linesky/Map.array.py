import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import *
import subprocess
import shutil
import os
from PIL import Image 
from PIL import ImageTk
import PIL
import array

images=None
ccanvas=None
def convert_rgb_to_16bit(red, green, blue):
    # Mapeia os valores de red, green e blue para os bits relevantes
    high_byte:int = ((red & 0b11000000) >> 2) | ((green & 0b11000000)>>4)
    low_byte:int = ((blue & 0b11000000) >> 6) | (high_byte)
    low_byte:str = chr(low_byte & 127)
    
    # Retorna os bytes high e low como uma tupla
    return low_byte

def msgbox(msgs:str,color:str):
    Window = tk.Toplevel(bg=color)

    
    filename = tk.filedialog.askopenfilename(title="load file")
    image = Image.open(filename)
    f1 = open(filename+".array","w")
    sss1="MapArray\0"
    f1.write(sss1)
    Width, Height = image.size
    rt1=Width//(256*256*256)
    meds2=Width-(rt1*(256*256*256))
    rt2=meds2//(256*256)
    meds2=meds2-(rt2*(256*256))
    
    rt3=meds2//256
    rt4=meds2-(rt3*256)
    f1.write(chr(rt4))
    f1.write(chr(rt3))
    f1.write(chr(rt2))
    f1.write(chr(rt1))
    rt1=Height//(256*256*256)
    meds2=Height-(rt1*(256*256*256))
    rt2=meds2//(256*256)
    meds2=meds2-(rt2*(256*256))
    rt3=meds2//256
    rt4=meds2-(rt3*256)
    f1.write(chr(rt4))
    f1.write(chr(rt3))
    f1.write(chr(rt2))
    f1.write(chr(rt1))
    rt3=8
    rt4=0
    f1.write(chr(rt3))
    f1.write(chr(rt4))
    f1.write(chr(rt4))
    f1.write(chr(rt4))

    f1.close()
    f1 = open(filename+".array","ba")
    # percorre todos os pixels da imagem e muda a cor azul para vermelho
    canvas = tk.Canvas(Window, width=Width, height=Height, bg=color)
    ssd=""
    for y in range(Height):
        for x in range(Width):
            # obtém o valor RGB do pixel atual
            r, g, b = image.getpixel((x, y))
            ssd1=convert_rgb_to_16bit(b,g,r)
            ssd=ssd+ssd1
            
            
            
            s=hex(b+g*256+r*256*256)
            s=s.replace("0x","000000")
            s1=len(s)
            s2=s1-6
            s="#"+s[s2:s1]
            #print(s)
            canvas.create_rectangle((x, y),(x+1,y+1),outline="", fill=s)
               

    
    b111=bytes(ssd.encode("ascii"))
   
    f1.write(b111)
    canvas.pack()
    f1.close()
    print("saved")
    
class BareboneBuilder:
    def __init__(self, root):
        i:int=0
        self.root = root
        self.root.title("")

        # Janela amarela
        self.root.configure(bg='blue')
        # Botões
        self.run_button = tk.Button(self.root, text="load file", command=self.build_kernel)
        self.run_button.pack(pady=5)
       

    def build_kernel(self):
        msgbox("hello world....",'blue') 
       
        
        
       






if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
