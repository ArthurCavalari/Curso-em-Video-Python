from math import sin, cos, tan, radians
an = float (input('Digite um ângulo para descobrir seu seno cosseno e tangente: '))

s = sin(radians(an))
c = cos(radians(an))
t = tan(radians(an))

print(f"""
             O ÂNGULO é: {an}
             O SENO é: {s:.2f}
             O COSSENO é: {c:.2f}
             A TANGENTE é: {t:.2f} 
""")