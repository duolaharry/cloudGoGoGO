# 实验启动方法

[TOC]

## 特别说明

本小组的code分为两种模式运行

long模式：做两个平台间的对比分析

short模式：做单个平台内的自身分析

本小组的ppt演示是通过exe进行，工程文件（14-直播相关数据.fs)是由Focusky进行编辑。

进入exe后，与ppt一样，按方向键的→与↓翻到下一页，←和↑翻到上一页。点击鼠标也能进行切换，但在视频播放页面鼠标点击屏幕是控制视频的播放与暂停的。因此建议使用方向键进行ppt播放控制。同时把鼠标移到屏幕最下方会有一些播放的控制面板细节。最后按ESC可以退出全屏播放。有任何问题欢迎随时联系组长，组长的邮箱是1041219412@qq.com，同时组长也有李传艺老师的微信。当然，有问题也可以百度或者谷歌。

## 项目结构

code
├── compute_part
│   ├── echo.sh
│   ├── longOutput.txt
│   ├── long_time_streaming.py
│   ├── shortOutput.txt
│   └── short_time_streaming.py
├── crawler_part
│   ├── douyu_crawler.py
│   ├── huya_crawler.py
│   ├── Long
│   │   ├── douyu
│   │   │   ├── people.txt
│   │   │   └── popular.txt
│   │   └── huya
│   │       ├── people.txt
│   │       └── popular.txt
│   ├── short
│   │   ├── people.txt
│   │   └── popular.txt
│   ├── uploadlong.sh
│   └── upload.sh
└── graph_part
    ├── long
    │   ├── bar1.js
    │   ├── bar.js
    │   ├── index.html
    │   ├── line1.js
    │   ├── line2.js
    │   ├── line.js
    │   ├── pie1.js
    │   ├── pie.js
    │   ├── render.js
    │   ├── test.sh
    │   ├── test.txt
    │   └── zingchart.min.js
    └── short
        ├── index.html
        ├── line1.js
        ├── line2.js
        ├── line.js
        ├── render.js
        ├── stack1.js
        ├── stack2.js
        ├── stack.js
        ├── test.sh
        ├── test.txt
        └── zingchart.min.js



## 提前准备

### 按照集群搭建手册进行连接

hadoop集群：（处于hadoop集群的机器没有系统要求）

wcy-pc namenode/datanode 192.168.0.118

jyx2-pc datanode 192.168.0.116

zqz-pc datanode 192.168.0.108

spark集群：（处于spark集群的机器必须统一使用Linux，且默认按照集群搭建手册使用python3.8）

wcy-pc master/worker 192.168.0.118

jyx-pc worker 192.168.0.104

zqz-pc worker  192.168.0.108

实际配置时需要修改相关配置。例如在/etc/hosts文件下加入对应的hostname与ip

### 安装和使用websocketd工具

由于使用golang编写，开发者预构建时已经打包所有依赖，该项目不需要额外的编译等构建工作，只需在项目release页下载对应平台的预构建压缩包（解压`.zip`文件可能需要`unzip`工具），在本地解压后将可执行文件拷贝到`/bin`或`/usr/bin`中即可。

要使用websocketd工具非常简单，其可以抓取任何标准输出，并以换行符`\n`为分界标志发送一行信息为WebSocket信息。

使用方法为：

```shell
websocketd --port=10080 ./script.sh
```

指定参数和会进行标准输出的可执行文件即可，每当建立一个WebSocket连接，websocketd都会执行指定的可执行文件，并将其标准输出作为WebSocket信息发送。欲了解更多信息，请查看websocketd的官方文档。

执行命令之后，终端不能被关闭，否则会停止程序的运行。

要在后台运行，可以使用`nohup`。

**如果不熟悉Linux Shell的操作的话，你可以参考：**

```shell
nohup websockted --port=10080 ./script.sh &
```

当然，我们也可以进程作为一个服务来使用。

**如果你不熟悉systemd的使用，也可以参考如下：**

```shell
[Unit]
Description=websocketd Daemon

[Service]
Type=simple
ExecStart=/bin/websockted --port=80 /path_of_scripts/script.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

若不熟悉systemd的使用，这个文本应该被命名为`websocketd.service`，并放置在`/lib/systemd/system/`路径或`/usr/lib/systemd/system/`路径下。

* `systemctl start websocketd`：启动服务。

* `systemctl stop websocketd`：停止服务。

* `systemctl restart websocketd`：重启服务。

* `systemctl enable websocketd`：使得服务开机自启动（随着字符界面）。

若不熟悉systemd的使用，请注意`.service`文件中只能使用绝对路径。

### 下载ZingChart库

只需下载ZingChart提供的`.js`文件即可（地址：https://cdn.zingchart.com/zingchart.min.js）。

在项目代码中，已经包含了此JavaScript文件，不需要额外下载。

### 安装和使用NGINX

由于本项目只使用了NGINX的内建功能和内建模块功能（只使用了Core Functionality，ngx_http_core_module，ngx_http_gzip_module，ngx_http_proxy_module），故而只需要使用包管理器安装，而不需要特意编译安装（如果想知道怎么编译安装NGINX可以参考NGINX官方文档，或者使用谷歌）：

```shell
sudo apt-get -y install nginx
```

或

```shell
sudo yum -y install nginx
```

如果你使用包管理安装，可以直接使用systemd操控NGINX服务。

如果你使用编译安装的方式安装的NGINX，你可以使用方法操作NGINX（假设你已经在系统PATH中加入NGINX安装路径中的sbin路径，或已经在系统PATH中创建了NGINX可执行文件的软链接）：

* `nginx`：启动NGINX。

* `nginx -s reload`：重加载配置文件。

* `nginx -s stop`：停止NGINX的运行（在正确关闭所有连接之后）。

关于NGINX其他命令，请参照NGINX官方文档（https://nginx.org/en/docs/）。

当然了，采用编译安装的你也可以使用systemd控制NGINX：

创建`nginx.service`如下（假设你设置的安装路径为`/usr/local/nginx/`）：

```shell
[Unit]
Description=NGINX Daemon
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
ExecStart=/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
ExecReload=/usr/local/nginx/sbin/nginx -s reload
ExecStop=/usr/local/nginx/sbin/nginx -s stop

[Install]
WantedBy=multi-user.target
```

* `systemctl start nginx`：启动NGINX。
* `systemctl stop nginx`：停止NGINX。
* `systemctl restart nginx`：重启NGINX。
* `systemctl reload nginx`：重新加载配置文件。
* `systemctl enable nginx`：令NGINX开机自启动（随着字符界面）。



## 数据爬取及存储模块

这里是使用jyx2-pc来执行爬取。

执行该模块的机器必须在hadoop集群中。

### py文件路径

* 虎牙：code/crawler_part/huya_crawler.py
* 斗鱼：code/crawler_part/douyu_crawler.py

注意，这两个py不需要提交到集群。

### 执行爬取方式

1. 分别在项目目录下找到上述两个py文件
2. 爬取结果有两种存储方式：long和short，long模式可以两个py文件同时运行，short模式只能运行一个
3. 如果选择long模式，将huya_crawler.py中41和43行地址分别设置为./Long/huya/people.txt和./Long/huya/popular.txt，将douyu_crawler.py中43和45行地址分别设置为./Long/douyu/people.txt和./Long/douyu/popular.txt
4. 如果选择short模式，将huya_crawler.py中41和43行地址分别设置为./short/people.txt和./short/popular.txt，或者将douyu_crawler.py中43和45行地址分别设置为./short/people.txt和./short/popular.txt(两个文件不可同时执行)
5. 分别运行huya_crawler.py和douyu_crawler.py即可(long模式下可同时运行，short模式下只能选择一个运行)
6. 代码设置无限循环爬取，除非手动停止，否则将在每次爬取完成后休息30秒，并继续下一次爬取，每次爬取-休息过程平均耗时大约90秒

### 运行结果

* 两个程序执行时都会在控制台打印每一个爬取到的直播间名字、热度和分类
* long模式运行huya_crawler.py，程序会将每个直播间数据按"name:直播类型 num:1"格式存入./Long/huya/people.txt，按"name:直播类型 num:热度"格式存入./Long/huya/popular.txt
* long模式运行douyu_crawler.py，程序会将每个直播间数据按"name:直播类型 num:1"格式存入./Long/douyu/people.txt，按"name:直播类型 num:热度"格式存入./Long/douyu/popular.txt
* short模式运行两个文件，程序都会将每个直播间数据按"name:直播类型 num:1"格式存入./short/people.txt，按"name:直播类型 num:热度"格式存入./short/popular.txt



## 流准备模块

这里是使用jyx2-pc来执行流准备。

执行该模块的机器必须与执行数据数据爬取及存储模块的机器是同一台机器。

执行该模块的机器必须在hadoop集群中。

该模块理论上不需要进行任何修改。如果你想放慢实行周期，你可以在两个脚本中的sleep一栏更改脚本的休眠时间。这里不建议修改，因为整个系统的周期是提前设定好的。

### 提前准备

参照代码详细解释文档，需要提前在hdfs上建好相应的文件夹。

需要注意的是，必须由执行该模块的机器来创建下列文件，否则会有写入权限的问题。

*如果出现了该问题，可以通过namenode的机器输入hdfs dfs -chmod /    来将所有目录改为可修改的。

hdfs dfs -mkdir /origin

hdfs dfs -mkdir /origin/people/

 hdfs dfs -mkdir /origin/popular/

 hdfs dfs -mkdir /longtime

 hdfs dfs -mkdir /longtime/douyu

hdfs dfs -mkdir  /longtime/huya

 hdfs dfs -mkdir /longtime/douyu/people/

 hdfs dfs -mkdir /longtime/douyu/popular/

hdfs dfs -mkdir  /longtime/huya/people/

 hdfs dfs -mkdir /longtime/huya/popular/

### shell脚本位置

- short模式：code/crawler_part/upload.sh
- long模式：code/crawler_part/uploadlong.sh

### 执行方式

进入到目录下。

在数据爬取模块成功运行完第一轮数据爬取后选择与数据爬取模块相同的模式执行对应的脚本。

### 运行结果

在固定的周期后，将在hdfs对应的目录下看到上传的带有时间戳的文件。



## 流计算模块

在启动了流准备模块后便可以向spark集群提交任务。

这里使用wcy-pc来提交。当然，spark集群内任意一台机器均可提交任务。但需要注意的是，哪一台机器提交任务就会在哪一台机器上本地化流计算结果，最终执行可视化模块时执行该模块的机器必须参与并担任主机B的角色，这一点后文会再次提及。

执行该模块的机器必须同时位于hadoop集群与spark集群内，这里推荐使用namenode与master双重身份的机器执行该模块。

### py文件目录

- long模式：code/compute_part/long_time_streaming.py
- short模式：code/compute_part/short_time_streaming.py

注意：上述两py文件不可在本地运行，必须提交到集群上方可运行。且不可同时提交到集群上，请参照之前的文档，选择对应模式提交对应py文件到集群。

### 提前准备

在code/compute_part/long_time_streaming.py下找到以下代码段。

```python
# 设置流监听，监听源为hdfs文件系统
sc = SparkContext(appName="PythonStreamingLongTime")
ssc = StreamingContext(sc, 90)
douyuPeople = ssc.textFileStream("hdfs://wcy-pc:9000/longtime/douyu/people/")
douyuPopu = ssc.textFileStream("hdfs://wcy-pc:9000/longtime/douyu/popular/")
huyaPeople = ssc.textFileStream("hdfs://wcy-pc:9000/longtime/huya/people/")
huyaPopu = ssc.textFileStream("hdfs://wcy-pc:9000/longtime/huya/popular/")
```

如果想改提交到集群上的appName，可以修改`sc = SparkContext(appName="PythonStreamingLongTime")`中的appName。

如果之前没有修改集群对应的运行周期，则不需要修改`ssc = StreamingContext(sc, 90)`中的第二个参数。再次强调，不推荐修改周期。

需要将wcy-pc改为对应hadoop集群的namenode的hostname。

如果你按照之前的流准备去创建目录，则其他地方不需要进一步改动。

在code/compute_part/short_time_streaming.py下找到以下代码段。

```python
# 设置流监听，监听源为hdfs文件系统
sc = SparkContext(appName="PythonStreamingShortTime")
ssc = StreamingContext(sc, 90)
people = ssc.textFileStream("hdfs://wcy-pc:9000/origin/people/")
popu = ssc.textFileStream("hdfs://wcy-pc:9000/origin/popular/")
```

如果想改提交到集群上的appName，可以修改`sc = SparkContext(appName="PythonStreamingLongTime")`中的appName。

如果之前没有修改集群对应的运行周期，则不需要修改`ssc = StreamingContext(sc, 90)`中的第二个参数。再次强调，不推荐修改周期。

需要将wcy-pc改为对应hadoop集群的namenode的hostname。

如果你按照之前的流准备去创建目录，则其他地方不需要进一步改动。

### 执行方式

选择与爬取、流准备相同的模式

选择同时位于hadoop集群与spark集群内的机器向集群提交任务

打开终端进入code/compute_part/目录下执行对应命令：

long模式：$SPARK_HOME/bin/spark-submit --master spark://wcy-pc:7077 long_time_streaming.py

short模式：$SPARK_HOME/bin/spark-submit --master spark://wcy-pc:7077 short_time_streaming.py

注意：应该把命令中的wcy-pc替换为对应的spark master的hostname

随后可以在终端窗口看到一些提示信息。进入spark：//wcy-pc：8080可以看到更多信息。

提示：如果想减少一些终端提示冗余信息，可以进入$SPARK_HOME/conf

在本目录下复制log4j.properties.template到本目录下并改名为log4j.properties，并将

```
# Set everything to be logged to the console
log4j.rootCategory=INFO, console
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.target=System.err
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n
```

`log4j.rootCategory=INFO, console`一栏的INFO改为WARN

### 运行结果

每隔一段周期，便会更新对应的文件。

- long模式：每隔90s便会更新code/compute_part/longOutput.txt
- short模式：每隔90s便会更新code/compute_part/shortOutput.txt

该文件是流计算运行结果的本地化，只会出现在提交了任务的机器上。所以后续可视化需要该机器继续参与。



## 可视化模块

准备主机A和B，主机A位于集群外（当然也可以位于集群内），主机B同时位于hadoop集群与spark集群内且参与了流计算模块的任务提交，主机A B均为Linux AMD64平台。

本小组实验中，主机B为wcy-pc，即hadoop的namenode、datanode以及spark的master、worker，同时在wcy-pc上向spark集群提交了任务。

### 主机B

主机B获取计算后的信息，将每次计算的信息写入一个文本文件中（实验中若选择short模式，则写入code/compute_part/shortOutput.txt，若选择long模式，则写入code/compute_part/longOutput.txt，其具体规约请查看关键代码解释）。

主机B上找到code/compute_part/echo.sh，其功能为每90秒对上一行提到的文本文件执行`cat`操作，示例如下：

```shell
#!/bin/bash
while :
do
	cat ./output.txt
	sleep 30
	echo
	sleep 30
	echo
	sleep 30
done
```

因为websocketd默认连接超时时间为60秒，所以每30秒发送一个空包以维持连接。

主机B上运行websocketd命令（假设当前处于`echo.sh`所在的目录，即code/compute_part/）：

```shell
websocked --port=10080 ./echo.sh
```

### 主机A

主机A上运行NGINX，其配置文件为（如果你使用包管理器安装的NGINX，其配置文件**可能**位于`/etc/nginx/nginx.conf`，若不在请使用谷歌；如果你使用编译安装的方式安装的NGINX，假设你设置的安装目录为`/usr/local/nginx/`，则配置文件位于`/usr/local/nginx/conf/nginx/nginx.conf`）：

```nginx
user root;
worker_processes 1;

events {
    worker_connections 1024;
}

http {
    include mime.types;
    default_type application/octet-stream;
    sendfile on;
    keepalive_timeout 65;
    gzip on;

    server {
        listen 80;
        server_name localhost;
        location / {
            root /home/ddch/Documents/sites/test/firstTest/long/;
            index index.html;
        }
        location =/ws {
            proxy_redirect off;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_pass http://192.168.0.118:10080;
        }
    }
}
```

**如果你不熟悉NGINX配置文件**，该配置文件的大意为，令NGINX启动一个HTTP服务，监听本机的80端口（80端口是标HTTP服务的标准端口，本小组实际实验时采用10080端口，即把listen 80改为listen 10080）。若HTTP请求中路径为`/ws`，则将请求以WebSocket连接处理，并转发至`192.168.0.118:10080`（该地址仅为示例，请根据主机B的实际IP地址填写；使用路径分流能达到端口复用和向用户屏蔽WebSocket真正服务端地址的效果）；若HTTP请求中路径为其他，统一将路径映射至`root`后指定的路径处理（文中地址仅为示例，请根据实际情况进行填写），且默认主页为指定路径下的`index.html`文件。例如，本实验中你可以将 root地址在long模式下改为code/graph_part/long或者在short模式下改为code/graph_part/short。此处路径不完整，再次强调，需要填写绝对路径。换句话说，code/graph_part/long前应该还有其他地址。假设项目地址为$PATH，则需改为$PATH/code/graph_part/long

如果你想要具体了解配置文件中每个语句的意义，可以阅读NGINX官方文档（https://nginx.org/en/docs/）。

### 结果

在浏览器中访问主机A的ip地址即可查看到可视化成果。



## 恭喜！您已经成功完成了实验！