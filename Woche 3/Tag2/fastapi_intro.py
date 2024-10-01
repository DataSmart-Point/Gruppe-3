from typing import Union

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()  # ertellt einen virtuellen Server


# Wrapper, der Routen definiert - GET ist die Methode, "/" ist der Pfad
@app.get("/")
def get_root():
    # Wir geben einen String als Response zurück - das wird der Client dann auslesen können
    return "Hi from da Server!"


@app.get("/test")
def get_test():
    # Wir können auch ein Dictionary als Response zurückgeben
    return {"Hi": "I'm a test object"}


# Zum Testen der Appfunktionalitäten definieren wir ein Object "items"
items = {"1": "item1", "2": "item2", "3": "item3"}


@app.get(
    "/items/{item_id}"
)  # Der Pfadparameter muss im Wrapper und in der Funktion gleich heißen
def get_item(item_id):
    # Wir schauen uns an, wie wir GET mit Pfad-Parametern durchführen können
    if item_id in items:
        return {"Your Item": items[item_id]}
    else:
        # Falls wir nichts finden, geben wir einen Status Code 404 zurück
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/items")
def filter_items(query: Union[str, None] = None):
    # Wir schauen uns an, wie wir GET mit Query-Parametern durchführen können
    if query is not None:
        if query in items:
            return {"Your Item": items[query]}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    else:
        # Wenn keine Query vorhanden, geben wir alle items zurück
        return items


class Item(BaseModel):
    id: int
    value: str
    is_active: Union[bool, None] = None


item1 = Item(id=1, value="item1", is_active=True)
item2 = Item(id=2, value="item2", is_active=None)

advanced_items = [item1, item2]


@app.post("/items")
def create_item(new_item: Item):
    # items object muss geupdatet werden
    advanced_items.append(new_item)
    return "New Item Created!"


@app.get("/advanced_items")
def get_advanced_items():
    return advanced_items


if __name__ == "__main__":
    # Wenn wir reload=True setzen, müssen wir als Argument für den Server folgende Form nutzen: "dateiname:name_des_servers"
    uvicorn.run("fastapi_intro:app", reload=True)  # Aktiviert den Server
