from fastapi import APIRouter, File, Form, UploadFile, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO

from fastapi.responses import StreamingResponse
from pathlib import Path
import pymysql
# import json

import for_sql



app = FastAPI()

origins = [ "*",]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  
    allow_methods=["*"],   
    allow_headers=["*"],  
)

def get_db_connection():
    conn = pymysql.connect(host='175.126.37.21', user='id231', password='pw231', port=13306, db='db231', charset='utf8')
    return conn

@app.get("/main")
def home():
    a = dict()
    # sql = """SELECT * FROM test03"""
    # d = for_sql.run(sql)
    # j = json.dumps(d, ensure_ascii=True)
    a['page'] = "main"
    a['text'] = ["메인 페이지는 여기에 작성", "페이지 내용은 main.py에 의해 호출됨", "프로젝트 결과를 웹으로 보여주는 위치를 여기서 시작"]
    # a['data'] = d
    return a

@app.get("/files/{file_name}")
async def get_file(file_name: str):
    file_path = Path("../image") / file_name  # 폴더 경로와 파일 이름을 합침
    print(file_path);

    if file_path.exists() and file_path.is_file():
        # 파일을 바이너리 모드로 열기
        file_like = open(file_path, mode="rb")
        
        # StreamingResponse로 반환
        return StreamingResponse(file_like, media_type="image/png")
    else:
        return {"에러": "파일을 찾을 수 없음"}

@app.get("/test02/{id}")
def dbfile(id: int):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT id, image FROM test02 WHERE id = %s"
    cursor.execute(query, (id))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result is None:
        raise HTTPException(status_code=404, detail="이미지를 찾을 수 없음")
    
    # 이미지 데이터를 BytesIO 객체로 변환
    image_data = result[1]  # 이미지 BLOB 데이터

    # StreamingResponse로 반환 (파일 형태에 맞는 MIME 타입 설정)
    return StreamingResponse(BytesIO(image_data), media_type="image/png")

@app.get("/detail1")
def home():
    a = dict() 
    a['page'] = "detail1"
    return a

@app.get("/detail2")
def home():
    a = dict() 
    a['detail2'] = "3"
    return a

@app.get("/detail3")
def home():
    a = dict() 
    a['detail4'] = "4"
    return a