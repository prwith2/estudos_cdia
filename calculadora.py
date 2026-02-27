a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
opr = input('Escolha a operação(+, -, * ou /): ') 
SOMA = a + b
SUBTRACAO = a - b
MULTIPLICACAO = a * b
DIVISAO = a / b
if opr == '+':
    print(SOMA)
if opr == '-':
    print(SUBTRACAO)
if opr == '*':
    print(MULTIPLICACAO)
if opr == '/':
    print(DIVISAO)