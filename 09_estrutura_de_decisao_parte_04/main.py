nome = input("Informe seu nome: ")
idade = float(input("Informe sua idade: "))

#ternario
result = "é maior de idade." if idade >= 18 else "é menor de idade."


#saida dos dados
print(f"{nome} {result}")