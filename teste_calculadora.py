import calculadora 

def main():
    a = 2
    b = 3 
    soma = calculadora.somar(a, b)
    print(f'{a} + {b} = {soma}')
    subtracao = calculadora.subtrair(a, b)
    pirnt(f'{a} - {b} = subtracao')

main()

def subtrair(a, b):
    return a - b 