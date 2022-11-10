# Faça função que calcule a área do trapézio, dados:
# a) Base maior, b) Base menor c) Altura
# Lembrando que a área pode ser calculada por: ((B+b) * h)/ 2

def calcula_area_trapezio(base_maior:int, base_menor:int, altura:int)-> int:
    return ((base_maior + base_menor) * altura)/ 2

base_maior = int(input("Entre com o valor da base_menor: "))
base_menor = int(input("Entre com o valor da base_maior: "))
altura = int(input("Entre com o valor da altura: "))
area = calcula_area_trapezio(base_maior, base_menor, altura)
print(f"Valor da área é: {area}")