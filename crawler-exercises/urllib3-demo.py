import urllib3
http = urllib3.PoolManager()
rq1 = http.request('GET', 'http://www.tipdm.com/tipdm/index.html')
print('服务器响应码: ', rq1.status)
print('Response Body: ', rq1.data)

print('='*20)
ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/65.0.3325.181'}
rq2 = http.request('GET', 'http://www.tipdm.com/tipdm/index.html', headers = ua)
print('服务器响应码: ', rq2.status)
print('Response Body: ', rq2.data)

