#Humberto Hernández Trejo

from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.geometry("655x570")

style = ttk.Style()
style.theme_use("clam")
style.map("Treeview")

#frames

tituloFrame = Frame(raiz, bg="gray40")
tituloFrame.grid(column=0, row= 0)

blackFrame = Frame(raiz,padx=22,pady=14,bg="black")
blackFrame.grid(column=0,row=1)

fondoFrame = Frame(blackFrame,padx=25,pady=6,bg="#482525")
fondoFrame.grid(column=0, row=1)

datosFrame = Frame(fondoFrame, padx=15,pady=5,bg="#482525")
datosFrame.grid(column=0, row=0)

opcFrame = Frame(fondoFrame,padx=5,pady=5,bg="#482525")
opcFrame.grid(column=2, row=0,sticky=(W))
imagenFrame = Frame(opcFrame,bg="#452525",pady=17)
imagenFrame.grid(column=0,row=0,sticky=(W))

listaFrame = Frame(fondoFrame,padx=10,pady=5,bg="#482525")
listaFrame.grid(column=0, row=2, sticky=(W),columnspan=3)
'''
#scroll del tamaño igual a la foto pero esta fuera del tree
scrollbar = ttk.Scrollbar(orient=VERTICAL)
scrollbar.set(0, 0.60)
scrollbar.place(x=594, y=309, height=229)

style=ttk.Style()
style.theme_use('clam')
style.configure("Vertical.TScrollbar", )'''

#datos
idP = StringVar()
Name = StringVar()
Desc = StringVar()
Quant = StringVar()
Price = StringVar()

#label titulo
ttk.Label(tituloFrame, text="Product management ",padding="20 5 44 5",font=("Arial", 36,"bold"),foreground="white",background="gray40").grid(column=1, row=0,sticky=(W))

#imagenes
imagen = PhotoImage(file="carrito.png")
bimagen = Label(tituloFrame)
bimagen.configure(background="gray40")
bimagen.grid(column=0 ,row=0,sticky=(W))
bimagen['image'] = imagen

limpia = PhotoImage(file="Limpiar.png")
limage = ttk.Label(imagenFrame,background="#452525")
limage['image'] = limpia

lupa = PhotoImage(file="lupa.png")
uimage = ttk.Label(imagenFrame,background="#482525")
uimage['image'] = lupa

#labels datos
ttk.Label(datosFrame, text="Id product:                 ",font=("Arial", 11,"bold"),foreground="white",background="#452525").grid(column=0, row=0,sticky=(W))
ttk.Label(datosFrame, text="Name: ",font=("Arial", 11,"bold"),foreground="white",background="#452525").grid(column=0, row=1,sticky=(W))
ttk.Label(datosFrame, text="Description:",font=("Arial", 11,"bold"),foreground="white",background="#452525").grid(column=0, row=2, sticky=(W))
ttk.Label(datosFrame, text="quantity ",font=("Arial", 11,"bold"),foreground="white",background="#452525").grid(column=0, row=3, sticky=(W))
ttk.Label(datosFrame, text="Price:",font=("Arial", 11,"bold"),foreground="white",background="#452525").grid(column=0, row=4, sticky=(W))

#guiones
ttk.Label(datosFrame, text="___________________",font=("Arial", 14,"bold"),foreground="white",background="#452525").grid(column=1, row=0,sticky=(S,E),pady=4)
ttk.Label(datosFrame, text="___________________",font=("Arial", 14,"bold"),foreground="white",background="#452525").grid(column=1, row=1,sticky=(S,E),pady=4)
ttk.Label(datosFrame, text="___________________",font=("Arial", 14,"bold"),foreground="white",background="#452525").grid(column=1, row=2, sticky=(S,E),pady=4)
ttk.Label(datosFrame, text="___________________",font=("Arial", 14,"bold"),foreground="white",background="#452525").grid(column=1, row=3, sticky=(S,E),pady=4)
ttk.Label(datosFrame, text="___________________",font=("Arial", 14,"bold"),foreground="white",background="#452525").grid(column=1, row=4, sticky=(S,E),pady=4)

#entry datos
idEntry = Entry(datosFrame, textvariable=idP, width=15,font=("Arial", 10,"bold"),foreground="white",background="#452525",borderwidth=0,highlightthickness=0).grid(column=1, row=0, sticky=(N,E))
NEntry = Entry(datosFrame, textvariable=Name, width=15,font=("Arial", 10,"bold"),foreground="white",background="#452525",borderwidth=0,highlightthickness=0).grid(column=1, row=1, sticky=(N,E))
descEntry = Entry(datosFrame,textvariable=Desc, width=15,font=("Arial", 10,"bold"),foreground="white",background="#452525",borderwidth=0,highlightthickness=0).grid(column=1, row=2, sticky=(N,E))
quantEntry = Entry(datosFrame,textvariable=Quant, width=15,font=("Arial", 10,"bold"),foreground="white",background="#452525",borderwidth=0,highlightthickness=0).grid(column=1, row=3, sticky=(N,E))
PriceEntry = Entry(datosFrame,textvariable=Price, width=15,font=("Arial", 10,"bold"),foreground="white",background="#452525",borderwidth=0,highlightthickness=0).grid(column=1, row=4, sticky=(N,E))

#buttons
Button(opcFrame,text="Save",padx=4,pady=5,width=15,font=("Arial",10,"bold"),bg="green",activebackground="#482525",foreground="white",activeforeground="#4c02a0",borderwidth=0,highlightthickness=0).grid(column=0,row=1,sticky=(E))
Button(opcFrame,text="Delete",padx=4,pady=5,width=15,font=("Arial",10,"bold"),bg="red",activebackground="#482525",foreground="white",activeforeground="#4c02a0",borderwidth=0,highlightthickness=0).grid(column=0,row=2,sticky=(W),pady=10)
Button(opcFrame,text="Update",padx=4,pady=5,width=15,font=("Arial",10,"bold"),bg="orange",activebackground="#482525",foreground="white",activeforeground="#4c02a0",borderwidth=0,highlightthickness=0).grid(column=0,row=3,sticky=(W),pady=10)
Button(imagenFrame,text="Back",font=("Arial",13,"bold"),width=5,bg="#482525",borderwidth=0,highlightthickness=0,activebackground="#482525",foreground="purple2").grid(column=2,row=0,sticky=(W))
Button(imagenFrame,image=lupa,bg="#482525",borderwidth=0,highlightthickness=0,activebackground="#482525").grid(column=0,row=0,sticky=(W),padx=5)
Button(imagenFrame,image=limpia,bg="#482525",borderwidth=0,highlightthickness=0,activebackground="#482525").grid(column=1,row=0,sticky=(W),padx=5)

#Tree para datos de muestra
tree = ttk.Treeview(listaFrame,columns=("c1", "c2", "c3","c4"))

#Añade una scrollbar al ttk tree
tree_scrollbar = ttk.Scrollbar(listaFrame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scrollbar.set)
tree_scrollbar.grid(row=0, column=1, sticky="ns")

#medida columnas
tree.column("#0", width=105,anchor=W)
tree.column("#1", width=105, anchor=W)
tree.column("#2", width=105, anchor=W)
tree.column("#3", width=105, anchor=W)
tree.column("#4", width=105, anchor=W)
#nombre columnas
tree.heading("# 0", text="idProduct", anchor=CENTER)
tree.heading("# 1", text="namep", anchor=CENTER)
tree.heading("# 2", text="description", anchor=CENTER)
tree.heading("# 3", text="quantity", anchor=CENTER)
tree.heading("# 4", text="unite_price", anchor=CENTER)
# Insertar datos en columnas
tree.insert('', 'end', text="1", values=("Condia", "lait", "24", "$100"))
tree.insert('', 'end', text="2", values=("la vache quirit", "fromage", "200", "$300"))
tree.insert('', 'end', text="3", values=( "hamound boualam", "boisson gaseuse", "98", "$90"))
tree.insert('', 'end', text="4", values=("Mina", "Chocolat", "80", "$50"))
tree.insert('', 'end', text="5", values=("Aroma", "cafe", "60", "$80"))
tree.insert('', 'end', text="6", values=("Facto", "Facto", "7000", "$600"))

#Ubica el ttk tree en la ventana
tree.grid(row=0, column=0, sticky="nsew")

# Configura el contenedor del ttk tree para que se ajuste al tamaño del ttk tree
listaFrame.columnconfigure(0, weight=1)
listaFrame.rowconfigure(0, weight=1)

raiz.mainloop()