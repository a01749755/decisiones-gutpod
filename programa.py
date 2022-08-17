#comparacion de tres monedas 
moneda1=int(input('Valor de la moneda: '))
moneda2=int(input('Valor de la moneda: '))
if(moneda1<moneda2):
    menorvalor=moneda1
else:
    menorvalor=moneda2
moneda3=int(input('Valor de la moneda: '))
if(moneda3<menorvalor):
        menorvalor=moneda3    
print(f'La moneda con menor valor es {menorvalor}')