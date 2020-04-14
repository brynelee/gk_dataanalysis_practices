from bs4 import BeautifulSoup
from lxml import etree
import requests
import chardet


def printl():
    print('='*100)


def printall(set_to_print):
    for elm in set_to_print:
        print(elm)


url = 'http://www.tipdm.com/tipdm/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
rgg = requests.get(url, headers=headers)

rgg.encoding = chardet.detect(rgg.content)['encoding']

html = rgg.content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')  # 生成Beautiful Soup对象
# print('输出格式化的Beautiful Soup对象：', soup.prettify())

printl()
print('head: ', soup.head)

printl()
print('title: ', soup.title)

printl()
target = soup.find_all('ul', class_='menu')
print('CSS类名匹配获取的节点：', target)

printl()
target2 = soup.find_all(id='menu')
print('关键字id匹配的节点：', target2)

printl()
target3 = soup.find_all('a')
# print('所有名称为a的节点：', target3)
urls = []
text = []
# 分别提取链接和文本
for tag in target3:
    urls.append(tag.get('href'))
    text.append(tag.get_text())

print('所有的链接：')
printall(urls)

print('所有链接的文本：')
printall(text)

