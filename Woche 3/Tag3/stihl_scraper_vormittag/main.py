import db
from mvc import controller

if __name__ == "__main__":
    # 0. Erstmal DB initialisieren
    db.initialize_db()

    while True:
        user_input = input(
            "\nWelchen Befehl willst ausführen (scrape oder retrieve)?\n"
        )

        if user_input == "scrape":
            # Webscraper laufen lassen
            controller.scrape_new_products()
        elif user_input == "retrieve":
            # Daten von DB auslesen Befehl
            controller.retrieve_data()
        else:
            print("Keine gültige Eingabe...")


# What now? - Potentielle Aufgaben für den Nachmittag
# 1. Daten in Pandas Dataframe überführen
# 2. Daten als CSV ausgeben
# -> model funktion: Daten auslesen -> view funktion: write_data_in_csv

# 3. Nur Produkte einer Kategorie heraussuchen
# 4. Produkte nach Filtern heraussuchen
# 5. DB - Update
# 6. DB - Delete
