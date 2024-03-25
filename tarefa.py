import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

#-----------------funções-------------

def adicionar_tarefa():
     tarefa = tarefa_entry.get()
     if tarefa:
         lista_tarefas.insert(0,tarefa)
         tarefa_entry.delete(0,END)
         salve_tarefas()
     else:
      messagebox.showerror('erro','digite uma tarefa')     
      
def remover_tarefa():
     selecionada = lista_tarefas.curselection()
     if selecionada:
         lista_tarefas.delete(selecionada[0])
         salve_tarefas()
     else:
         messagebox.showerror('error','escolha uma tarefa para deletar')
             

def salve_tarefas():
    with open('terefas.txt','w') as f:
     tarefas = lista_tarefas.get(0,E)
     for X in tarefas:
      f.write(X + '\n')
 
 
def carregar_tarefas():
    with open('tarefas.txt','r') as f:
        tarefas = f . readlines()      
        for x in tarefas:
         lista_tarefas.insert(0,x.strip())



#--------------------------------------



#-------------Interface--------------
janela =ctk.CTk('#09112e')
janela.minsize(350,450)
janela.maxsize(350,500)
janela.title('Lista de Tarefas V1.0')
#------------------------------------

#----Reserva de Fontes----
font1 = ('Arial',25,'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',10,'bold')
#--------------------------

ctk.CTkLabel(janela,text='Lista de Tarefas V1.0',font=font1,text_color='white').pack(pady=10)

add_botao = ctk.CTkButton(janela,text = 'Adicionar Tarefa', font = font2, text_color = 'white', fg_color = 'blue',cursor = 'hand2', corner_radius=5, width=120,command=adicionar_tarefa)
add_botao.place(x=20, y=80)

remove_botao = ctk.CTkButton(janela,text = 'Remover Tarefa', font = font2, text_color = 'white', fg_color='darkred' ,cursor = 'hand2', corner_radius=5, width=120,command=remover_tarefa)
remove_botao.place(x=180, y=80)

tarefa_entry = ctk.CTkEntry(janela,font= font2, text_color= 'black',fg_color='white', border_color='white', width=250,placeholder_text='Digite a sua tarefa')
tarefa_entry.pack(pady = 80)


lista_tarefas = Listbox(janela,width=45,height=15,font=font3)

lista_tarefas.place(x=18,y=170)
 
carregar_tarefas()

janela.mainloop()