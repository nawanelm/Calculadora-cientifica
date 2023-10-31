#iniciarei com uma calculadora simples e depois irei adicionando todas as outras funções


operador = input('Olá, seja bem vindo a minha calculadora\n'
      'selecione a opcão que deseja: \n'
      'somar = +\n'
      'subtrair = -\n'
      'dividir = /\n'
      'multiplicar = *\n'
      '>>>')
while (operador != '+') and (operador != '-') and (operador != '/') and (operador != '*'):
      operador = input('voce digitou uma operação inválida, digite novamente.'
      'somar = +\n'
      'subtrair = -\n'
      'dividir = /\n'
      'multiplicar = *\n'
      '>>>')

numero1 = input('digite o primeiro número')
numero2 = input('digite o segundo número')

#while numero1 != int:
#      print('voce não digitou um número inteiro, digite novamente: ')
#      numero1 = int(input('digite o primeiro número'))
#      numero2 = int(input('digite o segundo número'))

if operador == '+':
      op = 'soma'
      result = numero1 + numero2
elif operador == '-':
       op = 'subtração'
       result = numero1 - numero2
elif operador == '/':
      op = 'divisão'
      result = numero1 / numero2
else:
      op = 'multiplicação'
      result = numero1 * numero2

print('O resultado da sua {} é {}'.format(op, result))
