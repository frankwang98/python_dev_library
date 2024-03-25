#!/bin/bash

# 定义主机 IP 地址数组
declare -a hosts=("10.10.6.100" "10.10.6.110" "10.10.6.120" "10.10.6.130" 
                  "10.10.6.140" "10.10.6.150" "10.10.6.160" "10.10.6.170" "10.10.6.180")

# 循环遍历数组中的每个主机 IP 地址
for host in "${hosts[@]}"
do
    echo "Adding SSH key for ${host} to known_hosts..."
    ssh-keyscan -H "${host}" >> ~/.ssh/known_hosts # 获取 SSH 公钥
done

echo "All keys have been added."