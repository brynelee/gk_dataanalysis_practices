import pymysql
from bs4 import BeautifulSoup
from lxml import etree
import requests
import chardet

url = 'http://www.tipdm.com/tipdm/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
rgg = requests.get(url, headers=headers)

rgg.encoding = chardet.detect(rgg.content)['encoding']

html = rgg.content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')  # 生成Beautiful Soup对象

conn = pymysql.connect(host='xdubuntu1810', port=3306, user='root',
                       passwd='time4@FUN', db='test', charset='utf8', connect_timeout=1000)
cursor = conn.cursor()

target = soup.title.string
title = 'tipdm'
sql = 'insert into class (name,text) values(%s, %s)'
cursor.execute(sql, (title, target))
conn.commit()

data = cursor.execute('select * from class')
data = cursor.fetchmany()
print('查询获取的结果：', data)
conn.close()
