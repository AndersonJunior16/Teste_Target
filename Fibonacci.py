def gerar_fibonacci(num):
    fibonacci = [0,1]   

    while fibonacci[-1] < num:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)

    return fibonacci

def verificar(num):
    fibonacci = gerar_fibonacci(num)
    if num in fibonacci:
        return f"O número {num} pertence a Fibonacci!"
    else:
        return f"O número {num} não pertence a Fibonacci!"


num = int(input("Digite um valor para vermos se pertence e a Fibonacci: "))
resultado = verificar(num)
print(resultado)