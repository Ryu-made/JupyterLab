import requests as req
from bs4 import BeautifulSoup as bs
def printList():
    # 성균관대 대학식당 - 인문사회과학캠퍼스 - 법고을식당
    url = 'https://www.skku.edu/skku/campus/support/welfare_11.do?mode=info&srDt=2024-12-12&srCategory=L&conspaceCd=10201034&srResId=4&srShowTime=W'
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'
    }
    web = req.get(url, headers=headers)
    soup = bs(web.content, 'html5lib')    
    content = soup.select('.cafeteria_view .weekly_list .weeListWrap')    
    for item in content:
        print('='*10)
        date = item.select_one('.weeListTit').text.replace('\t', '').replace('\n', '')
        date = f'{date[date.find('(')+1:-1]} ({date[:1]})' 
        print(date)
        print('='*10)
        menu = item.select_one('li > pre').text.strip()
        price = item.select('li')[1].text.strip()
        print(menu)
        print(f'{price}￦')