from ast import For
from fastapi import FastAPI, Form
import jwt
from fastapi.middleware.cors import CORSMiddleware

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


# 더미 유저
users = [
    {
        "name": "김철수",
        "id": "kimchulsu",
        "password": "1234",
        "email": "kimchulsu@gmail.com",
        "phone": "010-1234-5678",
    }
]


# jwt 토큰 생성
def encode_jwt(user):
    payload = {
        "id": user["id"],
        "name": user["name"],
    }
    return jwt.encode(payload, secret_key, algorithm="HS256")


# id로 유저 찾기, 만약에 없으면 None 반환
def get_user(id):
    for user in users:
        if user["id"] == id:
            return user


@app.post("/register")
def register(
    # api 파라미터
    name: str = Form(...),
    id: str  = Form(...),
    password: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
):
    # 이미 존재하는 아이디인지 확인
    user = get_user(id)
    
    if user:
        return {"message": "이미 존재하는 아이디입니다."}

    # 존재하지 않는 아이디면 유저 추가
    user = {
        "name": name,
        "id": id,
        "password": password,
        "email": email,
        "phone": phone,
    }

    users.append(user)

    return {
        "token": encode_jwt(user),
        "message": "회원가입 성공",
    }


@app.post("/login")
def login(
    # api 파라미터
    id: str = Form(...),
    password: str = Form(...)
):
    # id로 유저 찾기
    user = get_user(id)

    # 유저가 없으면
    if not user:
        return {"message": "존재하지 않는 아이디입니다."}

    # 비밀번호가 틀리면
    if user["password"] != password:
        return {"message": "비밀번호가 틀렸습니다."}

    # 로그인 성공
    return {
        "token": encode_jwt(user),
        "message": "로그인 성공!"
    }


@app.post("/profile")
def profile(
    # api 파라미터
    token: str = Form(...),
):
    # 토큰 검증
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
    except:
        return {"message": "토큰이 유효하지 않습니다."}

    # id로 유저 찾기
    user = get_user(payload["id"])

    # 유저가 없으면
    if not user:
        return {"message": "존재하지 않는 아이디입니다."}

    # 프로필 정보 반환
    return {
        "name": user["name"],
        "id": user["id"],
        "email": user["email"],
        "phone": user["phone"],
    }
    

@app.get('/')
def index():
    return {"message": "Hello World"}

# 이 파일이 시작 지점이면
if __name__ == "__main__":
    # 서버를 실행하는 코드
    import uvicorn
    uvicorn.run('main:app', reload=True)