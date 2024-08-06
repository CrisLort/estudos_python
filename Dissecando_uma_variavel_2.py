#Faça um programa que leia algo e mostre na tela seu tipo primitivo e
#todas as informações possiveis sovbre ela

a = input('Digite algo:')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaço?', a.isspace())
print('É um número?', a.isnumeric())
print('É um alfabético?', a.isalpha())
print('É um alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em aminúsculas?', a.islower())
print('Está capitalizada?', a.istitle())