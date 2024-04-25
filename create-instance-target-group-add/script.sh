#!/bin/bash

ip_address=$(hostname -I | awk '{print $1}')
echo "IP Address: $ip_address"
old_ip_address=$(grep 'network.host:' /etc/elasticsearch/elasticsearch.yml | tail -n1 | awk '{ print $2}')
echo "OLD IP : $old_ip_address"
#sed 's/*\.*\.*\.*/"$newip"/g' log.txt > logmod.txt
sudo sed -i "s/${old_ip_address}/${ip_address}/g" /etc/elasticsearch/elasticsearch.yml
echo "Config Updated ====> DONE"
sudo systemctl restart elasticsearch.service
echo "elasticsearch Restared ====> DONE"
