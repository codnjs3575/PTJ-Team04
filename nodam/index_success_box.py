from bs4 import BeautifulSoup
import requests
import json

url = f'https://nosmk.khealth.or.kr/nsk/ntcc/index.do'

resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
nc_count = soup.find('section',class_="nc-count")
nc_count_dict = dict()
count_list = list()

for msg in nc_count.find_all('p'):
    msg = msg.text.strip().replace('명','')
    if msg.isalpha() == False :
        count_list.append(msg)
nc_count_dict['count1'] = count_list[0]
nc_count_dict['count2'] = count_list[1]

print(nc_count_dict)
res_json = json.dumps(nc_count_dict, ensure_ascii=False)

with open(f'nc_count.json', 'w', encoding='utf-8') as f:
    f.write(res_json)


