"""
Questão 3:
Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que 
são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
PRICE_IR = 11
PRICE_INSS = 8
PRICE_SYNDICATE = 5

value_hours = float(input("Entre com o valor que você ganha por hora: ").replace(",","."))
working_hours = int(input("Entre com a quantidade de horas trabalhadas no mês: "))
salary_brutto = value_hours * working_hours
discount_ir = (salary_brutto * PRICE_IR) / 100
discount_inss = (salary_brutto * PRICE_INSS) / 100
discount_syndicate = (salary_brutto * PRICE_SYNDICATE) / 100
salary_netto = salary_brutto - (discount_ir + discount_inss + discount_syndicate)

print(f"+ Salário Bruto : R${salary_brutto}")
print(f"- IR (11%) : R${discount_ir}")
print(f"- INSS (8%) : R${discount_inss}")
print(f"- Sindicato (5%) : R${discount_syndicate}")
print(f"= Salário Liquido : R${salary_netto}")