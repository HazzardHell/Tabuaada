#Exercisio de tabuada em Python

while True:
    try:
        i=int(input('Digite um número de 0 - 10 :'))
    except ValueError:
        print('Valor invalido para criar tabuada!')
        continue
    if i>10 or i<0:
        print('Valor está fora do range!\nTente novamente!')
        continue
    print('0x{}={}'.format(i, i * 0))
    print('1x{}={}'.format(i, i * 1))
    print('2x{}={}'.format(i, i * 2))
    print('3x{}={}'.format(i, i * 3))
    print('4x{}={}'.format(i, i * 4))
    print('5x{}={}'.format(i, i * 5))
    print('6x{}={}'.format(i, i * 6))
    print('7x{}={}'.format(i, i * 7))
    print('8x{}={}'.format(i, i * 8))
    print('9x{}={}'.format(i, i * 9))
    print('10x{}={}'.format(i, i * 10))

    print('\nMesma coisa só que feito no FOR\n')
    for numero in range(0,11):
        print('{} X {} = {}'.format(numero,i,i*numero))
