# proj-manage

&emsp;[本文说明](/README.md#本文说明)  
&emsp;[开发环境](/README.md#开发环境)  
&emsp;&emsp;&emsp;[wsl2配置](/README.md#wsl2配置)  
&emsp;&emsp;&emsp;[跨系统文件互传](/README.md#跨系统文件互传)  
&emsp;&emsp;&emsp;[LxRunOffline管理工具](/README.md#LxRunOffline管理工具)  
&emsp;&emsp;&emsp;[修改国内镜像](/README.md#修改国内镜像)  
&emsp;&emsp;&emsp;[virtualenvwrapper使用](/README.md#virtualenvwrapper使用)  
&emsp;[项目管理](/README.md#项目管理)  
&emsp;&emsp;&emsp;[相关命令](/README.md#相关命令)  
&emsp;&emsp;&emsp;[一般启动](/README.md#一般启动)  
&emsp;&emsp;&emsp;[supervisor使用](/README.md#supervisor使用)  
&emsp;&emsp;&emsp;[uwsgi使用](/README.md#uwsgi使用)  
&emsp;&emsp;&emsp;[nginx使用](/README.md#nginx使用)  
&emsp;&emsp;&emsp;[docker使用](/README.md#docker使用)

## 本文说明

项目管理相关  
开发语言：python  
开发环境：WSL2  
相关涉及：docker、supervisor、nginx、uwsgi

## 开发环境

### wsl2配置

wsl 是 win 自带的 Ubuntu 系统，各种安装教程随便搜到处都是。  
而 wsl2 相较于 wsl1 来说最大的一个区别就是 wsl2 有完整的 Linux 内核，wsl2 不再是文件夹形式存在于 win 盘中，而是会生成一个 ext4.vhdx 硬盘文件。  
我这里用 wsl2 最大的一个作用就是想直接用 docker，下面会说，还有一个优点是 win 与 wsl 文件互传更方便。

```
### 管理员权限下的 cmd 或 PowerShell
 
# 设置wsl版本为2
wsl --set-default-version 2
 
# 查询wsl版本
wsl -l -v
```

![image](/static/wsl2-v.png)

![image](/static/ext4-vhdx.png)

### 跨系统文件互传

相关命令行，知道下面两个命令就可以灵活的跨系统文件互传了。

```
# 在wsl中进入win中d盘中的PyProj
cd /mnt/d/PyProj/
 
# 在win中进入wsl中的lyf用户中
cd \\wsl$\Ubuntu-20.04\home\lyf\
```

另外 win 系统上的 ide 也可直接编辑wsl中的文件，简直太方便了。  
![image](/static/ide-open-ubuntu.png)

### LxRunOffline管理工具

用这东西主要是想把wsl安装的地址迁移一下，wsl默认是安装在c盘的。  
官方下载地址: [LxRunOffline](https://github.com/DDoSolitary/LxRunOffline/releases)  
直接下载 xxx-msvc.zip 格式就行。安装，然后加入系统环境变量。比如我的是 D:\AppData\LxRunOffline-v3.5.0-msvc

```
### LxRunOffline 常用命令
 
# 查看wsl版本
LxRunOffline list
 
# 移动（比如我的移动到指定位置 D:\Ubuntu）
LxRunOffline move -n Ubuntu-20.04 -d D:\Ubuntu
 
# 查看wsl的安装路径
LxRunOffline di -n Ubuntu-20.04
```

### 修改国内镜像

本文以国内清华源为主。清华源官网: [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)  
常用的镜像：ubuntu，pypi，docker-ce

Ubuntu-20.04镜像: [Ubuntu 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)  
选择适合的版本，按照使用说明操作就行。我这里是Ubuntu-20.04的  
![image](/static/tsinghua-ubuntu.png)

PyPi镜像: [PyPi镜像说明](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

```
# 命令行配置PyPi镜像
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
 
# 执行完成后会在用户目录下生成相应的pip配置文件
.config/
└── pip
    └── pip.conf
```

### virtualenvwrapper使用

virtualenvwrapper用于管理python的虚拟环境。

安装:

```
pip install virtualenv
pip install virtualenvwrapper
```

配置，在.bashrc文件里添加下面三行：vim .bashrc

```
# 安装的python路径，可用 `which python3` 查看
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
 
# 创建的虚拟环境存放的路径
export WORKON_HOME=$HOME/sanford/venv
 
#  用于激活virtualenvwrapper工具
source /usr/local/bin/virtualenvwrapper.sh
```

加载修改后的配置

```
source ~/.bashrc
```

相关命令:

```
# 指定py版本创建虚拟环境
mkvirtualenv -p python3 py3
 
# 查看所有虚拟环境
lsvirtualenv
 
# 进入虚拟环境
workon py3
 
# 退出虚拟环境
deactivate
 
# 删除虚拟环境
rmvirtualenv py3 
```

## 项目管理

### 相关命令

```
# 查看端口占用情况
netstat -apn | grep 2378

# 查看进程
ps aux | grep python

# 杀死进程
kill -9 pid
```

### 一般启动

执行main.py文件，或者将启动命令放入sh文件

```
/home/lyf/sanford/venv/py3/bin/python /home/lyf/sanford/apps/proj-manage/main.py
```

![image](/static/run-main.png)

### supervisor使用

安装：

```
apt-get install supervisor
```

配置文件说明：

```
/etc/supervisor/
├── conf.d
│   └── proj_manage_supvr.conf
└── supervisord.conf
```

supervisord.conf：全局的主要配置，默认不需要修改什么。需要关注的：logfile=/var/log/supervisor/supervisord.log；pidfile=/var/run/supervisord.pid  
conf.d：存放子进程配置文件的一个文件夹  
proj_manage_supvr.conf：自定义的关于这个项目的配置文件  
示例：[proj_manage_supvr](/config/proj_manage_supvr.conf)

开启多个进程，子进程配置文件添加下面两行配置(注意端口冲突)：

```开启多个进程
process_name=%(program_name)s_%(process_num)s
numprocs=4
```

相关命令：

```
# 启动supervisor
supervisord -c /etc/supervisor/supervisord.conf

# 查看所有服务
supervisorctl status

# 停用
supervisorctl stop aaa

# 启动
supervisorctl start aaa

# 重启
supervisorctl restart aaa

# 配置文件修改后重新加载
supervisorctl update

# 重新启动配置中的所有程序
supervisorctl reload

# 进入
supervisorctl -c /etc/supervisor/supervisord.conf
```

![image](/static/run-supervisorctl.png)

```
[2022-05-10 11:08:11,801] [INFO] [main.py:13] [77777] ===info===
[2022-05-10 11:08:11,801] [ERROR] [main.py:14] [77777] ===err===
[2022-05-10 11:08:11,801] [INFO] [_internal.py:224] [] 172.20.96.1 - - [10/May/2022 11:08:11] "GET /sanford HTTP/1.1" 200 -
```

### uwsgi使用

### nginx使用

### docker使用
