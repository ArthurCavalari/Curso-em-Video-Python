
iden = str(input('Digite seu nome completo >> '))
mai = iden.upper()
min = iden.lower()

div = iden.split()

iden = iden.replace(' ', '')
len(iden)

print(f'Seu nome com todas as letras maiusculas fica >> {mai}')
print(f'Seu nome com todas as letras minusculas fica >> {min}')
print(f'Seu nome inteiro tem {len(iden)} letras!')
print(f'Seu primeiro nome é {div[0]} e tem {len(div[0])} letras!')