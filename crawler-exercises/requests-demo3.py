import requests

url = 'http://www.tipdm.com/tipdm/index.html'

print('超时时间为2：',  requests.get(url, timeout=2))

requests.get(url, timeout=0.001)
