"""
01. Faça um programa que possua um vetor denominado A que armazene 6 números inteiros.
O programa deve executar os seguintes passos:

a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7
vetor_A = [1, 0, 5, -2, -5, 7]

b) Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] do vetor e
   mostre na tela esta soma.
vetor_A = [1, 0, 5, -2, -5, 7]
soma = vetor_A[0] + vetor_A[1] + vetor_A[5]
print(soma)

c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
vetor_A = [1, 0, 5, -2, -5, 7]
vetor_A[4] = 100
print(vetor_A)

d) Mostre na tela cada valor do vetor A, um em cada linha
vetor_A = [1, 0, 5, -2, -5, 7]
vetor_A[4] = 100
for valor in range(0,len(vetor_A)):
    print(vetor_A[valor])

02. Crie um programa que leia 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

lista = []
while len(lista) < 6:
    valor = int(input('Digite um valor inteiro: '))
    lista.append(valor)
print(lista)

03. Ler um conjunto de números reais, armazenando-os em vetor e calcular o quadrado dos componentes deste vetor,
    armazendo o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

lista1 = []
lista2 = []
while len(lista1) < 10:
    valor = round(random.uniform(0.0,100.0),2)
    lista1.append(valor)
for i in range(0,len(lista1)):
    lista2.append(round(pow(lista1[i],2),2))
print(lista1)
print(lista2)

04. Faça um programa que leia um vetor de 8 posições e, em suguida, leia também dois valores X e Y quaisquer
    correspondentes a duas posições no vetor. Ao final do programa deverá escrever a soma dos valores encontrados
    nas respectivas posições X e Y.

    lista = []
while len(lista) < 8:
    lista.append(randint(0,100))
indice1 = randint(0,7)
indice2 = randint(0,7)

print(lista)
print(f'Índices escolhidos: {indice1} e {indice2}')
print(f'Soma dos índices aleatórios: {lista[indice1] + lista[indice2]}')

05. Leia um vetor com 10 posições. Contar e escrever quantos valores pares ele possui.

lista = []
lista_par = []
contador = 0
while len(lista) < 10:
    lista.append(randint(0,100))
for i in range(0,len(lista)):
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
        contador += 1
print(lista)
print(f'Número de valores pares na lista: {contador}')
print(lista_par)

06. Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o
    menor elemento do vetor.

lista = []

while len(lista) < 10:
    lista.append(randint(0,100))
print(lista)
print(f'O maior valor do vetor: {max(lista)}')
print(f'O menor valor do vetor: {min(lista)}')

07. Escreva um programa que leia 10 números inteiros e armazene em um vetor. Imprima o vetor, o maior elemento e a
    posição que ele se encontra

lista = []
while len(lista) < 10:
    lista.append(randint(0,100))

maior = max(lista)
print(lista)
print(f'O maior elemento do vetor: {maior}')
print(f'O índice do maior elemento do vetor: {lista.index(maior)}')

08. Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem reversa.

lista = []
while len(lista) < 6:
    lista.append(randint(0,100))

print(lista)
print(f'Lista invertida: {lista[::-1]}')

09. Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos em ordem inversa.

lista = []
while len(lista) < 6:
    valor = randint(0,100)
    if valor % 2 == 0:
        lista.append(valor)

print(lista)
print(f'Vetor de elemntos pares invertido: {lista[::-1]}')

10. Faça um programa para ler a nota da prova de 15 alunos e armazene em um vetor, calcule e imprima a média geral.

notas = []
while len(notas) < 15:
    notas.append(round(uniform(0.0, 10.1),1))

print(notas)
print(f'A média da turma: {round(sum(notas)/len(notas),1)}')

11. Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a
    soma dos números positivos desse vetor.

lista = []
lista_negativa = []
soma = 0
while len(lista) < 10:
    lista.append(round(uniform(-100.0,100.0),2))

for i in range(0, len(lista)):
    if lista[i] < 0:
        lista_negativa.append(lista[i])
    else:
        soma = soma + lista[i]
print(lista)
print(f'Números negativos no vetor: {lista_negativa}')
print(f'Quantidade de números negativos: {len(lista_negativa)}')
print(f'A soma dos números positivos: {soma}')

12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor
    e a média dos valores.

lista = []
while len(lista) < 5:
    lista.append(randint(0,101))

print(lista)
print(f'Maior valor entre todos: {max(lista)}')
print(f'Menor valor entre todos: {min(lista)}')
print(f'Média dos valores: {round(sum(lista)/len(lista),2)}')

13. Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.

lista = []
while len(lista) < 5:
    lista.append(randint(0,101))

print(lista)
print(f'Posição do maior valor entre todos: {lista.index(max(lista))}')
print(f'Posição do menor valor entre todos: {lista.index(min(lista))}')

14. Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.

lista = []
while len(lista) < 10:
    lista.append(randint(1,10))

iguais = Counter(lista)
lista2 = []
for key in iguais:
    if iguais[key] > 1:
        lista2.append(key)

print(lista)
if len(lista2) == 0:
    print('Não existem valores iguais no vetor')
else:
    print(f'Valores iguas no vetor: {lista2}')

15. Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.

lista = []
while len(lista) < 20:
    lista.append(randint(1,100))
conjunto = set(lista)
print(f'Meu vetor: {conjunto}')

16. Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro.
    Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na
    ordem inversa. Caso o código for diferente de 1 e 2 escreva uma mensagem informando que o código é inválido.

print('Programa gerador de vetor de números reais')
print('Digite uma das opções abaixo:')
print('1. Vetor na ordem direta')
print('2. Vetor na ordem inversa')
print('0. Sair')
opcao = int(input('Opcão: '))
lista = []

while len(lista) < 5:
    lista.append(randint(1,100))

while opcao < 0 or opcao > 2:
    print('Opção inválida')
    sleep(3)
    print('Digite uma das opções abaixo:')
    print('1. Vetor na ordem direta')
    print('2. Vetor na ordem inversa')
    print('0. Sair')
    opcao = int(input('Opcão: '))

while opcao != 0:
    if opcao == 1:
        print(f'Vetor na ordem direta: {lista}')
        sleep(3)
        print('Digite uma das opções abaixo:')
        print('1. Vetor na ordem direta')
        print('2. Vetor na ordem inversa')
        print('0. Sair')
        opcao = int(input('Opcão: '))
    elif opcao == 2:
        print(f'Vetor na ordem inversa: {lista[::-1]}')
        sleep(3)
        print('Digite uma das opções abaixo:')
        print('1. Vetor na ordem direta')
        print('2. Vetor na ordem inversa')
        print('0. Sair')
        opcao = int(input('Opcão: '))
print('Programa encerrado.')

17. Leia um vetor de 10 posições e atribua o valor 0 para todos os elementos que possuírem valores negativos

lista = []
while len(lista) < 10:
    valor = randint(-100,100)
    if valor < 0 :
        valor = 0
    lista.append(valor)
print(lista)


18. Faça um programa que leia um vetor de 10 números. Leia um número x, conte os múltiplos de um número inteiro x num
    vetor e mostre-os na tela

lista = []
while len(lista) < 10:
    lista.append(randint(0,100))
num = int(input('Digite um número: '))

multiplos = []
for i in range(0,len(lista)):
    if lista[i] % num == 0:
        multiplos.append(lista[i])
print(f'Múltiplos desse número no vetor: {multiplos}')

19. Faça um vetor de tamanho 50 preenchido com os seguintes valor: (i + 5 * i) % (i + 1), sendo i a posição do elemento
    no vetor. Em seguida imprima o vetor na tela.

lista = []
for i in range(0,50):
    valor = (i + 5 * i) % (i + 1)
    lista.append(valor)
print(lista)

20. Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um vetor de 10 posições.
    Preencha em um segundo vetor apenas com os números ímpares do primeiro vetor. Imprima os dois vetores, 2 elementos
    por linha.

lista = []
impares = []
indice = 0
while len(lista) < 10:
    lista.append(randint(0,50))
    if lista[indice] % 2 != 0:
        impares.append(lista[indice])
        indice = indice + 1
    else:
        indice = indice + 1

print(lista)
print(impares)

21. Faça um programa que receba do usuário dos valores A e B, com 10 números inteiros cada. Crie um novo vetor
    denominado C, calculando C = A - B. Mostre na tela os dados do vetor C.

a = set()
b = set()
while len(a) < 10 and len(b) < 10:
    a.add(randint(1,100))
    b.add(randint(1,100))

c = a.difference(b)
print(f'Vetor A: {a}')
print(f'Vetor B: {b}')
print(f'Vetor C: {c}')

22. Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares os valores
    do primeiro e nas posições ímpares os valores do segundo.

lista1 = []
lista2 = []
while len(lista1) < 10 and len(lista2) < 10:
    lista1.append(randint(1,100))
    lista2.append(randint(1,100))

lista3 = []
contador = 0
for i in range(0,10):
    if i % 2 == 0:
        lista3.insert(i,lista1[contador])
    else:
        lista3.insert(i,lista2[contador])
        contador = contador + 1

print(f'Vetor 1 : {lista1}')
print(f'Vetor 2: {lista2}')
print(f'Vetor 3: {lista3}')

23. Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
    Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é
    dado por: x1 * y1 + x2 * y2 + ... + xn * yn.

lista1 = []
lista2 = []

while len(lista1) < 5 and len(lista2) < 5:
    lista1.append(round(uniform(0, 100), 2))
    lista2.append(round(uniform(0,100), 2))

soma = 0
for i in range(0,5):
    soma = soma + lista1[i] * lista2[i]
print(lista1)
print(lista2)
print(soma)

24. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
    representando a sua altura em metros. Encontre o aluno mais baixo e o mais alto.
    Mostre o número do aluno mais baixo e o do mais alto, juntamente com suas alturas.

alunos = {}.fromkeys(list(range(1,11)))
for key in alunos.keys():
    alunos[key] = round(uniform(1.50, 1.80), 2)

for key, value in alunos.items():
    if value == max(alunos.values()):
        idMaisAlto = key
        alturaMaisAlto = value
    elif value == min(alunos.values()):
        idMaisBaixo = key
        alturaMaisBaixo = value

print(f'Alunos e suas alturas: {alunos}')
print(f'Aluno mais alto da sala: id={idMaisAlto} altura={alturaMaisAlto}m')
print(f'Aluno mais baixo da sala: id={idMaisBaixo} altura={alturaMaisBaixo}m')

25. Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros números naturais que não são múltiplos
    de 7 ou que terminam com 7

numerosNaturais = set()
for num in range(1,101):
    valor = num
    valorStr = str(valor)
    if valor % 7 != 0 or len(valorStr) > 1 and valorStr[1] == '7':
        numerosNaturais.add(valor)

print(numerosNaturais)

26. Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números, onde m é a média do vetor.

v = []
while len(v) < 10:
    v.append(randint(1,100))

media = round(sum(v) / len(v), 2)
soma = 0
for valor in v:
    soma = round(soma + pow(valor - media, 2), 2)

desvio = round(sqrt(soma / len(v) - 1), 2)
print(v)
print(media)
print(soma)
print(desvio)

27. Leia 10 números inteiros e armazene-os em um vetor. Em seguida, escreva os elementos que são primos e suas
    respectivas posições no vetor.

lista = []
while len(lista) < 10:
    lista.append(randint(1,100))

print(f'Vetor: {lista}')
print('Números primos no vetor:')
for valor in lista:
    primo = True
    if valor != 1:
        for i in range(2, valor):
            if valor % i == 0:
                primo = False
        if primo:
          print(f'{valor} no índice {lista.index(valor)}')

28. Leia 10 números inteiros e armazene-os em um vetor v. Crie dois novo vetores v1 e v2.
    Copie os valores ímpares de v para v1 e os valores pares de v para v2.
    Note que cada um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os elementos são utilizados.
    No final, escreva os elementos UTILIZADOS de v1 e v2.

v = []
while len(v) < 10:
    v.append(randint(1,100))

v1 = []
v2 = []
for valor in v:
    if valor % 2 != 0:
        v1.append(valor)
    else:
        v2.append(valor)

print(v)
print(v1)
print(v2)

29. Faça um programa que receba 6 números inteiros e mostre:
    * Os números pares digitados;
    * A soma dos números pares digitados;
    * Os números ímpares digitados;
    * A quantidade de números digitados;

lista = []
while len(lista) < 6:
    lista.append(randint(1,100))

listaPares = []
listaImpar = []
for valor in lista:
    if valor % 2 == 0:
        listaPares.append(valor)
    else:
        listaImpar.append(valor)

print(f'Vetor: {lista}')
print(f'Números pares presentes no vetor: {listaPares}')
print(f'A soma dos números pares: {sum(listaPares)}')
print(f'Números impares presentes no vetor: {listaImpar}')

30. Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os 2 vetores
    anteriores, ou seja, que contém apenas os números que estão em ambos os vetores.
    O vetor não deve conter números repetidos.

conjuntoA = set()
conjuntoB = set()

while len(conjuntoA) < 10 and len(conjuntoB) < 10:
    conjuntoA.add(randint(1,20))
    conjuntoB.add(randint(1,20))

conjuntoIntersec = conjuntoA.copy()
conjuntoIntersec = conjuntoIntersec.intersection(conjuntoB)

print(f'Vetor A: {conjuntoA}')
print(f'vetor B: {conjuntoB}')
print(f'Elementos que estão em ambos os vetores A e B: {conjuntoIntersec}')


31. Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união entre
    os dois vetores anteriores, ou seja, que contém os números dos dois vetores.
    O vetor não deve conter números repetidos.

conjuntoA = set()
conjuntoB = set()

while len(conjuntoA) < 10 and len(conjuntoB) < 10:
    conjuntoA.add(randint(1,20))
    conjuntoB.add(randint(1,20))

conjuntoUniao = conjuntoA.copy()
conjuntoUniao = conjuntoUniao.union(conjuntoB)

print(f'Vetor A: {conjuntoA}')
print(f'vetor B: {conjuntoB}')
print(f'União entre os vetores A e B: {conjuntoUniao}')

32. Leia dois vetores de inteiros x e y, cada com 5 elementos (assuma que o usuário não informa elementos repetidos).
    Calcule e mostre os vetores resultantes em cada caso abaixo:
    * Soma entre x e y: soma de cada elemento x com o elemento da mesma posição y.
    * Produto entre x e y: multiplicação de cada elemento de x om o elemento da mesma posição y.
    * Diferença entre x e y: todos os elementos de x que não existam em y.
    * Interseção entre x e y: Apenas os elementos que aparecem nos dois vetores.
    * União entre x e y: todos os elementos de x e todos os elementos de y que não estão em x.

conjuntoX = set()
conjuntoY = set()
while len(conjuntoX) < 5:
    conjuntoX.add(randint(1,10))
while len(conjuntoY) < 5:
    conjuntoY.add(randint(1, 10))

listaX = list(conjuntoX)
listaY = list(conjuntoY)
soma = []
multiplicacao = []
for i in range(0,5):
    soma.append(listaX[i] + listaY[i])
    multiplicacao.append((listaX[i] * listaY[i]))

print(f'Vetor x: {listaX}')
print(f'Vetor y: {listaY}')
print(f'A soma dos vetores: {soma}')
print(f'A multiplicação dos vetores: {multiplicacao}')
print(f'A diferença dos vetor x com y: {conjuntoX.difference(conjuntoY)}')
print(f'A interseção dos vetores: {conjuntoX.intersection(conjuntoY)}')
print(f'A união dos vetores: {conjuntoX.union(conjuntoY)}')

33. Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor zero.
    Para isso, todos os elementos á frente do valor zero, devem ser movidos um posição para trás do vetor.

lista = []
while len(lista) < 15:
    valor = randint(0,15)
    print(valor)
    lista.append(valor)
    print(lista)
    sleep(3)

for valor in lista:
    if valor == 0:
        lista.pop(lista.index(valor))

print(lista)

34. Faça um programa para ler 10 números diferentes a serem armazenados em um vetor.
    Os dados deverão ser armazenados no vetor na ordem que forem sendo lidos, sendo que caso o usuario digite um número
    que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número.
    Note que cada valor digitado pelo usuário deve ser pesquisado no vetor, verificando se ele existe entre os números
    que já foram fornecidos. Exibir na tela final o que foi digitado.

lista = []
while len(lista) < 10:
    valor = randint(1, 20)
    print(valor)
    sleep(3)
    while valor in lista:
        print('Valor repetido, digite outro valor: ')
        valor = randint(1, 20)
        print(valor)
        sleep(3)
    lista.append(valor)

print(f'Valores digitados: {lista}')

35. Faça um programa que leia dois números a e b (positivos menores que 100) e:
    * Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o algorismo menos significativo.
    * Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores construídos anteriormente.
    Dica: Some as posições correspondetes. Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 á próxima
    posição.
    OBS: não entendi a pergunta

36. Leia um vetor com 10 números reais, ordene os elementos deste vetor e no final escreva os elementos do vetor
    ordenado.

lista = []
while len(lista) < 10:
    lista.append(round(uniform(0,100), 2))

print(lista)
lista.sort()
print(lista)

37. Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > .. > A11, ou seja, está ordenado em
    ordem crescente até o sexto elemento e, a partir do sexto elemento, está ordenado em ordem decrescete.
    Dado o vetor da questão anterior, proponha um algoritmo para ordernar os elementos.

lista = []
while len(lista) < 11:
    lista.append(round(uniform(0,100), 2))
lista.sort()
print(lista)

lista1 = []
for i in range(5,11):
    lista1.append(lista.pop())
lista = lista + lista1
print(lista)

38. Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, guardando-os num
    vetor. Ordene o valor assim que ele for digitado. Mostre ao final na tela os valores em ordem.

lista = []
while len(lista) < 10:
    valor = randint(0, 100)
    lista.append(valor)
    print(f'Valor digitado: {valor}')
    sleep(3)
    lista.sort()
    print(f'Lista: {lista}')
print(f'Vetor ordenado: {lista}')

39. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado
    Triângulo de pascal:

triangulo = []
valor = randint(1,10)
print(f'Valor digitado: {valor}')
for i in range(0, valor):
    lista = []
    for j in range(0, i+1):
        calculo = int(factorial(i) / (factorial(j) * factorial(i-j)))
        lista.append(calculo)
        # print(lista)
        # sleep(3)
    triangulo.append(lista)
    # print(f'Elementos no triangulo: {triangulo}')
    # sleep(3)
for i in range(0,len(triangulo)):
    print(triangulo[i])
"""

"""
1. Leia uma matriz 4x4, conte e escreva quantos valores maiores que 10 ela possui

matriz = []
while len(matriz) < 4:
    lista = []
    for i in range(0,4):
        lista.append(randint(0, 20))
    matriz.append(lista)
print(matriz)
print(f'Tamanho da matriz: {len(matriz)}')

maiores_10 = []
for linha in matriz:
    for valor in linha:
        if valor > 10:
            maiores_10.append(valor)

print(f'Valores maiores que 10 na matriz: {maiores_10}')
print(f'Total de valores maiores que 10: {len(maiores_10)}')

2. Declare uma matriz 5x5. Preencha com 1 a diagonal principal e com 0 os demais elementos.
   Escreva ao final a matriz obtida.

matriz = []
num = 5
for i in range(0,num):
    valor = [0, 0, 0, 0, 0]
    valor[i] = valor[i] + 1
    matriz.append(valor)

print(matriz)

3. Faça um programa que preenche uma matriz 4x4 com o produto do valor da linha e da coluna de cada elemento.
   Em seguida, imprima na tela a matriz.

matriz = []
for i in range(1, 5):
    lista = []
    for j in range(1, 5):
        num = i*j
        lista.append(num)
    matriz.append(lista)

for valor in matriz:
    print(valor)

4. Leia uma matriz 4x4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.

matriz = []
while len(matriz) < 4:
    lista = []
    for i in range(0, 4):
        lista.append(randint(1, 100))
    matriz.append(lista)

maior_valor = matriz[0][0]
for i in range(0, 4):
    for j in range(0, 4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            indice1_maior = i
            indice2_maior = j

print(f'A matriz:')
for valor in matriz:
    print(valor)
print(f'O maior valor da matriz: {maior_valor}')
print(f'Coordenadas do maior valor: {indice1_maior}:{indice2_maior}')

5. Leia uma matriz 5x5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final,
    escrever a localização(linha e coluna) ou uma mensagem de não encontrado.

matriz = []
while len(matriz) < 5:
    lista = []
    for i in range(0, 5):
        lista.append(randint(0, 30))
    matriz.append(lista)

valorX = randint(0, 30)
achou = False
print(f'Valor digitado: {valorX}')
for i in range(0,5):
    for j in range(0,5):
        if matriz[i][j] == valorX:
            achou = True
            indice1_maior = i
            indice2_maior = j

for valor in matriz:
    print(valor)
sleep(3)
if achou:
    print(f'Valor na linha {indice1_maior}, coluna {indice2_maior}.')
else:
    print('Valor não encontrado.')

6. Leia duas matrizes 4x4 e escreva uma terceira com os maiores de cada posição das matrizes lidas.

matriz1 = []
matriz2 = []
while len(matriz1) < 4 and len(matriz2) < 4:
    lista1 = []
    lista2 = []
    for i in range(0,4):
        lista1.append(randint(0, 100))
        lista2.append(randint(0, 100))
    matriz1.append(lista1)
    matriz2.append(lista2)

matriz3 = []
# maior = matriz1[0][0]
for i in range(0, 4):
    lista3 = []
    for j in range(0, 4):
        if matriz1[i][j] > matriz2[i][j]:
            lista3.append(matriz1[i][j])
        else:
            lista3.append(matriz2[i][j])
    matriz3.append(lista3)

print('Matriz 1:')
for valor in matriz1:
    print(valor)
print()
print('Matriz 2:')
for valor in matriz2:
    print(valor)
print()
print('Matriz 3:')
for valor in matriz3:
    print(valor)

7. Gerar e imprimir uma matriz de tamanho 10x10, onde seus elementos são da forma:
    A[i][j] = 2i + 7j, se i < j
    A[i][j] = 3i² - 1, se i = j
    A[i][j] = 4i³ - 5j², se i > j

matriz = []
while len(matriz) < 10:
    for i in range(0, 10):
        lista = []
        for j in range(0, 10):
            if i < j:
                lista.append(2 * i + 7 * j)
            elif i == j:
                lista.append(int(3 * pow(i, 2)) - 1)
            elif i > j:
                lista.append(int(4 * pow(i, 3)) - int(5 * pow(j, 2)))
        matriz.append(lista)

print('Matriz:')
for valor in matriz:
    print(valor)

8. Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão acima da diagonal principal.

matriz = []
while len(matriz) < 3:
    for i in range(0, 3):
        lista = []
        for j in range(0, 4):
            lista.append(randint(0,1))
        matriz.append(lista)

soma = 0
j = 1
for linha in matriz:
    if j == len(linha) - 1:
        break
    else:
        for i in range(j, len(linha)):
            soma = soma + linha[i]
        j = j + 1

print('Matriz:')
for valor in matriz:
    print(valor)
print(f'Soma dos elementos acima da diagonal principal: {soma}')

9. Leia uma matriz 3x3 elementos. Calcule a soma dos elementos que estão abaixo da diagonal principal.

soma = 0
j = 0
k = 0
for linha in matriz:
    if j == len(linha) - 1:
        break
    else:
        for i in range(j, k):
            soma = soma + linha[i]
        k = k + 1

print('Matriz:')
for valor in matriz:
    print(valor)
print(f'Soma dos elementos abaixo da diagonal principal: {soma}')

10. Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão na diagonal principal.

matriz = []
soma = 0
while len(matriz) < 3:
    for linha in range(0, 3):
        lista = []
        for coluna in range(0, 3):
            valor = randint(0, 1)
            if linha == coluna:
                soma = soma + valor
            lista.append(valor)
        matriz.append(lista)

for linha, valor in enumerate(matriz):
    print(f'{linha} -> {valor}')
print()
print(f'Soma da diagonal principal: {soma}')

11. leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão na diagonal secundária.

matriz = []
soma = 0
contador = 2
while len(matriz) < 3:
    for linha in range(0, 3):
        lista = []
        for coluna in range(0, 3):
            valor = randint(0, 1)
            if coluna == contador:
                soma = soma + valor
                contador = contador - 1
            lista.append(valor)
        matriz.append(lista)

for linha, valor in enumerate(matriz):
    print(f'{linha} -> {valor}')
print()
print(f'Soma da diagonal secundária: {soma}')

12. Leia uma matriz de 3x3 elementos. Calcule e imprima a sua transposta. 

matriz1 = []
soma = 0
contador = 2
while len(matriz1) < 3:
    for linha in range(0, 3):
        lista = []
        for coluna in range(0, 3):
            valor = randint(0, 1)
            lista.append(valor)
        matriz1.append(lista)
for linha in matriz1:
    print(linha)

matriz2 = []
while len(matriz2) < 3:
    for i in range(0, 3):
        lista = []
        for linha in matriz1:
            lista.append(linha[i])
        matriz2.append(lista)

print()
for linha in matriz2:
    print(linha)

13. Gere uma matriz 4x4 com valores no intervalo [1, 20].
    Escreva um programa que transforme a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a 
    todos os elementos acima da diagonal principal. Imprima a matriz original e a matriz transformada.

matriz1 = []
soma = 0
while len(matriz1) < 3:
    for linha in range(0, 3):
        lista = []
        for coluna in range(0, 3):
            valor = randint(1, 20)
            if linha == coluna:
                soma = soma + valor
            lista.append(valor)
        matriz1.append(lista)

for lista in matriz1:
    print(lista)

matriz2 = matriz1.copy()
for lista in matriz2:
    if matriz2.index(lista) == 0:
        for i in range(1, 3):
            lista[i] = 0
    elif matriz2.index(lista) == 1:
        lista[-1] = 0

print()
for lista in matriz2:
    print(lista)

14. Faça um programa que gere automaticamente números entre 0 e 99 de uma cartela de bingo.
    Sabendo que cada cartela deverá conter 5 linhas de 5 números, gere estes dados de modo a não ter números repetidos
    dentro das cartelas.
    O programa deve exibir a cartela gerada

valores = set()
for i in range(0, 25):
    valores.add(randint(0, 99))

cartela = []
contador = 0
lista = []
for valor in valores:
    lista.append(valor)
    contador = contador + 1
    if contador % 5 == 0 and contador != 0:
        cartela.append(lista)
        lista = []
    if len(cartela) == 5:
        break

print('Cartela gerada:')
for linha in cartela:
    print(linha)
    
15. Leia uma matriz 5x10 que se refere as respostas de 10 questões de múltipla escolha, referentes a 5 alunos.
    Leia também um vetor de 10 posições contendo o gabarito de respostas que podem se a, b, c ou d.
    Seu programa deverá comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado resultado,
    contendo a pontuação correspondente de cada aluno.

opcoes = 'abcd'
matriz = []
while len(matriz) < 5:
    lista = []
    for i in range(0, 10):
        lista.append(choice(opcoes))
    matriz.append(lista)

gabarito = []
while len(gabarito) < 10:
    gabarito.append(choice(opcoes))

resultado = []
for aluno in matriz:
    nota = 0
    for i in range(0, 10):
        if aluno[i] == gabarito[i]:
            nota = nota + 1
    resultado.append(nota)

for aluno in matriz:
    print(f'Resposta do aluno {matriz.index(aluno)}: {aluno}')

print()
print(f'Gabarito: {gabarito}')

print()
for nota in resultado:
    print(f'Nota do aluno {resultado.index(nota)}: {nota}')

16. Faça um programa para corrigir uma prova com 10 questões de múltilpla escolha(a, b, c, d ou e), em uma turma com 3
    alunos.
    Cada questão vale 1 ponto.
    Leia o gabarito e, para cada aluno, leia sua matrícula(número inteiro) e suas respostas.
    Calcule e escreva: Para cada aluno, escreva sua matrícula, suas respostas e sua nota.
    O percentual de aprovação, assumindo média 7.0.

turma = {}
opcao = 'abcde'

for i in range(1, 4):
    turma[i] = []

for aluno in turma.keys():
    for i in range(0, 10):
        turma[aluno].append(choice(opcao))

# Gabarito
gabarito = ['e', 'd', 'a', 'a', 'a', 'c', 'd', 'e', 'e', 'c']

aprovados = 0
reprovados = 0
for aluno, respostas in turma.items():
    nota = 0
    for i in range(0, 10):
        if respostas[i] == gabarito[i]:
            nota = nota + 1
    respostas.append(nota)
    if nota >= 7:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1

print(f'Gabarito: {gabarito}')
print()
for aluno, resposta in turma.items():
    print(f'{aluno} -> {resposta[0:9]} -> nota {resposta[10]}')
if aprovados != 0 or reprovados != 0:
    print(f'Percentual de aprovação da turma: {round((aprovados / (aprovados + reprovados)), 2) * 100}%.')
else:
    print(f'Percentual de aprovação da turma: 0%')

17. Leia uma matriz 10x3 com as notas de 10 alunos em 3 provas.
    Em seguida, escreva o número de alunos cuja pior nota na prova 1, o número de alunos cuja pior nota na prova 2 e 
    o número de alunos cuja pior nota foi na prova 3.
    Em caso de empate, das piores notas de um aluno, o critério de desempapate é arbitrário, mas o aluno deve ser
    contabilizado apenas uma vez. 

turma = {}
for i in range(1, 11):
    turma[i] = []

for notas in turma.values():
    for i in range(0, 3):
        notas.append(round(uniform(0, 10), 2))

# Primeira prova
pior_nota_1 = 0
pior_nota_2 = 0
pior_nota_3 = 0
for notas in turma.values():
    if notas[0] < 7:
        pior_nota_1 = pior_nota_1 + 1
    if notas[1] < 7:
        pior_nota_2 = pior_nota_2 + 1
    if notas[2] < 7:
        pior_nota_3 = pior_nota_3 + 1

for aluno, notas in turma.items():
    print(f'Aluno {aluno} -> Notas: {notas}')

print()
print(f'Quantidade de alunos com pior nota da prova 1: {pior_nota_1}')
print(f'Quantidade de alunos com pior nota da prova 2: {pior_nota_2}')
print(f'Quantidade de alunos com pior nota da prova 3: {pior_nota_3}')

18. Faça um programa que permita o usuário entrar com uma matriz 3x3 números inteiros.
    Em seguida, gere um array unidimensional pela soma dos números de cada coluna da matriz e mostra na tela esse array.

matriz = []
while len(matriz) < 3:
    lista = []
    for i in range(0, 3):
        lista.append(randint(-20, 20))
    matriz.append(lista)

# Cria matriz2 a partir da soma das colunas da matriz1
matriz2 = []
for i in range(0, len(matriz)):
    soma = 0
    soma = soma + matriz[0][i] + matriz[1][i] + matriz[2][i]
    matriz2.append(soma)

print('Matriz original:')
for linha in matriz:
    print(linha)
print()
print('Matriz resultante:')
print(matriz2)

19. Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes informações sobre alunos de 
    uma disciplina, sendo todas as informações do tipo inteiro:
    Primeira coluna: número de matrícula(use um inteiro)
    Seguna coluna: Média das provas
    Terceira coluna: Média dos trabalhos
    Quarta coluna: Nota final
    Elabore um programa que:
    a) Leia as três primeiras informações de cada aluno
    b) Calcule a nota final como sendo a soma da média das provas e da média dos trabalhos
    c) Imprima a matrícula do aluno que obteve a maior nota final(assuma que só existe uma maior nota)
    d) Imprima a média aritmética das notas finais

turma = []
matricula = 1
while len(turma) < 5:
    lista = []
    lista.append(matricula)
    lista.append(randint(0, 10))
    lista.append(randint(0, 10))
    nf = lista[1] + lista[2]
    if nf > 10:
        nf = 10
    lista.append(nf)
    matricula = matricula + 1
    turma.append(lista)

# buscando a maior nota da turma
maior_nota = turma[0][3]
for aluno in turma:
    if aluno[3] > maior_nota:
        maior_nota = aluno[3]
        aluno_mn = turma[turma.index(aluno)][0]


# Média da turma
soma = 0
for aluno in turma:
    soma = soma + aluno[3]
media = round(soma / 5, 2)

for aluno in turma:
    print(f'{aluno[0]} -> Média das provas: {aluno[1]} -> Média dos trabalhos: {aluno[2]} -> Nota final: {aluno[3]}')
print()
print(f'Aluno com maior nota final da turma: {aluno_mn} -> {maior_nota}')
print(f'Média aritmética das notas finais: {media}')

20. Faça uma programa que leia uma matriz 3x6 com valores reais:
    a) Imprima a soma de todos os elementos das colunas ímpares.
    b) Imprima a média aritmética dos elementos da segunda e quarta colunas.
    c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
    d) imprima a matriz modificada.

matriz = []
while len(matriz) < 3:
    lista = []
    for i in range(0, 6):
        lista.append(round(uniform(0, 20), 2))
    matriz.append(lista)

print('Matriz original:')
for linha in matriz:
    print(linha)

soma_impar = 0
soma_coluna = 0
print()
print('Matriz alterada:')
for linha in matriz:
    for i in range(0, 6):
        if i % 2 != 0:
            soma_impar = Decimal(soma_impar) + Decimal(linha[i])
        if i == 1 or i == 3:
            soma_coluna = Decimal(soma_coluna) + Decimal(linha[i])
        if i == 5:
            linha[5] = float(round(Decimal(linha[0]) + Decimal(linha[1]), 2))
    print(linha)
media = soma_coluna / 6
print()
print(f'A soma de todos os elementos das colunas ímpares: {soma_impar:0.2f}')
print(f'Soma da média aritmética dos elementos da segunda e quarta colunas: {media: 0.2f} ')

21. Faça um programa que leia duas matrizes 2x2 com valores reais.
    Ofereça ao usuário um menu de opções:
    a) Somar as duas matrizes
    b) Subtrair a primeira matriz da segunda 
    c) Adicionar uma constante ás duas matrizes
    d) Imprimir as matrizes
    Nas duas primeiras opções uma terceira matriz 3x3 deve ser criada.
    Na terceira opção o valor da constante deve ser lido e o resultado da adição da constante deve ser armazenado
    na própria matriz.    

matriz1 = []
matriz2 = []
while len(matriz1) < 2 and len(matriz2) < 2:
    lista1 = []
    lista2 = []
    for i in range(0, 2):
        lista1.append(randint(0, 50))
        lista2.append(randint(0, 50))
    matriz1.append(lista1)
    matriz2.append(lista2)

lista_de_opcoes = [1, 2, 3, 4]
matriz3 = []
matriz4 = []
constante = 0
while True:
    print('1.Somar as duas matrizes.')
    print('2.Subtrair a primeira matriz da segunda.')
    print('3.Adicionar uma constante ás duas matrizes.')
    print('4.Imprimir as matrizes.')
    print('')
    opcao = int(input('Opcao: '))

    if opcao in lista_de_opcoes:
        if opcao == 1:
            while len(matriz3) < 3:
                for i in range(0, 2):
                    lista = []
                    for j in range(0, 2):
                        lista.append(matriz1[i][j] + matriz2[i][j])
                    lista.append(0)
                    matriz3.append(lista)
                matriz3.append([0, 0, 0])
            print()
        elif opcao == 2:
            while len(matriz4) < 3:
                for i in range(0, 2):
                    lista = []
                    for j in range(0, 2):
                        lista.append(matriz1[i][j] - matriz2[i][j])
                    lista.append(0)
                    matriz4.append(lista)
                matriz4.append([0, 0, 0])
            print()
        elif opcao == 3:
            constante = int(input('Digite o valor da constante: '))
            print()
        elif opcao == 4:
            print('Matriz de número 1:')
            for linha in matriz1:
                print(linha)
            print()
            print('Matriz de número 2:')
            for linha in matriz2:
                print(linha)
            print()
            print('A soma das duas matrizes e transformação em uma matriz 3x3:')
            for linha in matriz3:
                print(linha)
            print()
            print('A subtração das duas matrizes e transformação em uma matriz 3x3:')
            for linha in matriz4:
                print(linha)
            print()
            if constante == 0:
                print('Constante igual a 0.')
                print('Matriz 1:')
                for linha in matriz1:
                    print(linha)
                print()
                print('Matriz 2:')
                for linha in matriz2:
                    print(linha)
                print()
            else:
                matriz1[0][0] = matriz1[0][0] + constante
                matriz2[0][0] = matriz2[0][0] + constante
                print(f'A soma da constante {constante} ás duas matrizes:')
                print('Matriz 1:')
                for linha in matriz1:
                    print(linha)
                print()
                print('Matriz 2:')
                for linha in matriz2:
                    print(linha)
                print()
    else:
        break

22. Faça um programa que leia duas matrizes A e B de tamanho 3x3 e calcule C = A * B.

a = []
b = []

while len(a) < 3 and len(b) < 3:
    lista1 = []
    lista2 = []
    for i in range(0, 3):
        lista1.append(randint(0, 20))
        lista2.append(randint(0,20))
    a.append(lista1)
    b.append((lista2))

c = []
for i in range(0, 3):
    lista = []
    for j in range(0, 3):
        mult = 0
        for k in range(0, 3):
            mult = mult + a[i][k] * b[k][j]
        lista.append(mult)
    c.append(lista)

print('Matriz A:')
for linha in a:
    print(linha)

print()
print('Matriz B:')
for linha in b:
    print(linha)

print()
print('Matriz C:')
for linha in c:
    print(linha)

23. Faça um programa que leia uma matriz A de tamanho 3x3 e calcule B = A².

a = []
while len(a) < 3:
    lista = []
    for i in range(0, 3):
        lista.append(randint(1, 10))
    a.append(lista)

b = []
for i in range(0, 3):
    lista = []
    for j in range(0, 3):
        mult = 0
        for k in range(0, 3):
            mult = mult + a[i][k] * a[k][j]
        lista.append(mult)
    b.append(lista)

print()
print('Matriz A:')
for linha in a:
    print(linha)

print()
print('Matriz B:')
for linha in b:
    print(linha)

"""

from random import *
from decimal import *
from collections import Counter
from time import *
from math import *
from copy import *

