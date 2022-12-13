def soma_num (n1=0, n2=0):
    n1 = float(input('Diga o primeiro número:'))
    n2 = float(input('Diga o segundo número: '))
    soma = n1 + n2
    print('O resultado da soma é: ', soma)

def subt_num ():
    n1 = float(input('Diga o primeiro número:'))
    n2 = float(input('Diga o segundo número: '))
    subt = n1 - n2
    print('O resultado da subtração é: ', subt)

def div_num ():
    n1 = float(input('Diga o primeiro número:'))
    n2 = float(input('Diga o segundo número: '))
    div = n1 // n2
    print('O resultado da divisão é: ', div)

def multp_num ():
    n1 = float(input('Diga o primeiro número:'))
    n2 = float(input('Diga o segundo número: '))
    multp = n1 * n2
    print('O resultado da multiplicação é: ', multp)

def main ():
    while True:
        print('[1] Dividir')
        print('[2] Subtrair')
        print('[3] Soma')
        print('[4] Multiplicar')
        print('[5] Encerrar')

        resp = int(input('Diga sua opção: '))
        if resp == 1:
            div_num()
        elif resp == 2:
            subt_num()
        elif resp == 3:
            soma_num()
        elif resp == 4:
            multp_num()
        elif resp == 5:
            break
        else:
            print(':) repete')
            main()

main()