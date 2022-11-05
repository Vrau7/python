#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
#compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
#escreva o custo total da compra. Ao final perguntar se deseja repetir e fazer o calculo de outra compra.
continuar = 'S'
while continuar == 'S':

     Maçã = int(input("Quantidade de maçãs: "))
     if   Maçã >=12:
          Valor = 1.00
     else:
          Valor =  1.30
     Valor_final = Valor * Maçã
     print("O valor final é: ", Valor_final)
     continuar = input("Deseja repetir e fazer o calculo de outra compra? s ou n ").upper()

