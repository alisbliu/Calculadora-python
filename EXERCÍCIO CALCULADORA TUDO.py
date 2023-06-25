def realizar_calculo():
 
# Loop caso insira um n1 inválido.
 while True:
  try:
   n1 = int(input("Insira o primeiro número: "))
   break
  except ValueError:
   print ("Insira um número válido!")
 
# Loop caso insira um n2 inválido.
 while True:
  try:
   n2 = int(input("Insira o segundo número: "))
   break
  except ValueError:
   print ("Insira um número válido!")

# Loop caso insira uma operação inválida.
 operacao = (input("Insira a operação desejada (+,-,*,/): "))
 while operacao not in ("+","-","*","/"):
  operacao = (input("Insira uma operação válida: "))

# Regras para realizar as operações e mostrar resultado.
 if operacao == ("+"):
  operacao = n1 + n2
  print (f"A soma de {n1} + {n2} = {operacao}.")

 elif operacao == ("-"):
  operacao = n1 - n2
  print (f"A subtração de {n1} - {n2} = {operacao}.")

 elif operacao == ("*"):
  operacao = n1 * n2
  print (f"A multiplicação de {n1} * {n2} = {operacao}.")

 elif operacao == ("/"):
  operacao = n1 / n2
  print (f"A divisão de {n1} / {n2} = {operacao}.")

 resposta = input("Deseja realizar outro cálculo? (Sim/Não): ")

 if resposta.lower() == "sim" or resposta.lower() == "s":
      realizar_calculo()
 else:
      print("Encerrando calculadora.")
      
# Chama a função para reiniciar a calculadora
realizar_calculo()