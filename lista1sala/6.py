pv=float(input("digite o valor da prestação"))
tj=float(input("digite o valor da taxa de juros"))
t=float(input("digite o tempo em atraso"))
pa=pv+(pv*(tj/100)*t)
print("o valor da prestação em atraso é", pa)