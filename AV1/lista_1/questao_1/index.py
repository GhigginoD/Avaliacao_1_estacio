"""
Questão 1: 
Tendo como dado de entrada a altura (h) de uma pessoa, construa um 
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7
"""
height = float(input("Entre com uma altura: ").replace(",", "."))
m_weight= (72.7 * height) - 58
f_weight = (62.1 * height) - 44.7
print(f"O peso ideal para um homem de altura {height}m é de {m_weight:.2f}kg.")
print(f"O peso ideal para uma mulher de altura {height}m é de {f_weight:.2f}kg.")