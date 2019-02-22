#!/bin/bash

set -eux

trap "pkill -f rabbitmq-server -9" SIGINT SIGTERM SIGHUP

cd /var/lib/rabbitmq
export PATH=/usr/lib/rabbitmq/bin:$PATH
rabbitmq-server &

wait
