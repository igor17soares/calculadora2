import sys
import math

for t in range(0, 4):

    if (t > 0) and (t < 3):
        print("\nSENHA INCORRETA, TENTE NOVAMENTE!!!")

    elif t == 3:
        print("\nACESSO NEGADO!!!")
        sys.exit()

    password = str(input("Digite a senha para utilizar o programa (3 tentativas!): "))

    if password == "python123":
        q = int(input("\nQuantas vezes você deseja executar o programa? "))

        for i in range(q):

            print("\nQual categoria de operações você quer realizar?")
            print("Digite 1 para operações básicas(+, -, x, /, log, raiz, pot, % ou bhascara)")
            print("Digite 2 para operações geométricas (área, perímetro, seno, cosseno, tangente, Pitágoras)")
            print("Digite 3 para operações envolvendo circunferência")
            alternative = str(input())

            if alternative == "1":

                print("\nQual operação você deseja realizar?")
                print("RESPONDA: soma, subtração, multiplicação, divisão, log, raiz, potenciação, % ou bhascara")
                question = str(input())

                if question == "soma":
                    n = int(input("\nQuantos números você quer somar? "))
                    addition = 0

                    for j in range(n):
                        c = j + 1

                        if n == 1:
                            x = float(input("Digite o número: "))
                            addition = x

                        else:
                            x = float(input(f"Digite o {c}º número: "))
                            addition += x

                    print(f"\n{question.upper()} = {addition}")

                elif question == "subtração":
                    n = int(input("\nQuantos números você deseja subtrair? "))
                    operation = 0
                    for g in range(n):
                        c = g + 1

                        if n == 1:
                            x = float(input("Digite o número: "))
                            operation = x

                        else:
                            x = float(input(f"Digite o {c}º número: "))

                            if c == 1:
                                operation = x

                            else:
                                operation -= x

                    print(f"\n{question.upper()}: {operation}")

                elif question == "multiplicação":
                    n = int(input("\nQuantos números você quer multiplicar? "))
                    addition = 1
                    for k in range(n):
                        c = k + 1

                        if n == 1:
                            x = float(input("Digite o número: "))
                            addition = x

                        else:
                            x = float(input(f"Digite o {c}º número: "))
                            addition *= x

                    print(f"\n{question.upper()} = {addition}")

                elif question == "divisão":
                    x = float(input("Digite o numerador: "))
                    y = float(input("Digite o denominador: "))
                    z = x / y
                    print(f"\n{x} / {y} = {z}")

                elif question == "log":
                    x = float(input("Digite o logaritmando: "))
                    y = float(input("Digite a base: "))
                    z = math.log(x, y)
                    print(f"\n{question.upper()} = {z}")

                elif question == "potenciação":
                    x = float(input("Digite a base: "))
                    y = float(input("Digite o expoente: "))
                    z = math.pow(x, y)
                    print(f"\nRESULTADO = {z}")

                elif question == "%":
                    x = float(input("Digite o número: "))
                    y = float(input("Digite a porcentagem do número: "))
                    z = (x * y) / 100
                    print(f"\n{y}% de {x} = {z}")

                elif question == "raiz":
                    n = float(input("Digite um número para saber sua raiz quadrada: "))
                    z = math.sqrt(n)
                    print(f"\n{question.upper()} QUADRADA DE {n} = {z}")

                elif question == "bhascara":
                    a = float(input("\nCoeficiente A: "))
                    b = float(input("Coeficiente B: "))
                    c = float(input("Coeficiente C: "))
                    d = (b**2) - (4 * a * c)
                    if d < 0:
                        print("\nA EQUAÇÃO NÃO APRESENTA RAÍZES REAIS!!!")
                    elif d == 0:
                        x = (-b + math.pow(d, 2)) / (2 * a)
                        print(f"\nx = {x}")
                    elif d > 0:
                        x1 = (-b + math.pow(d, 2)) / (2 * a)
                        x2 = (-b - math.pow(d, 2)) / (2 * a)
                        print(f"\nx1 = {x1} \n x2 = {x2}")

            elif alternative == "2":

                print("Qual operação você quer realizar?")
                print("RESPONDA: area, perimetro, sen, cos, tan ou pitagoras")
                operation = str(input())

                if operation == "area":
                    print(f"\nVocê deseja saber a {operation} de qual figura geométrica?")
                    print("RESPONDA: quadrado, triangulo, retangulo, trapezio ou losango")
                    fig = str(input())

                    if fig == "quadrado":
                        side = float(input(f"\nDigite a medida do lado do {fig}: "))
                        area = math.pow(side, 2)
                        print(f"{operation.upper()} DO {fig.upper()} = {area}")

                    elif fig == "retangulo":
                        l1 = float(input(f"\nDigite a medida do lado maior do {fig}: "))
                        l2 = float(input(f"Digite a medida do lado menor do {fig}: "))
                        area = l1 * l2
                        print(f"\n{operation.upper()} DO {fig.upper()} = {area}")

                    elif fig == "triangulo":
                        base = float(input(f"\nDigite o valor da base do {fig}: "))
                        size = float(input(f"Digite o valor da altura do {fig}: "))
                        area = (base * size) / 2
                        print(f"\n{operation.upper()} DO {fig.upper()} = {area}")

                    elif fig == "losango":
                        d1 = float(input(f"\nDigite o valor da diagonal maior do {fig}: "))
                        d2 = float(input(f"Digite o valor da diagonal menor do {fig}: "))
                        area = (d1 * d2) / 2
                        print(f"\n{operation.upper()} DO {fig.upper()} = {area}")

                    elif fig == "trapezio":
                        b1 = float(input(f"\nDigite o valor da base maior do {fig}: "))
                        b2 = float(input(f"Digite o valor da base menor do {fig}: "))
                        h = float(input(f"Digite o valor da altura do {fig: }"))
                        area = ((b1 + b2) * h) / 2
                        print(f"\n{operation.upper()} DO {fig.upper()} = {area}")

                elif operation == "perimetro":
                    print(f"\nVocê deseja saber o {operation} de qual figura geométrica?")
                    print("RESPONDA: quadrado, triangulo, retangulo, trapezio ou losango")
                    fig = str(input())

                    if fig == "quadrado":
                        side = float(input(f"\nDigite a medida do lado do {fig}: "))
                        p = side * 4
                        print(f"{operation.upper()} DO {fig.upper()} = {p}")

                    elif fig == "retangulo":
                        l1 = float(input(f"\nDigite a medida do lado maior do {fig}: "))
                        l2 = float(input(f"Digite a medida do lado menor do {fig}: "))
                        p = (l1 * 2) + (l2 * 2)
                        print(f"\n{operation.upper()} DO {fig.upper()} = {p}")

                    elif fig == "triangulo":
                        m1 = float(input(f"\nDigite o valor da 1ª medida do {fig}: "))
                        m2 = float(input(f"Digite o valor da 2ª medida do {fig}: "))
                        m3 = float(input(f"Digite o valor da 3ª medida do {fig}: "))
                        p = m1 + m2 + m3
                        print(f"\n{operation} DO {fig.upper()} = {p}")

                    elif fig == "losango":
                        side = float(input(f"\nDigite o valor do lado do {fig}: "))
                        p = 4 * side
                        print(f"{operation.upper()} DO {fig.upper()} = {p}")

                    elif fig == "trapezio":
                        b1 = float(input(f"\nDigite o valor da base maior do {fig}: "))
                        b2 = float(input(f"Digite o valor da base menor do {fig}: "))
                        l1 = float(input(f"Digite o valor do 3º lado do {fig: }"))
                        l2 = float(input(f"Digite o valor do 4º lado do {fig}"))
                        p = b1 + b2 + l1 + l2
                        print(f"\n{operation.upper()} do {fig.upper()} = {p}")

                elif operation == "cos":
                    ca = float(input("\nDigite o valor do cateto adjacente: "))
                    hip = float(input("Digite o valor da hipotenusa: "))
                    cos = ca / hip
                    print(f"\n{operation.upper()} = {cos}")

                elif operation == "sen":
                    co = float(input("\nDigite o valor do cateto oposto: "))
                    hip = float(input("Digite o valor da hipotenusa: "))
                    sen = co / hip
                    print(f"\n{operation.upper()} = {sen}")

                elif operation == "tan":
                    co = float(input("\nDigite o valor do cateto oposto: "))
                    ca = float(input("Digite o valor do cateto adjacente: "))
                    tan = co / ca
                    print(f"\n{operation.upper()} = {tan}")

                elif operation == "pitagoras":
                    print("\nQual lado você deseja saber?")
                    print("RESPONDA: cateto ou hipotenusa")
                    side = str(input())

                    if side == "hipotenusa":
                        a = float(input("\nDigite o valor do 1º cateto: "))
                        b = float(input("Digite o valor do 2º cateto: "))
                        hip = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
                        print(f"\n{side.upper()} = {hip}")

                    if side == "cateto":
                        a = float(input("\nDigite o valor do outro cateto: "))
                        hip = float(input("Digite o valor da hipotenusa: "))
                        b = math.sqrt(math.pow(hip, 2) - math.pow(a, 2))
                        print(f"\n{side.upper()} = {b}")

            elif alternative == "3":
                print("\nQual medida da circunferência você deseja saber?")
                print("RESPONDA: area, perimetro ou pi")
                operation = str(input())

                if operation == "area":
                    r = float(input("\nDigite o valor do raio: "))
                    area = math.pi * math.pow(r, 2)
                    print(f"{operation.upper()} = {area}")

                elif operation == "perimetro":
                    r = float(input("\nDigite o valor do raio: "))
                    p = 2 * math.pi * r
                    print(f"{operation.upper()} = {p}")

                elif operation == "pi":
                    print(f"\n {operation.upper()} = {math.pi}")

        sys.exit()
