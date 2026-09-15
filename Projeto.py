import random
import unicodedata
from os import name, system
from pathlib import Path

MAX_ERROS = 6

TEMAS = {
    1: {"nome": "Frutas", "arquivo": "listaFrutas.txt"},
    2: {"nome": "Animais", "arquivo": "listaAnimais.txt"},
    3: {"nome": "Objetos", "arquivo": "listaObjetos.txt"},
    4: {"nome": "Países", "arquivo": "listaPais.txt"},
}

FORCA = [
    r"""
       --------
       |      |
       |
       |
       |
       |
       -
    """,
    r"""
       --------
       |      |
       |      O
       |
       |
       |
       -
    """,
    r"""
       --------
       |      |
       |      O
       |      |
       |      |
       |
       -
    """,
    r"""
       --------
       |      |
       |      O
       |     \|
       |      |
       |
       -
    """,
    r"""
       --------
       |      |
       |      O
       |     \|/
       |      |
       |
       -
    """,
    r"""
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     /
       -
    """,
    r"""
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     / \
       -
    """,
]


def limpar_tela():
    """Limpa o terminal no Windows, macOS ou Linux."""
    system("cls" if name == "nt" else "clear")


def normalizar_texto(texto):
    """Remove acentos e converte o texto para minúsculas."""
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )


def escolher_tema():
    """Solicita um tema válido ao jogador."""
    print("Escolha um tema:\n")

    for numero, tema in TEMAS.items():
        print(f"{numero} - {tema['nome']}")

    while True:
        entrada = input("\nDigite o número do tema: ").strip()

        if not entrada.isdigit():
            print("Digite apenas o número da opção.")
            continue

        opcao = int(entrada)

        if opcao not in TEMAS:
            print("Escolha uma opção entre 1 e 4.")
            continue

        return opcao


def carregar_palavras(nome_arquivo):
    """Carrega a lista de palavras do arquivo selecionado."""
    caminho = Path(__file__).resolve().parent / "arquivos" / nome_arquivo

    with caminho.open("r", encoding="utf-8") as arquivo:
        palavras = [
            palavra.strip().lower()
            for palavra in arquivo.read().split(",")
            if palavra.strip()
        ]

    if not palavras:
        raise ValueError(f"Nenhuma palavra encontrada em {nome_arquivo}.")

    return palavras


def montar_palavra_oculta(palavra, letras_tentadas):
    """Monta a palavra exibida, preservando espaços e hífens."""
    exibicao = []

    for caractere in palavra:
        if not caractere.isalpha():
            exibicao.append(caractere)
        elif normalizar_texto(caractere) in letras_tentadas:
            exibicao.append(caractere)
        else:
            exibicao.append("_")

    return " ".join(exibicao)


def palavra_completa(palavra, letras_tentadas):
    """Retorna True quando todas as letras da palavra foram descobertas."""
    return all(
        not caractere.isalpha()
        or normalizar_texto(caractere) in letras_tentadas
        for caractere in palavra
    )


def solicitar_letra(letras_tentadas):
    """Solicita uma única letra ainda não utilizada."""
    while True:
        tentativa = input("\nDigite uma letra: ").strip().lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Digite apenas uma letra.")
            continue

        letra_normalizada = normalizar_texto(tentativa)

        if letra_normalizada in letras_tentadas:
            print("Você já tentou essa letra. Escolha outra.")
            continue

        return letra_normalizada


def jogar_rodada():
    """Executa uma rodada completa do jogo."""
    limpar_tela()

    print("=" * 42)
    print("           JOGO DA FORCA")
    print("=" * 42)

    opcao = escolher_tema()
    tema = TEMAS[opcao]
    palavras = carregar_palavras(tema["arquivo"])
    palavra = random.choice(palavras)

    letras_tentadas = set()
    letras_erradas = []
    erros = 0
    palavra_normalizada = normalizar_texto(palavra)

    while erros < MAX_ERROS:
        limpar_tela()

        print("=" * 42)
        print(f"JOGO DA FORCA | Tema: {tema['nome']}")
        print("=" * 42)
        print(FORCA[erros])
        print(montar_palavra_oculta(palavra, letras_tentadas))
        print(f"\nErros: {erros}/{MAX_ERROS}")
        print(
            "Letras erradas:",
            " ".join(letras_erradas) if letras_erradas else "nenhuma",
        )

        letra = solicitar_letra(letras_tentadas)
        letras_tentadas.add(letra)

        if letra not in palavra_normalizada:
            erros += 1
            letras_erradas.append(letra)

        if palavra_completa(palavra, letras_tentadas):
            limpar_tela()
            print(FORCA[erros])
            print(montar_palavra_oculta(palavra, letras_tentadas))
            print(f"\nVocê venceu! A palavra era: {palavra.upper()}")
            return

    limpar_tela()
    print(FORCA[MAX_ERROS])
    print(f"\nVocê perdeu! A palavra era: {palavra.upper()}")


def deseja_jogar_novamente():
    """Pergunta se o jogador deseja iniciar uma nova rodada."""
    while True:
        resposta = input("\nDeseja jogar novamente? [S/N]: ").strip().lower()

        if resposta in {"s", "sim"}:
            return True

        if resposta in {"n", "nao", "não"}:
            return False

        print("Digite S para sim ou N para não.")


def main():
    while True:
        jogar_rodada()

        if not deseja_jogar_novamente():
            print("\nObrigado por jogar!")
            break


if __name__ == "__main__":
    main()
