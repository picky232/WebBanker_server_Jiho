# FastAPI

# Server RUN
# uvicorn main:app --reload

##############################################################
# < IMPORT > #################################################
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import Hash
##############################################################


##############################################################
# < 응답 주고 받기 > ############################################
##############################################################
# 요청 받기 (Get request form Client)
# data = await request.json()  -> data를 json type으로 변경

# 응답 반환 (Response to Cleint)
# return {}
##############################################################


app = FastAPI()

@app.get("/signup", response_class=HTMLResponse)
async def root(request: Request):
    return



TempData = {
	"UserName": "Jiwon",
	"UserId": "user01",
	"UserPw": "pass123##",
    "UserPwRe": "pass123##",
	"UserEmail": "abcd@gmail.com"
}




############### 회원가입 ###############
@app.post("/newuser1")
async def newuser1(request: Request):
    try:  
        data = await request.json()     
    except:
        return{""}
    
    try:
        if data["UserId"] == TempData["UserId"]:
            return {"Success" : False, "ErrorCode" : "sameid"}
        if data["UserPw"] != data["UserPwRe"]:
            return {"Success" : False, "ErrorCode" : "n-samepw"}
        return {"Success" : True, "UserId" : data["UserId"]}    
    except:
        return{"Success" : False}
######################################




############### 로그인 #################

@app.post("/userlogin")
async def userlogin(request: Request):
    try:
        data = await request.json()
    except:
        return{"Success" : False, "ErrorCode" : "dataerr"}
    try:
        if data["UserId"] != TempData["UserId"]:
            return {"Success" : False, "ErrorCode" : "iderror"}
        if data["UserPw"] != TempData["UserPw"]:
            return {"Success" : False,"ErrorCode" : "pwerror"}
        return {"Success" : True}
    except:
        return {"Success" : False}

######################################
