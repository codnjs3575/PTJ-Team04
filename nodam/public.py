
from bs4 import BeautifulSoup
import requests, json

######### 전국 시도 코드 딕셔너리 만들기 ###################################
def getSido(url):  
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, 'html.parser')

    a = soup.find('select',{'id':'area'})
    option_list = a.select('option')

    sido_ = list(map(lambda x: x.text, option_list[1:]))
    sido_code = list(map(lambda x: x['value'], option_list[1:]))

    print(sido_code)
    print(len(sido_code))

    sido_dict = dict(zip(sido_,sido_code))
    return sido_dict

#########   지역별 마지막 페이지 찾기   ###################################
def pageCheck(url_, sido):
    url = url_+f'?area={sido}&column=all&search='
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    ul_list = soup.find('ul',{'class':'paginationListNum seed_cf'})
    
    Page = ul_list.find_all('a')
    if len(Page) == 0:
        lastPage = ul_list.find('strong').text
    else:
        lastPage = Page[-1].text

    return lastPage

#########     전국 보건소 딕셔너리     ###################################
def getPublic(url_, sido, lastPage):
    sido_list =[]

    for page in range(1,int(lastPage)+1):
        url = url_+f'?area={sido}&column=all&search=&spage={page}'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        tbody_list = soup.find_all('tr')[1:]
        for i in range(len(tbody_list)):
            juso_dict ={
                    'area':tbody_list[i].find_all('td')[0].string,
                    'public':tbody_list[i].find_all('td')[1].string,
                    'address':tbody_list[i].find_all('td')[2].string,
                    'tel':tbody_list[i].find_all('td')[3].string
                }
            sido_list.append(juso_dict)
    
    return sido_list


if __name__ == '__main__':
    dict_ = {}
    url = 'https://nosmk.khealth.or.kr/nsk/user/extra/ntcc/262/service/healthServiceSearch/jsp/LayOutPage.do' 

    sido_dict = getSido(url) 
    for sido in sido_dict.values(): 
        lastPage = pageCheck(url, sido)
        result = getPublic(url, sido, lastPage)
        dict_[sido] = result

    # list key 생성
    res_dict ={
        'list': dict_
    }

    result_json = json.dumps(res_dict, ensure_ascii=False) # list key 지우고 싶으면 : res_dict -> dict_로 변경
    with open('./publicHealth.json','w',encoding='utf_8') as f:
        f.write(result_json)
