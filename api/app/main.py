from fastapi import FastAPI
from .routers import url_router, auth
from . import models
from .database import engine
import uvicorn
 
models.Base.metadata.create_all(bind=engine)



app = FastAPI()

@app.get("/")
def index():
    return {"Message": "to see the API docs, go to /docs"}

app.include_router(url_router.router)
app.include_router(auth.router)




