"""
Projeto para calcular notas PUCPR com PESOS.
"""

# inputs

print("*** INSIRA OS PESOS DAS NOTAS SEM '%' ***")
peso_AE1 = float(input('Insira o peso da AE1: '))  # Ex: 10% = 10
peso_AE2 = float(input('Insira o peso da AE2: '))
peso_ATP = float(input('Insira o peso da ATP: '))  # Ex: 40% = 40
peso_ARP = float(input('Insira o peso da ARP: '))

conferencia = peso_AE1 + peso_AE2 + peso_ATP + peso_ARP

if conferencia != 100:
    print('*** PESOS ERRADOS VEREFIQUE OS VALORES')
    input('Pressione enter para continuar...')
else:
    print('*** PESOS VALIDADOS OK !!!!')
    print("\n*** INSIRA AS NOTAS COM PONTO '.' NÃO USE VIRGULA.")
    nota_AE1 = float(input('Insira a NOTA da AE1: '))  # Ex: nota 9,5 = 9.5
    nota_AE2 = float(input('Insira a NOTA da AE2: '))
    nota_ATP = float(input('Insira a NOTA da ATP: '))
    nota_ARP = float(input('Insira a NOTA da ARP: '))

    # calculo

    ae1 = peso_AE1*nota_AE1
    ae2 = peso_AE2*nota_AE2
    atp = peso_ATP*nota_ATP
    arp = peso_ARP*nota_ARP

    media = (ae1+ae2+atp+arp) / 100

    print('Sua media é:', media)
    if media >= 7:
        print('PARABENS VOCE PASSOU >:)')
        input('Pressione enter para continuar...')
    else:
        print('VOCE NÃO PASSOU >:(.')
        input('Pressione enter para continuar...')
