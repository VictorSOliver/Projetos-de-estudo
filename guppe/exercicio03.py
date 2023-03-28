""""
#1 Faça um programa que mostre os cincos primeiros números múltiplos de 3, considerando números maiores que 0

for num in range(1,6):
    print(num * 3, end=" ")

#2 Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes.
#A primeira vez deve usar a estrutura de repetição for, a segunda while, e a terceira do while.

# For
for _ in range(0,3):
    for num in range(1,101):
        print(num,end=' ')
    print("")

# While
vezes = 0
while vezes < 3:
    num = 1
    while num <= 100:
        print(num, end=' ')
        num = num + 1
    print('')
    num = 1
    vezes = vezes + 1

# Do while
vezes = 0
while True:
    num = 1
    while (num <= 100):
        print(num, end=' ')
        num = num + 1
    print('')
    vezes = vezes + 1
    if vezes == 3:
        break;

#3 Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e
#terminando em 0. Mostrar uma mensagem 'FIM!' após a contagem

for num in range(100,-1,-1):
    print(f'Contagem: {num}')
    sleep(1)
print('FIM!')

#4 Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000,
#imprimindo seu valor na tela, até que seu valor seja 100_000

for num in range(0,100_001,+1000):
    print(num)

#5 Faça um programa que peça ao usuário para digitar 10 valores em some-os

parada = 10
soma = 0
for num in range(1,parada+1):
    valor = int(input(f'Digite o valor {num}/{parada}: '))
    soma = soma + valor
print(f'Valor da soma dos 10 valores: {soma}')

#6 Faça um programa que leia 10 inteiros e imprima sua média

soma = 0
parada = 10
for num in range(0,parada):
    valor = int(input(f'Digite o valor {num+1}/{parada}: '))
    soma = soma + valor
media = Decimal(soma/10)
print(f'A média dos 10 valores: {media:.1f}')

#7 Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média

soma = 0
parada = 10
n_elementos = 10
for num in range(0,parada):
    valor = int(input(f'Digite o valor {num+1}/{parada} positivo: '))
    if valor >= 0:
        soma = soma + valor
    else:
        n_elementos = n_elementos - 1
media = Decimal(soma/n_elementos)
print(f'A média dos valores positivos: {media:.1f}')

#8 Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido

lenght = 10
a = []
for i in range(0,lenght):
    a.insert(i,int(input(f'Digite o valor {i+1}/{lenght}: ')))
maior = a[0]
menor = a[0]

for j in range(1,lenght):
    if a[j] > maior:
        maior = a[j]
    elif a[j] < menor:
        menor = a[j]
print(f'Maior valor dentre os 10 valores: {maior}')
print(f'Menor valor dentre os 10 valores: {menor}')

#9 Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

n_valores = int(input('Digite um número: '))
print(f'Os primeiros {n_valores} ímpares: ')
for i in range(0,n_valores+1):
    if i % 2 != 0:
        print(i)

#10 Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.

j = 0
for i in range(0,51):
    if i % 2 == 0:
        j = j + i
        print(j)
        sleep(1)
print(f'A soma dos 50 primeiros números pares: {j}')

#11 Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem
#crescente

n_valores = int(input('Digite um número: '))
print(f'Números de 0 até {n_valores}:')
for i in range(0,n_valores+1):
    print(i)

#12 Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem
#decrescente

n_valores = int(input('Digite um número: '))
print(f'Números de {n_valores} até 0:')
for i in range(n_valores,-1,-1):
    print(i)

#13 Faça um programa que leia um número inteiro, positivo e par N e imprima todos os números pares de 0 até N
#em ordem crescente

n_valores = int(input('Digite um valor positivo e par: '))
while n_valores < 0 or n_valores % 2 != 0:
    print('Valor incorreto!')
    n_valores = int(input('Digite um valor positivo e par: '))
print(f'Valores pares de 0 até {n_valores}: ')
for i in range(0, n_valores+1, +2):
    print(i)

#14 Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
#decrescente

n_valores = int(input('Digite um valor positivo e par: '))
while n_valores < 0 or n_valores % 2 != 0:
    print('Valor incorreto!')
    n_valores = int(input('Digite um valor positivo e par: '))
print(f'Valores pares de {n_valores} até 0: ')
for i in range(n_valores, -1, -2):
    print(i)

#15 Faça um programa que leia um número inteiro, positivo e ímpar N e imprima todos os números ímpares de 1 até N
#em ordem crescente

n_valores = int(input('Digite um valor positivo e ímpar: '))
while n_valores < 0 or n_valores % 2 == 0:
    print('Valor incorreto!')
    n_valores = int(input('Digite um valor positivo e ímpar: '))
print(f'Valores ímpares de 0 até {n_valores}: ')
for i in range(1, n_valores+1):
    if i % 2 != 0:
        print(i)

#16 Faça um programa que leia um número inteiro, positivo e ímpar N e imprima todos os números ímpares de 1 até N
#em ordem decrescente

n_valores = int(input('Digite um valor positivo e ímpar: '))
while n_valores < 0 or n_valores % 2 == 0:
    print('Valor incorreto!')
    n_valores = int(input('Digite um valor positivo e ímpar: '))
print(f'Valores ímpares de {n_valores} até 1: ')
for i in range(n_valores, 0, -1):
    if i % 2 != 0:
        print(i)

#17 Faça um programa que leia um número inteiro positivo n e calcule a soma dos primeiros n primeiros números naturais.

n_valores = int(input('Digite um valor positivo: '))
while n_valores < 0:
    print('Valor incorreto!')
    n_valores = int(input('Digite um valor positivo: '))
j = 0
for i in range(n_valores+1):
    j = j + i
print(f'A soma dos primeiros {n_valores} valores positivos: {j}')

#18 Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número
#foi lido. A quantidade de números a serem lidos deve ser fornecido pelo usuário.

n_valores = int(input('Digite a quantidade de valores a serem lidos: '))
lista = []
for i in range(n_valores):
    valor = int(input(f'Digite o valor {i+1}/{n_valores}: '))
    lista.append(valor)
maior = lista[0]
contador = 0
for i in range (len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    elif lista[i] == maior:
        contador = contador + 1
print(f'Maior valor dentre {n_valores} valores: {maior}')
print(f'Quantas vezes o maior valor foi lido: {contador}')

#19 Escreva um algortimo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que
#compôem o número

valor = int(input('Digite um valor entre 100 e 999: '))
while valor < 100 or valor > 999:
    print('Valor incorreto!')
    valor = int(input('Digite um valor entre 100 e 999: '))
valor = str(valor)
for letra in valor:
    print(letra)

#20 Ler uma sequência de números inteiros e determinar se eles são pares ou não.
#Deverá ser informado o número de dados lidos e o número de valores pares.
#O processo termina quando for digitado o número 1000.

contador = 0
contador_par = 0
n_valores = int(input('Digite o número de valores a serem lidos: '))
print('OBS: para encerrar o processo a qualquer momento, digite o número 1000.')
for i in range(n_valores):
    valor = int(input(f'Digite um valor {i+1}/{n_valores}: '))
    contador = contador + 1
    if valor % 2 == 0:
        contador_par = contador_par + 1
    if valor == 1000:
        print('Valor digitado = 1000')
        break
print(f'Quantidade de valores lidos: {contador}')
print(f'Quantidade de valores pares lidos: {contador_par}')

#21 Faça um programa que receba dois números. Calcule e mostre:
#a soma dos números pares desse intervalo de números, incluindo os números digitados;
#a multiplicação dos números ímpares desse intervalo, incluindo os digitados.

contador_par = 0
contador_impar = 0
soma_par = 0
mult_impar = 1
lista_par = []
lista_impar = []
inicio = int(input('Digite o valor do início do intervalo: '))
final = int(input('Digite o valor do final do intervalo: '))
for i in range(inicio+1,final):
    if i % 2 == 0:
        lista_par.append(i)
        soma_par = soma_par + i
        contador_par = contador_par + 1
    else:
        lista_impar.append(i)
        mult_impar = mult_impar * i
        contador_impar = contador_impar + 1
print(f'Quantidade de valores par dentro do intervalo: {contador_par}')
print(f'A soma dos valores pares dentro do intervalo: {soma_par}')
print(f'Valores par dentro do intervalo: {lista_par}')
print()
print(f'Quantidade de valores ímpar dentro do intervalo: {contador_impar}')
print(f'A multiplicação dos valores ímpares dentro do intervalo: {mult_impar}')
print(f'Valores ímpar dentro do intervalo: {lista_impar}')

#22 Escreva um programa completo que permita qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas
#(válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética.
#O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa,
#o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação

soma = 0
contador = 0
chave = True
print('OBS: o programa a seguir irá encerrar após um valor inserido não constar dentro do intervalo')
print('Digite uma sequência de notas no intervalo de 10 a 20: ')
while chave:
    valor = int(input())
    if valor < 10 or valor > 20:
        break
    else:
        soma = soma + valor
        contador = contador + 1
media = soma/contador
print(f'Média aritmética de todas as notas inseridas: {media:.2f}')

#23 Faça um algoritmo que leia um número positivo e imprima seus divisores:

valor = int(input('Digite um valor positivo: '))
while valor < 0:
    print('Valor incorreto!')
    valor = int(input('Digite um valor positivo: '))
    print('Seus divisores:')
for i in range(valor,0,-1):
    if valor % i == 0:
        print(i)

#24 Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
#com exceção dele próprio.

soma = 0
valor = int(input('Digite um valor: '))
for i in range(valor-1,0,-1):
    if valor % i == 0:
        print(i)
        soma = soma + i
print(f'A soma de todos seus divisores, excluindo ele próprio: {soma}')

#25 Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.

soma = 0
print('Números naturais que são múltiplos de 3 ou 5 até 1000:')
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        soma = soma + i
print(f'A soma desses números: {soma}')

#26 Faça um algortimo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.

valor = int(input('Digite um valor: '))
for i in range(1,valor+1):
    if i % 11 == 0:
        print(f'Primeiro múltiplo de {valor} é do número 11.')
        break
    elif i % 13 == 0:
        print(f'Primeiro múltiplo de {valor} é do número 13.')
        break
    elif i % 17 == 0:
        print(f'Primeiro múltiplo de {valor} é do número 17.')
        break

#27 Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).

h = 0
valor = int(input('Digite um valor positivo: '))
while valor < 0:
    print('Valor incorreto!')
    valor = int(input('Digite um valor positivo: '))
for i in range(1,valor+1):
    h = h + 1/i
print(f'H(n) = {h:.2f}')

#28 Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E,
#conforme a fórmula dada no problema.

e = 1
aux = 1
valor = int(input('Digite um valor positivo: '))
while valor < 0:
    print('Valor incorreto!')
    valor = int(input('Digite um valor positivo: '))
for i in range(0,valor):
    fatorial = 1
    for j in range(1,aux+1):
        #print(f'aux entrada = {j}/{aux}')
        fatorial = fatorial * j
        #print(f'Saida {j}/{aux}: {fatorial}')
    print(f'Valor do fatorial: {fatorial}')
    e = e + Decimal(1/fatorial)
    print(f'E {i}/{valor}: {e}')
    aux = aux + 1
print(f'E = {e:.2f}')

#29 Escreva um programa para calcular o valor da série dada pelo problema, para 5 termos:

s = 0
aux = 2
for i in range(0,5):
    fatorial = 1
    for j in range(1,aux+1):
        fatorial = fatorial * j
    s = s + Decimal(1/fatorial)
    aux = aux + 2
print(f'S = {s:.2f}')

#30 Faça um programa para calcular as sequências dadas pelo problema.

soma1 = 0
soma2 = 0
soma3 = 0
n = int(input('Digite o valor de n: '))
for i in range(1,n+1):
    soma1 = soma1 + i
print(f'Valor da primeira soma: {soma1}')
j = 1
for i in range(0, 2*n-1):
    soma2 = soma2 + j - (j+1)
    j = j + 1
print(f'Valor da segunda soma: {soma2}')
j = 1
for i in range(0, 2*n-1):
    soma3 = soma3 + j + (j+2)
    print(f'Valor de soma3: {soma3}')
    j = j + 4
print(f'Valor da terceira soma: {soma3}')

#31 Faça um programa que calcule o  valor de S dado no problema:

s = 0
j = 1
for i in range(1,100, +2):
    s = s + Decimal(i/j)
    #print(f'S = {s:.2f}')
    j = j + 1
print(f'S = {s:.2f}')

#32 Faça um programa que simule o lançamento de dois dados, d1 e d2, n vezes e tem como saída
#o número de cada dado e a relação entre eles (>,<,=) de cada lançamento.

vezes = int(input('Digite o número de vezes que deseja lançar os dois dados: '))
while vezes < 0:
    print('Valor incorreto!')
    vezes = int(input('Digite o número de vezes que deseja lançar os dois dados: '))
for i in range(0,vezes):
    d1 = randint(1,6)
    d2 = randint(1,6)
    print(f'Valor do dado 1: {d1}, valor do dado 2: {d2}')
    if d1 > d2:
        print('Relação: d1 > d2')
    elif d1 < d2:
        print('Relação: d1 < d2')
    elif d1 == d2:
        print('Relação: d1 = d2')

#33 Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros
#naturais que são múltiplos de i ou j ou ambos.

contador = 0
aux = 0
i = int(input('Digite o valor de i: '))
j = int(input('Digite o valor de j: '))
while i <= 0 or j <= 0:
    print('Valores incorretos!')
    i = int(input('Digite o valor de i: '))
    j = int(input('Digite o valor de j: '))
multiplos = int(input('Digite o número de múltiplos você deseja de retorno: '))
while contador < multiplos:
    if aux % i == 0 or aux % j == 0:
        print(aux)
        contador = contador + 1
    aux = aux + 1

#34 Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20.
#Exemplo: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto

lista = []
contador = 0
mmc = 1

for i in range(1,21):
    lista.append(i)
print(lista)
while True:
    for i in range(0,20):
        if lista[i] % 2 == 0:
            lista[i] = lista[i]/2
            contador = contador + 1
    if contador >= 1:
        mmc = mmc * 2
    elif contador < 1:
        break
    contador = 0
while True:
    for i in range(0,20):
        if lista[i] % 3 == 0:
            lista[i] = lista[i] / 3
            contador = contador + 1
    if contador >= 1:
            mmc = mmc * 3
    elif contador < 1:
            break
    contador = 0
while True:
    for i in range(0,20):
        if lista[i] % 5 == 0:
            lista[i] = lista[i] / 5
            contador = contador + 1
    if contador >= 1:
            mmc = mmc * 5
    elif contador < 1:
            break
    contador = 0
while True:
    for i in range(0,20):
        if lista[i] % 7 == 0:
            lista[i] = lista[i] / 7
            contador = contador + 1
    if contador >= 1:
        mmc = mmc * 7
    elif contador < 1:
        break
    contador = 0
while True:
    for i in range(0,20):
        if lista[i] % 11 == 0:
            lista[i] = lista[i] / 11
            contador = contador + 1
    if contador >= 1:
        mmc = mmc * 11
    elif contador < 1:
        break
    contador = 0
while True:
    for i in range(0,20):
        if lista[i] % 13 == 0:
            lista[i] = lista[i] / 13
            contador = contador + 1
    if contador >= 1:
        mmc = mmc * 13
    elif contador < 1:
        break
    contador = 0
while True:
    for i in range(0,20):
        if lista[i] % 17 == 0:
            lista[i] = lista[i] / 17
            contador = contador + 1
    if contador >= 1:
        mmc = mmc * 17
    elif contador < 1:
        break
    contador = 0
while True:
    for i in range(0,20):
        if lista[i] % 19 == 0:
            lista[i] = lista[i] / 19
            contador = contador + 1
    if contador >= 1:
        mmc = mmc * 19
    elif contador < 1:
        break
    contador = 0

print(f'Lista modificada: {lista}')
print(mmc)

#35 Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário define o
#valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números ímpares contidos
#neste intervalo. Caso o usuário digite um intervalo inválido(começando por um valor maior que o valor final) deve ser
#escrito uma mensagem de erro na tela, 'Intervalo de valores inválido' e o programa termina.

inicial = int(input('Digite o valor inical do intervalo: '))
final = int(input('Digite o valor final do intervalo: '))
soma = 0
while True:
    if inicial > final or inicial == final:
        print('Intervalo de valores inválido!')
        break
    else:
        diferenca = final - inicial
        for i in range(1,diferenca):
           proximo = inicial + i
           print(proximo, end=' ')
           if proximo % 2 != 0:
               soma = soma + proximo
        break
print()
print(f'A soma dos valores ímpares neste intervalo: {soma}')

#36 Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o
#quadrado da soma.

soma_quadrados = 0
quadrado_soma = 0

for i in range(1,101):
    soma_quadrados = soma_quadrados + pow(i,2)
for i in range (1,101):
    quadrado_soma = quadrado_soma + i
quadrado_soma = pow(quadrado_soma,2)
diferenca = quadrado_soma - soma_quadrados
print('A diferença entre o quadrado da soma e a soma dos quadrados dos 100 primeiros números naturais:')
print(diferenca)

#37 Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem propriedade seguinte:
#a soma de mais baixa ordem com os dois digitos de mais alta ordem elevada ao quadrado é igual ao próprio número.


print('"A soma dos dois dígitos de mais baixa e alta ordem elevada ao quadrado resulta no próprio número"')
print('Os números que atendem esta propriedade entre 1000 e 9999 são:')
for i in range(1000,10_000):
    soma = 0
    quadrado_soma = 0
    aux = str(i)
    digito_baixo = ''
    digito_alto = ''
    for i in range(0, 4):
        if i >= 0 and i < 2:
            digito_baixo = digito_baixo + aux[i]
        else:
            digito_alto = digito_alto + aux[i]
    soma = int(digito_baixo) + int(digito_alto)
    quadrado_soma = int(pow(soma,2))
    if str(quadrado_soma) == aux:
        print(f'Achado!: {quadrado_soma}')

#38 Faça um programa que calcule o terno pitagórico a, b, c para o qual a + b + c = 1000.
#Um terno pitagórico é um conjunto de três números naturais a, b, c para a propriedade dada pelo problema


a + b + c = 1000
a² + b² = c²
c = 1000 - a - b


for i in range(1,1001):
    for j in range(i+1,1001):
        c = 1000 - i - j
        if i*i + j*j == c*c:
            print(i,j,c)

#39 Faça um programa que calcule a área de um triângulo, cuja a base e a altura são fornecidas pelo usuário.
#Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.

print('Programa para calcular a área de um triãngulo.')
base = Decimal(input('Digite o valor da medida da base do triângulo: '))
altura = Decimal(input('Digite o valor da medida da altura do triângulo: '))
while True:
    if base <= 0 or altura <= 0:
        print('Valor(es) incorreto(s).')
        sleep(1)
        print('Programa para calcular a área de um triãngulo.')
        base = Decimal(input('Digite o valor da medida da base do triângulo: '))
        altura = Decimal(input('Digite o valor da medida da altura do triângulo: '))
    else:
        break
area = (base * altura) / 2
print(f'Valor da área deste triângulo: {area:.2f} m²')

#40 Elabore um progra que faça a leitura de vários numéros inteiros, ate que se digite um número negativo.
#O programa tem que retornar o maior e o menor número lido

lista = []
while True:
    valor = randint(-1,100)
    if valor < 0:
        break
    else:
        lista.append(valor)
for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > chave:
        lista[j + 1] = lista[j]
        j = j - 1
    lista[j + 1] = chave
print('Valores:')
print(lista)
print(f'Maior valor dentre todos os valores: {lista[len(lista)-1]}')
print(f'O menor valor dentre todos os valores: {lista[0]}')

#41 Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado
#O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para resistência igual a zero.

print('Programa para calcular a associação em paralelo de dois resistores')
while True:
    r1 = randint(0,100)
    r2 = randint(0,100)
    if r1 == 0 or r2 == 0:
        break
    else:
        print(f'Resistor 1: {r1}')
        print(f'Resistor 2: {r2}')
        a = Decimal(r1 * r2) / (r1 + r2)
        print(f'Valor da associação em paralelo dos dois resistores: {a:.2f}')
        break

#42 Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores
#lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

print('Programa que calcula o quadrado, cubo e raiz quadrada de um valor inserido.')
print('OBS: o programa encerra caso seja passado um valor negativo ou zero.')
while True:
    valor = Decimal(input('Digite um valor: '))
    if valor <= 0:
        break
    else:
        print(f'O valor ao quadrado: {pow(valor,2):.2f}')
        print(f'O valor ao cubo: {pow(valor,2):.2f}')
        print(f'A raiz do valor: {sqrt(valor):.2f}')

#43 Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade 0)
#e calcule a idade média desse grupo.

contador = 0
soma = 0
print('Programa para calcular a média de um grupo de pessoas.')
print('OBS: o programa encerra após ser inserido uma idade de valor 0.')
while True:
    idade = int(input('Digite o valor da idade: '))
    if idade == 0:
        break
    else:
        soma = soma + idade
        contador = contador + 1
media = Decimal(soma/contador)
print(f'A média da idade desse grupo de pessoas: {media:.2f} anos')

#44 Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior
# ao número lido.

proximo = 0
anterior = 0
numero = int(input('Digite um número inteiro: '))
while numero < 0:
    print('Valor inválido!')
    numero = int(input('Digite um número inteiro: '))
while True:
    print(proximo)
    if proximo > numero:
        break
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo = proximo + 1

#45 Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice-versa.
#Você deve criar um menu com duas opções de conversão e com uma opção para finalizar o programa.
#O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado quando a opção finalizar
#for escolhida.

print('Programa de conversão da velocidade de km/h para m/s e vice-versa')
while True:
    print('Digite uma das opções abaixo:')
    print('1. Km/h para m/s.')
    print('2. M/s para km/h.')
    print('3. Sair.')
    opcao = int(input('Opcão: '))
    if opcao == 1:
        valor = Decimal(input('Digite a velocidade em km/h: '))
        conversao = valor / Decimal(3.6)
        print(f'Valor da conversão: {conversao:.2f} m/s')
        sleep(1)
    elif opcao == 2:
        valor = Decimal(input('Digite a velocidade em m/s: '))
        conversao = valor * Decimal(3.6)
        print(f'Valor da conversão: {conversao:.2f} km/h')
        sleep(1)
    elif opcao == 3:
        print('Processo encerrado...')
        break
#46 Faça um programa que gera um número aleatório de 1 a 1000.
#O usuário deve tentar acertar qual o número foi gerado, a cada tentativa o programa deverá informar se o chute é menor
#ou maior gerado.
#O programa acaba quando o usuário acerta o número gerado.
#O programa deve informar em quantas tentativas o número foi descoberto.

tentativas = 0
chave = randint(1,1000)
while True:
   chute = int(input('Digite um valor: '))
   if chute > chave:
       print('Estimativa alta!')
       tentativas = tentativas + 1
   elif chute < chave:
       print('Estimativa baixa')
       tentativas = tentativas + 1
   elif chute == chave:
       print('Você encontrou o valor!')
       print(f'Valor encontrado: {chave}')
       print(f'Número de tentativas: {tentativas}')
       break

#47 Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
#Adição (opção 1)
#Subtração (opção 2)
#Multiplicação (opção 3)
#Divisão (opção 4)
#Saida (opção 5)
#O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de
#opções.
#O programa só termina quando for escolhida a opção de saída.

while True:
    print('Digite uma das operações abaixo:')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')
    opcao = int(input('Operação: '))

    if opcao == 1:
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        soma = n1 + n2
        print(f'Resultado da soma: {soma:.2f}')
        sleep(2)
    elif opcao == 2:
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        sub = n1 - n2
        print(f'Resultado da subtração: {sub:.2f}')
        sleep(2)
    elif opcao == 3:
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        mult = n1 * n2
        print(f'Resultado da multiplicação: {mult:.2f}')
        sleep(2)
    elif opcao == 4:
        n1 = Decimal(input('Digite o primeiro número: '))
        n2 = Decimal(input('Digite o segundo número: '))
        while n2 == 0:
            print('O segundo número deve ser diferente de zero!')
            n2 = Decimal(input('Digite o segundo número: '))
        div = n1 / n2
        print(f'Resultado da divisão: {div:.2f}')
        sleep(2)
    elif opcao == 5:
        break

#48 Faça um programa que some os termos de valor par da sequência de Fibonacci,
#cujos valores não ultrapassem quatro milhões.

proximo = 0
anterior = 0
soma = 0
while proximo <= 4_000_000:
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo % 2 == 0:
        if proximo <= 4_000_000:
            soma = soma + proximo
    if proximo == 0:
        proximo = proximo + 1
print(f'Valor da soma dos valores pares menores que 4 milhões: {soma}')

#49 o funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário.
#Carlos gosta de fazer aplicações na cardeneta de poupança e vai aplicar seu salário integralmente nela, pois está
#rendendo 2% ao mês.
#João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês.
#Construa um programa que deverá calcular e mostrar a quantidade de meses necessárias para que o valor pertencente
#a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas.

salario1 = Decimal(5000)
salario2 = Decimal(salario1/3)
meses = 0
rendimento1 = salario1 * Decimal(0.02)
rendimento2 = salario2 * Decimal(0.05)

while rendimento1 > rendimento2:
    rendimento1 = rendimento1 + (rendimento1 * Decimal(0.02))
    print(f'Rendimento de Carlos: {rendimento1:.2f}')
    rendimento2 = rendimento2 + (rendimento2 * Decimal(0.05))
    print(f'Rendimento de João: {rendimento2:.2f}')
    meses = meses + 1
    sleep(2)
print(f'Quantidade de meses para ultrapassar o rendimento de Carlos: {meses} meses')
print(f'Valor do rendimento de Carlos: R$ {rendimento1:.2f}')
print(f'Valor do rendimento de João: R$ {rendimento2:.2f}')

#50 Chico tem 1.50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano.
#Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior do que Chico.

taxa_chico = Decimal('0.02')
taxa_ze = Decimal('0.03')
altura_chico = Decimal('1.50')
altura_ze = Decimal('1.10')
anos = 0
while altura_chico >= altura_ze:
    altura_chico = altura_chico + taxa_chico
    print(f'Altura de Chico: {altura_chico}')
    altura_ze = altura_ze + taxa_ze
    print(f'Altura de Zé: {altura_ze}')
    anos = anos + 1
print(f'Quantidade de anos para Zé ultrapassar a altura de Chico: {anos} anos')
print(f'Altura de Chico: {altura_chico}')
print(f'Altura de Zé: {altura_ze}')

#51 Um funcionário recebe um aumento anual.
#Em 1995 foi contratado por 2000 reais.
#Em 1996 recebeu um aumento de 1.5%.
#A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior.
#Faça um programa que determine o salário atual do funcionário.

salario = Decimal('2030')
taxa = Decimal('0.015')
aumento = 0

for i in range (1997,2008):
    taxa = taxa * 2
    aumento =  salario + (salario * taxa)
    salario = aumento
    print(f'Salario em {i}: {salario:.2f}')
    print(f'Aumento de salário: {taxa:.2f}%')
    sleep(1)
print(f'Salário do funcionário em 2021: R$ {salario:.2f}')

#52 Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas
#notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível.
#Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1.

valor = Decimal(input('Digite o valor a ser sacado: '))
nota = 0
if valor / 100 > 0:
    nota = int(valor/100)
    valor = valor - nota*100
    print(f'Quantidade de notas de R$ 100: {nota}')
if valor / 50 > 0:
    nota = int(valor/50)
    valor = valor - nota*50
    print(f'Quantidade de notas de R$ 50: {nota}')
if valor / 20 > 0:
    nota = int(valor / 20)
    valor = valor - nota * 20
    print(f'Quantidade de notas de R$ 20: {nota}')
if valor / 10 > 0:
    nota = int(valor / 10)
    valor = valor - nota * 10
    print(f'Quantidade de notas de R$ 10: {nota}')
if valor / 5 > 0:
    nota = int(valor / 5)
    valor = valor - nota * 5
    print(f'Quantidade de notas de R$ 5: {nota}')
if valor / 2 > 0:
    nota = int(valor / 2)
    valor = valor - nota * 2
    print(f'Quantidade de notas de R$ 2: {nota}')
if valor / 1 > 0:
    nota = int(valor / 1)
    valor = valor - nota * 1
    print(f'Quantidade de notas de R$ 1: {nota}')

#53 Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado triângulo de
#Floyd.

valor = int(input('Digite o valor do triângulo de Floyd: '))
numero = 1
for i in range(0, valor):
    for j in range(0, i+1):
        print(f'{numero} ', end=' ')
        numero = numero + 1

    print()

#54 Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não.

numero = int(input('Digite um número maior do que 1: '))
primo = True
while numero <= 1:
    print('Número inválido!')
    numero = int(input('Digite um número maior do que 1: '))
for i in range (2,numero):
    if numero % i == 0:
            primo = False
if primo:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')

#55 Escreva um programa que leia um inteiro não negativo 'n' e imprima a soma dos 'n' primeiros números primos.

somaPrimos = 0
n = int(input('Digite um número inteiro não negativo: '))
while n < 0:
    print('Número inválido.')
    n = int(input('Digite um número inteiro não negativo: '))
if n <= 1 and n > 0:
    print(f'O valor da soma dos primeiros números primos até o valor {n}: {somaPrimos}')
else:
    primo = True
    for i in range(2, n):
        for j in range(2,i):
            if i % j == 0:
                primo = False
        if primo:
            somaPrimos = somaPrimos + i
    print(f'O valor da soma dos primeiros números primos até o valor {n}: {somaPrimos}')

#56 Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões.

somaPrimos = 0
for i in range(2,2_000_000):
    primo = True
    for j in range(2,i):
        if i % j == 0:
            primo = False
    if primo:
        somaPrimos = somaPrimos + i
        print(somaPrimos)
print(f'O valor da soma de todos os  números primos abaixo de 2 milhões: {somaPrimos}')

#57 Faça um programa que conte os números primos que existem entre a e b,
#onde a e b são números fornecidos pelo usuário.

a = int(input('Digite o limite inferior: '))
b = int(input('Digite o limite superior: '))

for i in range(a+1,b):
    primo = True
    for j in range(2,i):
        if i % j == 0:
            primo = False
    if primo:
        print(i,end=' ')

#58 Faça um programa que some os números primos existentes entre a e b,
#onde a e b são números informados pelo usuário.

a = int(input('Digite o limite inferior: '))
b = int(input('Digite o limite superior: '))
soma = 0
for i in range(a+1,b):
    primo = True
    for j in range(2,i):
        if i % j == 0:
            primo = False
    if primo:
        soma = soma + i
print(f'A soma dos números primos entre {a} e {b}: {soma} ')

# 59 Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor de kw/h,
# e para cada habitante entre com os seguintes dados:
# consumo do mês e o código do consumidor (1- residencial, 2- comercial, 3- industrial).
# No final, imprima o maior, o menor e a média do consumo dos habitantes;
# E por fim o total de consumo de cada categoria de consumidor

num_consumidor = int(input('Digite o número de habitantes: '))
soma_residencial = 0
soma_comercial = 0
soma_industrial = 0
maior = 0
menor = 0

for i in range(0,num_consumidor):
    print('Digite abaixo um dos códigos do consumidor:')
    print('1. Residencial')
    print('2. Comercial')
    print('3. Industrial')
    opcao = int(input('Opção: '))
    while opcao < 1:
        print('Opção inválida!')
        print('Digite abaixo um dos códigos do consumidor:')
        print('1. Residencial')
        print('2. Comercial')
        print('3. Industrial')
        opcao = int(input('Opção: '))
    if opcao == 1:
        consumo = Decimal(input('Digite o consumo do consumidor em kW/h: '))
        soma_residencial = soma_residencial + consumo
    elif opcao == 2:
        consumo = Decimal(input('Digite o consumo do consumidor em kW/h: '))
        soma_comercial = soma_comercial + consumo
    elif opcao == 3:
        consumo = Decimal(input('Digite o consumo do consumidor em kW/h: '))
        soma_industrial = soma_industrial + consumo
    if maior == 0:
        maior = consumo
    if menor == 0:
        menor = consumo
    if consumo >= maior:
        maior = consumo
    if consumo <= menor:
        menor = consumo
media = (soma_residencial + soma_comercial + soma_industrial) / num_consumidor

print()
print(f'O maior valor de consumo: {maior:.2f} kW/h')
print(f'O menor valor de consumo: {menor:.2f} kW/h')
print(f'A média de consumo da cidade: {media:.2f} kW/h')
print('Consumo por categoria de consumidor:')
print(f'1. Residencial: {soma_residencial:.2f} kW/h')
print(f'2. Comercial: {soma_comercial:.2f} kW/h')
print(f'3. Industrial: {soma_industrial:.2f} kW/h')

# 60 Faça um programa que leia vários números, calcule e mostre:
# a) A soma dos números digitados;
# b) A quantidade de números digitados;
# c) A média de números digitados;
# d) O maior número digitado;
# e) O menor número digitado;
# f) A média dos números pares;
# Finalize a entrada de dados caso o usuário informe o valor 0.

contador = 0
contador_par = 0
soma = 0
soma_par = 0
maior = 0
menor = 0

print("OBS: Para encerrar o programa, insira o valor '0'")
sleep(1)

while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break
    contador = contador + 1
    soma = soma + numero
    if numero % 2 == 0:
        contador_par = contador_par + 1
        soma_par = soma_par + numero
    if maior == 0:
        maior = numero
    if menor == 0:
        menor = numero
    if numero >= maior:
        maior = numero
    if numero <= menor:
        menor = numero

media = Decimal(soma / contador)
media_par = Decimal(soma_par / contador_par)

print('Informações a respeito dos números digitados:')
print(f'A soma dos números digitados: {soma}')
print(f'A quantidade de números digitados: {contador}')
print(f'A média dos números digitados: {media:.2f}')
print(f'O maior número digitado: {maior}')
print(f'O menor número digitado: {menor}')
print(f'A média dos números pares digitados: {media_par:.2f}')

# 61 Faça um programa que calcule o maior número palídromo feito a partir do produto de dois números de 3 dígitos.
# Ex: O maior palíndromo feito a partir do produto de dois números de dois dígitos é 9009 = 91 * 99.

maior = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        produto = str(i * j)
        if produto == produto[::-1]:
            if maior == 0:
                maior = int(produto)
            if int(produto) >= maior:
                a = i
                b = j
                maior = int(produto)

print(f'O maior número palíndromo feito a partir do produto de {a} e {b}:')
print(maior)

# 62 Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro, cinco,
# então há 2 + 4 + 4 + 6 + 5 = 22 letras usadas no total.
# Faça um programa que conte quantas letras seriam utilizadas se todos os números de 1 a 1000 fossem escritos em palavras.
# OBS: Não conte espaços ou hifens

soma = 0

for i in range(1, 1001):
    numero = num2words(i,lang='pt')
    print(numero)
    soma = soma + (len(numero) - numero.count(' '))
print(f'A soma de todas as letras de 1 a 1000: {soma}')
"""
import decimal
from time import *
from decimal import *
from random import *
from math import *
from num2words import *

nome = 'Victor de Sousa Oliveira'
lista1 = []
lista2 = list(range(11))
lista3 = sorted(lista1)
lista4 = list(range(11,21))

lista5 = lista2 + lista4
# print(lista2)
# print(lista5)

lista2.append(21)
lista4.append(22)
# print(lista2)
# print(lista5)

receita = {'jan': 100, 'fev': 250, 'mar': 290, 'abr': 330}




