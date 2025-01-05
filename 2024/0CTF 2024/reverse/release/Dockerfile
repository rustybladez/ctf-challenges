from ubuntu:24.04

RUN apt-get update && apt-get install -y -q \
        python3 \
        socat \
        binutils \
        libc6-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /chal
COPY service.py /chal/
COPY secret.py /chal/
COPY run.sh /chal/
COPY not_linker /chal/
COPY a.o /chal/
COPY b.o /chal/
COPY Scrt1.o /usr/lib/Scrt1.o

WORKDIR /chal

CMD ["/chal/run.sh"]
