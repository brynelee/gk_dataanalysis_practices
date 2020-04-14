import json
from lxml import etree
import requests
import chardet


url = 'http://www.tipdm.com/tipdm/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
rgg = requests.get(url, headers=headers)

rgg.encoding = chardet.detect(rgg.content)['encoding']

html = rgg.content.decode('utf-8')

html = etree.HTML(html, parser=etree.HTMLParser(encoding='utf-8'))

content = html.xpath('//ul[starts-with(@id, "me")]/li/a/text()')
print('标题菜单的文本：', content)

# 使用dump方法写入文件
with open('output.json', 'w') as fp:
    json.dump(content, fp)
