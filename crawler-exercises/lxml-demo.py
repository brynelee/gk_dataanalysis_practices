from lxml import etree
import requests

url = 'http://www.tipdm.com/tipdm/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
rgg = requests.get(url, headers=headers)


html = rgg.content.decode('utf-8')
html = etree.HTML(html, parser=etree.HTMLParser(encoding='utf-8'))
result = etree.tostring(html, encoding='utf-8',
                        pretty_print=True, method='html')
# print('修正后的HTML: ', result)
# print(result.decode('utf-8'))

result = html.xpath('head')
print('名称定位结果：', result)

result1 = html.xpath('/html/head/title')
print('节点层级定位结果', result1)

result3 = html.xpath('//title')
print('搜索定位title节点结果：', result3)

# xpath谓语示例last(), position(), =, <, >
result4 = html.xpath('//header[@class]')
print('class属性定位结果：', result4)

result5 = html.xpath('//ul[@id="menu"]')
print('id属性定位结果：', result5)


# 功能函数示例text, starts-with, contains, and
title = html.xpath('//title/text()')
print('title节点的文本内容：', title)

# 定位id值以me开头的ul节点并提取其所有子孙节点a内的文本内容
content = html.xpath('//ul[starts-with(@id, "me")]/li//a/text()')
for i in content:
    print(i)
