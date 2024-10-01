#Função que verifica a existencia da Letra 'A' e suas variantes, e as conta    
def verificar_e_contar(palavra):
    letras_a = ['a', 'á', 'à', 'â', 'ã']

    #Contador de letras 'A'
    cont = 0
    for letra in palavra.lower():
        if letra in letras_a:
            cont += 1

    #Mensagem apropriada para a questão
    if cont > 0:
        return f"A letra 'A' aparece {cont} vezes dentro da palavra"
    else:
        return "Não existe 'A' dentro da palavra"


#Principal - Escrever a palavra e chamar a função 
palavra = str(input("Digite uma Palavra: "))
resultado= verificar_e_contar(palavra)
print(resultado)