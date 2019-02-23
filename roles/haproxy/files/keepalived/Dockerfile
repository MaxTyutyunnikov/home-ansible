FROM ubuntu:18.04

SHELL ["/bin/bash", "-c"]

RUN set -eux; \
    apt-get update; \
    apt-get install --no-install-recommends -y keepalived; \
    rm -rf /var/lib/apt/lists/* /etc/keepalived/*

COPY start.sh /
COPY keepalived.conf /etc/keepalived/

RUN chmod +x /start.sh

CMD /start.sh
