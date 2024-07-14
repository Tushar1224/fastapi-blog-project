from fastapi import FastAPI
from blog import  models
from blog.database import engine
from blog.routers import blog, user, authentication
# import uvicorn

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# if __name__=='__main__':
#     uvicorn.run(app, host="127.0.0.1",port=9000)

#pip install virtualenv
#python3 -m venv app
#Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
#.\app\Scripts\Activate.ps1
#pip install -r /path/to/requirements.txt
#uvicorn main:app --reload