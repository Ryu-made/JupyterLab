import requests as req
from dotenv import load_dotenv
import os  

def getOpenAPI (url, pageno=1, rows=10, type='json'):    
    if load_dotenv(dotenv_path='.env'):
        KEY = os.getenv('SERVICE_KEY')
    else:
        raise LookupError('serviceKey가 설정되지 않았습니다. .env 파일에 변수를 작성해주세요.')
   
    params = {
    'serviceKey' : KEY,
    'resultType' : type,
    'pageNo' : pageno,
    'numOfRows' : rows
    }
   
    r = req.get(url, params=params)
    
    j = r.json()
    return j['response']

def getOpenAPIFull (url, type='json'):

    j = getOpenAPI(url=url, pageno=1, rows=10, type=type)
    tc = j['body']['totalCount']
    if tc > 1000:
        r = getOpenAPI(url=url, pageno=0, rows=0, type=type)
        for i in range(1, int(tc/1000)+2):
            r['body']['items']['item'] += getOpenAPI(url=url, pageno=i, rows=1000, type=type)['body']['items']['item']

        return r
        
    return getOpenAPI(url=url, pageno=1, rows=tc, type=type)