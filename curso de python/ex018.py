from math import radians, sin, cos, tan
an = float(input('digite um angulo: '))
seno = sin(radians(an))
cos = cos(radians(an))
tg = tan(radians(an))
print('o angulo {} tem cosseno de {:.2f}'.format(an, seno))
print('o angulo {} tem seno de {:.2f}'.format(an, cos))
print('o angulo {} tem tangente de {:.2f}'.format(an, tg))