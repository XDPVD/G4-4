from fastapi import FastAPI
import uvicorn

app = FastAPI()  

@app.get("/")
def read_root():
    return {"Hello": "aea"}


uvicorn.run(app,host="0.0.0.0",port="8080")