km = float(input('quantos km o carro percorreu?'))
d = int(input('por quantos dias ele foi alugado?'))
pd = d*60
pkm = km*0.15
pf = pkm + pd
print('voce pagou R${:.2f} pelo uso do carro'.format(pf))