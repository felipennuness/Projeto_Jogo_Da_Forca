# Jogo da Forca em Python

Projeto de estudo desenvolvido em **Python** com execução pelo terminal. O jogo permite escolher um tema, sorteia uma palavra aleatória a partir de arquivos de texto e acompanha as tentativas do jogador até a vitória ou o limite de erros.

## Funcionalidades

- escolha entre quatro temas: **Frutas, Animais, Objetos e Países**;
- palavras carregadas de arquivos externos;
- seleção aleatória da palavra;
- desenho progressivo da forca no terminal;
- validação para aceitar apenas uma letra por tentativa;
- bloqueio de letras repetidas;
- comparação de letras sem exigir acentuação na digitação;
- preservação de espaços e hífens em palavras compostas;
- exibição das letras erradas e do total de erros;
- opção de iniciar uma nova rodada sem reiniciar o programa.

## Tecnologias e conceitos praticados

- Python 3
- funções
- estruturas condicionais e loops
- listas, conjuntos e dicionários
- leitura de arquivos
- tratamento e normalização de strings
- `pathlib`
- seleção aleatória com `random`
- organização do fluxo principal com `main()`

## Como executar

É necessário ter o **Python 3** instalado.

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/felipennuness/Projeto_Jogo_Da_Forca.git
cd Projeto_Jogo_Da_Forca
```

Execute:

```bash
python Projeto.py
```

Em alguns ambientes, o comando pode ser:

```bash
python3 Projeto.py
```

## Estrutura

```text
Projeto_Jogo_Da_Forca/
├── Projeto.py
├── pseudocodigo.txt
├── README.md
└── arquivos/
    ├── listaAnimais.txt
    ├── listaFrutas.txt
    ├── listaObjetos.txt
    └── listaPais.txt
```

## Regras do jogo

O jogador possui até **6 erros** para descobrir a palavra. A cada erro, uma nova parte do desenho da forca é exibida.

Letras com acento podem ser descobertas digitando a versão sem acento. Por exemplo, ao digitar `a`, o jogo também reconhece `á`, `ã` e `â` na palavra sorteada.

Espaços e caracteres como hífen são exibidos automaticamente e não precisam ser adivinhados.

## Objetivo do projeto

Este projeto foi criado como exercício prático de programação em Python, com foco em lógica de programação, modularização, manipulação de strings, arquivos e interação com o usuário pelo terminal.
