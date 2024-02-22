import os 
import random

nsorteado =  random. randint(1,100)




while  True:

  palpite = int(input("digite um numero  entre 1 e 100: "))
  os.system('cls')
  if (palpite == nsorteado):
      print("Você acertou!!")
      break
  elif ( palpite > nsorteado):
      print("O numero sorteado é menor!!")
  else:
      print("O número sorteado é maior!!")  
