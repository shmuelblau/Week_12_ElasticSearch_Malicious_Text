from fastapi import FastAPI
from fastapi.responses import JSONResponse 


import uvicorn

from models.manager import Manager
from models.logger import get_logger
from config import *



app = FastAPI()

log =  get_logger()

manager = Manager(weapons_file , tweets_file)


log.info(f"host ={host}")

manager.start_operation()

# =================================================================


@app.get("/")
def home():

    
    
    return "manager.tweets"




@app.post("/change-connection")
def ChangeConnection():

    
    return "בוצע"

    






if __name__ == "__main__":
    
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)