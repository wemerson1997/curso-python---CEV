resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp =  str(input('Quer continar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e menor foi {}'.format(maior, menor))