import customtkinter as ctkn 
import os


ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('green')


janela = ctkn.CTk()
janela.geometry("500x300")
janela.iconbitmap('Gas-pump256_25049.ico')

janela.title('combustivel app 2024')

#funcoes
def calcular():
  d = int(distancia.get())
  c = int(consumo.get())
  p = float(preco.get())
  valor = (d/c)*p
 

  resultado.configure(text= f'o gasto total da viagem foi R${valor:.2f}')






titulo = ctkn.CTkLabel(janela,text= "Combustivel",text_color='white',font=('Verdana',25,'bold'))
titulo.pack(padx=10,pady=10)


distancia = ctkn.CTkEntry(janela,placeholder_text='digite a distancia da viagem: ',width=250,height=25,fg_color='white',text_color='black',placeholder_text_color='gray')
distancia.pack(padx=10,pady=10)

consumo = ctkn.CTkEntry(janela,placeholder_text='digite a consumo da viagem: ',width=250,height=25,fg_color='white',text_color='black',placeholder_text_color='gray')
consumo.pack(padx=10,pady=10)

preco = ctkn.CTkEntry(janela,placeholder_text='digite a preco do combustivel: ',width=250,height=25,fg_color='white',text_color='black',placeholder_text_color='gray')
preco.pack(padx=10,pady=10)


botao = ctkn.CTkButton(janela,text='calcular',width=50,height=10,fg_color='darkgreen',text_color='black',font=('verdana',30,'bold'),hover_color='darkred',command=calcular)
botao.pack(padx=10,pady=10)

resultado = ctkn.CTkLabel(janela,text='',text_color='yellow',font=('verdana',18,'bold'))
resultado.pack(padx=10,pady=10)


janela.mainloop()
