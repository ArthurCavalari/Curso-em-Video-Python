nome = str(input('Digite seu nome: ')).lower()
if nome == 'arthur':
    print('Que nome lindo!')
else:
    print('Seu nome é bem comum!')
print(f'Bom dia, {nome}!')


n1 = float(input('Digite sua primeira nota > '))
n2 = float(input('Digite sua segunda nota  > '))
m = (n1 + n2)/2
print(f'A sua nota foi {m:.1f}')
if m >= 7.0:
    print('Você passou de ano!!')
else:
    print('Você não passou de ano!')
print('--------- Fim ---------')
