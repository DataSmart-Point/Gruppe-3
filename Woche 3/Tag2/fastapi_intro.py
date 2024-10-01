from typing import Union

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()  # ertellt einen virtuellen Server


# Wrapper, der Routen definiert - GET ist die Methode, "/" ist der Pfad
@app.get("/")
def get_root():
    return "Hi from da Server!"


@app.get("/test")
def get_test():
    return {"Hi": "I'm a test object"}


items = {"1": "item1", "2": "item2", "3": "item3"}


@app.get("/items/{item_id}")
def get_item(item_id):
    if item_id in items:
        return {"Your Item": items[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/items")
def filter_items(q: Union[str, None] = None):
    if q is not None:
        if q in items:
            return {"Your Item": items[q]}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    else:
        return items


if __name__ == "__main__":
    # Wenn wir reload=True setzen, müssen wir als Argument für den Server folgende Form nutzen: "dateiname:name_des_servers"
    uvicorn.run("fastapi_intro:app", reload=True)  # Aktiviert den Server
