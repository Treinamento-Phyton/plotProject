#notas = [ 5.6, 7.3, 8.4, 2.5]
#soma = 0.0

def media(notas):
    soma = 0.0
    for nota in notas:
        soma = soma + nota
#    soma = sum(notas)
    media = soma / len(notas)
    return media
print(media([ 5.6, 7.3, 8.4, 2.5 ]))
print('A media do aluno é:', media([1,3,8,9,7]))
print('A media do aluno é: {:.2f}'.format(media([6.2,4,8,7.5,9])))