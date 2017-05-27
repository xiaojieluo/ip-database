from celery import Celery
import requests
import json

from db import db

broker = 'redis://localhost:6379'
backend = 'redis://localhost:6379'

app = Celery('Collection', broker = broker, backend = backend)

@app.task(bind=True)
def ip(self, ip):
    url = 'http://ip-api.com/json/'
    try:
        r = requests.get(url+ip)
        html = r.json()

        if html.get('status', '') == 'fail':
            return '[fail]'
        else :
            update('ip', {'query':html.get('query', '')}, html)
            print(html)
            return '[ok]'

    except requests.ConnectionError as e:
        with open('log.txt', 'w') as fp:
            fp.write(ip+'...ConnectionError\n')

        raise self.retry(exc=e, countdown=5, max_retries=10)

def update(type_, query, data):
    '''
    当数据不存在时,更新 mongodb 数据库
        type_ : 类型
        data  : 要写入数据库的内容, dict 格式,
            { text:'', result:'' }
    '''
    database = db[type_]
    if isinstance(data, str):
        data = json.loads(data)
    if database.find_one(query) is None:
        database.insert_one(data)
