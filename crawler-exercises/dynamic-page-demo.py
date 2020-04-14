import requests
import json
url = 'http://www.ptpress.com.cn/bookinfo/getBookListForWS'
return_data = requests.get(url).text
data = json.loads(return_data)
news = data['data']
for n in news:
    bookName = n['bookName']
    author = n['author']
    price = n['price']
    print("新书名：", bookName, '\n', "作者：", author, '\n', "价格：", price)
    print('\n')
