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

###Escolher a cor principal do jogo
   Na linha de comando de execução do jogo depois do nome do labirinto, se você adicionar ou `--color
    
    * Escolher seu personagem
    
    * Trocar cor principal do jogo
    
    * Ativar modo demonstração

    
Para obter detalhes digite python3 main.py -h
