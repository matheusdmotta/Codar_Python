'''
Escreva um programa para calcular o ordenado líquido de um empregado de uma
determinada firma que é pago consoante o número de horas que trabalhou.
As Taxas são as seguintes.
IRS = 20% se salário bruto >= 1000€.
15% se salário bruto >= 600€ e < 1000€.
10% se salário bruto < 600€.
Horas Extras = acima de 35H cada Hora vale 1,5H (incluindo horas trabalhadas durante
o fim de semana).
Segurança Social = 11% sobre o salário bruto.

O programa deve pedir para digitar o seguinte:
Número do empregado.
Número de horas que o empregado trabalhou.
Valor Hora que o empregado é pago.
'''

numero_do_empregado = input("Digite o número do empregado: ")
numero_de_horas_trabalhadas = input("Digite o número de horas que o empregado trabalhou: ")
valor_hora = input("Digite o valor por hora que o empregado é pago: ")
salario_bruto = 0
if numero_do_empregado.isdigit() and numero_de_horas_trabalhadas.isdigit() and valor_hora.isdigit():
    numero_do_empregado = int(numero_do_empregado)
    numero_de_horas_trabalhadas = int(numero_de_horas_trabalhadas)
    valor_hora = float(valor_hora)

    if numero_de_horas_trabalhadas > 35:
        horas_extras = numero_de_horas_trabalhadas - 35
        salario_bruto = (35 * valor_hora) + (horas_extras * valor_hora * 1.5)
    else:
        salario_bruto = numero_de_horas_trabalhadas * valor_hora

    if salario_bruto >= 1000:
        irs = salario_bruto * 0.20
    elif salario_bruto >= 600:
        irs = salario_bruto * 0.15
    else:
        irs = salario_bruto * 0.10

    seguranca_social = salario_bruto * 0.11
    salario_liquido = salario_bruto - irs - seguranca_social

    print(f"Número do empregado: {numero_do_empregado}")
    print(f"Salário bruto: {salario_bruto:.2f}€")
    print(f"IRS: {irs:.2f}€")
    print(f"Segurança Social: {seguranca_social:.2f}€")
    print(f"Salário líquido: {salario_liquido:.2f}€")