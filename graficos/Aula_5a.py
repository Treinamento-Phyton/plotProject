notas = [ 5.6, 7.3, 8.4, 2.5]
soma = 0.0

print('A lista tem {0:.1f} elementos'.format(len(notas)))

for nota in notas:
    soma = soma + nota
    print(nota)
media = soma / len(notas)
#media = soma / 4
print('soma das notas é:', soma)
print('a media das notas é: {:.1f}'.format(media))

