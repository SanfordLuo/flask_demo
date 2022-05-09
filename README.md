# proj-manage

&emsp;[本文说明](/README.md#本文说明)  
&emsp;[开发环境](/README.md#开发环境)  
&emsp;&emsp;[wsl2配置](/README.md#wsl2配置)  
&emsp;&emsp;[跨系统文件互传](/README.md#跨系统文件互传)  
&emsp;&emsp;[LxRunOffline管理工具](/README.md#LxRunOffline管理工具)  
&emsp;&emsp;[修改国内镜像](/README.md#修改国内镜像)  
&emsp;&emsp;[virtualenvwrapper使用](/README.md#virtualenvwrapper使用)

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

### 修改国内镜像

### virtualenvwrapper使用

### 其他命令

```
# 在wsl中进入win中d盘中的PyProj
cd /mnt/d/PyProj/

# 在win中进入wsl中的lyf用户中
cd \\wsl$\Ubuntu-20.04\home\lyf\

# win与wsl文件复制
cp -a /mnt/d/PyProject/proj-manage /home/lyf/sanford/apps/

# 查看进程
ps aux | grep python

# 查看端口占用情况
netstat -apn | grep 2378
```

### WSL2 安装配置

```
### 管理员权限下的 cmd 或 PowerShell

# 设置wsl版本为2
wsl --set-default-version 2

# 查询wsl版本
wsl -l -v
```

### supervisor管理python服务

###### 安装

```
apt-get install supervisor
```

###### 配置文件说明

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
开启多个进程(没有端口冲突的情况下)：

```开启多个进程
process_name=%(program_name)s_%(process_num)s
numprocs=4
```

###### 相关命令

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
 
