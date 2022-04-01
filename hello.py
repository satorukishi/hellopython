# Imprime na tela
print('Hello World')
print('Meu primeiro código em Python!')

#Declaração de variável. Pode ser de diversos tipo como:
#str para armazenar textos
#int para armazenar números inteiros
#float para armazenar números com pontos flutuante (casas decimais)
#etc
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

# input serve para solicitar ao usuário que digite alguma coisa. O que ele digitar será atribuído a variável "idade"
idade = input('Informe sua idade:')
idade = int(idade)

# if testa uma condição lógica. Se for True (Verdadeiro), executa os códigos que estão dentro do if.
# else executa os códigos se a condição for False (Falso).
if (idade > 17):
    print('Maior de idade')
else:
    print('É menor de idade')

#A variável do tipo booleana armazena True ou False
verdadeiro = True
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

# a palavra "and" serve para testarmos duas condições lógicas no mesmo if e as duas condições DEVEM ser True
if (v1 and v2):
    print('Operador AND deu verdadeiro')
else:
    print('Operador AND deu falso')

if (v1 and f1):
    print('Operador AND deu verdadeiro')
else:
    print('Operador AND deu falso')

# a palavra "or" por outro lado, basta que pelo menos uma das condições lógicas sejam verdadeiras.
if (v1 or v2):
    print('Operador OR deu verdadeiro')
else:
    print('Operador OR deu falso')

if (v1 or f1):
    print('Operador OR deu verdadeiro')
else:
    print('Operador OR deu falso')

# o caractere "^" testa as duas condições lógicas e somente uma delas devem ser True
if (v1 ^ v2):
    print('Operador XOR deu verdadeiro')
else:
    print('Operador XOR deu falso')

if (v1 ^ f1):
    print('Operador XOR deu verdadeiro')
else:
    print('Operador XOR deu falso')


print('Acabou a aula')