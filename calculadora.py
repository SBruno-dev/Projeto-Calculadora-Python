from time import sleep

# \ - - - - - SCRIPT CRIADO POR BRUNO SILVA - - - - /

print("\n-- Calculadora em Python --\n")
sleep(2)

def recebeInput():
    receber_input = int(input("Escolha o tipo de cálculo que deseja fazer:\n 1 -> Soma (+) \n 2 -> Subtração (-) \n 3 -> Multiplicação (x) \n 4 -> Divisão (/)\n Escolha de 1 a 4: "))
    if receber_input == 1:
        sleep(1)
        print(f"Ok o valor escolhido foi: {receber_input}\n")
        sleep(2)
        valor1 = int(input("Digite um primeiro valor que deseja calcular: "))
        if valor1 != str:
            valor2 = int(input(f"OK valor {valor1} recebido, agora digite um segundo valor: "))
            if valor2 != str:
                print(f"OK Valor {valor2} recebido")
                print("calculando")
                print('.'), sleep(1), print('..'), sleep(2), print('...')
                sleep(2)
                print(f"\nO Cálculo de {valor1} " '+' f" {valor2} é igual a:", valor1 + valor2)
            else:
                False
        else:
            False
            # \ - - - - - - FAZ O CALCULO PARA SUBTRAÇÃO - - - - - - /
    elif receber_input == 2:
        sleep(1)
        print(f"Ok o valor escolhido foi: {receber_input}\n")
        sleep(2)
        valor1 = int(input("Digite um primeiro valor que deseja calcular: "))
        if valor1 != str:
            valor2 = int(input(f"OK valor {valor1} recebido, agora digite um segundo valor: "))
            if valor2 != str:
                print(f"OK Valor {valor2} recebido")
                print("calculando")
                print('.'), sleep(1), print('..'), sleep(2), print('...')
                sleep(2)
                print(f"O Cálculo de {valor1} " '-' f" {valor2} é igual a:", valor1 - valor2)
            else:
                False
        else:
            False
            # \ - - - - - - FAZ O CALCULO PARA MULTIPLICAÇÃO - - - - - - /
    elif receber_input == 3:
        sleep(1)
        print(f"Ok o valor escolhido foi: {receber_input}\n")
        sleep(2)
        valor1 = int(input("Digite um primeiro valor que deseja calcular: "))
        if valor1 != str:
            valor2 = int(input(f"OK valor {valor1} recebido, agora digite um segundo valor: "))
            if valor2 != str:
                print(f"OK Valor {valor2} recebido")
                print("calculando")
                print('.'), sleep(1), print('..'), sleep(2), print('...')
                sleep(2)
                print(f"\nO Cálculo de {valor1} " 'x' f" {valor2} é igual a:", valor1 * valor2)
            else:
                False
        else:
            False
            # \ - - - - - - FAZ O CALCULO PARA DIVISÃO - - - - - - /
    elif receber_input == 4:
        sleep(1)
        print(f"Ok o valor escolhido foi: {receber_input}\n")
        sleep(2)
        valor1 = int(input("Digite um primeiro valor que deseja calcular: "))
        if valor1 != str:
            valor2 = int(input(f"OK valor {valor1} recebido, agora digite um segundo valor: "))
            if valor2 != str:
                print(f"OK Valor {valor2} recebido")
                print("calculando")
                print('.'), sleep(1), print('..'), sleep(2), print('...')
                sleep(2)
                print(f"\nO Cálculo de {valor1} " '/' f" {valor2} é igual a:", valor1 / valor2)
            else:
                False
        else:
            False
        # - - - - - CASO NÃO SEJA NENHUMA DAS 4 OPÇÕES ACIMA, IRÁ CAIR NO ELSE QUE RETORNARÁ PARA O INCIO DO SCRIPT - - - - -
    else:
        False
        print("\nOPS, Acho que algo saiu fora do esperado.. \n")
        sleep(3)
        print("- - REINICIANDO - -")
        sleep(2)
        recebeInput()
        

recebeInput()
    