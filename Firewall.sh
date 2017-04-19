#!/bin/bash
ebtables -A FORWARD -p IPv4 -i wlan0 --ip-dst 69.25.139.140 --ip-proto tcp --ip-dport 80 -j ACCEPT;
ebtables -A FORWARD -p IPv4 -i wlan0 --ip-dst 52.88.120.190 --ip-proto tcp --ip-dport 443 -j ACCEPT;
ebtables -A FORWARD -p IPv4 -i wlan0 --ip-dst 52.27.236.3 --ip-proto tcp --ip-dport 443 -j ACCEPT;
ebtables -A FORWARD -p IPv4 -i wlan0 --ip-dst 54.218.99.79 --ip-proto tcp --ip-dport 443 -j ACCEPT;
ebtables -A FORWARD -p IPv4 -i wlan0 --ip-proto tcp -j DROP;