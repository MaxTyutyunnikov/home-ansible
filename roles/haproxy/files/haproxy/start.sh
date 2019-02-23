#!/bin/bash

set -eux

trap "pkill -f haproxy -9" SIGINT SIGTERM SIGHUP

setcap CAP_NET_BIND_SERVICE=+eip /usr/sbin/haproxy

haproxy -Ds -f /etc/haproxy/haproxy.cfg &

wait
