frase = str(input('Digite uma frase >> ')).strip()
frase = frase.lower()

print(f"""
      A letra "A" aparece > {frase.count('a')} vezes na frase.
      A primeira letra "A" apareceu na posição > {frase.find('a')+ 1}
      A última letra "A" apareceu na posição > {frase.rfind('a') + 1}
""")