echo "欢迎使用此Linux脚本 此脚本是由一个Linux小白所写 许多内容很不完善 还请大家给些建议 写的不好多多见谅 提建议请加:109896498"
source(){
changesource(){
read -r -p "1)Debian_bullseye
2)Debian_buster
3)Ubuntu-ports
4)退出
请选择：" input
case $input in
1) echo 'deb http://mirrors.ustc.edu.cn/debian/ bullseye main contrib non-free
deb http://mirrors.ustc.edu.cn/debian/ bullseye-updates main contrib non-free
deb http://mirrors.ustc.edu.cn/debian/ bullseye-backports main contrib non-free
#deb http://mirrors.ustc.edu.cn/debian-security/ bullseye/updates main contrib non-free
deb http://mirrors.ustc.edu.cn/debian-security bullseye-security main contrib non-free' >/etc/apt/sources.list
apt update && apt upgrade ;;
2)echo 'deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free' >> sources.list
apt update && apt upgrade;;
3)echo 'deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-security main restricted universe multiverse' >> sources.list
apt update && apt upgrade ;;
4) exit ;;
esac
}
read -r -p "1)更新源(Update source)
2)换源(Change source)
3)退出(exit)
请选择：" input
case $input in
1) apt update && apt upgrade ;;
2)changesource ;;
3) exit;;
esac
}
read -r -p "1)源功能(Source function)
2)查询系统 and Qemu版本
3)安装Qemu(此版本为官网最新版本(6.1) )
4)编译Qemu
请选择：" input
case $input in
1)echo "请稍等(Please wait a moment)"
 source;;
 2)neofetch && qemu-system-i386 --version
 source;;
 3)apt install qemu-system-*
 source;;
 4)echo "敬请期待下次更新"
esac