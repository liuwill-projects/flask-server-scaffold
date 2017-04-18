FROM python:2.7-alpine

MAINTAINER Will Liu, liuwill@live.com

ENV ALPINE_VERSION=3.5
# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# install ca-certificates so that HTTPS works consistently
# the other runtime dependencies for Python are installed later
RUN apk add --no-cache ca-certificates
# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

RUN apt-get update \
	&& pip install flask-cors -i https://pypi.tuna.tsinghua.edu.cn/simple \
	&& pip install Flask -i https://pypi.tuna.tsinghua.edu.cn/simple \
	&& mkdir /var/www \
	&& mkdir /usr/src/app \
	&& service ssh start

WORKDIR /usr/src/app

EXPOSE 22 80 443 5000