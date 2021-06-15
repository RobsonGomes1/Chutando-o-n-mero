try:
    from random import randint

    nu = randint(1, 100)
except:
    print('Desculpa, mas aconteceu um erro na solicitação')
else:
    Aviso1 = print('Chute do 1 adiante ;)')
    aviso = print('escreva "[Sair]" para finalizar')
    ch = str
    ch1 = 0
    while ch != 'sair'.strip():
            from time import sleep
            ch1 = int(input('Chute um numero: \n '.strip()))
            sleep(1.0)

            ch = str(input('Deseja sair? Caso não... Aperte ENTER: '.strip() ))
            sleep(1.0)

            if ch1 <= nu:

                print('Quase hein!!!')
                sleep(1.0)
            elif ch1 >= nu:
                print('Quase lá!!!')
                sleep(1.0)

            elif ch1 == nu:
                print('Acertouuuu!!')

                sleep(1.0)
    else:
        if ch == 'sair'.strip():
            print('Até breve!!')
            sleep(1.0)



finally:
    print('Bem vindo e volte sempre!')