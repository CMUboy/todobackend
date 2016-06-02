FROM jmenga/todobackend-base:latest
MAINTAINER Justin Menga <justin.menga@gmail.com>

copy target /wheelhouse

RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse
