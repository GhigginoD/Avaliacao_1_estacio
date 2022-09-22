"""
3. Faça um Programa que peça um número e
informe se o número é inteiro ou decimal. 
"""

number = input("Entre com um número: ")
if ("," in number) or ("." in number): print("O número é um decimal")
else: print("O número é um inteiro")