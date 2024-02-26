# import tkinter
 
# janela = tkinter.Tk()
# janela.geometry('500x300')

# def ola():
#  print('oi tudo bem !!!')

# titulo = tkinter.Label(janela,text='bem vindo ao aplivativo')
# botao = tkinter.Button(janela,text='calcular', command=ola)
# titulo.pack(padx=10,pady=10)
# botao.pack(padx=10,pady=10)

# janela.mainloop()
# \\\\\\\\\\\\\\\\\\\


import customtkinter  as ctkn



janela = ctkn.CTk() #criaçao de janela
janela.geometry('500x300') #tamanho da janela 



titulor = ctkn.CTkLabel(janela,text='Bahia é o mundo',text_color='darkred',font=('arial',28))
titulor.pack(padx=10,pady=10) 

login=ctkn.CTkEntry(janela,placeholder_text='Qual seu nome, torcedor?',width=250)
login.pack(padx=10,pady=10)

cpf=ctkn.CTkEntry(janela,placeholder_text='digite seu cpf',width=250,show='♥')
cpf.pack(padx=10,pady=10)

botao = ctkn.CTkButton(janela,text='entrar',text_color='blue')
botao.pack(padx=10,pady=10)


janela.mainloop()



