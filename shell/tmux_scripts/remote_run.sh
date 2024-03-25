session="router"

window1="info_router"
window2="log_monitor"
window3="ros_bag"

if ! tmux list-sessions | grep -q $session; then
    tmux new-session -d -t router
fi

# info_router
if ! tmux list-windows -t $session | grep -q $window1; then
    # 如果窗口不存在，则创建新窗口
    echo "Create new window: $window1"
    tmux new-window -t $session -n $window1
    tmux send-keys -t router:$window1 "source devel/setup.bash" C-m
    tmux send-keys -t router:$window1 "rosrun n_info_router n_info_router _local_port:=8881 _local_id:=1001 _local_heart_port:=8891 truck_1" C-m
else
    echo "Window '$window1' already exists in session '$session'"
    tmux send-keys -t router:$window1 "source devel/setup.bash" C-m
    tmux send-keys -t router:$window1 "rosrun n_info_router n_info_router _local_port:=8881 _local_id:=1001 _local_heart_port:=8891 truck_1" C-m
fi

# log_monitor
if ! tmux list-windows -t $session | grep -q $window2; then
    # 如果窗口不存在，则创建新窗口
    echo "Create new window: $window2"
    tmux new-window -t $session -n $window2
    tmux send-keys -t router:$window2 "python3 log_monitor.py" C-m
else
    echo "Window '$window2' already exists in session '$session'"
    tmux send-keys -t router:$window2 "python3 log_monitor.py" C-m
fi

# ros_bag
# if ! tmux list-windows -t $session | grep -q $window3; then
#    # 如果窗口不存在，则创建新窗口
#    tmux new-window -t $session -n $window3
#    tmux send-keys -t router:$window3 "rosbag play -l roadside.bag" C-m
# else
#    echo "Window '$window3' already exists in session '$session'"
#    tmux send-keys -t router:$window3 "rosbag play -l roadside.bag" C-m
# fi
