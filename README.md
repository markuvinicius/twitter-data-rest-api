# Twitter Data REST Api
Restfull API feita em python para consumo dos dados do twitter coletados no projeto Twitter Data.

## Features
Oferece um grupo de endpoints para consumo dos dados ingeridos na base NoSql Cassandra pelo projeto Twitter Data.

## EndPoints
- **host:500/tags** Retorna uma estrutura de dados em formato json contendo a lista de tags coletadas pelo projeto, separadas e quantificadas por idioma 
- **host:500/tags/<string:idioma>** Retorna uma estrutura de dados em formato json contendo a lista quantificada de tags coletadas pelo projeto, referente ao idioma informado (pt, en, es, fr, ...)
- **host:500/users/<string:data>** Retorna uma estrutura de dados em formato json contendo lista dos 5 usuários com maior número de seguidores para a data informada.

## Set-Up
### Python
Esta aplicação foi construída/testada utilizando a versão 2.7 do Python.<br>
<a href=https://www.python.org/download/releases/2.7/>Instalação Python 2.7 </a>

### PyPi
A execução desta aplicação requer a instalação de pacotes e bibliotecas específicas. Recomenda-se o uso do `virtualenv` para segregar um ambiente virtual para execução e o pacote `pip` para a instalação dos pacotes.<br>
Mais informações sobre a instalação do `virtualenv` estão aqui <a href=https://virtualenv.pypa.io/en/stable/installation/>aqui</a>

- **Instalação com `virtualenv`-** Execute os seguintes comandos no terminal:<br>
    - `virtualenv --python=Python2.7 $VENV_DIR/venv` <br>
    Este comando criará um novo ambiente virtual Python chamado **venv** no diretório **$VENV_DIR**
    - `source $VENV_DIR/venv/bin/activate` <br>
    Este comando apontará o bash para o arquivo activate do ambiente virtual e carregará as bibliotecas necessárias para o ambiente.
    - `pip install -r $APP_DIR/requirements.txt` <br>
    Este comando instalará todas as dependências necessárias para a execução do projeto

## Execução
Para facilitar a execução do projeto, é fornecido um script shell na em `scripts/start_application.sh`. <br>
A execução deverá ocorrer na porta padrão do Flask (host:5000)