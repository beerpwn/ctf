FROM ubuntu:xenial
WORKDIR /
RUN apt-get update && \
  apt-get -y install wget socat
RUN wget https://github.com/beerpwn/ctf/blob/master/2019/UTCTF_ctf/pwn/jendys/pwnable?raw=true -O pwnable
RUN wget https://raw.githubusercontent.com/beerpwn/ctf/master/2019/UTCTF_ctf/pwn/jendys/socat.sh
RUN chmod +x socat.sh pwnable
RUN ./socat.sh
EXPOSE 2323
