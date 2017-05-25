#!/bin/bash


NAME="processarcartaofidelidade"                                               # Name of the application
DJANGODIR=/home/infog2/ProcessarCartaoFidelidade                   # Django project directory
SOCKFILE=/home/infog2/gunicorn.sock  # we will communicte using this unix socket
USER=infog2                                                     # the user to run as
GROUP=infog2                                                    # the group to run as
NUM_WORKERS=3                                                   # how many worker processes should Gunicorn spawn
DJANGO_WSGI_MODULE=wsgi                  # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/infog2/.virtualenvs/processa_cartao_fidelidade/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/infog2/.virtualenvs/processa_cartao_fidelidade/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=0.0.0.0:5050 \
  --log-level=debug \
  --log-file=-


