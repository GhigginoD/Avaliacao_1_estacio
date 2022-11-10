# Faça um programa em Python com uma função chamada soma_imposto. A função
# possui dois parâmetros formais:
# a) taxa_imposto, que é a quantia de imposto sobre vendas expressa em
# porcentagem; e
# b) custo, que é o custo de um item antes do imposto. A função "altera" o valor de
# custo para incluir o imposto sobre vendas.
# O programa principal deve pedir os dados e usar a função para calcular preço do produto.

def soma_imposto(taxa:int, custo:float) -> float:
    return custo + ((custo * taxa)/100)
taxa = int(input("Entre com o valor da taxa em porcentagem: "))
custo = float(input("Entre com o custo do produto: ").replace(',', '.'))
total = soma_imposto(taxa, custo)
print(f"Preço total do produto com impostos é dê: {total:.2f}")