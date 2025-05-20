car = float(input('Qual a velocidade do seu carro: '))
multa = float((car - 80) * 7)

if car > 80:
    print(f'Você terá que pagar R${multa:.2f} pela sua velocidade de {car:.0f}Km/h')
    print('Tome mais cuidado! Dirija com segurança!')
else:
    print(f'Você está dentro do limite de velocidade a {car:.0f}Km/h!')
    print('Boa viagem! Dirija com segurança!')