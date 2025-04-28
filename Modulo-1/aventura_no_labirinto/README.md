<h1 align=center> Aventura no Labirinto </h1>

Neste jogo seu objetivo é encontrar a saída do labirinto, coletando os tesouros espalhados pelo caminho e tentando fazer o mínimo de movimentos possível.

Este jogo é um trabalho prático do curso de Python Intermediário do Projeto Desenvolve de Bom Despacho, feito pelo aluno Henrique Lelles Gontijo.


## Bibliotecas Externas
   O jogo necessita de algumas bibliotecas externas para ser executado, sendo necessário baixá-las com o comando "pip". Antes de fazer isso é recomendável criar um ambiente virtual que conterá apenas as bibliotecas necessárias para fazer o jogo funcionar, a fim de evitar sejam instaladas no python globa e assim manter tudo mais organizado.

### Criando Ambiente Virtual
   Utilizando o comando `cd` no terminal navegue até a pasta raíz do projeto (aventura_no_labirinto). Para criar o ambiente digite `python -m venv "nome_do_ambiente"` caso esteja no Windows, mas se seu sitema operacional for uma distribuição Unix use o comando `python3` no lugar de apenas `python`. Lembre-se de criar o ambiente na pasta raiz do projeto para ficar mais fácil de achá-lo depois.

   Em seguida é necessário ativar o ambiente, para isso, digite `\"nome_do_ambiente"\Scripts\activate` caso esteja no Windows e `source "nome_do_ambiente"/bin/activate` para as distribuições Unix.

### Instalando Bibliotecas
   Todas as bibliotecas estão listadas, com suas respectivas versões, no arquivo "requirements.txt", então (com o ambiente virtual ativado) digite `pip -r requirements.txt` e todas elas serão instaladas automaticamente.

<hr>

## Rodando o Jogo
   O jogo possui três labirintos inicialmente, sendo eles "labirinto_pequeno", "labirinto_medio" e "labirinto_grande". Para iniciar o jogo, é preciso digitar `python main.py` + nome do labirinto escolhido. Caso esteja utilizando um sitema operacional de distribuição Unix utilize `python3` ao invés de apenas `python`.

   É importante ressaltar que o terminal deve ficar em tela cheia para evitar que a visualização fique quebrada.

## Interface de CLI
Através da interface de CLI você pode fazer algumas mudanças em relação à execução do jogo:

   #### Escolher a cor principal do jogo
   Adicionando `--color` mais o nome de uma cor em inglês, tudo isso na linha de comando para executar o jogo, é possível mudar mudar a cor principal da interface do jogo.
    
   #### Escolher cor do seu personagem
   Com `--player_color` mais o nome de umma cor em inglês é possível escolher a cor do seu personagem.

   #### Escolher personagem
   Já com `--player` mais 1 ou 3 caracteres, você pode customizar o seu personagem.

   #### Ativar modo demonstração
   Usando o comando `--demonstration` sem nenhum parâmetro, é ativado o modo demonstração, onde o computador começa a jogar o jogo sozinho. Quando iniciado, para sair do modo demonstração use o comando `Ctrl + C` ou espere a máquina percorrer todo o labirinto.
    
### Exemplos da interface CLI:
   * `python main.py labirinto_medio --color blue`
   * `python main.py labirinto_medio --player_color red`
   * `python main.py labirinto_medio --player uwu`
   * `python main.py labirinto_medio --demonstration`

No caso dos comandos que definem cores de interface e personagem, clicando <a href="https://rich.readthedocs.io/en/stable/appendix/colors.html" target="_blank"">aqui<a/> você verá uma lista de todas os nomes de cores que você pode colocar. Além dessa maneira, é possível escolher as cores através de código hexadecimal ou rgb como demonstrado a seguir: `python main.py labirinto_medio --color #ff0000 --player_color "rgb(255,215,0)"`
    
Para obter detalhes digite python3 main.py -h
