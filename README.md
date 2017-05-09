# ProcessarCartaoFidelidade
Esse projeto faz o processamento do cartão fidelidade da Rádio Táxi PI. Para tal é utilizada uma micro API que recebe requisições para pagamentos utilizando o cartão fidelidade da Rádio Táxi, persiste os dados recebidos em banco de dados utilizando o SGBD Sqlite(já integrado com o Flask), e processa um por vez os pagamentos através de um script que roda ininterruptamente.

## Iniciando
As instruções a seguir irão lhe auxiliar a continuar o desenvolvimento ou dar manutenção ao projeto.

### Pré-requisitos
#### Python
Antes de iniciar você precisa ter instalado Python 3.5 em sua máquina. Você pode fazer a instalação através do comando:
```
sudo apt-get install python-3.5
```
#### Ambiente Virtual
Para isso você deve instalar o VirtualEnvWrapper com os seguintes comandos:
```
sudo pip install virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
Em seguida crie seu ambiente virtual:
```
mkvirtualenv -p <caminho_para_python> venv_name
```
<i>Nota: para encontrar o caminho para o Python use o comando </i>``` which python3 ```.


Para ativar seu ambiente virtual(faça isso sempre que for trabalhar no projeto) digite:
```
workon venv_name
```
#### Flask
Como a micro API foi desenvolvida em Flask é essencial que você tenha esse pacote instalado. Para isso use o comando:
```
pip install flask
```
#### Dataset
Para que possa utilizar o banco de dados você deve instalar também o pacote Dataset usando o comando:
```
pip install dataset
```

## Configurando o projeto
Modifique o arquivo ```config.py``` para que os campos de URLs, TIMEOUT e caminho para criação e busca dos arquivos sejam corretamente preenchidos.

## Executando
Para executar você deve:
* Ativar seu ambiente virtual com o comando:
```
workon <nome_do_ambiente_virtual>
```
* Iniciar o servidor Flask:
```
python3 app.py
```
* Iniciar o processador de pagamentos:
```
python3 processa_fila_pagamentos.py
```

## GO TO CODE! :)
Created by: J. Patrício
