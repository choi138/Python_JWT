from ast import For
from fastapi import FastAPI, Form
import jwt
from fastapi.middleware.cors import CORSMiddleware
import pymysql

secret_key = "asdfghjkl"

origins = [
    "http://localhost:3000",
    "http://localhost:3000/register",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# encode_jwt
def encode_jwt(user):
    payload = {
        "id": user["id"],
        "name": user["name"],
    }
    return jwt.encode(payload, secret_key, algorithm="HS256")

# db
def db_connect():
    conn = pymysql.connect(host='127.0.0.1', user='root', database='test', port=3306, charset='utf8')
    curs = conn.cursor()
    return conn, curs

# db에 encode한 jwt 토큰 유저추가
def db_add_user(user):
    conn, curs = db_connect()
    curs.execute("INSERT INTO userTable VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (user["id"], user["password"], user["name"], user["email"], user["phone"], encode_jwt(user)))
    conn.commit()
    conn.close()