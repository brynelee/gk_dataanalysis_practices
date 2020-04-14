import requests
import chardet
url = 'http://www.tipdm.com/tipdm/index.html'
rgg = requests.get(url)
print('结果类型', type(rgg))
print('状态码', rgg.status_code)

print('编码：', rgg.encoding)
rgg.encoding = chardet.detect(rgg.content)['encoding']
print('更正过的编码：', rgg.encoding)

print('响应头：', rgg.headers)
print('网页内容：', rgg.text)
