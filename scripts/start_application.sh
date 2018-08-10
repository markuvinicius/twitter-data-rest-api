#!/usr/bin/env bash
echo 'Definindo variáveis'

## HOME DA APLICAÇÃO
export DIR=/Users/Marku/Documents/WorkSpace/twitter-data-rest-api
export APP=$DIR/app.py

## HOME DO VIRTUALENV COM AS DEPENDENCIAS INSTALADAS
export VENV_DIR=$DIR/venv/bin


#source no virtualenv
echo 'Activating virtualenv'
source $VENV_DIR/activate

export FLASK_APP=$APP
export FLASK_ENV=development

python -m flask run

echo 'Data Collected sucessfully'
echo 'deactivating virtualenv'
deactivate;
