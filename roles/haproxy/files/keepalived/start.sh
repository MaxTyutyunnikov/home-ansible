#!/bin/bash

set -ux

function term {
    kill -INT $(cat /run/keepalived.pid)
    # This should help prevent the container dieing before the vrrp thread has
    # properly removed the vip
    # https://github.com/acassen/keepalived/issues/159#issuecomment-155714115
    sleep 1
}

function hup {
    kill -HUP $(cat /run/keepalived.pid)
}

trap term SIGINT SIGTERM
trap hup SIGHUP

rm -f /run/keepalived.pid /run/vrrp.pid

/usr/sbin/keepalived -DPnl &
PID=$!

wait $PID
trap - SIGINT SIGTERM
trap - SIGHUP
wait $PID
EXIT_STATUS=$?
