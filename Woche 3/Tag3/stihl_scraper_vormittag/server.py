from typing import Annotated

import db
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from mvc import controller

app = FastAPI()
security = HTTPBasic()


users = {"julien": "12345", "marco": "asdfg"}


def validate_user_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    # TODO: db - get user credentials
    user_name = credentials.username
    if user_name in users:
        if users[user_name] == credentials.password:
            return {"username": credentials.username}
        else:
            raise HTTPException(status_code=401, detail="Wrong Password!")
    else:
        raise HTTPException(status_code=401, detail="User Name does not exist!")


@app.on_event("startup")
def startup():
    # DB initialisieren
    db.initialize_db()


# Beispiel von geschützter Route mit der API
@app.get("/users/me")
def read_current_user(current_user: dict = Depends(validate_user_credentials)):
    return f'You are successfully logged in, {current_user["username"]}'


# Routen definieren
# 1. scrapen
@app.get("/scrape")
def scrape_data(current_user: dict = Depends(validate_user_credentials)):
    controller.scrape_new_products()


# 2. daten wiedergeben
@app.get("/data")
def get_all_data(current_user: dict = Depends(validate_user_credentials)):
    template = controller.retrieve_data()
    return template


if __name__ == "__main__":
    uvicorn.run("server:app", reload=True)
