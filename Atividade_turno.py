#Atividade turno

turno = input("Qual turno voce estuda? Caso seja Matutino digite M, Vespertino digite V e Noturno N: ").upper()

match turno:
     case "M":
          print("Bom dia!")
     case "T":
          print("Boa tarde!")
     case "N":
          print ("Boa noite!")
     case _:
          print("Valor invalido")




