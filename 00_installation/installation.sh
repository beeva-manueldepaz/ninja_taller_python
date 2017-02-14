#!/usr/bin/env bash

# OJO Rutas aptas para Mac/Ubuntu

# Para instalar el wrapper
sudo pip install virtualenvwrapper

# Añadir en .profile o en .bashrc esas tres líneas
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh

# Para crear un virtualenv ninja con Python3
mkvirtualenv -p /Users/manuel.depaz/.pyenv/shims/python3 ninja

# Creamos en el IDE ninja_2 con la misma config

# Actualizamos el pip
easy_install -U pip
pip --version

# Para buscar paquetes
pip search flask

# Para instalar paquetes por consola
pip install flask
pip install pytest
