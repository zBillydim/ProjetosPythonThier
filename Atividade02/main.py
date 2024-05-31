import random

def escolher_palavra(lista_palavras):
    return random.choice(lista_palavras)
def exibir_forca(tentativas, palavra, letras_corretas):
    print("Jogo da Forca")
    print("Tema: Desenvolvimento de Software Python")
    print(f"Tentativas restantes: {tentativas}")
    palavra_mostrada = ''.join([letra if letra in letras_corretas else '_' for letra in palavra])
    print(f"Palavra: {palavra_mostrada}")
    return input("Digite uma letra: ").lower()
def jogo_da_forca():
    lista_palavras = ["desenvolvimento", "programação", "algoritmo", "software", "inteligência artificial", "machine learning", "python", "código", "computador", "internet"]
    palavra_aleatoria = escolher_palavra(lista_palavras)
    tentativas = 6
    letras_corretas = set()
    menu = True
    while menu:
        letra = exibir_forca(tentativas, palavra_aleatoria, letras_corretas)
        if len(letra) != 1:
            print("Por favor, digite apenas uma letra.")
            continue
        if letra in palavra_aleatoria:
            letras_corretas.add(letra)
            if set(palavra_aleatoria) == letras_corretas:
                print("Parabéns! Você acertou a palavra.")
                opcao = input("Deseja jogar novamente? (s/n): ").lower()
                if opcao == 's':
                    jogo_da_forca()
                else:
                    print("Obrigado por jogar!")
                    menu = False           
        else:
            tentativas -= 1
    if tentativas == 0:
        print("Você perdeu! A palavra era:", palavra_aleatoria)
        opcao = input("Deseja jogar novamente? (s/n): ").lower()
        if opcao == 's':
            jogo_da_forca()
        else:
            print("Obrigado por jogar!")
            menu = False
jogo_da_forca()
