v = int(input('qual velocidade voce esta dirigindo?'))
if v<=80:
    print('muito bem! dirija com seguranca ')
else:
    print('voce sera multado por sua incopetencia')
    multa = (v-80)*7
    print('voce deve pagar a multa de R${:.2f}'.format(multa))
