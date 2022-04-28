# flask_demo

用于测试 docker、flask、nginx、uwsgi  
开发环境：wsl

### 其他命令

win与wsl文件复制：cp -a /mnt/d/flask_demo /home/lyf/sanford/apps/  
查看进程：ps aux | grep python  
查看端口占用情况：netstat -apn | grep 2378

### supervisor管理python服务

###### 安装

```
apt-get install supervisor
```

###### 配置文件说明

```
/etc/supervisor/
├── conf.d
│   └── flask_demo_supervisor.conf
└── supervisord.conf
```

supervisord.conf：全局的主要配置，默认不需要修改什么。需要关注的：logfile=/var/log/supervisor/supervisord.log；pidfile=/var/run/supervisord.pid  
conf.d：存放子进程配置文件的一个文件夹  
flask_demo_supervisor.conf：自定义的关于这个项目的配置文件  
示例：[flask_demo_supervisor](/config/flask_demo_supervisor.conf)  
开启多个进程(没有端口冲突的情况下)：

```开启多个进程
process_name=%(program_name)s_%(process_num)s
numprocs=4
```

###### 相关命令

启动supervisor：supervisord -c /etc/supervisor/supervisord.conf  
查看所有服务：supervisorctl status  
停用：supervisorctl stop aaa  
启动：supervisorctl start aaa  
重启：supervisorctl restart aaa   
配置文件修改后重新加载：supervisorctl update  
重新启动配置中的所有程序：supervisorctl reload  
进入：supervisorctl -c /etc/supervisor/supervisord.conf  
