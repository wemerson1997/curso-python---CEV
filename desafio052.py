numero = int(input('Digite um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        tot +=1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido por {} vezes'.format(numero, tot))
if tot == 2:
    print('\033[31mE por isso ele é PRIMO')
else:
    print('E por isso \033[33mELE NÃO É PRIMO!')
