# Desafio - Jogo de Xadrez em Console

## 📝 Descrição

Este projeto é uma implementação completa de um jogo de Xadrez para ser jogado entre dois jogadores no terminal (console). O objetivo foi desenvolver toda a lógica do xadrez, incluindo a movimentação de todas as peças, capturas, e a verificação de condições de xeque e xeque-mate.

Este repositório foi criado para cumprir os requisitos do desafio da disciplina, focando na clareza do código, na estruturação da lógica e na documentação do projeto.

## 🏗️ Estrutura do Projeto

* **`xadrez.py`**: Arquivo único contendo toda a lógica do jogo. Isso inclui:
    * A representação do tabuleiro.
    * As regras de movimento para cada uma das peças (Peão, Torre, Cavalo, Bispo, Rainha, Rei).
    * A validação de jogadas.
    * O controle de turnos.
    * A detecção de xeque e xeque-mate.
* **`README.md`**: Esta documentação, que explica o projeto e como executá-lo.

## ⚙️ Como Executar o Jogo

1.  Certifique-se de ter o **Python 3** instalado em seu computador.
2.  Faça o download do arquivo `xadrez.py`.
3.  Abra um terminal (ou Prompt de Comando no Windows) na pasta onde você salvou o arquivo.
4.  Execute o seguinte comando para iniciar o jogo:
    ```bash
    python xadrez.py
    ```

## 룰 Como Jogar

* O jogo é para dois jogadores no mesmo computador.
* As jogadas devem ser inseridas no formato de **notação de coordenadas**, indicando a casa de origem e a casa de destino.
* Exemplos de jogadas válidas: `e2e4`, `g1f3`, `a7a5`.
* O jogo irá anunciar de quem é a vez (Brancas ou Pretas) e se um dos reis está em xeque.
* O jogo termina e anuncia o vencedor quando um jogador aplica um xeque-mate no adversário.
