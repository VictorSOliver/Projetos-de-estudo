"""
1. Crie uma função que recebe como parêmetro um número inteiro e devolve o dobro.

def dobro(num):
    return num * 2


numero = int(input('Digite um número inteiro: '))
print(f'O dobro desse número: {dobro(numero)}')

2. Faça uma função que receba a data atual(dia, mês e ano em inteiro) e exibe-a na tela no formato textual por extenso.
   Ex: Data: 01/01/2000, imprimir: 1 de janeiro de 2000

def data_extensa(d, m, a):
    locale.setlocale(locale.LC_TIME, 'pt_BR')
    data = date(a, m, d)

    return data.strftime('%d de %B de %Y')


dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
print(data_extensa(dia, mes, ano))

3. Faça uma função para verificar se um número é positivo ou negativo.
   Sendo que o valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.

def positivo_ou_negativo(n): # Caso positivo retorna 1, negativo retorna -1 e 0 caso o valor for zero.
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

num = int(input('Digite um número: '))
print(f'O número é {positivo_ou_negativo(num)}')

4. Faça uma função para verificar se um número é um quadrado perfeito.
   Um quadrado perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de outro número.
   Ex: 1, 4, 9...

def quadrado_perfeito(num):
    for i in range(1, num):
        div = num / i
        if div == i :
            return True
    return False


numero = int(input('Digite um número inteiro positivo: '))
if quadrado_perfeito(numero):
    print(f'O número {numero} é um quadrado perfeito.')
else:
    print(f'O número {numero} não é um quadrado perfeito.')

5. Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
   Sendo que o raio é passado por parâmetro.
   V = 4/3 * pi * R³

def volume_esférico(r):
    return Decimal(4/3) * Decimal(math.pi) * Decimal(pow(r, 3))


raio = float(input('Digite o tamanho do raio da circuferência: '))
print(f'Volume da circuferência: {volume_esférico(raio): .2f}')

6. Faça uma função que receba 3 números inteiros como parâmetro, representando horas,
   minutos e segundos, e os converta em segundos

def converter_segundos(hora, minuto, segundo):
    hora_sg = hora * 3600
    min_sg = minuto * 60
    return f'{segundo + hora_sg + min_sg} segundos. '


horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
print(f'Tempo convertido em segundos: {converter_segundos(horas, minutos, segundos)}')

7. Faça um função que receba uma temperatura em graus Celcius e retorne-o convertida em graus Fahrenheit.
   A fórmula de conversão é: F = C * (9.0 / 5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celcius.

def conversao_fahrenheit(temperatura):
    return temperatura * Decimal(9 / 5) + 32


temp_celcius = Decimal(input('Digite a temperatura em Celcius: '))
print(f'A temperatura convertida em graus Fahrenheit: {conversao_fahrenheit(temp_celcius):.2f}F')

8. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = sqrt(a² + b²).
   Faça uma função que receba os valores de a e b e calcule o valor da hipotenusa atravès da equação.

def hipotenusa(cat_a, cat_b):
    return math.sqrt(pow(a, 2) + pow(b, 2))


a = Decimal(input('Digite o cateto "a" do triângulo: '))
b = Decimal(input('Digite o cateto "b" do triângulo: '))
print(f'A hipotenusa do triângulo: {hipotenusa(a, b):.2f}')

9. Faça uma funcão que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro.
   O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = pi * raio² * altura, onde
   pi = 3,141592.

def volume_cilindro(r, h):
    return Decimal(f'{math.pi:.6f}') * Decimal(pow(r, 2)) * h


raio = Decimal(input('Digite o tamanho do raio do cilindro: '))
h = Decimal(input('Digite a altura do cilindro: '))
print(f'Volume do cilindro: {volume_cilindro(raio, h):.2f}m³')

10. Faça uma função que receba dois números e retorne qual deles é o maior:

def maior_entre_dois(num1, num2):
    return max(num1, num2)


numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print(f'O maior número dentre os dois: {maior_entre_dois(numero1, numero2)}')

11. Elabore uma função que receba três notas de um aluno como parâmetros e uma letra.
    Se a letra for A, a função deverá calcular a média aritmética das notas do aluno;
    Se for P, deverá calcular  média ponderada, com pesos 5, 3 e 2.

def media(a, b, c, ltr):
    if ltr == 'A':
        return (a + b + c) / 3
    return (a * 5 + b * 3 + c * 2) / 10

nota1 = Decimal(input('Digite a primeira nota: '))
nota2 = Decimal(input('Digite a segunda nota: '))
nota3 = Decimal(input('Digite a terceira nota: '))
print('Digite a letra das seguintes operações:')
print('A. Média aritmética.')
print('P. Média ponderada.')
letra = str(input('Opcão: '))

if letra == 'A':
    print(f'A média aritmética das três notas: {media(nota1, nota2, nota3, letra):.1f}')
else:
    print(f'A média ponderada das três notas: {media(nota1, nota2, nota3, letra):.1f}')

12. Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algarismos.
    Por exemplo, o número 251 corresponderá o valor 8(2 + 5 + 1).
    Se o número lido não for maior do que zero, o programa terminará com a mensagem 'Número inválido.'

def soma_algarismos(num):
    if int(num) <= 0:
        print('Número inválido.')
    else:
        soma = 0
        for algarismo in num:
            soma = soma + int(algarismo)
        print(f'Soma dos algarismo do número {num}: {soma}')


numero = str(input('Digite um número inteiro maior do que zero: '))
soma_algarismos(numero)

13. Faça uma função que receba dois valores numéricos e um símbolo.
    Este símbolo representará a operação que se deseja efetuar com os números.
    Se o símbolo for + deverá ser realizada uma adição, se for - uma subtração, se for / uma divisão e se for *
    uma multiplicação.

    def calculadora(n1, n2, simb):
    if simb == '+':
        return n1 + n2
    elif simb == '-':
        return n1 - n2
    elif simb == '/':
        if n2 == 0:
            return 'Divisão por zero.'
        else:
            return round(n1 / n2, 2)
    elif simb == '*':
        return n1 * n2

while True:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print('Selecione uma das opções abaixo:')
    print('+ -> Adição')
    print('- -> Subtração')
    print('/ -> Divisão')
    print('* -> Multiplicação')
    print('$ -> Sair')
    simbolo = str(input('Digite o símbolo da operação desejada: '))
    if simbolo == '$':
        break

    print()
    print(f'{num1} {simbolo} {num2} = {calculadora(num1, num2, simbolo)}')

14. Faça uma função que receba a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um
    percurso, calcule o consumo em km/l e escreva uma mensagem de acordo com a tabela do problema.

def consumo_de_veiculo(dist, gas):
    div = round(dist / gas, 2)
    if div < 8:
        return 'Venda o carro!'
    elif div >= 8 and div <= 14:
        return 'Econômico!'
    elif div > 14:
        return 'Super econômico!'

distancia = int(input('Digite a distância percorrida pelo veículo: '))
gasolina = int(input('Digite a quantidade de gasolina consumida durate o trajeto: '))

print()
print('Quanto ao consumo do veículo:')
print(consumo_de_veiculo(distancia, gasolina))

15. Crie um programa que receba três valores(obrigatoriamente maiores que zero), representando ás medidas dos três
    lados de um triângulo. Elabore funções para:
    a) Determinar se os lados formam um triângulo, sabendo que:
       O comprimento de cada lado do triãngulo é menor que a soma dos outros dois lados.
    b) Determinar e mostrar o tipo do triângulo, caso as medidas formem um triângulo. Sabendo que:
       Chama-se equilátero o triângulo que tem três lados iguais.
       Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
       Recebe o nome de escaleno o triângulo que tem três lados de comprimento diferentes.

def compara_lados(lad1, lad2, lad3):
    if lad1 < lad2 + lad3 and lad2 < lad1 + lad3 and lad3 < lad1 + lad2:
        return True
    return False


def tipo_triangulo(lad1, lad2, lad3):
    if lad1 == lad2 and lad1 == lad3 and lad2 == lad3:
        return 'O triângulo é equilátero.'
    elif lad1 == lad2 or lad1 == lad3 or lad2 == lad3:
        return 'O triângulo é isósceles.'
    else:
        return 'O triãngulo é escaleno.'


lado1 = Decimal(input('Digite o comprimento do lado 1 do triângulo: '))
lado2 = Decimal(input('Digite o comprimento do lado 2 do triângulo: '))
lado3 = Decimal(input('Digite o comprimento do lado 3 do triângulo: '))
while lado1 == 0 or lado2 == 0 or lado3 == 0:
    print()
    print('O comprimento de um lado não pode ser igual a 0.')
    if lado1 == 0:
        lado1 = Decimal(input('Digite o comprimento do lado 1 do triângulo: '))
    elif lado2 == 0:
        lado2 = Decimal(input('Digite o comprimento do lado 2 do triângulo: '))
    elif lado3 == 0:
        lado3 = Decimal(input('Digite o comprimento do lado 3 do triângulo: '))

if compara_lados(lado1, lado2, lado3):
    print(tipo_triangulo(lado1, lado2, lado3))
else:
    print()
    print('Um dos lados é maior do que a soma dos outros, portanto não é um triângulo.')

16. Faça um função chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando vários símbolos de igual(Ex: =====).
    A função recebe por parâmetro quantos sinais de igual serão mostrados.

def DesenhaLinha(numl):
    for i in range(0, numl):
        print('=', end='')


linhas = int(input('Digite a quantidade de linhas que serão desenhados na tela: '))
print()
DesenhaLinha(linhas)

17. Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a soma dos N inteiros existentes
    entre eles.

def soma_entre_numeros(num1, num2):
    soma = 0
    for i in range(num1 + 1, num2):
        soma = soma + i
    return soma


numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print()
print(f'A soma dos números entre {numero1} e {numero2}:')
print(soma_entre_numeros(numero1, numero2))

18. Faça uma função que receba por parãmetro dois valores X e Z.
    Calcule e retorne o resultado de X ^ Z para o programa principal.
    Atenção: não utilize nenhuma função pronta de exponenciação.

def expo(num1, num2):
    return num1 ** num2


numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

print()
print(f'{numero1} ^ {numero2} = {expo(numero1, numero2)}')

19. Faça uma função que retorne o maior fator primo de um número.

def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def maior_fat_primo(num):
    aux = num
    maior_primo = 2
    if num == 2:
        return maior_primo
    else:
        while num != 1:
            for i in range(2, aux + 1):
                while num % i == 0:
                    num = num / i
                    if primo(i):
                        if i > maior_primo:
                            maior_primo = i
        return maior_primo


numero = int(input('Digite um número: '))
print(f'O maior fator primo deste número: {maior_fat_primo(numero)}')

20. Faça um algoritmo que receba um número inteiro positivo n e calcule o seu fatorial, n!.

def fatorial(num):
    fat = num
    if fat == 0:
        return 1
    for i in range(1, num):
        fat = fat * i
    return fat


numero = int(input('Digite um número para o cálculo: '))
print(f'{numero}! = {fatorial(numero)}')

21. Escreva uma função para determinar a quantidade de números primos abaixo de N.

def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primos_abaixo(num):
    conta = 0
    for i in range(2, num):
        if primo(i):
            conta = conta + 1
    return conta


numero = int(input('Digite um número para o cálculo de números primos abaixo dele: '))
print(f'Quantidade de números primos abaixo de {numero}: {primos_abaixo(numero)}')

22. Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com pontos de exclamação,
    conforme o exemplo dado pelo problema.

def mostra_linha(nlinha):
    for i in range(0, nlinha):
        for j in range(0, i + 1):
            print('!', end=' ')
        print()

numero_linha = int(input('Digite o número de linhas que você deseja imprimir o caractere !: '))
print()
mostra_linha(numero_linha)

23. Escreva uma função que gera um triângulo lateral de altura 2* n-1 e n largura.

def triangulo_lateral(larg, h):
    for i in range(0, h):
        if i >= larg:
            for k in range(0, j):
                print('*', end=' ')
            j = j - 1
            print()
        else:
            for j in range(0, i + 1):
                print('*', end=' ')
            print()


largura = int(input('Digite a largura do triângulo lateral a ser gerado: '))
altura = 2 * largura - 1
triangulo_lateral(largura, altura)

24. Escreva uma função que gera um triângulo de altura e lados n e base 2* n-1.

def gera_triangulo(h): # h = altura
    for i in range(1, h + 1):
        for espaco in range(0, h - i):
            print(end='  ')
        largura = 2 * i - 1
        for j in range(0, largura):
            print('*', end=' ')
        print()


altura = int(input('Digite a altura do triângulo a ser gerado: '))
gera_triangulo(altura)

25. Faça uma função que receba um inteiro N como parâmetro, calcule e retorne o resultado da seguinte série:
    S = 2/4 + 5/5 + 10/6 + ... + (N² + 1) / (N + 3)

def calcula_serie(num):
    serie = 0
    for i in range(1, num + 1):
        serie = serie + Decimal((pow(i, 2) + 1) / (i + 3))
    return serie


numero = int(input('Digite um número para o cálculo da série (N² + 1) / (N + 3):  '))
print(f'Resultado: {calcula_serie(numero):.2f}')

26. Faça um algoritmo que receba um número inteiro positivo n e calcule o somatório de 1 até n.

def somatorio(num):
    soma = 0
    for i in range(1, num+1):
        soma = soma + i
    return soma


numero = int(input('Digite um número inteiro para o cálculo do somatório de 1 até n: '))
print(f'Resultado do somatório: {somatorio(numero)}')

27. Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor do seno desse ângulo
    usando sua respectiva sére de Taylor.


def fatorial(num):
    if num != 0:
        fat = num
        for i in range(1, num):
            fat = fat * i
        return fat
    return 1


def graus_para_radianos(ang):
    ang = ang * Decimal(round(math.pi, 6)) / 180
    return ang


def seno_taylor(ang):
    ang_rad = graus_para_radianos(ang)
    soma = 0
    for i in range(0, 6):
        soma = soma + Decimal(pow(-1, i) / fatorial(2 * i + 1)) * Decimal(pow(ang_rad, 2 * i + 1))
    return soma


angulo = Decimal(input('Digite o valor do ângulo a ser calculado seu seno usando uma série de Taylor: '))
print(f'Seno de {angulo}º = {seno_taylor(angulo):.2f}')
print()
print(f'Sin({angulo}) = {math.sin(graus_para_radianos(90)):.2f}')

28. Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor do cosseno desse ângulo
    usando sua respectiva série de Taylor.

def expo(a, b):
    return a ** b


def fatorial(num):
    if num != 0:
        fat = num
        for i in range(1, num):
            fat = fat * i
        return fat
    return 1


def graus_para_radianos(a):
    a = a * (round(math.pi, 6) / 180)
    return a


def cos_taylor(ang):
    soma = 0
    ang_rad = graus_para_radianos(ang)
    for i in range(0, 6):
        x = Decimal(pow(-1, i) / fatorial(2 * i))
        y = Decimal(ang_rad ** (2 * i))
        soma = soma + x * y
    return soma


angulo = float(input('Digite o valor do ãngulo em graus para o cálculo de seu cosseno: '))
print(f'O cosseno de {angulo}º = {cos_taylor(angulo):.2f}')


29. Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor do seno hiperbólico desse
    ângulo usando sua respectiva série de Taylor.

def fatorial(num):
    if num != 0:
        fat = num
        for i in range(1, num):
            fat = fat * i
        return fat
    return 1


def graus_para_radianos(a):
    a = a * (round(math.pi, 6) / 180)
    return a


def seno_taylor(ang):
    ang_rad = graus_para_radianos(ang)
    soma = 0
    for i in range(0, 6):
        x = Decimal(pow(ang_rad, 2 * (i + 1)) / fatorial(2 * (i + 1)))
        soma = soma + x
    return soma


angulo = float(input('Digite o valor do ângulo a ser calculado seu seno hiperbólico: '))
print(f'Seno hiperbólico de {angulo}º = {seno_taylor(angulo):.2f}')

30. Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule o valor cosseno hiperbólico
    usando sua respectiva série de Taylor.

def graus_para_radianos(a):
    a = a * (round(math.pi, 6) / 180)
    return a


def fatorial(num):
    if num == 0:
        return 1
    else:
        fat = num
        for i in range(1, num):
            fat = fat * i
        return fat


def cosseno_taylor(ang):
    soma = 0
    ang_rad = graus_para_radianos(ang)
    for i in range(0, 6):
        x = Decimal(pow(ang_rad, 2 * i) / fatorial(2 * i))
        soma = soma + x
    return soma

angulo = float(input('Digite o ângulo para o cálculo do cosseno hiperbólico utilizando sua série de Taylor: '))
print(f'Resultado do cosseno de {angulo}: {cosseno_taylor(angulo):.2f}')

31. Faça uma função para calcular o número neperiano usando uma série.
    A função deve ter como parâmetro o número de termos que serão somados(note que, quanto maior o número, mais próxima
    a resposta estará do valor e.

def num_neporiano(n_termos):
    soma = 0
    for i in range(0, n_termos):
        soma = soma + 1 / (math.factorial(i))
    return soma


print('Programa para calcular um número neporiano usando uma série')
numero_termos = int(input('Digite o número de termos: '))
print(num_neporiano(numero_termos))

32. Faça uma função chamada 'simplifica' que recebe como parâmetro o numerodor e o denominador de uma fração.
    Esta função deve simplificar a fração recebida dividindo o numerador e o denominador pelo maior fator possível.
    Por exemplo, a fração 36/60 simplifica para 3/5 dividindo o numerador e denominador por 12.
    A função deve modificar as variáveis passadas como parâmetro.

def simplifica(num, den):
    continua = True
    while continua:
        menor = num
        if den < menor:
            menor = den
        for i in range(2, menor + 1):
            if num % i == 0 and den % i == 0:
                divisor_comum = i
                num = int(num / divisor_comum)
                den = int(den / divisor_comum)
            else:
                continua = False
    return f'{num}/{den}'


print('Programa para simplificar uma fração, dado numerador e denominador.')
numerador = int(input('Digite o valor do numerador: '))
denominador = int(input('Digite o valor do denominador: '))
while denominador == 0:
    print('O denominador não pode ter valor igual a 0.')
    denominador = int(input('Digite o valor do denominador: '))
print(f'Expressão simplificada: {simplifica(numerador, denominador)}')

33. Faça uma função que receba um número N e retorne a soma dos algarismos de N!.
    Ex: Se N = 4, N! = 24. Logo, a soma de seus algarismos é 2 + 4 = 6
def soma_de_algarismos(num):
    fatorial = math.factorial(num)
    if len(str(fatorial)) > 1:
        soma = 0
        for i in range(0, len(str(fatorial))):
            str_fatorial = str(fatorial)
            soma = soma + int(str_fatorial[i])
        return soma
    else:
        return fatorial


print('Programa para calcular a soma dos algarismos de um fatorial.')
numero = int(input('Digite um número: '))
print(f'A soma dos algarismos da fatorial deste número: {soma_de_algarismos(numero)}')

34. Faça uma função não recursiva que receba um número inteiro positivo ímpar N e retorne o fatorial duplo desse
    número. O fatorial duplo é definido como o produto de todos os números naturais ímpares de 1 até algum número
    natural ímpar N. Assim, o fatorial duplo de 5 é: 5!! = 1 * 3 * 5 = 15

def fatorial_duplo(num):
    fat_duplo = 1
    for i in range(1, num + 1):
        if i % 2 != 0:
            fat_duplo = fat_duplo * i
    return fat_duplo


print('Programa para calcular o fatorial duplo de um número ímpar.')
numero = int(input('Digite um número ímpar: '))
while numero % 2 == 0:
    print('O número digitado não é ímpar!')
    sleep(2)
    numero = int(input('Digite um número ímpar: '))
print(f'{numero}!! = {fatorial_duplo(numero)}')

35. Faça uma função não recursiva que receba um número inteiro positivo n e retorne o fatorial quádruplo desse número.
    O fatorial de um número n dado por (2n)!/n!

def fat_quadruplo(num):
    numerador = math.factorial(2 * num)
    denominador = math.factorial(num)
    return numerador / denominador


print('Programa para calcular o fatorial quádruplo de um número inteiro positivo.')
numero = int(input('Digite um número inteiro positivo: '))
while numero < 0:
    print('Número digitado não é positivo.')
    sleep(2)
    numero = int(input('Digite um número inteiro positivo: '))
print(f'Resultado: {fat_quadruplo(numero)}')

36. Faça uma função não recursiva que receba um número inteiro positivo N e retorne o superfatorial desse número.
    O superfatorial de um número N é definida pelo produto dos N primeiros fatoriais de N.
    Assim, o superfatorial de 4 é sf(4) = 1! * 2! * 3! * 4! = 288

def superfatorial(num):
    if num == 0:
        return math.factorial(0)
    else:
        sf = 1
        for i in range(1, num+1):
            sf = sf * math.factorial(i)
        return sf


print('Programa para calcular o superfatorial de um número positivo.')
numero = int(input('Digite um número positivo: '))
while numero < 0:
    print('Numéro digitado não é positivo!')
    numero = int(input('Digite um número positivo: '))
print(f'O superfatorial de {numero}: {superfatorial(numero)}')

37. Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o hiperfatorial(H(n)) desse número.

def hiperfatorial(num):
    hf = 1
    for i in  range(1, num + 1):
        hf = hf * math.pow(i, i)
    return hf


print('Programa para calcular o hiperfatorila de um número inteiro positivo.')
numero = int(input('Digite o valor de um número inteiro positivo: '))
while numero < 0:
    print('O número digitado não é positivo!')
    numero = int(input('Digite o valor de um número inteiro positivo: '))
print(f'H({numero}) = {hiperfatorial(numero)}')

38. Faça uma função não recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número.
    Um fatorial exponencial é um inteiro positivo n elevado à potência de n - 1, que por sua vez é elevado à potência
    de n - 2 e assim em diante.

def fatorial_exponencial(num):
    if num == 0 or num == 1:
        return 1
    fatorial = pow(2, 1)
    for i in range(3, num + 1):
        fatorial = pow(i, fatorial)
    return fatorial


print('Programa para calcular o fatorial exponencial de um número inteiro positivo.')
numero = int(input('\nDigite o valor de um número inteiro positivo: '))
while numero < 0:
    print('O número digitado não positivo!')
    numero = int(input('Digite o valor de um número inteiro positivo: '))
print(f'O fatorial exponencial de {numero}: {fatorial_exponencial(numero)}')


39. Faça uma função 'troque', que recebe duas variavéis reais de A e B e troca o valor delas.

def troca(a, b):
    aux1 = a
    aux2 = b
    return aux2, aux1


print('Programa para trocar o valor de duas variáveis, A e B ')
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
print(f'\nA = {a}, B = {b}')

a, b = troca(a, b)
print(f'\nApós a troca:')
print(f'A = {a}, B = {b}')

40. Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele possui.

def qtd_pares(lista):
    qtd_par = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            qtd_par = qtd_par + 1
    return qtd_par


print('Programa para contar quantos velores pares há em uma lista.')
lista = []
for i in range(0, 10):
    lista.append(randint(1, 30))
print('Lista gerada com valores aleatórios:'
      f'\n{lista}')

print(f'\nQuantidade de valores pares na lista: {qtd_pares(lista)}')

41. Faça uma função que receba um vetor de inteiros e retorne o maior valor.

def maior_valor(list):
    maior = list[0]
    for i in range(1, len(list)):
        if list[i] > maior:
            maior = list[i]
    return maior


print('Programa para retornar o maior valor de uma lista.')
lista = []
print('\nLista:')
for i in range(0, 10):
    lista.append(randint(1, 30))
print(lista)
print(f'\nO maior valor da lista de inteiros: {maior_valor(lista)}')

42. Faça uma função que receba um vetor de reais e retorne a média dele.

def media_real(lista):
    soma = 0
    for i in range(0, len(lista)):
        soma = soma + Decimal(lista[i])
    media = soma / len(lista)
    return media


print('Programa para calcular a média de um vetor de valores reais')
lista = []
for i in range(0, 10):
    lista.append(round(uniform(1, 30), 2))
print('\nLista de reais:')
print(lista)
print(f'\nA média do valor dessa lista: {media_real(lista):0.2f}')

43. Faça uma função que receba um vetor de inteiros e o preencha com números aleatórios sem repetição.

def numeros_aleatorios():
    return sample(range(1, 30), 10)


print('Programa que retorna uma lista de valores inteiros aleatórios sem repetição.')
print('\nLista de valores inteiros aleatórios sem repetição:')
print(f'{numeros_aleatorios()}')

44. Faça uma função que receba como parâmetro um vetor X de 30 inteiros e retorne, também por parâmetro, dois vetores
    A e B. O vetor A deve conter os elementos pares de X e o vetor B os elementos ímpares.

def pares_impares(lista):
    a = []
    b = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            a.append(lista[i])
        else:
            b.append(lista[i])
    return a, b


print('Programa para gerar dois vetores com valores pares e ímpares através de um vetor mãe.')
x = sample(range(1, 30), 10)
print('\nLista mãe:')
print(x)
lista_a, lista_b = pares_impares(x)
print('\nOs valores pares da lista mãe:')
print(lista_a)
print('\nOs valores ímpares da lista mãe:')
print(lista_b)

45. Faça uma função que calcule o desvio padrão de um vetor 'v' contendo 'n' números, onde 'm' é a média do vetor.

def desvio_padrao(lista):
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
    media = Decimal(soma) / len(lista)
    print(f'\nMedia: {media}')
    soma_quadrado = 0
    for i in range(len(lista)):
        soma_quadrado = round(soma_quadrado + pow(lista[i] - media, 2), 2)
    soma_quadrado = soma_quadrado / 3
    desvio = sqrt(soma_quadrado)
    return desvio


print('Programa para calcular o desvio padrão de um vetor.')
v = sample(range(1, 30), 10)
print(v)
print(f'\nDesvio padrão do vetor: {desvio_padrao(v):0.2f}')

46. Crie um programa contendo as seguintes funções que recebem um vetor V números reais como parâmetro:
    Impressão normal do vetor
    Impressão inversa
    Função que retorna média aritmética dos elementos do vetor

def impressao(v):
    print(v)


def impressao_reversa(v):
    print(v[::-1])


def media(v):
    soma = 0
    for i in range(len(v)):
        soma = soma + Decimal(v[i])
    m = soma / len(v)
    return m


print('Programa para retornar uma função dentre 3 de um vetor de números reais')
lista = []
conjunto = set()
for i in range(10):
    x = round(uniform(1, 20), 2)
    while x in conjunto:
        x = round(uniform(1, 20), 2)
    conjunto.add(x)
    lista.append(x)
print('\nDigite uma das opções abaixo: ')
print('1. Impressão do vetor')
print('2. Impressão reversa do vetor')
print('3. Média do vetor')
print('0. Sair')
opcao = int(input('\nOpção: '))

while opcao != 0:
    if opcao == 1:
        impressao(lista)
        print('\nDigite uma das opções abaixo: ')
        print('1. Impressão do vetor')
        print('2. Impressão reversa do vetor')
        print('3. Média do vetor')
        print('0. Sair')
        opcao = int(input('\nOpção: '))
    elif opcao == 2:
        impressao_reversa(lista)
        print('\nDigite uma das opções abaixo: ')
        print('1. Impressão do vetor')
        print('2. Impressão reversa do vetor')
        print('3. Média do vetor')
        print('0. Sair')
        opcao = int(input('\nOpção: '))
    elif opcao == 3:
        print(f'Média aritmética do vetor de numeros reais: {media(lista):0.2f}')
        print('\nDigite uma das opções abaixo: ')
        print('1. Impressão do vetor')
        print('2. Impressão reversa do vetor')
        print('3. Média do vetor')
        print('0. Sair')
        opcao = int(input('\nOpção: '))

47. Faça uma função que receba uma matriz 4 x 4 e retorne quantos valores maiores do que 10 ela possui.

def maior_que_10(m):
    m10 = []
    for lista in m:
        for elemento in lista:
            if elemento > 10:
                m10.append(elemento)
    return len(m10)


print('Programa que retorna quantos valores maiores do que 10 existem em uma matriz')
matriz = []
conjunto = set()
while len(matriz) < 4:
    lista = []
    for i in range(4):
        lista.append(randint(1, 20))
    matriz.append(lista)
print(f'\n{matriz}')
print(f'Quantidade de valores maiores que 10 na matriz: {maior_que_10(matriz)}')

48. Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão acima da diagonal
    principal.

def soma_diagsuperior(m):
    soma = 0
    j = 1
    for linha in m:
        for i in range(j, 3):
            soma = soma + linha[i]
        j = j + 1
    return soma


print('Programa para retornar a soma dos elementos que estão abaixo da diagonal principal de uma matriz 3 x 3.')
matriz = []
while len(matriz) < 3:
    lista = []
    for i in range(3):
        lista.append(randint(1, 20))
    matriz.append(lista)
print(matriz)
print(f'\nA soma dos elemetos abaixo da diagonal principal: {soma_diagsuperior(matriz)}')

49. Faça uma função que receba uma matriz de 3 x 3 elementos.
    Calcule e retorne a soma dos elementos que estão abaixo da diagonal principal.

def soma_diaginferior(m):
    soma = 0
    j = 0
    for linha in m:
        for i in range(0, j):
            soma = soma + linha[i]
        j = j + 1
    return soma


print('Programa para calcular a soma dos valores abaixo da diagonal principal de uma matriz 3 x 3')
matriz = []
while len(matriz) < 4:
    lista = []
    for i in range(4):
        lista.append(randint(1, 20))
    matriz.append(lista)
print(matriz)
print(f'\nA soma dos valores abaixo da diagonal principal: {soma_diaginferior(matriz)}')


50. Faça uma função que receba uma matriz de 3 x 3 elementos.
    Calcule e retorne a soma dos elementos que estão na diagonal principal.

def soma_diagonal(m):
    soma = 0
    i = 0
    for lista in m:
        soma = soma + lista[i]
        i = i + 1
    return soma

print('Programa que retorna a soma de elementos da diagonal de uma matriz')
matriz = []
while len(matriz) < 3:
    lista = []
    for i in range(3):
        lista.append(randint(1, 20))
    matriz.append(lista)
print('Matriz:')
print(matriz)
print(f'\nA soma dos elementos da diagonal dessa matriz: {soma_diagonal(matriz)}')

51. Faça uma função que receba uma matriz de 3 x 3 elementos.
    Calcule e retorne a soma dos elementos que estão na diagonal secundária.

def soma_diagsecundaria(m):
    soma = 0
    i = -1
    for linha in m:
       soma = soma + linha[i]
       i = i - 1
    return soma

print('Programa para calcular a soma dos elementos da diagonal secundária de uma matriz 3 x 3 ')
matriz = []
while len(matriz) < 3:
    lista = []
    for i in range(3):
        lista.append(randint(1, 20))
    matriz.append(lista)
print(matriz)
print(f'\nA soma dos elementos da diagonal secundária: {soma_diagsecundaria(matriz)}')

52. Escreva uma função que recebe uma matriz quadrada de ordem N e calcule sua transposta.

def matriz_transposta(m, ord):
    transposta = []
    while len(transposta) < ord:
        for i in range(ord):
            lista = []
            for linha in m:
                lista.append(linha[i])
            transposta.append(lista)
    return transposta


print('Programa para calcular a transposta de uma dada matriz')
matriz = []
ordem = int(input('\nDigite a ordem de uma matriz quadrada: '))
while len(matriz) < ordem:
    lista = []
    for i in range(ordem):
        lista.append(randint(1, 20))
    matriz.append(lista)
print('Matriz:')
for linha in matriz:
    print(linha)

print('\nA transposta dessa matriz:')
for linha in matriz_transposta(matriz, ordem):
    print(linha)

53. Faça uma função que verifica se uma matriz quadrada de ordem N é a matriz identidade

def matriz_identidade(m):
    contador = 0
    for linha in m:
        for elemento in linha:
            if elemento == 1 and linha.index(elemento) == contador:
                contador = contador + 1
    if contador == len(m):
        return True


print('Programa para verificar se dada matriz quadrada é a matriz identidade')
ordem = int(input('Digite a ordem da matriz quadrada: '))

matriz = []
while len(matriz) < ordem:
    lista = []
    for i in range(ordem):
        lista.append(randint(0, 1))
    matriz.append(lista)

while not matriz_identidade(matriz):
    matriz = []
    while len(matriz) < ordem:
        lista = []
        for i in range(ordem):
            lista.append(randint(0, 1))
        matriz.append(lista)
    print()
    for linha in matriz:
        print(linha)
    print('A matriz não é matriz identidade.')

print()
for linha in matriz:
    print(linha)
print('A matriz é matriz identidade.')

54. Faça uma função que recebe, por parâmetro, uma matriz A[4][4] e retorna a soma dos seus elementos.

def soma_matriz(a):
    soma = 0
    for linha in a:
        for elemento in linha:
            soma = soma + elemento
    return soma


print('Programa para calcular a soma dos elementos de uma matriz A[4][4].')
A = []
while len(A) < 4:
    lista = []
    for i in range(4):
        lista.append(randint(1, 20))
    A.append(lista)

print('\nMatriz A:')
for linha in A:
    print(linha)
print(f'\nA soma dos elementos da matriz A: {soma_matriz(A)}')

55. Faça uma função que recebe, como parâmetro, uma matriz A[3][3] e retorna a soma dos elementos da sua diagonal
    principal e da sua diagonal secundária.

def soma_diagonal(a):
    soma = 0
    i = 0
    j = -1
    for linha in a:
        soma = soma + linha[i] + linha[j]
        i = i + 1
        j = j - 1
    return soma


print('Programa que calcula a soma dos elementos da diagonal principal e secundária de uma matriz A[3][3].')
A = []
while len(A) < 3:
    lista = []
    for i in range(3):
        lista.append(randint(1, 20))
    A.append(lista)
print('\nMatriz A:')
for linha in A:
    print(linha)

print(f'A soma dos elementos da diagonal principal e secundária: {soma_diagonal(A)}')

56. Faça uma função que recebe, por parâmetro, uma matriz A[7][6] e uma linha N e retorne a soma dos elementos dessa
    linha.

def soma_linha(a, l):
    soma = 0
    l = l - 1
    for elemento in a[l]:
        soma = soma + elemento
    return soma

print('Programa que calcula a soma dos elementos de uma dada linha de uma matriz A[7][6].')
A = []
while len(A) < 7:
    lista = []
    for i in range(6):
        lista.append(randint(1, 20))
    A.append(lista)
print('\nMatriz A:')
for linha in A:
    print(linha)
linha = int(input('Digite a linha que deseja calcular a soma de seus elementos: '))

print(f'\nA soma dos elementos da linha {linha}: {soma_linha(A, linha)}')

57. Faça uma função que recebe, como parâmetro, uma matriz A[7][6] e uma coluna N e retorne a soma dos elementos dessa
    coluna.

def soma_coluna(a, col):
    soma = 0
    col = col - 1
    for linha in a:
        soma = soma + linha[col]
    return soma


print('Programa que calcula a soma dos elementos de uma dada coluna de uma matriz A[7][6].')
A = []
while len(A) < 7:
    lista = []
    for i in range(6):
        lista.append(randint(1, 20))
    A.append(lista)
print('\nMatriz A:')
for linha in A:
    print(linha)
coluna = int(input('\nDigite a coluna que deseja calcular a soma de seus elementos: '))
print(f'A soma dos elementos da coluna {coluna}: {soma_coluna(A, coluna)}')

58. Faça uma função que receba, por parâmetro, duas matrizes quadradas de ordem N, A e B, e retorna a matriz C,
    também por parâmetro, que seja o produto matricial de A e B.

def prod_matricial(a, b):
    j = 0
    c = []
    for linha in a:
        lista = []
        i = 0
        for elemento in linha:
            prod = elemento * b[i][j]
            lista.append(prod)
            i = i + 1
        c.append(lista)
        j = j + 1
    return c


print('Programa para calcular o produto matricial de duas matrizes quadradas de ordem inserida pelo usuário, A e B.')
A = []
B = []
ordem = int(input('\nDigite a ordem de ambas matrizes: '))
while len(A) < ordem and len(B) < ordem:
    lista1 = []
    lista2 = []
    for i in range(ordem):
        lista1.append(randint(1, 20))
        lista2.append(randint(1, 20))
    A.append(lista1)
    B.append(lista2)
print('\nMatriz A:')
for linha in A:
    print(linha)
print('\nMatriz B:')
for linha in B:
    print(linha)

print('\nProduto matricial entre A e B: ')
C = prod_matricial(A, B)
for linha in C:
    print(linha)

59. Faça uma função que recebe, por parâmetro, 2 vetores de 10 elementos inteiros e que calcule e retorne,
    também por parãmetro, o vetor união dos dois primeiros.

def uniao_vetores(a, b):
    c = set(a)
    c = c.union(b)
    return c


print('Programa para calcular o vetor resultante da união entre os vetores A e B.')
A = []
B = []
for i in range(10):
    A.append(randint(1, 20))
    B.append(randint(1, 20))
print('\nVetor A:')
print(A)
print('\nVetor B:')
print(B)

C = uniao_vetores(A, B)
print(f'\nA união entre esses vetores: {C}')

60. Escreva uma função que retorne a primeira posição de uma sub-string dentro de uma string.
    Caso a sub-string não seja encontrada, a função deve retornar -1.

def sub_string(s, busc):
    existe = s.find(busc)
    return existe


print('Programa para encontrar uma sub-string de uma determinada string.')
S = str(input('Digite uma string: '))
busca = str(input('Digite a substring a procurar: '))
if sub_string(S, busca):
    print(f'\nPrimeira posição da substring "{busca}": {sub_string(S, busca)}')
else:
    print('Essa substring não existe na string.')

61. Escreva uma função que compare e retorne verdadeiro, caso uma string seja anagrama da outra, e falso,
    caso contrário.

def anagrama(p1, p2):
    contador = 0
    for letra in p2:
        if letra in p1:
            contador = contador + 1
    if contador == len(p1):
        return True


print('Programa para identificar se uma dada string é anagrama de outra.')
palavra1 = str(input('\nDigite uma palavra: '))
palavra2 = str(input('Digite outra palavra: '))

if anagrama(palavra1, palavra2):
    print(f'\nA palavra {palavra2} é anagrama da palavra {palavra1}')
else:
    print(f'\nA palavra {palavra2} não é anagrama da palavra {palavra1}')

62. Crie uma função que calcula o comprimento de uma string e que possui a seguinte assinatura:
    void tamanho(char *str, int *strsize)

def tamanho(str, strsize):
    print(f"O tamanho da string '{str}': {strsize}")


print('Programa que retorna a string e seu comprimento.')
print('OBS: o programa ignora espaços em branco nas strings')
str = str(input('\nDigite uma palavra ou caractere: '))
tamanho(str, len(str))

63. Crie uma função que compara duas strings e que retorna se elas são iguais ou diferentes.

def compara_string(s1, s2):
    s1 = s1.strip()
    s2 = s2.strip()
    if s1 == s2:
        print(f"\nAs strings '{s1}' e '{s2}' são iguais.")
    else:
        print(f"\nAs strings '{s1}' e '{s2}' são diferentes.")



print('Programa que equipara duas strings.')
str1 = str(input('\nDigite a primeira palavra ou caractere: '))
str2 = str(input('Digite a segunda palavra ou caractere: '))

compara_string(str1, str2)

64. Implemente a função a qual recebe duas strings, str1 e str2, e concatena a string apontada por str2 à string
    apontada por str1.

def concatena_string(s1, s2):
    str_concatenada = str1.join(str2)
    return s2 + s1


print('Programa que concatena duas strings.')
str1 = str(input('\nDigite a primeira string: '))
str2 = str(input('Digite a segunda string:'))

print(f"\nA concatenação da string '{str2}' com '{str1}': {concatena_string(str1, str2)}")

65. Implemente a função a qual recebe duas strings, str1 e str2, e um valor inteiro positivo N.
    A função concatena não mais que N caracteres da string apontada por str2 à string apontada por str1
    e termina str1 com NULL.

def concatena_str(s1, s2, n):
   return s1 + s2[0:n]

print('Programa que concatena duas strings até um número N limite.')
str1 = str(input('\nDigite a primeira string: '))
str2 = str(input('Digite a segunda string: '))
N = int(input('Digite um número inteiro e positivo: '))
while N < 0:
    print('\nO número digitado não é positivo.')
    N = int(input('Digite um número inteiro e positivo: '))
print(concatena_str(str1, str2, N))

66. Faça uma função que dado um caractere qualquer retorne o mesmo caractere sempre em maiúsculo.

def char_maiuscula(c):
    return c.capitalize()


print('Programa que dado um caractere, ele sempre retornará em maiúsculo.')
char = str(input('Digite um caractere: '))
while not re.search(r'[a-zA-z]+?', char):
    print('\nEntrada incorreta.')
    sleep(1)
    char = str(input('Digite um caractere: '))

print(f'\nCaractere digitado: {char_maiuscula(char)}')

67. Faça uma rotina que receba como parêmetro um vetor de caracteres e seu tamanho.
    A função deverá ler uma string do teclado, caractere por caractere, usando uma função getchar() até que o usuário
    digite enter ou o tamanho máximo do vetor seja alcançado.
* NÂO CONSEGUI FAZER

68. Faça uma função que receba duas strings e retorne a intercalação letra a letra da primeira com a segunda string.
    A string intercalada deve ser retornada na primeira string.

def intercala_strings(s1, s2):
    str_inter = ''
    i = 0
    for letra in s1:
        str_inter = str_inter + letra
        if i < len(s2):
            str_inter = str_inter + s2[i]
            i = i + 1
    print(f'contador = {i}')
    while i < len(s2):
        str_inter = str_inter + s2[i]
        i = i + 1
        print(f'contador = {i}')
    return str_inter



print('Programa que intercala duas strings, letra a letra.')
str1 = str(input('\nDigite a primeira string: '))
str2 = str(input('Digite a segunda string: '))

str1 = intercala_strings(str1, str2)
print(f'\nString intercalada: {str1}')

"""

from math import *
import random
import sys
from math import pow
from random import *
from datetime import *
import locale
from decimal import *
from time import *
import re
import keyboard

