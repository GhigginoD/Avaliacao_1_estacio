# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# a) A entrada é dada em dois inteiros.
# b) Deve haver pelo menos duas funções: uma para a conversão e uma para a saída.
# c) Registre a informação A.M./P.M. como um valor "A" para A.M. e "P" para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para
# registrar se é A.M. ou P.M.
# d) Inclua um loop que permita que o usuário repita esse cálculo para novos valores
# de entrada todas as vezes que desejar, digitando um valor negativo para a hora
# quando quiser encerrar

def converte(hora:int, minutos:int) -> None:
    hora = hora % 12
    if hora < 10:
        hora = "0" + str(hora)
    if minutos < 10:
        minutos = "0" + str(minutos)
    mostra_hora(f"{hora}:{minutos} {tipo}")

def mostra_hora(horario:str) -> None:
    print(horario)

while True:  
    hora = int(input("Entre com a hora: ")) 
    if hora in range(0,12):
        tipo = 'A.M'
    elif hora in range(12,25):
        tipo = 'P.M'
    else: 
        print('Horário inválido!')
        break
    minutos = int(input("Entre com os minutos: "))
    converte(hora, minutos)