from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # ertellt einen virtuellen Server


# Wrapper, der Routen definiert - GET ist die Methode, "/" ist der Pfad
@app.get("/")
def get_root():
    return "Hi from da Server!"


@app.get("/test")
def get_test():
    return {"Hi": "I'm a test object"}


if __name__ == "__main__":
    # Wenn wir reload=True setzen, müssen wir als Argument für den Server folgende Form nutzen: "dateiname:name_des_servers"
    uvicorn.run("fastapi_intro:app", reload=True)  # Aktiviert den Server
