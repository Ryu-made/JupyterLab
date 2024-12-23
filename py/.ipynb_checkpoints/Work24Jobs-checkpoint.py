import requests as req
from bs4 import BeautifulSoup as bs

def printResult(cnt, pageno, kword):    
    url = 'https://www.work24.go.kr/wk/a/b/1200/retriveDtlEmpSrchList.do?&codeDepth2Info=11000&sortField=DATE&sortOrderBy=DESC&benefitSrchAndOr=O&codeDepth1Info=11000&empTpGbcd=1&siteClcd=all&searchMode=Y&careerTypes=N&academicGbnoEdu=noEdu&enterPriseGbn=all'
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'
    }
    # kword = 'java|python|spring|javascript'
    prm = {
        'resultCnt': cnt,
        'pageIndex': pageno,
        'keyword': kword,
        'srcKeyword': kword
    }
    web = req.get(url, headers=headers, params=prm)
    print(web)
    soup = bs(web.content, 'html5lib')
    noresult = '검색된 내용이 없습니다.'
    tbl = soup.select_one('#contentArea tbody')
    rows = tbl.select('tr')
    if rows[0].select_one('td').text == noresult:
        print(noresult)
    else:
        srchCnt = soup.select_one('.box_table_hd > .section_left').text.strip()
        srchCnt = srchCnt[srchCnt.rfind(' ')+1:]
        print(f'총 검색결과: {srchCnt}')
        print('+'*60)
        for i, row in enumerate(rows, cnt*(pageno-1)+1):
            cell = row.select_one('td')
            company = cell.select_one('.box_chk-group a').text.strip()
            titleSelector = cell.select_one('.t3_sb')
            title = titleSelector.text.strip()
            title = title[:title.find('\n')]
            detail = titleSelector.get_attribute_list('href')[0]
            print(f'{i}: {title} / {company} \ndetails=\'{detail}\'\n')
        print('+'*60)