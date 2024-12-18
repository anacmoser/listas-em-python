def bhaskara(a, b, c):
    if a != 0:
        delta = (b**2) -4*a*c
        if delta < 0:
            return "Esta equação não possui solução real."
        elif delta == 0:
            x1 = (-b) / (2*a)
            return f"A equação tem uma raiz real: {x1}"
        else:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            return f"A equação tem duas raízes reais e diferentes: {x1} e {x2}"
    else:
        return "O coeficiente A deve ser diferente de zero."
a = float(input("Digite o valor do coeficiente A: "))
b = float(input("Digite o valor do coeficiente B: "))
c = float(input("Digite o valor do coeficiente C: "))
resultado = bhaskara(a, b, c)
print(resultado)