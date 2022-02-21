from bs4 import BeautifulSoup
import requests

url = f'https://nosmk.khealth.or.kr/nsk/ntcc/index.do'

resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
print(soup)
# classname = 'KL4Bh'

# print(soup.find('div',class_=classname))
# bodys = soup.div.parent
# print(bodys)