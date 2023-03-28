"""
#1 Faça um programa que receba dois números e mostre qual deles é o maior

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número:'))

if numero1 > numero2:
    print(f'O maior número dentre os dois: {numero1}')
elif numero1 < numero2:
    print(f'O maior número dentre os dois: {numero2}')
else:
    print('Os números são idênticos')

#2 Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
#Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

numero = int(input('Digite um número positivo: '))
if numero >= 0:
    print(f'O valor da raíz quadrada do número inserido: {sqrt(numero):.2f}')
else:
    print('Número inválido')

#3 Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o numéro ao quadrado.

numero = Decimal(input('Digite um número real: '))
if numero >= 0:
    print(f'O valor da raíz quadrada desse número: {sqrt(numero):.2f}')
else:
    print(f'O valor do número inserido elevado ao quadrado: {pow(numero,2):.2f}')

#4 Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
#O número digitado ao quadrado;
#A raiz quadrada do número digitado.

numero = int(input('Digite um número positivo: '))
if numero >= 0:
    print(f'O valor do número inserido ao quadrado: {pow(numero,2):.2f}')
    print(f'O valor da raíz quadrada do número inserido: {sqrt(numero):.2f}')
else:
    print('Número inválido.')

#5 Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.

numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número inserido é par.')
else:
    print('O número inserido é ímpar.')

#6 Escreva um programa que receba um número inteiro e verifique se este número é par ou ímpar

numero = int(input('Digite um número inteiro positivo: '))
if numero >= 0:
    if numero % 2 == 0:
        print('O número inserido é inteiro e par. ')
    else:
        print('O número inserido é inteiro e ímpar.')
else:
    print('Número inválido.')

#7 Faça um programa que receba dois números e mostre o maior.
#Se por acaso os dois números forem iguais, imprima a mensagem 'Números iguais'.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 > numero2:
    print(f'O maior número dentre os dois: {numero1}')
elif numero1 < numero2:
    print(f'O maior número dentre os dois: {numero2}')
else:
    print('Os números são idênticos')

#8 Faça um programa que leia 2 notas de um aluno,
#verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente,
#um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido,
#este fato deve ser informado ao usuário e o programa termina.

getcontext().prec = 2
nota1 = Decimal(input('Digite a primeira nota do aluno: '))
nota2 = Decimal(input('Digite a segunda nota do aluno: '))
if(nota1 < 0.0 or nota1 > 10.0) or (nota2 < 0.0 or nota2 > 10.0):
    print('Nota inválida.')
else:
    print(f'Média do aluno: {(nota1 + nota2)/2:.2f}')

#9 Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20%
#do salário imprima: 'Empréstimo não concedido', caso contrário imprima: 'Empréstimo concedido'.

salario = Decimal(input('Digite o salário do funcionário: '))
emprestimo = Decimal(input('Digite o valor do empréstimo: '))
if emprestimo > salario * Decimal(0.2):
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')

#10 Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as
#seguintes fórmulas (onde h corresponde a altura):
#Homens: (72.7 * h) - 58
#Mulheres: (62.1 * h) - 44.7

altura = Decimal(input('Digite o valor da altura em metros: '))
sexo = input('Digite o seu sexo: ')
sexo  = sexo.capitalize()
homem_peso = Decimal(72.7) * altura - Decimal(58)
mulher_peso = Decimal(62.1) * altura - Decimal(44.7)
if sexo == 'Masculino':
    print(f'Seu valor de peso ideal: {homem_peso:.2f}')
elif sexo == 'Feminino':
    print(f'Seu valor de peso ideal: {mulher_peso:.2f} kg')

#11 Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus
#algarismos. Por exemplo, ao número 251 corresponderá o valor 8(2 + 5 + 1).
#Se o número lido não for maior do que zero, o programa terminará com a mensagem 'Número inválido'.

numero = input('Digite um valor inteiro e maior do que zero: ')
soma = 0
if int(numero) < 0 :
    print('Número inválido.')
else:
    for x in numero:
        soma = soma + int(x)
    print(soma)

#12 Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido".
#Se o número for positivo, calcular o logaritmo deste número.

numero = int(input('Digite um número inteiro: '))
if numero < 0:
    print ("Número inválido.")
else:
    print(f'Logaritmo desse número: {log(numero,10):.2f}')

#13 Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
#A primeira e a segunda prova tem peso 1 e a terceira tem peso 2.
#Ao final, mostrar  a média do aluno e indicar se o mesmo foi aprovado ou reprovado.
#A nota para aprovação de ser igual ou superior a 60 pontos.

nota1 = Decimal(input('Digite o valor da 1ª nota: '))
nota2 = Decimal(input('Digite o valor da 2ª nota: '))
nota3 = Decimal(input('Digite o valor da 3º nota: '))
media_ponderada = (nota1 * 1 + nota2 * 1 + nota3 * 2)/ (1 + 1 + 2)
if media_ponderada >= 60:
    print(f'Aluno(a) aprovado(a)! Média: {media_ponderada:.1f}')
else:
    print(f'Aluno(a) reprovado(a), média: {media_ponderada:.1f}')

#14 A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
#respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três provas
#mencionadas anteriormente obedece aos pesos:
#Trabalhos de laboratório: 2;
#Avaliação semestral: 3;
#Exame final: 5;
#De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9), de recuperação
#(entre 3 e 3.9) ou se foi aprovado. Faça todas as verificações necessárias.

nota_laboratorio = Decimal(input('Digite a nota das ativiadades de laboratório do(a) estudante: '))
nota_avaliação = Decimal(input('Digite a nota da avaliação semestral do(a) estudante: '))
exame_final = Decimal(input('Digite a nota do exame final do(a) estudante: '))
media_ponderada = (nota_laboratorio * 2 + nota_avaliação * 3 + exame_final * 5)/(2 + 3 + 5)
if media_ponderada >= 0 and media_ponderada <= 2.9:
    print(f'O(A) estudante está reprovado(a), média: {media_ponderada:.1f}')
elif media_ponderada >= 3 and media_ponderada <= 3.9:
    print(f'O(A) estudante está de recuperação, média: {media_ponderada:.1f}')
else:
    print(f'O(A) estudante está aprovado(a)! Média: {media_ponderada:.1f}')

#15 Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondete a este
#número.

dia_da_semana = int(input('Digite um dia da semana, que seja um número inteiro entre 1 e 7: '))

if dia_da_semana == 1:
    print('Hoje é domingo!')
elif dia_da_semana == 2:
    print('Hoje é segunda-feira!')
elif dia_da_semana == 3:
    print('Hoje é terça-feira!')
elif dia_da_semana == 4:
    print('Hoje é quarta-feira!')
elif dia_da_semana == 5:
    print('Hoje é quinta-feira!')
elif dia_da_semana == 6:
    print('Hoje é sexta-feira!')
elif dia_da_semana == 2:
    print('Hoje é sábado!')
else:
    print('Número inválido.')

#16 Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número.

mes = int(input('Digite um mês, que seja um número inteiro entre 1 e 12: '))
if mes == 1:
    print('O mês digitado é janeiro.')
elif mes == 2:
    print('O mês digitado é fevereiro.')
elif mes == 3:
    print('O mês digitado é março.')
elif mes == 4:
    print('O mês digitado é abril.')
elif mes == 5:
    print('O mês digitado é maio.')
elif mes == 6:
    print('O mês digitado é junho.')
elif mes == 7:
    print('O mês digitado é julho.')
elif mes == 8:
    print('O mês digitado é agosto.')
elif mes == 9:
    print('O mês digitado é setembro.')
elif mes == 10:
    print('O mês digitado é outubro.')
elif mes == 11:
    print('O mês digitado é novembro.')
elif mes == 12:
    print('O mês digitado é dezembro.')
else:
    print('Número inválido.')

#17 Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
# A = ((basemaior + basemenor) * altura) / 2
#Lembre-se a base maior e a base menor devem ser números maiores que zero.

base_maior = Decimal(input('Digite o valor da base maior do trapézio: '))
base_menor = Decimal(input('Digite o valor da base menor do trapézio: '))
if base_maior > 0  and base_menor > 0:
    if base_maior > base_menor:
        area = ((base_maior + base_menor)* 5 )/2
        print(f'Valor da área do trapézio: {area:.2f}')
    else:
        print('Valores inválidos.')
else:
    print('Valores inválidos.')

#18 Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
#O usuário escolhe uma das operações e o seu programa então pede dois valores númericos e realize a operação,
#mostrando o resultado saindo.

print('Digite um das opções abaixo:')
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
opcao = int(input('Opção: '))

if opcao == 1:
    numero1 = Decimal(input('Digite o primeiro valor: '))
    numero2 = Decimal(input('Digite o segundo valor:'))
    print(f'Resultado: {numero1 + numero2}')
elif opcao == 2:
    numero1 = Decimal(input('Digite o primeiro valor: '))
    numero2 = Decimal(input('Digite o segundo valor:'))
    print(f'Resultado: {numero1 - numero2}')
elif opcao == 3:
    numero1 = Decimal(input('Digite o primeiro valor: '))
    numero2 = Decimal(input('Digite o segundo valor:'))
    print(f'Resultado: {numero1 * numero2}')
elif opcao == 4:
    numero1 = Decimal(input('Digite o primeiro valor: '))
    numero2 = Decimal(input('Digite o segundo valor:'))
    print(f'Resultado: {numero1 / numero2}')

#19 Faça um programa oara verificar se um determinado número inteiro é divisìvel por 3 ou 5, mas não simultaneamente
#pelos dois.

numero = int(input('Digite um número que seja divisível por 3 ou 5, mas não pelos dois: '))
if numero % 3 == 0 and not numero % 5 == 0:
    print('Número divisível por 3')
elif numero % 5 == 0 and not numero % 3 == 0 :
    print('Número divisível por 5')
else:
    print(f'Número inválido: {numero}')

#20 Dados três valores A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um
#triângulo escaleno, equilátero ou isósceles, considerando os seguintes conceitos:
#O comprimento de cada lado de um triângulo é o menor do que a soma dos outros dois lados;
#Chama-se equilátero o triângulo que tem três lados;
#Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais;
#Recebe o nome de escaleno o triângulo que tem três lados diferentes.

ladoA = Decimal(input('Digite o valor do lado A do triângulo: '))
ladoB = Decimal(input('Digite o valor do lado B do triângulo: '))
ladoC = Decimal(input('Digite o valor do lado C do triângulo: '))

if ladoA <= ladoB + ladoC and ladoB <= ladoA + ladoC and ladoC <= ladoA + ladoB:
    triangulo = True
else:
    triangulo = False

if triangulo:
    if ladoA == ladoB and ladoB == ladoC:
        print('O triângulo equilátero.')
    elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os valores inseridos não formam um triângulo.')

#21 Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
#Escreva uma mensagem de erro se a opção for inválida.

print('Digite uma da opções abaixo:')
print('1- Soma de 2 números')
print('2- Diferença entre 2 números (maior pelo menor)')
print('3- Produto entre 2 números')
print('4- Divisão entre os 2 números (o denominador não pode ser zero)')
opcao = int(input('Opção: '))

if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    validacao = True
else:
    validacao = False

if validacao:
    if opcao == 1:
        numero1 = Decimal(input('Digite o primeiro valor: '))
        numero2 = Decimal(input('Digite o segundo valor:'))
        print(f'Resultado: {numero1 + numero2}')
    elif opcao == 2:
        numero1 = Decimal(input('Digite o primeiro valor: '))
        numero2 = Decimal(input('Digite o segundo valor:'))
        if numero1 > numero2:
            print(f'Resultado: {numero1 - numero2}')
        else:
            print(f'Resultado: {numero2 - numero1}')
    elif opcao == 3:
        numero1 = Decimal(input('Digite o primeiro valor: '))
        numero2 = Decimal(input('Digite o segundo valor:'))
        print(f'Resultado: {numero1 * numero2}')
    elif opcao == 4:
        numero1 = Decimal(input('Digite o primeiro valor: '))
        numero2 = Decimal(input('Digite o segundo valor:'))
        if numero2 == 0:
            print('Denominador igual a zero')
        else:
            print(f'Resultado: {numero1 / numero2}')
else:
    print('Opção inválida.')

#22 Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
#As condições de aposentadoria são:
#Ter pelo menos 65 anos;
#Ou ter trabalhado pelo menos 30 anos;
#Ou ter pelo menos 60 anos e trabalhado pelo menos 25

idade = int(input('Digite sua idade: '))
tempo_servico = int(input('Digite seu tempo de serviço: '))
if idade >= 65:
    ok1 = True
else:
    ok1 = False
if tempo_servico >= 30:
    ok2 = True
else:
    ok2 = False
if idade >= 60 and tempo_servico >= 25:
    ok3 = True
else:
    ok3 = False

if ok1 or ok2 or ok3:
    print('O usuário já pode se aposentar.')
else:
    print('O usuário não pode se aposentar por agora.')

#23 Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for
#divisível por 4 e não for divisíviel por 100, por exemplo: 1988, 1992, 1996.

ano = int(input('Digite o valor do ano: '))
if ano % 400 == 0 or ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano digitado é bissexto.')
    else:
        print('O ano digitado não é bissexto.')
else:
    print('O número digitado não é bissexto.')

#24 Uma empresa vende o mesmo produto pra quatro diferentes estados. Cada estado possui uma taxa diferente de imposto
#sobre o produto (MG: 7%; SP: 12%; RJ: 15%; MS: 8%). Faça um programa em que um usuário entre com o valor e o estado
#destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será
#vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.

valor = Decimal(input('Digite o valor do destino do produto: '))
print('Digite o destino do produto dentre as opções abaixo: ')
print('1- MG')
print('2- SP')
print('3- RJ')
print('4- MS')
destino = int(input('Opção: '))

if destino == 1:
    preco_final = valor + (valor * Decimal(0.07))
    print(f'O valor do produto a ser vendido: R$ {preco_final:.2f}')
    print('Destino MG')
elif destino == 2:
    preco_final = valor + (valor * Decimal(0.12))
    print(f'O valor do produto a ser vendido: R$ {preco_final:.2f}')
    print('Destino: SP')
elif destino == 3:
    preco_final = valor + (valor * Decimal(0.15))
    print(f'O valor do produto a ser vendido: R$ {preco_final:.2f}')
    print('Destino: RJ')
elif destino == 4:
    preco_final = valor + (valor * Decimal(0.08))
    print(f'O valor do produto a ser vendido: R$ {preco_final:.2f}')
    print('Destino: MS')

#25 Calcule as raízes da equação de 2º grau.

print('Programa para calcular as raízes de uma função de 2º grau.')
a = Decimal(input('Digite o valor de a: '))
b = Decimal(input('Digite o valor de b: '))
c = Decimal(input('Digite o valor de c: '))

if a != 0:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Não existe raíz para essa função.')
    elif delta == 0:
        raiz1 = (-b + delta.sqrt()) / (2 * a)
        print(f'Raiz única: x = {raiz1:.2f}')
    elif delta > 0:
        raiz1 = (-b + delta.sqrt()) / (2 * a)
        raiz2 = (-b - delta.sqrt()) / (2 * a)
        print(f'Raiz da função: x1 = {raiz1:.2f} e x2 = {raiz2:.2f}')
else:
    print('Não é um equação de segundo grau.')

#26 Leia a distância em km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
#calcule o consumo em km/l e escreva a mensagem de acordo com a tabela abaixo:

distancia = Decimal(input('Digite a distância percorrida: '))
gasolina = Decimal(input('Digite o consumo de gasolina em litros: '))
consumo = distancia / gasolina

if consumo >= 8 and consumo < 14:
    print('Carro econômico!')
elif consumo > 12:
    print('Caroo super econômico!')
else:
    print('Melhor vender o carro!')

#27 Escreva um programa que, dada a idade de nadador, classifique-o em uma das seguintes categorias:

idade = int(input('Digite sua idade: '))
print('Sua classificação de nadador:')

if idade >= 5 and idade <= 7:
    print('Infantil A.')
elif idade >= 8 and idade <= 10:
    print('Infantil B.')
elif idade >= 11 and idade <= 13:
    print('Juvenil A.')
elif idade >=14 and idade <= 17:
    print('Juvenil B.')
elif idade >= 18:
    print('Sênior.')

#28 Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes medidas de acordo
#com um valor numérico digitado pelo usuário:
#a) Geométrica
#b) Ponderada
#c)Harmônica
#d)Aritmética

print('Digite uma das operações abaixo: ')
print('a) Geométrica')
print('b) Ponderada')
print('c) Harmônica')
print('d) Aritmética')
opcao = input('Opcão: ')

if opcao == 'a':
    numero1 = Decimal(input('Digite o primeiro valor: '))
    numero2 = Decimal(input('Digite o segundo valor: '))
    numero3 = Decimal(input('Digite o terceiro valor: '))
    geometrica = numero1 * numero2 * numero3
    geometrica = geometrica.sqrt()
    print(f'Resultado: {geometrica:.2f}')
elif opcao == 'b':
    numero1 = Decimal(input('Digite o primeiro valor: '))
    numero2 = Decimal(input('Digite o segundo valor: '))
    numero3 = Decimal(input('Digite o terceiro valor: '))
    ponderada = (numero1 + 2 * numero2 + 3 * numero3)/6
    print(f'Resultado: {ponderada:.2f}')
elif opcao == 'c':
    numero1 = Decimal(input('Digite o primeiro valor: '))
    numero2 = Decimal(input('Digite o segundo valor: '))
    numero3 = Decimal(input('Digite o terceiro valor: '))
    harmonica = 1 / (1/numero1 + 1/numero2 + 1/numero3)
    print(f'Resultado: {harmonica:.2f}')
elif opcao == 'd':
    numero1 = Decimal(input('Digite o primeiro valor: '))
    numero2 = Decimal(input('Digite o segundo valor: '))
    numero3 = Decimal(input('Digite o terceiro valor: '))
    aritmetica = (numero1 + numero2 + numero3) / 3
    print(f'Resultado: {aritmetica:.2f}')
else:
    print('Opção inválida.')

#29 Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100.
#Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta:
#'qual é soma de a + b?', onde a e b são os números aleatórios. Peça a resposta.
#Faça cinco perguntas ao aluno, e mostre para eles as perguntas e respostas corretas, além de quantas vezes o aluno acertou.

a1 = randint(1,100)
b1 = randint(1,100)
ok = 0
print(f'1ª pergunta: Qual é a soma de {a1} + {b1}?')
resposta_aluno = int(input('Resposta: '))
resposta1 = a1 + b1
if resposta_aluno == resposta1:
    ok += 1

a2 = randint(1,100)
b2 = randint(1,100)
print(f'2ª pergunta: Qual é a soma de {a2} + {b2}?')
resposta_aluno = int(input('Resposta: '))
resposta2 = a2 + b2
if resposta_aluno == resposta2:
    ok += 1

a3 = randint(1,100)
b3 = randint(1,100)
print(f'3ª pergunta: Qual é a soma de {a3} + {b3}?')
resposta_aluno = int(input('Resposta: '))
resposta3 = a3 + b3
if resposta_aluno == resposta3:
    ok += 1

a4 = randint(1,100)
b4 = randint(1,100)
print(f'4ª pergunta: Qual é a soma de {a4} + {b4}?')
resposta_aluno = int(input('Resposta: '))
resposta4 = a4 + b4
if resposta_aluno == resposta4:
    ok += 1

a5 = randint(1,100)
b5 = randint(1,100)
print(f'5ª pergunta: Qual é a soma de {a5} + {b5}?')
resposta_aluno = int(input('Resposta: '))
resposta5 = a5 + b5
if resposta_aluno == resposta5:
    ok += 1

print('Resolução:')
print(f'1ª pergunta: Qual é a soma de {a1} + {b1}?')
print(f'Resposta correta: {resposta1}')
print(f'2ª pergunta: Qual é a soma de {a2} + {b2}?')
print(f'Resposta correta: {resposta2}')
print(f'3ª pergunta: Qual é a soma de {a3} + {b3}?')
print(f'Resposta correta: {resposta3}')
print(f'4ª pergunta: Qual é a soma de {a4} + {b4}?')
print(f'Resposta correta: {resposta4}')
print(f'5ª pergunta: Qual é a soma de {a5} + {b5}?')
print(f'Resposta correta: {resposta5}')
print(f'Quantas respostas o aluno(a) acertou?: {ok}')

#30 Faça um programa que receba três números e mostre-os em ordem crescente

numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))
numero3 = int(input('Digite o terceiro número inteiro: '))

if numero1 >= numero2 and numero1 >= numero3:
    if numero2 >= numero3:
        print(f'Números em ordem crescente: {numero3}, {numero2}, {numero1}')
    else:
        print(f'Números em ordem crescente: {numero2}, {numero3}, {numero1}')
elif numero2 >= numero1 and numero2 >= numero3:
    if numero1 >= numero3:
        print(f'Números em ordem crescente: {numero3}, {numero1}, {numero2}')
    else:
        print(f'Números em ordem crescente: {numero1}, {numero3}, {numero2}')
elif numero3 >= numero1 and numero3 >= numero2:
    if numero1 >= numero2:
        print(f'Números em ordem crescente: {numero2}, {numero1}, {numero3}')
    else:
        print(f'Números em ordem crescente: {numero1}, {numero2}, {numero3}')

#31 Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela,
#verifique e mostre qual classificação dessa pessoa.

altura = Decimal(input('Digite a sua altura: '))
peso = Decimal(input('Digite seu peso: '))

if altura < Decimal(1.20) and peso <= 60:
    print('Você está no grupo A.')
elif altura < Decimal(1.20) and (peso > 60 or peso <= 90):
    print('Você está no grupo D.')
elif altura < Decimal(1.20) and peso > 90:
    print('Você está no grupo G.')
elif Decimal(1.20) < altura <= Decimal(1.7) and peso <= 60:
    print('Você está no grupo B.')
elif Decimal(1.20) < altura <= Decimal(1.7) and 60 < peso <= 90:
    print('Você está no grupo E.')
elif Decimal(1.20) < altura <= Decimal(1.7) and peso > 90:
    print('Você estpa no grupo H.')
elif altura > Decimal(1.7) and peso <= 60:
    print('Você está no grupo C.')
elif altura > Decimal(1.7) and 60 < peso <= 90:
    print('Você está no grupo F.')
elif altura > Decimal(1.7) and peso > 90:
    print('Você está no grupo I.')

#32 Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
#O programa deve calcular o valor a ser pago por aquele lanche.
#Considere que a cada execução somente será calculado um pedido.
#O cardápio da lanchonete segue o padrão proposto.

codigo = int(input('Digite o código do lanche: '))
quantidade = int(input('Digite a quantidade do lanche: '))
if codigo == 100:
    custofinal = quantidade * Decimal(1.2)
    print(f'Cachorro quente x{quantidade}: R$ {custofinal:.2f}.')
elif codigo == 101:
    custofinal = quantidade * Decimal(1.3)
    print(f'Bauru simples x{quantidade}: R$ {custofinal:.2f}.')
elif codigo == 102:
    custofinal = quantidade * Decimal(1.5)
    print(f'Bauru com ovo x{quantidade}: R$ {custofinal:.2f}.')
elif codigo == 103:
    custofinal = quantidade * Decimal(1.2)
    print(f'Hamburguer x{quantidade}: R$ {custofinal:.2f}.')
elif codigo == 104:
    custofinal = quantidade * Decimal(1.7)
    print(f'Cheeseburguer x{quantidade}: R$ {custofinal:.2f}.')
elif codigo == 105:
    custofinal = quantidade * Decimal(2.2)
    print(f'Suco x{quantidade}: R$ {custofinal:.2f}.')
elif codigo == 106:
    custofinal = quantidade * 1
    print(f'Refrigerante x{quantidade}: R$ {custofinal:.2f}.')
else:
    print('Código inválido!')

#33 Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo,
#e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela.)

preco_antigo = Decimal(input('Digite o preço antigo: R$ '))
if preco_antigo <= 50:
    preco_novo = preco_antigo + (preco_antigo * Decimal(0.05))
    if preco_novo <= 80:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Barato!')
    elif 80 < preco_novo <= 120:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Normal!')
    elif 120 < preco_novo <= 200:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Caro!')
    elif preco_novo > 200:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Muito caro!')
elif 50 < preco_antigo <= 100:
    preco_novo = preco_antigo + (preco_antigo * Decimal(0.1))
    if preco_novo <= 80:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Barato!')
    elif 80 < preco_novo <= 120:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Normal!')
    elif 120 < preco_novo <= 200:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Caro!')
    elif preco_novo > 200:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Muito caro!')
elif preco_antigo > 100:
    preco_novo = preco_antigo + (preco_antigo * Decimal(0.15))
    if preco_novo <= 80:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Barato!')
    elif 80 < preco_novo <= 120:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Normal!')
    elif 120 < preco_novo <= 200:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Caro!')
    elif preco_novo > 200:
        print(f'Valor do preço novo: R$ {preco_novo:.2f}')
        print('Muito caro!')
else:
    print('Valor inválido!')

#34 Leia a nota e o número de faltas de um aluno, e escreva seu conceito.
#De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

nota = Decimal(input('Digite a nota do aluno(a): '))
if 9 <= nota <= 10:
    faltas = int(input('Digite o número de faltas do aluno(a): '))
    if faltas > 20:
        print('Conceito do aluno(a): B')
    else:
        print('Conceito do aluno(a): A')
elif Decimal(7.5) <= nota <= Decimal(8.9):
    faltas = int(input('Digite o número de faltas do aluno(a): '))
    if faltas > 20:
        print('Conceito do aluno(a): C')
    else:
        print('Conceito do aluno(a): B')
elif 5 <= nota < Decimal(7.4):
    faltas = int(input('Digite o número de faltas do aluno(a): '))
    if faltas > 20:
        print('Conceito do aluno(a): D')
    else:
        print('Conceito do aluno(a): C')
elif 4 <= nota < Decimal(4.9):
    faltas = int(input('Digite o número de faltas do aluno(a): '))
    if faltas > 20:
        print('Conceito do aluno(a): E')
    else:
        print('Conceito do aluno(a): D')
elif Decimal(0.0) <= nota <= Decimal (3.9):
    faltas = int(input('Digite o número de faltas do aluno(a): '))
    if faltas > 20:
        print('Conceito do aluno(a): E')
    else:
        print('Conceito do aluno(a): E')

#35 Leia uma data e determine se ela é válida. Ou seja,
#verifique se o mês está entre  dia 1 e 12 e se o dia existe naquele mês.
#Note que fevereiro tem 29 dias em anos bissextos e 28 dias em anos não bissextos.

ano = int(input('Digite o ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    mes = int(input('Digite o mês: '))
    if 1 <= mes <= 12:
        dia = int(input('Digite o dia: '))
        if mes == 4 and 1 < dia > 30:
            print('Data inválida.')
        elif mes == 6 and 1 < dia > 30:
            print('Data inválida.')
        elif mes == 8 and 1 < dia > 30:
            print('Data inválida.')
        elif mes == 11 and 1 < dia > 30:
            print('Data inválida.')
        elif mes == 1 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 3 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 5 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 7 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 8 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 9 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 12 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 2 and 1 < dia > 29:
            print('Data inválida.')
        else:
            print('Data válida.')
    else:
        print('Data inválida.')
else:
    mes = int(input('Digite o mês: '))
    if 1 <= mes <= 12:
        dia = int(input('Digite o dia: '))
        if mes == 4 and 1 < dia > 30:
            print('Data inválida.')
        elif mes == 6 and 1 < dia > 30:
            print('Data inválida.')
        elif mes == 8 and 1 < dia > 30:
            print('Data inválida.')
        elif mes == 11 and 1 < dia > 30:
            print('Data inválida.')
        elif mes == 1 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 3 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 5 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 7 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 8 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 9 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 12 and 1 < dia > 31:
            print('Data inválida.')
        elif mes == 2 and 1 < dia > 28:
            print('Data inválida.')
        else:
            print('Data válida.')
    else:
        print('Data inválida.')

#36 Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor.
#Para calcular a comissão, considere a tabela do problema.

venda = Decimal(input('Digite o valor da venda: R$ '))
if venda >= 100_000:
    comissao = venda * Decimal(0.16) + 700
    print(f'Valor da comissão: R$ {comissao:.2f}')
elif 80_000 <= venda < 100_000:
    comissao = venda * Decimal(0.14) + 650
    print(f'Valor da comissão: R$ {comissao:.2f}')
elif 60_000 <= venda < 80_000:
    comissao = venda * Decimal(0.14) + 650
    print(f'Valor da comissão: R$ {comissao:.2f}')
elif 40_000 <= venda < 60_000:
    comissao = venda * Decimal(0.14) + 550
    print(f'Valor da comissão: R$ {comissao:.2f}')
elif 20_000 <= venda < 40_000:
    comissao = venda * Decimal(0.14) + 500
    print(f'Valor da comissão: R$ {comissao:.2f}')
elif venda < 20_000:
    comissao = venda * Decimal(0.14) + 400
    print(f'Valor da comissão: R$ {comissao:.2f}')

#37 O número de horas a pagar é sempre inteiro e arrendondado por excesso.
#Deste modo, quem estacionar durante 61 minutos pagará por duas horas,
#que é o mesmo que pagaria se tivesse permanecido 120 minutos.
#Os momentos de chegada ao parque e partida deste são apresentados na forma de pares inteiros, representando horas e minutos.
#Por exemplo, o par 12 50 representará "dez para uma da tarde". Pretende-se criar um program que,
#lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento.
#Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas.
#Portanto, se uma dada hora de chegada for superior à de partida, isso não é uma situação de erro,
#antes significará que a partida ocorreu no dia seguinte ao da chegada.

chegada = input('Digite a hora de chegada: ')
chegada = chegada.split(' ')
hora_chegada = int(chegada[0])
hora_chegada = hora_chegada * 60
minuto_chegada = int(chegada[1])
total_chegada = hora_chegada + minuto_chegada
print(total_chegada)

saida = input('Digite a hora de saída: ')
saida = saida.split(' ')
hora_saida = int(saida[0]) * 60
minuto_saida = int(saida[1])
total_saida = hora_saida + minuto_saida
print(total_saida)

print((total_saida - total_chegada)/60)
tempo_h = ceil((total_saida - total_chegada)/60)

taxa = 0
if 1 <= tempo_h <= 2:
    taxa = 1
elif 2 < tempo_h <= 4:
    taxa = Decimal(1.4)
elif tempo_h > 4 and tempo_h >= 5:
    taxa = 2

total = taxa * tempo_h
print(f'Total a pagar: R$ {total:.2f}')

#39 Uma empresa decide dar um aumento ao seus funcionários de acordo com a tabela que considera o salário atual
#e o tempo de serviço de cada funcionário.
#Os funcionários com menor terão um aumento proporcionalmente maior que os funcionários com um salário maior,
#e conforme o tempo de serviço na empresas, cada funcionário irá receber um bônus adicional de salário.
#Faça um programa que fala:
#o valor do salário atual do funcionário;
#o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).
#Use as tabelas do problema para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado,
#ou uma mensagem caso o funcionário não tenha direito a nenhum momento.

salario_atual = Decimal(input('Digite o valor do seu salário atual: R$ '))
anos_de_ingresso = int(input('Digite o ano de ingresso na empresa: '))
bonus = 0
taxa_reajuste = 0
ano_atual = datetime.now()
anos_de_servico = ano_atual.year - anos_de_ingresso
if 1 <= anos_de_servico <= 3:
    bonus = 100
    if salario_atual <= 500:
        taxa_reajuste = Decimal(0.25)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 1000:
        taxa_reajuste = Decimal(0.20)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 1500:
        taxa_reajuste = Decimal(0.15)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 2000:
        taxa_reajuste = Decimal(0.10)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    else:
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
        print('Você não tem direito a aumento.')
elif 4 <= anos_de_servico <= 6:
    bonus = 200
    if salario_atual <= 500:
        taxa_reajuste = Decimal(0.25)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 1000:
        taxa_reajuste = Decimal(0.20)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 1500:
        taxa_reajuste = Decimal(0.15)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 2000:
        taxa_reajuste = Decimal(0.10)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    else:
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
        print('Você não tem direito a aumento.')
elif 7 <= anos_de_servico <= 10:
    bonus = 300
    if salario_atual <= 500:
        taxa_reajuste = Decimal(0.25)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 1000:
        taxa_reajuste = Decimal(0.20)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 1500:
        taxa_reajuste = Decimal(0.15)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 2000:
        taxa_reajuste = Decimal(0.10)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    else:
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
        print('Você não tem direito a aumento.')
elif anos_de_servico > 10:
    bonus = 500
    if salario_atual <= 500:
        taxa_reajuste = Decimal(0.25)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 1000:
        taxa_reajuste = Decimal(0.20)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 1500:
        taxa_reajuste = Decimal(0.15)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    elif salario_atual <= 2000:
        taxa_reajuste = Decimal(0.10)
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
    else:
        salario_reajustado = salario_atual * taxa_reajuste + salario_atual + bonus
        print(f'Seu salário reajustado é de: R$ {salario_reajustado:.2f}')
        print('Você não tem direito a aumento.')

#40 O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
#A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela do problema.
#Leia o custo de fábrica e escreva o custo ao consumidor:

custo_fabrica = Decimal(input('Digite o valor de fábrica do veículo: R$ '))
if custo_fabrica <= 12_000:
    custo_comissao = custo_fabrica * Decimal(0.05)
    custo_imposto = 0
    custo_total = custo_fabrica + custo_comissao + custo_imposto
elif 12_000 < custo_fabrica <= 25_000:
    custo_comissao = custo_fabrica * Decimal(0.10)
    custo_imposto = custo_fabrica * Decimal(0.15)
    custo_total = custo_fabrica + custo_comissao + custo_imposto
elif custo_fabrica > 25_000:
    custo_comissao = custo_fabrica * Decimal(0.15)
    custo_imposto = custo_fabrica * Decimal(0.20)
    custo_total = custo_fabrica + custo_comissao + custo_imposto
print(f'O custo total deste veículo: R$ {custo_total:.2f}')

#41 Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

imc = Decimal(input('Digite seu IMC: '))
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 < imc <= 24.9:
    print('Saudável.')
elif 24.9 < imc <= 29.9:
    print('Peso em excesso.')
elif 29.9 < imc <= 34.9:
    print('Obesidade grau I.')
elif 34.9 < imc <= 39.9:
    print('Obesidade grau II (severa).')
elif imc > 39.9:
    print('Obesidade grau III (mórbida).')
"""
import math
from decimal import *
from math import *
from random import *
from datetime import *






