import requests

url = 'http://www.tipdm.com/tipdm/index.html'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
rgg = requests.get(url, headers = headers)

print('响应头：', rgg.headers)
print('网页内容：', rgg.text)
