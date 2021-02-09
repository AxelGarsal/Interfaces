from tkinter import *
#se crea la pantalla principal
raiz = Tk()
raiz.title("Ventana Principal")
#para cambiar el icono
raiz.iconbitmap("caritax.ico")
#Tamaño de la ventana pero no es necesario
#raiz.geometry("550x550")
#Cambiar color de fondo
raiz.config(bg='cyan3')
#El frame que va dentro de la raiz se pone igual que la raiz
frame1 = Frame(raiz)
#Luego se empaqueta para que quede dentro de la ventana raiz
frame1.pack()
frame1.config(bg='green3')
frame1.config(width='330', height='330')
frame1.config(bd=10)
frame1.config(relief='sunken')
#para poner el frame en un posicion deseada se una el metodo side='' y el anchor=''
frame2 = Frame()
frame2.pack()
frame2.config(bg='pink2')
frame2.config(width='220', height='120')
frame2.pack(side='left', anchor='s')
#Para un borde diferente flat, groove, raised, ridge, solid, or sunken
frame2.config(bd=10)
frame2.config(relief='sunken')
label1 = Label(frame2, text="HOLA, qidowendew")
label1.pack()
label2 = Label(frame1, text = "aqui ando")
label2.pack()
#un tercer frame
label3 =Label(raiz, text='algoalfo ad', fg= 'yellow3', font=('arial',20)).place(x='10', y = '10')
#par aagregar una imagen
imagen1=PhotoImage(file='ESCUDO-FES.png')
Label(raiz, image=imagen1).place(x='50', y ='50')


#bucle infinito para ejecutar eventos y debe estar siempre al final
raiz.mainloop()
