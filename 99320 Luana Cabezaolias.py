def calcular_delta(a,b,c):  # achar o valor de delta
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Não há raízes com o delta é negativo.")
    
    elif delta == 0:   # delta = 0 
        x = -b / (2 * a)
        print(f'As raízes são iguais, sendo elas: {x}')

    else:    # se delta for maior que 0
        x1 = (-b + delta) / (2 * a)
        x2 = (-b - delta) / (2 * a)
        soma_das_raizes = x1 + x2
        produto_das_raizes = x1 * x2
        print(f"A primeira raiz vale: {x1: .2f} \n e a segunda raiz vale: {x2: .2f}.")
        print(f" A soma das raízes é:" , soma_das_raizes )
        print(f"O produto das raízes é", produto_das_raizes)
        
    Xv = -b / (2 * a)             # x do vertice
    Yv = - delta / (4 * a)        # y do vertice
    print(f"O X do vértice é {Xv: .2f} \n e o Y do vértice é {Yv: .2f}.")


def grafico_da_funcao(a,b,c):
    i = -100
    x = []
    y = []
    while i < 10:
        x.append(i)
        f = a * i ** 2 + b * i + c
        y.append(f)
        i += 1

    print (x)
    print(y)


# Pedir ao usuário os valores de a, b e c
a = float(input("Informe o valor de (a): "))
b = float(input("Informe o valor de (b): "))
c = float(input("Informe o valor de (c): "))

calcular_delta(a, b, c)
grafico_da_funcao(a, b, c)

