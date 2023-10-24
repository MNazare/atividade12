 # Exercício Python 12: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
 
import time
print("Chama-se ano bissexto o ano ao qual é acrescentado um\ndia extra, ficando com 366 dias, um dia a mais do que os\nanos normais de 365 dias, ocorrendo a cada quatro anos.")
time.sleep(3)
print("se você tem a curiosidade de saber se um ano é bissexto digite ele abaixo:")
ano = int(input("digite o ano "))
time.sleep(1)
if (ano % 4 == 0):
    print("BOA!", ano, "É UM ANO BISSEXTO")
else:
    print("OH NÃO!", ano, "NÃO É UM ANO BISSEXTO")