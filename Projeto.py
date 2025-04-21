#projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

#import
import random
from os import system, name

#Função para limpar a tela a cada execução

def limpa_tela():
    
    #Windows
    if name == 'nt':
        _= system('cls')

    # Mac ou Linux
    else:
        _= system('clear')  

def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

#Função
def game():
    
    limpa_tela()
    print("\nBem-Vindo(a) ao jogo da forca!")
    temaJogo = ['Frutas','Animais','Objetos','Pais']
    while True:
        try:
            opcao= int(input("Escolha um tema para o jogo: \n 1 - Frutas \n 2 - Animais \n 3 - Objetos \n 4 - Pais \n"))
            if opcao not in [1, 2, 3, 4]:
                print("Escolha um número entre 1 e 4!")
                continue
        except:
            print ("Você não digitou um número!")
            continue
        else:
            print ("\nTema Ecolhido: ",temaJogo[opcao - 1])
            print("Adivinhe a palavra abaixo:\n")
            break

    # Lista de palavras para o jogo
    nomeLista = ['listaFrutas.txt','listaAnimais.txt','listaObjetos.txt','listaPais.txt']
    arquivo_selecionado = nomeLista[opcao - 1]  # Subtrai 1 para pegar o índice correto da lista

    with open(f'arquivos/{arquivo_selecionado}', 'r', encoding='utf8', newline = '\r\n') as arquivo:
        conteudo = arquivo.read().replace(' ', '').split(',')
        palavras = [palavra.lower() for palavra in conteudo]

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Letras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior do que zero
    while chances > 0:

        #print
        print(display_hangman(chances))
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:"," ".join(letras_erradas))

        #Tentativa
        while(True):
            tentativa = input("\nDigite uma letra: ").lower()
            if tentativa.isalpha() and len(tentativa) == 1:
                break  # Sai do loop de validação
            else:
                print("Por favor, digite apenas uma única letra.")


        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -=1
            letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break

    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:",palavra)

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")