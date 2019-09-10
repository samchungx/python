import requests
url = "http://www.baidu.com"
kv = {'user-agent':'Mozilla/5.0'}
r = requests.get(url)
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.text[1000:2000])
