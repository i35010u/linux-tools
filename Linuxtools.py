import os
print("欢迎使用此Linux脚本(目前仅支持Debian系发行版) 此脚本是由一个Linux小白所写 许多内容很不完善 还请大家给些建议 写的不好多多见谅 提建议请加:109896498")
def change_sources(发行版):
    if(发行版=="1"|发行版=="2"|发行版=="3"):
        os.system("sudo mkdir /etc/apt/backup")
        os.system("sudo mv /etc/apt/sources.list /etc/apt/backup/sources.list")
        a=open("/etc/apt/sources/list","w")
    else:
        return
    if(发行版=="1"):
        print('''deb http://mirrors.ustc.edu.cn/debian/ bullseye main contrib non-free
deb http://mirrors.ustc.edu.cn/debian/ bullseye-updates main contrib non-free
deb http://mirrors.ustc.edu.cn/debian/ bullseye-backports main contrib non-free
#deb http://mirrors.ustc.edu.cn/debian-security/ bullseye/updates main contrib non-free
deb http://mirrors.ustc.edu.cn/debian-security bullseye-security main contrib non-free''',file=a)
        a.close()
        os.system("sudo apt update && apt upgrade -y")
    if(发行版=="2"):
        print('''deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free''',file=a)
        a.close()
        os.system("sudo apt update && apt upgrade -y")
    if(发行版=="3"):
        print('''deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ focal-security main restricted universe multiverse''',file=a)
        os.system("sudo apt update && apt upgrade -y")
b=input('''
1)更新源以及软件包
2)更换清华源
3)退出
请输入编号:
''')
if(b=="1"):
    os.system("apt update && apt upgrade -y")
if(b=="2"):
    发行版=input('''
请输入您的发行版:
1)Debian_bullseye
2)Debian_buster
3)Ubuntu-ports
4)退出
请输入编号:
''')
    change_sources(发行版)
if(b=="3"):
    del()
