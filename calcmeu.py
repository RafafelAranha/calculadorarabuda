numero1 = float(input("Digite o primeiro número:"))
operador = (input("Digite o operador(+-*/):"))
numero2 = float(input("Digite o segundo número:"))

if operador == "+":
    result1 = (numero1+numero2)
    print (f"Resultado: {result1}")

elif operador == "/":
    result2 = (numero1/numero2)
    print (f"Resultado: {result2} ")

elif operador == "-":
    result3 = (numero1-numero2)
    print (f"Resultado:{result3}")

elif operador == "*":
    result4 = (numero1*numero2)
    print (f"Resultado: {result4}")

else:

    print("Operação não válida.")

