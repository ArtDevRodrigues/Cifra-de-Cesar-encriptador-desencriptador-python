import bibliotecaDeCriptografia as bc
import tkinter as tk 

tela = tk.Tk()
tela['bg']='#2d2d2d'
tela.title("Encriptador e Desencriptador")

#===Area dos Comandos===#

def encriptar ():

    nome = str(bc.Encriptar(ed1.get()))
    ed2.delete(0, tk.END)
    ed2.insert(0,nome)
   
def desencriptar ():

    nome = str(bc.Desencriptar(ed2.get()))
    ed1.delete(0, tk.END)
    ed1.insert(0,nome)
    

#===Detalhamento Da Tela===#

lb1 = tk.Label(tela, text='Insira a Palavra a Ser Encriptada: ',  bg='#949494').place(x=85,y=20)
ed1 = tk.Entry(tela, bg='#949494', width=50)
ed1.place(x=25,y=50)
bt1 = tk.Button(tela, text='Encriptar', bg='#949494', fg='#473232', width=15, command= encriptar ).place(x=115,y=80)

lb2 = tk.Label(tela, text='Insira a Palavra a Ser Desencriptada: ', bg='#949494').place(x=85,y=120)
ed2 = tk.Entry(tela, bg='#949494', width=50)
ed2.place(x=25,y=150)
bt2 = tk.Button(tela, text='Desencriptar', bg='#949494', fg='#473232', width=15, command=desencriptar).place(x=115,y=180)

#===ETC===#

tela.geometry('400x300')

tela.mainloop()