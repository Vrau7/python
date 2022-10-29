#Crie um programa para calcular as notas obtidas pelo aluno do
#ensino médio, deverá mostrar mensagem para ser digitado a
#nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado, se está em recuperação ou foi reprovado
#sem chance de recuperação.
#• Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

nota1 = float(input("Nota primeiro bimestre:"))
nota2 = float(input("Nota Segunda bimestre:"))
nota3 = float(input("Nota terceiro bimestre:"))
nota4 = float(input("Nota quarto bimestre:"))

resultado = (nota1 + nota2 + nota3 + nota4)
print("resultado foi: ", resultado)
if resultado<40:
    print("REPROVADO")
elif resultado<60:
    print("RECUPERAÇÃO")
elif resultado >=60:
    print("APROVADO")