# Microblog
Este é o trabalho final da disciplina de Python II. Consiste em basicamente um protótipo de rede social construído com Flask.

## Instruções para testar o projeto
Antes de testar o site são necessárias algumas ações:

### Preparando ambiente
* No terminal utilize o comando `cd` para acessar a pata raiz do projeto (Trabalho Final);
* Crie um ambiente virtual com o comando `python venv "nome_do_ambiente"`, caso esteja no Windows, mas caso esteja utilizando um Sistema Operacional derivado de Unix (Linux, por exemplo) utilize `python3 venv "nome_do_ambiente`;
* Ative o ambiente virtual com `\"nome_do_ambiente"\Scripts\activate` caso esteja no Windows ou `source "nome_do_ambiente"/bin/activate` se estiver em Linux. Caso deseje desativar o ambiente digite  `deactivate`;
* Instale as bibliotecas utilizadas no projeto com o comando `pip install -r requirements.txt`;

### key.json
Para o projeto funcionar você deve criar o arquivo key.json, o qual deve conter uma chave de acesso que será utilizada pelo Flask para fins de segurança. O conteúdo do arquivo deve seguir o padrão abaixo, mas você pode substituir _pd12345678_ por sua própria chave secreta:

`
{
    "secret_key" : "pd12345678"
}
`

## Executando o projeto
Após ter terminado os passos anteriores, ainda na pasta raiz do projeto, digite `flask run microblog` e o terminal irá exibir o link da página em que o site estiver funcionando.

Caso deseje encurtar o comando, crie o arquivo .flaskenv e nele escreva `FLASK_APP=microblog.py`. Desse modo será necessário apenas digitar `flask run`.