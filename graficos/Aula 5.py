


def media(notas):
    soma = 0

#notas = [5, 6, 7, 8, 9]

    for nota in notas:
        soma = soma + nota
#   media = soma/5
    media = soma/ len(notas)
    return media


print('media = {:.2f}'.format(media([10, 5, 4, 3])))
print('media = {:.2f}'.format(media([10, 8, 6, 7])))

#print('soma = ', soma)
#print('media = ', media)

#print('media = {:.2f}'.format(media))
