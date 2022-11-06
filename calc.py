import sys
import math

for t in range(0, 4):
    if (t > 0) and (t < 3):
        print("\nSENHA INCORRETA TENTE NOVAMENTE!!!")

    elif t == 3:
        print("\nACESSO NEGADO!!!")
        sys.exit()

    senha = str(input("Digite a senha para utilizar o programa: "))

    if senha == "python123":
        q = int(input("\nQuantas vezes você deseja executar o programa? "))

        for i in range(q):

            print("\nQual o operação você quer realizar?")
            print("(RESPONDA +, -, x, /, log, raiz, pot, % ou bhascara)")
            question = str(input())

            if question == "+":
                n = int(input("\nQuantos números você quer somar? "))
                addition = 0
                for j in range(n):
                    x = float(input("Digite um número: "))
                    addition += x
                print(f"\nRESULTADO = {addition}")

            elif question == "-":
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                z = x - y
                print(f"\n{x} - {y} = {z}")

            elif question == "x":
                n = int(input("\nQuantos números você quer multiplicar? "))
                addition = 1
                for k in range(n):
                    x = float(input("Digite um número: "))
                    addition *= x
                print(f"\nRESULTADO = {addition}")

            elif question == "/":
                x = float(input("Digite o numerador: "))
                y = float(input("Digite o denominador: "))
                z = x / y
                print(f"\n{x} / {y} = {z}")

            elif question == "log":
                x = float(input("Digite o logaritmando: "))
                y = float(input("Digite a base: "))
                z = math.log(x, y)
                print(f"\nLOGARITMO = {z}")

            elif question == "pot":
                x = float(input("Digite a base: "))
                y = float(input("Digite o expoente: "))
                z = x ** y
                print(f"\nRESULTADO = {z}")

            elif question == "%":
                x = float(input("Digite o número: "))
                y = float(input("Digite a porcentagem do número: "))
                z = (x * y) / 100
                print(f"\nRESULTADO = {z}")

            elif question == "raiz":
                n = float(input("Digite o índice do radical: "))
                x = float(input("Digite o radicando: "))
                z = math.pow(x, n)
                print(f"\nRESULTADO = {z}")

            elif question == "bhascara":
                print("Digite o valor de A, B e C:")
                a = float(input())
                b = float(input())
                c = float(input())
                d = (b**2) - (4 * a * c)
                if d < 0:
                    print("\nA equação não apresenta raízes reais")
                elif d == 0:
                    x = (-b + math.pow(d, 2)) / (2 * a)
                    print(f"\nx = {x}")
                elif d > 0:
                    x1 = (-b + math.pow(d, 2)) / (2 * a)
                    x2 = (-b - math.pow(d, 2)) / (2 * a)
                    print(f"\nx1 = {x1} \n x2 = {x2}")

        sys.exit()
