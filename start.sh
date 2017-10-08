#!/bin/bash
# Diretorio e arquivo de log
# set -e
# LOGFILE=/logs/gunicorn.log
# LOGDIR=$(dirname $LOGFILE)
# # Numero de processo simultaneo, modifique de acordo com seu processador
# NUM_WORKERS=3
# # Usuario/Grupo que vai rodar o gunicorn
# #GROUP=root
# # Endereço local que o gunicorn irá rodar
# ADDRESS=127.0.0.1:8000
# Ativando ambiente virtual e executando o gunicorn para este projeto
# source /home/myusr/envs/myproject/bin/activate
cd /src/
# test -d $LOGDIR || mkdir -p $LOGDIR
# exec gunicorn -w $NUM_WORKERS --bind=$ADDRESS  --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE sthima.wsgi:application
gunicorn -b 127.0.0.1:8000 -w 4 --log-level=info --pid=gunicorn-pid.txt sthima.wsgi:application