nome = str(input('Digite seu nome completo: ')).strip().title()
primeiro = nome.split()
nome = nome.split()
print(f"""
      Seu primeiro nome é >> {primeiro[0]}
      Seu ultimo nome é   >> {nome[len(nome) -1]}
""")
print(len(nome))
