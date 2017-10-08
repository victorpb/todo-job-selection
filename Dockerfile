FROM ubuntu:14.04
MAINTAINER Victor Pereira <victtor.vpb@gmail.com>

RUN sudo apt-get update
RUN sudo apt-get install -y python3-pip nginx supervisor
RUN echo "alias python='python3'" >> ~/.bashrc


ADD requirements.txt ./requirements.txt
ADD . /src
RUN mkdir /logs
RUN mkdir /src/db
WORKDIR /src
ADD nginx.conf /etc/nginx/sites-enabled/
ADD nginx.conf /etc/nginx/sites-available/
ADD supervisor.conf /etc/supervisor/conf.d

RUN pip3 install -r ./requirements.txt
RUN pip3 install gunicorn
RUN rm /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default

RUN service nginx restart
EXPOSE 80
