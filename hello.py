print('Hello World')
print('Meu primeiro código em Python!')

numero = 23

print(numero)
print('Oi, o número escolhido foi: ', numero)

outroNumero = 10
soma = numero + outroNumero
print(numero,' + ', outroNumero, ' = ', soma)

reais = 53.5553

somaReais = reais - numero
print(somaReais)

nome = 'Fumabare'
mensagem = 'Olha o diamante no pulso, my buddy!'
print(nome,'!', mensagem)

nome = 'Dericky'
mensagem = 'Olha o diamante no pulso, my buddy!'
print(nome,'!', mensagem)

mensagem = nome + ' do Para'
print(mensagem)

idade = 15
print(nome, 'tem', idade, 'anos.')


idade = input('Informe sua idade:')
idade = int(idade)

if (idade > 17):
    print('Maior de idade')
else:
    print('É menor de idade')


verdadeiro = True # ou False
print(nome,"é do Para?")
print(verdadeiro)
if (not verdadeiro):
    print('Não é verdadeiro')
else:
    print('Não é falso')


v1 = True
v2 = True
f1 = False
f2 = False

if (v1 and v2):
    print('Operador AND deu verdadeiro')
else:
    print('Operador AND deu falso')

if (v1 and f1):
    print('Operador AND deu verdadeiro')
else:
    print('Operador AND deu falso')




if (v1 or v2):
    print('Operador OR deu verdadeiro')
else:
    print('Operador OR deu falso')

if (v1 or f1):
    print('Operador OR deu verdadeiro')
else:
    print('Operador OR deu falso')


if (v1 ^ v2):
    print('Operador XOR deu verdadeiro')
else:
    print('Operador XOR deu falso')

if (v1 ^ f1):
    print('Operador XOR deu verdadeiro')
else:
    print('Operador XOR deu falso')


print('Acabou a aula')