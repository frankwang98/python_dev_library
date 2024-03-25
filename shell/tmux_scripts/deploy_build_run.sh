#!/bin/bash

# 定义远程服务器的用户名和地址
declare -a servers=(
    # "nvidia@10.10.6.100 A0"
    # "nvidia@10.10.6.110 A1"
    "nvidia@10.10.6.120 A2"
    # "nvidia@10.10.6.130 A3"
    # "nvidia@10.10.6.140 A4"
    "nvidia@10.10.6.150 A5"
    # "nvidia@10.10.6.160 A6"
    "nvidia@10.10.6.170 A7"
    # "nvidia@10.10.6.180 A8"
    # "ubuntu@10.10.8.56 A9"
)

declare -a password="nvidia" # 对应服务器的密码
# declare -a password="wangzf" # test

# 本地 ZIP 文件路径
remote_file="sensor_roadside_info_router"
local_zip_file="sensor_roadside_info_router.zip"
local_file_path="${HOME}/sensor_roadside_info_router"
cd $local_file_path

# 远程目录路径
remote_dir="~/"
# remote_dir="~"

# 循环遍历所有服务器
for server in "${servers[@]}"
do
    end=${#server}
    start=`expr index "$server" A`
    start=`expr $start - 1`
    substring=${server:start:end}
    echo $substring
    sed -i "s/ A./ $substring/g" src/config/n_info_router.ini
    
    end=`expr $start - 1`
    zip -rq $local_zip_file *.py *.sh src/ -x "deploy*"
    # 将文件传输到远程服务器
    sshpass -p "${password}" scp "${local_zip_file}" "${server:0:end}:${remote_dir}"

    # 连接到服务器，使用 tmux 创建新会话进行操作
    sshpass -p "${password}" ssh -t "${server:0:end}" bash -c "'
        # 解压文件
        unzip -oq ${local_zip_file} -d ${remote_file}
        rm $local_zip_file

        cd ${remote_file}
        source /opt/ros/noetic/setup.sh
        bash build.sh
        bash remote_stop.sh
        bash remote_run.sh
        sleep 3
        rm -r src/nodes
    '"
    echo "Completed processing ${server:0:end}"
done

rm $local_zip_file
echo "All done."
