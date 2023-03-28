"""
1. Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro

num = int(input('Digite um número inteiro para obter seu dobro: '))
dobro = lambda num: num * 2
print(f'O dobro de {num}: {dobro(num)}')
------------------------------------------------------------------------------------------------------------------------
2. Faça uma função que receba a data atual(dia, mês e ano em inteiro) e exibe-a na tela no formato textual por extenso.
   Ex: Data: 01/01/2000, imprimir: 1 de janeiro de 2000

def func(*args):
    locale.setlocale(locale.LC_TIME, 'pt_BR')
    d, m, a = args
    data = date(a, m, d)
    return data.strftime('\n%d de %B de %Y')


dia = int(input('Digite o dia do mês: '))
while dia > 31:
    dia = int(input('Digite o dia do mês: '))
mes = int(input('Digite o mês do ano: '))
while mes > 12:
    mes = int(input('Digite o mês do ano: '))
ano = int(input('Digite o ano: '))
print(func(dia, mes, ano))
------------------------------------------------------------------------------------------------------------------------
3. Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo,
  -1 se negativo e 0 se for igual a 0.

def inteiro(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0


num = int(input('Digite um número: '))
print(inteiro(num))
------------------------------------------------------------------------------------------------------------------------
4. Faça uma função para verificar se um número é um quadrado perfeito.
   Um quadrado perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de outro número inteiro
   Ex: 1, 4, 9

def quadradoPerf(n):
    for i in range(1, n+1):
        quadrado = i ** 2
        if quadrado == n:
            return f'{n} é um quadrado perfeito.'
        elif quadrado > n:
            break
    return f'{n} não é um quadrado perfeito.'


num = int(str(input('Digite um número não negativo: ')))
while num < 0:
    print('Número digitado é negativo!')
    sleep(1)
    num = int(input('\nDigite um número não negativo: '))
print(quadradoPerf(num))
------------------------------------------------------------------------------------------------------------------------
5. Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
   Sendo que o raio é passado por parâmetro.

decimal.getcontext().prec = 2

def volume_esferico(r):
    volume = Decimal(str(4/3)) * Decimal(math.pi) * (r ** 3)
    return f'O valor do volume dessa esfera é de {volume}'


raio = Decimal(input('Digite o valor do raio: '))
print(volume_esferico(raio))
------------------------------------------------------------------------------------------------------------------------
6. Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segundos e os converta
   em segundos.

def convert_seg(*arg):
    segundos = 0
    for i in range(3):
        if i == 0:
            segundos = segundos + arg[i] * 3600
        elif i == 1:
            segundos = segundos + arg[i] * 60
        else:
            segundos = segundos + arg[i]
    return f'Tempo convertido: {segundos}s'


horas = int(input('Digite a hora: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
print(convert_seg(horas, minutos, segundos))
------------------------------------------------------------------------------------------------------------------------
7. Faça uma função que receba uma temperatura em graus Celcius e retorne-a convertida em graus Fahrenheit.
   A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celcius.

def fahren_converter(t):
    temp_fahren = t * Decimal(str(9.0/5.0)) + Decimal('32.0')
    return f'A temperatura em Fahrenheit: {temp_fahren}F'


temp_celcius = Decimal(input('Digite a temperatura em Celcius: '))
print(fahren_converter(temp_celcius))

------------------------------------------------------------------------------------------------------------------------
8. Seja a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = (a² + b²)^1/2.
   Faça uma função que receba os calores de a e b e calcule o valor da hipotenusa da equação.

def func(c1, c2):
    soma = c1 ** 2 + c2 ** 2
    return f'Resultado: {soma.sqrt():.2f}'
    pass


cat1 = Decimal(input('Digite o valor do primeiro cateto: '))
cat2 = Decimal(input('Digite o valor do segundo cateto: '))
print(func(cat1, cat2))
========================================================================================================================
Obs: essas questões foram geradas pelo chatGPT.

1. Faça um programa que peça ao usuário para digitar uma frase e conte quantas vezes a letra 'a' aparece na frase.

   frase = input('Digite uma frase: ')
   qtd_a = list(filter(lambda letra: letra == 'a', frase))
   print(f"Quantidade de vezes que a letra 'a' aparece na frase: {len(qtd_a)}")
------------------------------------------------------------------------------------------------------------------------
2. Escreva uma função que receba como entrada uma lista de números e retorne o maior número da lista.

   lista_num = [random.randint(0, 50) for i in range(10)]
   print(lista_num)
   print(f'Maior elemento na lista: {max(lista_num)}')
------------------------------------------------------------------------------------------------------------------------
3. Escreva um programa que leia um número inteiro do usuário e verifique se é par ou ímpar.
   Use a função integrada "input" para receber o número do usuário.

   num = input('Digite um número: ')
   if num % 2 == 0:
       print(f'O número {num} é par')
   else:
       print(f'O número é ímpar')
------------------------------------------------------------------------------------------------------------------------
4. Faça um programa que receba uma lista de números e calcule a média aritmética dos números da lista.

   lista = [random.randint(0, 20) for i in range(5)]
   print(lista)
   print(f'A média da lista: {mean(lista):.2f}')
------------------------------------------------------------------------------------------------------------------------
5. Escreva uma função que receba uma string e retorne a string invertida. Por exemplo, se a entrada for "python",
   a saída deve ser "nohtyp".

   string = input('Digite uma frase ou palavra: ')
   print(''.join(reversed(string)))
------------------------------------------------------------------------------------------------------------------------
6. Faça um programa que receba uma lista de palavras e retorne uma lista contendo o tamanho de cada palavra.
   Use a função integrada "len" para calcular o tamanho de cada palavra.

lista_palavras = []
tam = int(input('Digite o número de palavras que deseja incluir na lista: '))
while len(lista_palavras) < tam:
    lista_palavras.append(input('Digite uma palavra: '))

print('\nPalavras contidas na lista e seus respectivos tamanhos:')
for palavra in lista_palavras :
    print(f'{palavra}: {len(palavra)}')
------------------------------------------------------------------------------------------------------------------------
7. Escreva uma função que receba uma lista de números e retorne uma lista contendo apenas os números pares da lista.

lista_num = [random.randint(1, 50) for i in range(10)]
lista_par = list(filter(lambda num: num % 2 == 0, lista_num))
print(f'A lista de números gerada: {lista_num}')
print(f'A lista de números pares: {lista_par}')
------------------------------------------------------------------------------------------------------------------------
8. Faça um programa que receba uma lista de números e ordene a lista em ordem crescente.
   Use a função integrada "sorted" para fazer a ordenação.

lista = [random.randint(1, 40) for i in range(10)]
lista_cresc = sorted(lista)
print(f'Lista: {lista}')
print(f'Lista em ordem crescente: {lista_cresc}')
------------------------------------------------------------------------------------------------------------------------
9. Use a função len() para encontrar o número de caracteres em uma string.

string = input('Digite uma palavra ou frase: ')
print(f'Palavra ou frase digitada: {string}')
print(f'Tamanho: {len(string)} ')
------------------------------------------------------------------------------------------------------------------------
11. Use a função abs() para encontrar a distância absoluta entre dois números.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print(f'A distância absoluta entre os dois números: {abs(dif:= num1 - num2)}')
------------------------------------------------------------------------------------------------------------------------
12. Use a função max() para encontrar o maior número em uma lista.

lista = [random.randint(1, 100)for i in range(10)]
print(lista)
print(f'O maior elemento da lista: {max(lista)}')
------------------------------------------------------------------------------------------------------------------------
13. Use a função sum() para encontrar a soma dos números em uma lista.

lista = [random.randint(1, 100) for i in range(10)]
print(lista)
print(f'A soma da lista: {sum(lista)}')
------------------------------------------------------------------------------------------------------------------------
14. Use a função round() para arredondar um número para o inteiro mais próximo.

num = float(input('Digite um número: '))
print(f'O número arrendondado para o inteiro mais próximo: {round(num)}')
------------------------------------------------------------------------------------------------------------------------
15. Use a função filter() para encontrar todos os números pares em uma lista.

lista = [random.randint(1, 100) for i in range(15)]
lista_par = list(filter(lambda num: num % 2 == 0, lista))
print(lista)
print(f'Lista de números pares: {lista_par}')
------------------------------------------------------------------------------------------------------------------------
16. Use a função map() para converter todos os elementos em uma lista em seus valores absolutos.

lista = [random.randint(-100, 100) for i in range(15)]
lista_abs = list(map(lambda num: abs(num), lista))
print(lista)
print(f'Lista de números absolutos: {lista_abs}')
------------------------------------------------------------------------------------------------------------------------
17. Use a função sorted() para classificar uma lista de palavras em ordem alfabética.

palavras = ['gato', 'cachorro', 'passarinho', 'leão', 'zebra', 'girafa', 'macaco',
            'elefante', 'tartaruga', 'peixe']
palavras_sort = sorted(palavras)
print(f'Lista de palavras: {palavras}')
print(f'Lista em ordem alfabética: {palavras_sort}')
------------------------------------------------------------------------------------------------------------------------
18. Use a função any() para verificar se pelo menos um valor em uma lista é verdadeiro.

lista = [False, [], '', 1]
print(lista)
print(f'Existe algum elemento verdareiro nesta lista? {any(lista)}')
------------------------------------------------------------------------------------------------------------------------
19. Use a função all() para verificar se todos os valores em uma lista são verdadeiros.

lista = [1, 'Bola', ['a', 'b', 'c'], (100, ), {'a': 'lista telefônica'}]
print(lista)
print(f'Todos os valores desta lista são verdadeiros? {all(lista)}')
------------------------------------------------------------------------------------------------------------------------
20. Use a função zip() para combinar duas listas em um dicionário,
    onde a primeira lista é a chave e a segunda lista é o valor.

chave = [letra for letra in 'abcd']
valor = [num ** 2 for num in range(4)]
dict = dict(tupla for tupla in list(zip(chave, valor)))
print(f'Chaves: {chave}')
print(f'Valores: {valor}')
print('\nDicionário criado a partir das duas listas:')
print(dict)
------------------------------------------------------------------------------------------------------------------------
21. Use a função min() e max() para encontrar a menor e a maior temperatura
    em uma lista de temperaturas em graus Celsius e converta-as em graus Fahrenheit.

def celcius_para_fahrenheit(tc):
    return (tc * Decimal(str(9/5))) + 32

temperatura_c = [random.randint(0, 100) for i in range(10)]
print(f'Lista de temperaturas em graus Celcius: {temperatura_c}')
print(f'Maior temperatura: {max(temperatura_c)}ºC')
print(f'Menor temperatura: {min(temperatura_c)}ºC')

print(f'\nMaior temperatura convertida em graus Fahrenheit: {celcius_para_fahrenheit(max(temperatura_c)):.2f}')
print(f'Menor temperatura convertida em graus Fahrenheit: {celcius_para_fahrenheit(min(temperatura_c)):.2f}')
------------------------------------------------------------------------------------------------------------------------
22. Use a função filter() e map() para encontrar a média dos valores pares em uma lista.

lista = [random.randint(1, 50) for i in range(15)]
print(lista)
lista_par = list(filter(lambda n: n % 2 == 0, lista))
print(f'Valores pares: {lista_par}')
media = sum(map(lambda np: np / len(lista_par), lista_par))
print(f'A média dos valores pares: {media:.2f}')
------------------------------------------------------------------------------------------------------------------------
23. Como usar a função zip() e a função enumerate() para iterar
    sobre duas listas simultaneamente e imprimir o índice e o valor de cada item em ambas as listas?

lista1 = [random.randint(1, 10) for i in range(10)]
lista2 = [random.randint(11, 20) for i in range(10)]
print(lista1)
print(lista2)

zipped = list(enumerate(zip(lista1, lista2)))
print(zipped)
------------------------------------------------------------------------------------------------------------------------
24. Use a função sorted() para classificar uma lista de dicionários com base em um valor específico em cada dicionário.

pessoas = [
    {"nome": "João", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "José", "idade": 27, "cidade": "Belo Horizonte"},
    {"nome": "Ana", "idade": 35, "cidade": "Curitiba"}
]
print('Lista de Dicionários:')
pprint(pessoas)

pessoas_sorted = sorted(pessoas, key=itemgetter('idade'), reverse=True)
print('\nLista de Dicionários ordenados por chave específica:')
pprint(pessoas_sorted)
------------------------------------------------------------------------------------------------------------------------
25. Dada uma lista de dicionários com informações sobre carros,
    escreva uma função que retorne a média de preços dos carros que possuem mais de 150 cavalos de potência:

def media_carros(dic):
    carros_150_cavalos = list(filter(lambda c: c['potencia'] > 150, dic))
    return sum(map(lambda c: c['preco'], carros_150_cavalos)) / len(carros_150_cavalos)


carros = [
    {"marca": "Fiat", "modelo": "Palio", "potencia": 120, "preco": 25000},
    {"marca": "Ford", "modelo": "Focus", "potencia": 160, "preco": 35000},
    {"marca": "Chevrolet", "modelo": "Cruze", "potencia": 180, "preco": 45000},
    {"marca": "Volkswagen", "modelo": "Golf", "potencia": 130, "preco": 30000},
    {"marca": "Fiat", "modelo": "Uno", "potencia": 90, "preco": 20000},
    {"marca": "Renault", "modelo": "Sandero", "potencia": 110, "preco": 23000},
]

print('Lista de dicionários de carros:')
pprint(carros)
print(f'\nMédia dos preços de carros com 150 cavalos: {media_carros(carros):.2f} ')
------------------------------------------------------------------------------------------------------------------------
26. Dada uma lista de números, escreva uma função que retorne uma lista
    contendo apenas os números que são divisíveis por 3 e por 5:

def div_3_5(lst):
    return list(filter(lambda d: d % 3 == 0 and d % 5 == 0, lst))


lista = list({random.randint(1, 50) for i in range(20)})
print(lista)
print(f'\nLista de números divisíveis por 3 e 5:')
print(div_3_5(lista))
------------------------------------------------------------------------------------------------------------------------
27. Dada uma lista de tuplas contendo informações sobre alunos,
    escreva uma função que retorne o nome do aluno com a maior média de notas:

def media_alunos(lst):
    lst_copy = list(map(lambda tupla: (tupla[0], round(sum(tupla[1]) / len(tupla[1]), 2)), lst))
    aluno, nota = max(lst_copy, key=itemgetter(1))
    return f'{aluno} possui a maior média da turma: {nota}'


alunos = [
    ("João", [8, 7, 9]),
    ("Maria", [9, 9, 10]),
    ("Pedro", [7, 8, 8]),
    ("Ana", [10, 9, 8]),
    ("Lucas", [6, 7, 5])
]
print('Alunos e suas médias:')
pprint(alunos)
print(f'\n{media_alunos(alunos)}')
media_alunos(alunos)
------------------------------------------------------------------------------------------------------------------------
28. Dada uma lista de palavras, escreva uma função que retorne uma lista contendo apenas as palavras que contém
    as vogais "a", "e", "i", "o" e "u" em ordem alfabética:

def apenas_vogais(lst):
    vogais = list('aeiou')
    lista = []
    for palavra in lst:
        vogais_in = list(filter(lambda letra: letra in vogais, palavra))
        if vogais_in == vogais:
            lista.append(palavra)
    return sorted(lista)


with open('Palavras pentavogalicas.txt', encoding='UTF-8') as leitor:
    palavras = [palavra.rstrip('\n\t') for palavra in leitor.readlines()]
    palavras_mod = random.sample(palavras, len(palavras))

print('Lista de palavras que possuem todas as vogais em ordem alfabética: ')
print(apenas_vogais(palavras_mod))
------------------------------------------------------------------------------------------------------------------------
29. Crie uma função que receba uma lista de strings e retorne uma nova lista
    com as strings ordenadas pelo número de caracteres de forma decrescente,
    utilizando a função sorted com uma função lambda.

def lista_ord(lst):
    return sorted(lst, key=len, reverse=True)


lista = ['carro', 'vaca', 'lona', 'paralelepípedo', 'vinte', 'cachorro', 'meia', 'jantar']
print(lista)
print(f'\nLista ordenada pelo número de caracteres de forma decrescente:')
print(lista_ord(lista))
------------------------------------------------------------------------------------------------------------------------
30. Crie uma função que receba uma lista de dicionários contendo informações sobre livros,
    incluindo título, autor e preço, e retorne uma nova lista de dicionários contendo apenas
    os livros com preço acima de uma certa quantia, passada como argumento da função.
    Utilize a função filter com uma função lambda.

def filtrarPorPreco(lst, p):
    return list(filter(lambda l: l['preco'] > p, lst))


livros = [
    {'titulo': 'A menina que roubava livros', 'autor': 'Markus Zusak', 'preco': 39.90},
    {'titulo': '1984', 'autor': 'George Orwell', 'preco': 29.90},
    {'titulo': 'O senhor dos anéis', 'autor': 'J.R.R. Tolkien', 'preco': 59.90},
    {'titulo': 'O pequeno príncipe', 'autor': 'Antoine de Saint-Exupéry', 'preco': 19.90},
    {'titulo': 'Dom Quixote', 'autor': 'Miguel de Cervantes', 'preco': 49.90},
    {'titulo': 'Cem anos de solidão', 'autor': 'Gabriel García Márquez', 'preco': 39.90},
    {'titulo': 'O nome da rosa', 'autor': 'Umberto Eco', 'preco': 29.90},
    {'titulo': 'O apanhador no campo de centeio', 'autor': 'J.D. Salinger', 'preco': 24.90},
    {'titulo': 'O grande Gatsby', 'autor': 'F. Scott Fitzgerald', 'preco': 34.90},
    {'titulo': 'A revolução dos bichos', 'autor': 'George Orwell', 'preco': 19.90}
]

preco = float(input('Digite o preço de limite mínimo para filtrar a coleção de livros: '))
print('\nLista filtrada:')
pprint(filtrarPorPreco(livros, preco))
------------------------------------------------------------------------------------------------------------------------
31. Crie uma função que receba uma lista de números e retorne uma nova lista contendo apenas os números ímpares,
    utilizando a função filter com uma função lambda.

def impares(lst):
    return list(filter(lambda num: num % 2 != 0, lst))


numeros = [random.randint(1, 50) for num in range(15)]
print(numeros)
print('Lista com apenas os números ímpares:')
print(impares(numeros))
------------------------------------------------------------------------------------------------------------------------
32. Crie uma função que receba uma lista de strings e retorne uma nova lista contendo apenas as strings que são
    palíndromos (ou seja, que podem ser lidas da mesma forma de trás para frente),
    utilizando a função filter com uma função lambda.

def palindromo(lst):
    return list(filter(lambda palavra: list(palavra) == list(reversed(palavra)), lst))


palavras = ["ana", "arara", "banana", "casa", "carro",
            "desenvolvimento", "ele", "ovo", "reviver", "sopa", "tenet", "xadrez"]
print('Lista de palavras:')
print(palavras)
print('\nLista de palavras palindrômicas:')
print(palindromo(palavras))
------------------------------------------------------------------------------------------------------------------------
33. Crie uma função que receba uma lista de dicionários contendo informações sobre pessoas, incluindo nome,
    idade e cidade, e retorne uma nova lista de dicionários contendo apenas as pessoas com idade entre dois valores
    passados como argumentos da função. Utilize a função filter com uma função lambda.

def filtra_idade(lst, li, ls):
    return list(filter(lambda pessoa: li < pessoa['idade'] < ls, lst))


pessoas = [{"nome": "João Silva", "idade": 25, "cidade_nascimento": "São Paulo"},
           {"nome": "Maria Souza", "idade": 35, "cidade_nascimento": "Rio de Janeiro"},
           {"nome": "Pedro Santos", "idade": 20, "cidade_nascimento": "Belo Horizonte"},
           {"nome": "Ana Oliveira", "idade": 30, "cidade_nascimento": "Porto Alegre"},
           {"nome": "Lucas Pereira", "idade": 28, "cidade_nascimento": "Curitiba"}]
pprint(pessoas)

print('\nDigite abaixo os limites inferior e superior para filtrar as pessoas por idade')
lim_inf = int(input('Digite o limite inferior: '))
lim_sup = int(input('Digite o limite superior: '))
print(f'\nPessoas entre {lim_inf} e {lim_sup} anos:')
pprint(filtra_idade(pessoas, lim_inf, lim_sup))
------------------------------------------------------------------------------------------------------------------------
34. Crie uma função que receba uma lista de números e retorne uma nova lista contendo a soma acumulada dos números
    na lista, utilizando a função reduce da biblioteca functools.

def soma_numeros(lst):
    return reduce(lambda x, y: x + y, lst)


numeros = [random.randint(1, 50) for i in range(5)]
print('Lista de números:')
print(numeros)
print('\nSoma desses números:')
print(soma_numeros(numeros))

35. Crie uma função que receba duas listas de números de mesmo comprimento e
    retorne uma nova lista contendo o produto dos elementos correspondentes de cada lista, utilizando a função zip.

def lista_prod(n1, n2):
    return list(map(lambda x: x[0] * x[1], zip(n1, n2)))


num1 = [random.randint(1, 10) for i in range(5)]
num2 = [random.randint(1, 10) for i in range(5)]
print('Lista 1:')
print(num1)
print('Lista 2:')
print(num2)
print('\nLista contendo o produto de cada elemento das duas listas:')
print(lista_prod(num1, num2))
=======================================================================================================================
36. Crie uma função que receba uma lista de dicionários contendo informações sobre pessoas,
    incluindo nome, idade e cidade, e retorne uma nova lista de dicionários contendo as informações de cada pessoa,
    ordenadas pelo nome em ordem alfabética, utilizando a função sorted com uma função lambda.

def sort_lista(lst):
    return sorted(lst, key=lambda p: p['nome'])


pessoas = [{"nome": "João Silva", "idade": 25, "cidade_nascimento": "São Paulo"},
           {"nome": "Maria Souza", "idade": 35, "cidade_nascimento": "Rio de Janeiro"},
           {"nome": "Pedro Santos", "idade": 20, "cidade_nascimento": "Belo Horizonte"},
           {"nome": "Ana Oliveira", "idade": 30, "cidade_nascimento": "Porto Alegre"},
           {"nome": "Lucas Pereira", "idade": 28, "cidade_nascimento": "Curitiba"}]
print('Lista de pessoas:')
pprint(pessoas)
print('\nLista de pessoas ordenadas por ordem alfabética:')
pprint(sort_lista(pessoas))
=======================================================================================================================
37. Crie uma função que receba uma lista de dicionários contendo informações sobre produtos,
    incluindo nome, preço e quantidade, e retorne o valor total do estoque,
    utilizando a função sum com uma função lambda.

def soma_estoque(lst):
    return sum(map(lambda prod: prod['preço'] * prod['quantidade'], lst))


produtos = [
    {"nome": "Maçã", "preço": 2.50, "quantidade": 10},
    {"nome": "Banana", "preço": 1.50, "quantidade": 20},
    {"nome": "Laranja", "preço": 3.00, "quantidade": 15},
    {"nome": "Pêra", "preço": 2.75, "quantidade": 8},
    {"nome": "Uva", "preço": 4.00, "quantidade": 12}
]
print('Lista de produtos:')
pprint(produtos)
print(f'\nO valor total do estoque: R$ {soma_estoque(produtos):.2f}')
=======================================================================================================================
38. Crie uma função que receba uma lista de números e retorne uma nova lista contendo a raiz quadrada de cada número,
    utilizando a função map com a função sqrt do módulo math.

def sqrt_list(lst):
    return list(map(lambda num: round(math.sqrt(num), 2), lst))


numeros = [random.randint(1, 50) for i in range(5)]
print('Lista de números:')
print(numeros)
print('\nLista contendo a raiz quadrada de cada número: ')
print(sqrt_list(numeros))
"""


