from re import split

frase = str('Amo A iara')
#            0123456789

frase2 = str('      Sou boomer!  ')

print(frase)

frase.count('a')#nesse exemplo mostra quantos "a" minusculos tem na frase

frase.find('iara')#procura "iara" em uma string
frase.find('Android')

len(frase)#conta quantos caracteres/mede o comprimento

frase.replace('Amo', 'Adoro')#troca o que eu quiser por outra coisa(não salva então não muda a string de fato, porque só muda na instancia do replace substitua, mas da pra mudar de fato salvando na variavel a mudança)

frase.upper()#deixa tudo em maiusculo
frase.lower()#deixa tudo em minusculo

frase.capitalize()#tudo em minusculo e só a primeira em maiusculo

frase.title()#todas primeiras letras de palavras ficam maiusculas

frase2.strip()#tira espaços sobrando de começo e fim de strings
frase2.rstrip()#tira apenas espaços excedentes do final
frase2.lstrip()#tira apenas espaços excedentes do começo

verificar = ('Amo' in frase)#ve se existe "Amo" na frase e retorna v ou f

frase.split()#separa a palavra em blocos pelos espaços ex: "Amo A iara"
#                                                           012 0 0123
#                                                            0  1  2
dividido = frase.split()

'-'.join(frase)#junta os blocos com algo que você quiser/baseado no espaço


fat = frase[6:]#do 9 ate o fim
fat2 = frase[1::3]#pulando de três em três ate o fim
fat3 = frase[:8]#do começo ate o 8(mas o 8 n conta)
fat4 = frase [0:10:2]#do 1 ate o 10 pulando de dois em dois
fat5 = frase [4]#so o 4

print(fat)
print(fat2)
print(fat3)
print(fat4)
print(fat5)
print(frase.count('a', 0 ,9))#mostrando quantas letras "a" tem do zero ate o 9(sem contar o 9)
print(frase.find('iara'))#mostra em que caracter encontrou o inicio dos caracteres
print(frase.find('Android'))#mostra -1 pq nao tem na string
print(verificar)
print(frase.split())#listas são identificadas por colchetes
print(dividido[2])#mostra o terceiro item da lista
print(dividido[2][2])#mostra o 3 caracter do terceiro item da lista
print(frase.replace('Amo', 'Adoro'))
print(frase.upper())
troll = str (input('quem falar em maiusculo é gay, isso é um teste: '))
print(troll.upper())
gay = str(input('AGORA QUEM FALAR EM MINUSCULO É GAY, NÃO ME DECEPCIONE: '))
print(gay.lower())
print(frase.capitalize())
print(frase.title())
print(frase2.strip())
print(len(frase2))#muito util
print(frase2.rstrip())
print(frase2.lstrip())
print('-'.join(frase))

print("""Nessa aula, vamos aprender operações com String no Python.
 As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(),
upper(), lower(), capitalize(), title(), strip(), junção com join().""")#escreve a frase toda pulando linha nos lugares desejados