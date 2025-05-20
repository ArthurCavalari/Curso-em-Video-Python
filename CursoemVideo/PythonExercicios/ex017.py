from math import hypot
print('Vamos calcular a hipotenusa de um triângulo retângulo!!')
co = float (input('Digite o comprimento do cateto oposto: '))
ca = float (input('Digite o cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir: {hi:.2f}')
