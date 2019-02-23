FROM ubuntu:18.04

SHELL ["/bin/bash", "-c"]

RUN set -eux; \
    apt-get update; \
    apt-get install --no-install-recommends -y haproxy; \
    rm -rf /var/lib/apt/lists/* /etc/haproxy/*

COPY start.sh /
COPY haproxy.cfg /etc/haproxy

RUN chmod +x /start.sh

CMD /start.sh
