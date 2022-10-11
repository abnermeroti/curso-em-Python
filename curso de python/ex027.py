nome = str(input('digite seu nome completo')).strip()
dividido = nome.split()
print('seu primeiro nome: {} '.format(dividido[0]))
print('seu ultimo nome: {}'.format(dividido[len(dividido)-1]))