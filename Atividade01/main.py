import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
def mostrar_menu():
    print('Menu')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
def somar(numero1: float, numero2: float) -> str:
  resultado = float(numero1) + float(numero2)
  return locale.format_string('%.2f', resultado, grouping=True)
def subtrair(numero1: float, numero2: float) -> str:
  resultado = float(numero1) - float(numero2)
  return locale.format_string('%.2f', resultado, grouping=True)
def multiplicar(numero1: float, numero2: float) -> str:
  resultado = float(numero1) * float(numero2)
  return locale.format_string('%.2f', resultado, grouping=True)
def dividir(numero1: float, numero2: float) -> str:
  if(numero2 == 0):
    return "Impossível dividir por zero"
  resultado = float(numero1) / float(numero2)
  return locale.format_string('%.2f', resultado, grouping=True)
menu = True
while menu:
    mostrar_menu()
    opcao = input('Escolha uma opção: ')
    if opcao == '5':
        print('Saindo...')
        menu = False
    elif opcao in ['1', '2', '3', '4']:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        
        if opcao == '1':
            print(f'Resultado: {somar(num1, num2)}')
        elif opcao == '2':
            print(f'Resultado: {subtrair(num1, num2)}')
        elif opcao == '3':
            print(f'Resultado: {multiplicar(num1, num2)}')
        elif opcao == '4':
            print(f'Resultado: {dividir(num1, num2)}')
    else:
        print('Opção inválida. Tente novamente.')