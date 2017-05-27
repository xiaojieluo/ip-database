# ip-dataabse
ip database

数据采集自 ip-api.com

在celery 队列中获取数据并存入 mongodb 数据库

支持中断恢复采集

支持 python3+

# How to Install

```python

pip install -r requirements.txt

```

#  How to Use

## step1. configure mongodb information
ip-database 会将采集的数据存储到 mongodb 中,所以需要在 db.py 中配置 mongodb 的连接信息

## step 1. start redis and celery

celery 使用 redis 存储任务队列,需要启动 redis-server

```shell

$ redis-server

$ celery -A task worker --loglevel=info
```

## step 2. start ip-database

```python
python ip.py
```
