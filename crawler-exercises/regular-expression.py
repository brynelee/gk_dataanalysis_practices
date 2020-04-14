import chardet
import requests
import re
pat = re.compile(r'\d+')
print('成功匹配', re.search(pat, 'abc45'))

pat2 = re.compile(r'\d+')
print("get results: ", re.findall(pat, 'abc2c3ed'))


url = 'http://www.tipdm.com/tipdm/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
rgg = requests.get(url, headers=headers)
rgg.encoding = chardet.detect(rgg.content)['encoding']

title_pattern = r'(?=<title>).*?(?=</title>)'
title_com = re.compile(title_pattern, re.M | re.S)
title_search = re.search(title_com, rgg.text)
title = title_search.group()
print('标题内容', title)
# 使用findall方法查找title中的内容
print('标题内容', re.findall(r'<title>(.*?)</title>', rgg.text))
