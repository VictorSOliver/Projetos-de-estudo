"""
#1 Faça um programa que leia um inteiro e o imprima

numero = int(input('Digite um valor: '))
print(numero)

#2 Faça um programa que leia um número real e o imprima

numero = float(input('Digite um valor: '))
print(numero)

#3 Peça um usúario para digitar três valores inteiros e imprima a soma deles

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
numero3 = int(input('Digite o terceiro valor: '))
soma = numero1 + numero2 + numero3
print(f'A soma dos três valores: {soma}')

#4 Leia um numero real e imprima o quadrado desse número

numero = float(input('Digite um valor: '))
numeroquadrado = numero ** 2
print(f'O quadrado do valor é: {numeroquadrado}')

#5 Leia um número real e imprima a 5 parte deste número

numero = float(input('Digite um valor: '))
numero = numero/5
print(f'O valor da quinta parte desse número: {numero}')

#6 Leia um temperatura em Celcius e apresente-a convertida em graus Fahrenheit.
A fórmula para conversão é F = C*(9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celcius.

temperatura = float(input('Digite a temperatura: '))
conversaoF = float(temperatura * (9.0/5.0) + 32.0)
print(f"A conversão da temperatura de {temperatura}C para Fahrenheit: {conversaoF}F")

#7 Leia um temperatura em graus Fahrenheit e apresente-a convertida em graus Celcius.
#A fórmula de conversão é: C = 5.0 * (F - 32.0)/9.0, sendo C a temperatura em Celcius
#e F a temperatura em Fahrenheit.

temperatura = float(input('Digite o valor da temperatura: '))
conversaoC = float(5 * (temperatura - 32)/9)
print(f"A conversão do temperatura de {temperatura}F para Celcius: {conversaoC}C")

#8 Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celcius.
#A fórmula para conversão é C = K - 273.15, sendo C a temperatura em graus Celcius
#e K a temperatura em Kelvin

temperatura = float(input('Digite o valor da temperatura: '))
conversaoC = float(temperatura - 273.15)
print(f'A conversão da temperatura de {temperatura}K para Celcius: {conversaoC}C')

#9 Leia uma temperatura em gruas Celcius e apresente-a convertida em graus Kelvin.
#A fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celcius
#e K a temperatura em Kelvin.

temperatura = float(input('Digite o valor da temperatura: '))
conversaoK = float(temperatura + 273.15)
print(f'A conversão da temperatura de {temperatura}C para Kelvin: {conversaoK}')

#10 Leia uma velocidade em km/h e apresente-a convertida em m/s.
#A fórmula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.

velocidade_km = float(input('Digite o valor da velocidade em km/h: '))
velocidade_m = float(velocidade_km/3.6)
print(f'A conversão da velocidade de {velocidade_km}km/h para m/s: {velocidade_m}m/s')

#11 Leia uma velocidade em m/s e apresente-a convertida em km/h.
#A fórmula da conversão é: K = M * 3.6, sendo K a velocidade em km/h e M a velocidade em m/s.

velocidade_m = Decimal(input('Digite o valor da velocidade em m/s: '))
velocidade_km = velocidade_m * Decimal(3.6)
print(f'A conversão da velocidade de {velocidade_m}m para km/h: {velocidade_km}km')

#12 Leia uma distância em milhas e apresente-a convertida em quilômetros.
#A fórmula  de conversão é: K = 1.61 * M, sendo K a distância em quilômetros e M a distância em milhas.

distancia_milhas = Decimal(input('Digite o valor da distãncia em milhas: '))
distancia_k = distancia_milhas * Decimal(1.61)
print(f'A conversão da distância de {distancia_milhas}M para km: {distancia_k}km')

#13 Leia uma distância em quilômetros e apresente-a convertida em milhas.
#A fórmula de conversão e: M = K/1.61 sendo K a distância em quilômetros e M em milhas.

distancia_km = Decimal(input('Digite o valor da distância em km:'))
distancia_milhas = distancia_km/Decimal(1.61)
print(f'A conversão da distãncia de {distancia_km}km para milhas: {distancia_milhas}M')

#14 Leia um ângulo em graus e apresente-o em radianos.
#A fórmula de conversão é: R = G * pi/180, sendo G o ãngulo em graus e R o ângulo em radianos
#e pi = 3.14

angulo_graus = Decimal(input('Digite o valor do ângulo em graus: '))
angulo_radiano = angulo_graus * Decimal(3.14)/180
print(f'A conversão do ângulo de {angulo_graus} graus para radianos: {angulo_radiano} radianos')

#15 Leia um ângulo em radianos e apresente-o em graus.
#A fórmula de conversão é: G = R * 180/pi, sendo o ângulo em graus e R o ângulo em radianos e pi = 3.14

angulo_radianos = Decimal(input('Digite o valor do ângulo em radianos: '))
angulo_graus = angulo_radianos * 180/Decimal(3.14)
print(f'A conversão do ângulo de {angulo_radianos} radianos para graus: {angulo_graus} graus')

#16 Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
#A fórmula de conversão é: C = P * 2.54, Sendo C o comprimento em centímetros e P o comprimento em polegadas.

comprimento_polegadas = Decimal(input('Digite o valor do comprimento em polegadas: '))
comprimento_cent = comprimento_polegadas * Decimal(2.54)
print(f'A conversão do comprimento de {comprimento_polegadas} polegadas para cm: {comprimento_cent} cm')

#17 Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas
#A fórmula de comversão é: P = C / 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.

comprimento_cm = Decimal(input('Digite o valor do comprimento em centímetros: '))
comprimento_polegadas = comprimento_cm / Decimal(2.54)
print(f'A conversão do comprimento de {comprimento_cm} centímetros para polegadas: {comprimento_polegadas} polegadas')

#18 Leia um valor de volume em metros cúbicos e apresente-o convertido em litros.
#A fórmula de conversão é L = 1000 * M, sendo L o volume em litros e M o volume em metros cúbicos.

volume_m3 = Decimal(input('Digite o valor do volume em metros cúbicos: '))
volume_l = 1000 * volume_m3
print(f'A conversão do volume de {volume_m3} metros cúbicos para litros: {volume_l}l')

#19 Leia um valor de volume em litros e apresente-o convertido em metros cúbicos.
#A fórmula de conversão é M = L / 1000, sendo M o volume em metros cúbicos e L o volume em litros.

volume_l = Decimal(input('Digite o valor do volume em litros: '))
volume_m3 = volume_l / 1000
print(f'A conversão do volume de {volume_l}l para metros cúbicos: {volume_m3} metros cúbicos')

#20 Leia um valor de massa em quilogramas e apresente-o convertido em libras.
#A fórmula  de conversão é: L = K / 0.45, sendo K a massa em quilogramas e L a massa em libras.

massa_kg = Decimal(input('Digite o valor da massa em kg: '))
massa_libras = massa_kg / Decimal(0.45)
print(f'A conversão da massa de {massa_kg}kg para libras: {massa_libras}lb')

#21 Leia um valor de massa em libras e apresente-o convertido em quilogramas.
#A fórmula  de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.

massa_lb = Decimal(input('Digite o valor da massa em libras: '))
massa_kg = massa_lb * Decimal(0.45)
print(f'A conversão da massa de {massa_lb}lb para libras: {massa_kg}kg')

#22 Leia um valor de comprimento em jardas e apresente-o convertido em metros.
#A fórmula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.

comprimento_j = Decimal(input('Digite o valor do comprimento em jardas: '))
comprimento_m = Decimal(0.91) * comprimento_j
print(f'A conversão do comprimento de {comprimento_j} jardas para metros: {comprimento_m}m')

#23 Leia um valor de comprimento em metros e apresente-o convertido em jardas.
#A fórmula de conversão é: J = M / 0.91, sendo J o comprimento em jardas e M o comprimento em metros.

comprimento_m = Decimal(input('Digite o valor do comprimento em metros: '))
comprimento_j = comprimento_m / Decimal(0.91)
print(f'A conversão do comprimento de {comprimento_m}m para jardas: {comprimento_j} jardas')

#24 Leia um valor de área em metros quadrados e apresente-o convertido em acres.
#A fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A a área em acres

area_m2 = Decimal(input('Digite o valor da área em metros quadrados: '))
area_acres = area_m2 * Decimal(0.000242)
print(f'A conversão do comprimento de {area_m2}m² para acres: {area_acres} acres')

#28 Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos

valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
valor3 = int(input('Digite o 3º valor: '))
soma_dos_quadrados = valor1 ** 2 + valor2 ** 2 + valor3 ** 2
print(f'A soma do quadrado dos três valores: {soma_dos_quadrados}')

#29 Leia 4 notas, calcule a média aritmética e imprima o resultado

nota1 = Decimal(input('Digite a 1ª nota: '))
nota2 = Decimal(input('Digite a 2ª nota: '))
nota3 = Decimal(input('Digite a 3ª nota: '))
nota4 = Decimal(input('Digite a 4ª nota: '))
media_artm = (nota1 + nota2 + nota3 + nota4)/4
print(f'Média aritmética dos 4 valores inseridos: {media_artm}')

#30 Leia um valor em real e a contação do dólar. Em seguida, imprima o valor correspondente em dólares.

getcontext().prec = 3
real = Decimal(input('Digite um valor em reais: '))
dolar = Decimal(input('Digite a cotação atual do dólar: '))
conversao_dolar = real / dolar
print(f'O valor de R${real} em dólares: {conversao_dolar}$')

#31 Leia um número inteiro e imprima o seu antecessor e o seu sucessor

numero = int(input('Digite um valor: '))
print(f'Próximo valor: {numero + 1}')
print(f'Valor antecessor: {numero -1}')


#32 Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro

numero = int(input('Digite um valor: '))
sucessor = numero + 1
antecessor = numero - 1
print(f'O valor da soma de seu sucessor: {numero + sucessor}')
print(f'O valor da soma de seu : {numero + antecessor}')

#33 Leia o tamanho do lado de um quadrado e imprima como resultado sua área

lado = Decimal(input('Digite o valor do lado do quadrado : '))
area = lado ** 2
print(f'O valor da área deste quadrado: {area}')

#34 Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
#A área do círculo é pi * raio², considere pi = 3.141592.

raio = Decimal(input('Digite o valor do raio do círculo: '))
area = pi * pow(raio, 2)
print(f'O valor da área deste círculo: {area:.2f}')

#35 Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raiz quadrada(a²+b²).
#Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação.
#Imprima o resultado dessa operação

cateto_a = Decimal(input('Digite o valor do cateto a do triângulo: '))
cateto_b = Decimal(input('Digite o valor do cateto b do triângulo: '))
hipotenusa = hypot(cateto_a,cateto_b)
print(f'O valor da hipotenusa deste triângulo: {hipotenusa}')

#36 Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
#O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = pi * raio² * altura,
#onde pi = 3.141592.

altura = Decimal(input('Digite o valor da altura do cilindro: '))
raio = Decimal(input('Digite o valor do raio do cilindro: '))
area = 2 * (Decimal(pi) * Decimal(pow(raio, 2))) + 2 * (Decimal(pi) * raio * altura)
print(f'O valor da área deste cilindro: {area:.2f}')

#37 Faça um programa que leia o valor de um produto e imprima o valor com desconto,
#tendo em vista que o desconto foi de 12%.

preco = Decimal(input('Digite o valor da compra: '))
desconto = Decimal(0.12)
preco_final = preco - (preco * desconto)
print(f'O valor final com desconto foi de: R${preco_final:.2f}')

#38 Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de
#25%

salario = Decimal(input('Digite o valor do salário: '))
aumento = Decimal(0.25)
salario_final = salario + (salario * aumento)
print(f'O valor do salário apos o aumento é de: R${salario_final}')

#39 A importãncia de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
#Sendo que a da quantia total:
#O primeiro ganhador receberá 46%
#O segundo receberá 32%
#o terceiro receberá o restante
#Calcule e imprima a quantia ganha por cada um dos ganhadores.

ganhador1 = Decimal(780000) * Decimal(0.46)
ganhador2 = Decimal(780000) * Decimal(0.32)
ganhador3 = Decimal(780000) - (ganhador1 + ganhador2)
print(f'Valor ganho pelo primeiro ganhador: R$ {ganhador1:.2f}')
print(f'Valor ganho pelo segundo ganhador: R$ {ganhador2:.2f}')
print(f'Valor ganho pelo terceiro ganhador: R$ {ganhador3:.2f}')

#40 Uma empresa contrata um encanador a R$ 30,00 por dia.
#Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
#paga, sabendo-se que são descontados 8% para imposto de renda.
dias_trabalhados = Decimal(input(('Digite o número de dias trabalhados pelo encanador: ')))
salario = dias_trabalhados * Decimal(30)
taxa_ir = Decimal(0.08)
salario_liquido = salario - (salario * taxa_ir)
print(f'Salário líquido a ser pago: R$ {salario_liquido:.2f}')

#41 Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
#Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.

valor_hora = Decimal(input('Digite o valor/hora: '))
horas_trabalhadas = Decimal(input('Digite o número de horas trabalhadas: '))
salario = valor_hora * horas_trabalhadas
salario_final = salario + (salario * Decimal(0.1))
print(f'Salário a ser pago: R$ {salario_final:.2f}')

#42 Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário
#tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.

salario_base = Decimal(input('Digite o valor do salário base: '))
salario_liquido = salario_base + (salario_base * Decimal(0.05)) - (salario_base * Decimal(0.07))
print(f'O valor líquido a receber será de: R$ {salario_liquido:.2f}')

#43 Escreva um programa de ajufa para vendedores. A partir de um valor total lido, mostre:
#o total a pagar com desconto de 10%;
#o valor de cada parcela, no parcelamento de 3x sem juros;
#a comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto);
#a comissão do vendedor, no caso da venda ser parcelada(5% sobre o valor total).

total_compra = Decimal(input('Digite o valor da compra: '))
valorAvista = total_compra - (total_compra * Decimal(0.1))
comissaoAvista = valorAvista * Decimal(0.05)
comissaoAprazo = total_compra * Decimal(0.05)
print(f'Valor a vista: R$ {valorAvista:.2f}')
print(f'Valor de cada parcela 3x: R${(total_compra / 3):.2f}')
print(f'Comissão a receber, caso a vista: R$ {comissaoAvista:.2f}')
print(f'Comissão a receber, caso a prazo: R$ {comissaoAprazo:.2f}')

#44 Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
#Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.

altura_degrau = Decimal(input('Digite a altura do degrau, em cm, desejada: '))
altura_desejada = Decimal(input('Digite a altura, em m, que deseja alcançar: '))
numero_degraus = int((altura_desejada * 100) / altura_degrau)
print(f'Número de degraus para alcançar uma altura de {altura_desejada:.2f}m: {numero_degraus}')

#45 Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema.

letra = input('Digite uma letra maiúscula: ')
print(f'Conversão da letra inserida para minúscula: {chr(ord(letra) + 32)}')

#46 Faça um programa que leia um número inteiro positivo de três digitos (de 100 a 99).
#Gere outro número formado pelos dígitos invertidos do número lido.

numero = int(input('Digite um valor inteiro: '))
numero_s = str(numero)
print(numero_s[::-1])

#47 Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

numero = int(input('Digite um número de 4 algarismos: '))
numero_s = str(numero)
print(f'{numero_s[0]}')
print(f'{numero_s[1]}')
print(f'{numero_s[2]}')
print(f'{numero_s[3]}')

#48 Leia um valor inteiro em segunodos, e imprima-o em horas, minutos e segundos.

numero_segundos = int(input('Digite um valor de tempo em segundos: '))
print(str(timedelta(seconds = numero_segundos)))

#49 Faça um programa para ler um horário(hora, minuto e segundo) de iniício e a duração, em segundos,
#de uma experiência biológica. O programa deve resultar com o novo horário(hora, minuto e segundo) do término da mesma.

tempo_hora = int(input('Digite o valor da hora do experimento: '))
tempo_minuto = int(input('Digite o valor da minuto experimento: '))
tempo_segundo = int(input('Digite o valor da segundo experimento: '))
tempo_inicio = timedelta(hours=tempo_hora, minutes=tempo_minuto, seconds=tempo_segundo)
tempo_termino = int(input('Digite o tempo de término do experimento em segundos: '))
tempo_termino = timedelta(seconds=tempo_termino)
print(f'Previsão de término do experimento: {str(tempo_inicio + tempo_termino)}')

#50 Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.

idade = int(input('Digite o sua idade: '))
data_atual = datetime.now()
print(f'Seu ano de nascimento é: {data_atual.year - idade}')

#51 Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0,0).

x = Decimal(input('Digite o valor da coordenada x: '))
y = Decimal(input('Digite o valor da coordenada y: '))
pitagoras = sqrt(pow(x,2) + pow(y,2))
print(f'A distância da origem: {pitagoras}')

#52 Faça um programa para ler as dimensões de um terreno(comprimento c e largura l),
#bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.

comprimento = Decimal(input('Digite o valor do comprimento do terreno em metros: '))
largura = Decimal(input('Digite o valor da largura do terreno em metros: '))
preco_tela = Decimal(input('Digite o preço da tela por metro: '))
totalApagar = (preco_tela * largura) * (comprimento * preco_tela)
print(f'Preço a pagar pelo tela: R${totalApagar:.2f}')
"""
from decimal import *
from math import *
from datetime import *

