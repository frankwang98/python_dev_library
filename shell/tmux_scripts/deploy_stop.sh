#!/bin/bash

# 定义远程服务器的用户名和地址
declare -a servers=(
    "nvidia@10.10.6.100"
    "nvidia@10.10.6.110"
    "nvidia@10.10.6.120"
    "nvidia@10.10.6.130"
    "nvidia@10.10.6.140"
    "nvidia@10.10.6.150"
    "nvidia@10.10.6.160"
    "nvidia@10.10.6.170"
    "nvidia@10.10.6.180"
)

# declare -a servers=(
#     "ubuntu@10.10.8.56"
# )

declare -a password="nvidia"
# declare -a password="wangzf" # 对应服务器的密码

# 本地 ZIP 文件路径
remote_file="sensor_roadside_info_router"

# 循环遍历所有服务器
for server in "${servers[@]}"
do
    echo "Processing ${server}..."

    # 连接到服务器，使用 tmux 创建新会话进行操作
    sshpass -p "${password}" ssh -t "${server}" bash -c "'
        cd ${remote_file}
        bash remote_stop.sh
    '"
    echo "Completed processing ${server}"
done

echo "All done."
