import math

q = int(input("Quantas vezes você deseja executar o programa? "))

for i in range(q):

    question = str(input("Qual o operação você quer realizar? \n(RESPONDA +, -, x, /, log, pot ou %) "))

    if question == "+":
        n = int(input("Quantos números você quer somar? "))
        addition = 0
        for i in range(n):
            x = float(input("Digite um número: "))
            addition += x
        print(f"RESULTADO = {addition}")
    else:
        if question == "-":
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
            z = x - y
            print(f"{x} - {y} = {z}")
        else:
            if question == "x":
                n = int(input("Quantos números você quer multiplicar? "))
                addition = 1
                for i in range(n):
                    x = float(input("Digite um número: "))
                    addition *= x
                print(f"RESULTADO = {addition}")
            else:
                if question == "/":
                    x = float(input("Digite o numerador: "))
                    y = float(input("Digite o denominador: "))
                    z = x / y
                    print(f"{x} / {y} = {z}")
                else:
                    if question == "log":
                        x = float(input("Digite o logaritmando: "))
                        y = float(input("Digite a base: "))
                        z = math.log(x,y)
                        print(f"LOGARITMO = {z}")
                    else:
                        if question == "pot":
                            x = float(input("Digite a base: "))
                            y = float(input("Digite o expoente: "))
                            z = x ** y
                            print(f"RESULTADO = {z}")
                        else:
                            if question == "%":
                                x = float(input("Digite o número: "))
                                y = float(input("Digite a porcentagem do número: "))
                                z = (x * y) / 100
                                print(f"RESULTADO = {z}")



















