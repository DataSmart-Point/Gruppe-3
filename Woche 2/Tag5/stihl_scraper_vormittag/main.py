import controller
import db

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
