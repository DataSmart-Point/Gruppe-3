import db
import uvicorn
from fastapi import FastAPI, HTTPException
from mvc import controller

app = FastAPI()


@app.on_event("startup")
def startup():
    # DB initialisieren
    db.initialize_db()


# Routen definieren
# 1. scrapen
@app.get("/scrape")
def scrape_data():
    controller.scrape_new_products()


# 2. daten wiedergeben
@app.get("/data")
def get_all_data():
    template = controller.retrieve_data()
    return template


if __name__ == "__main__":
    uvicorn.run("server:app", reload=True)

# What now? - Potentielle Aufgaben für den Nachmittag
# 1. Daten in Pandas Dataframe überführen
# 2. Daten als CSV ausgeben
# -> model funktion: Daten auslesen -> view funktion: write_data_in_csv

# 3. Nur Produkte einer Kategorie heraussuchen
# 4. Produkte nach Filtern heraussuchen
# 5. DB - Update
# 6. DB - Delete
