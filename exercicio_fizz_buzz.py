# Exercicio FizzBuzz

print(10*"#", " Iniciando Exercicio FizzBuzz ", 10*"#")


n = 1
qntd = (int(input('Digite a quantidade de numeros para verificar: ')))

for i in range(1, n + qntd):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print(10*"#", f" Finalizado ({qntd}) ", 10*"#")
