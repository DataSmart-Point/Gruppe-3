import controller
import model

if __name__ == "__main__":
    # 0. Erstmal DB initialisieren
    model.initialize_db()
    # 1. Alle Produktkategorien scrapen
    # controller aufrufen und produktkategorien scrapen
    produkt_categories = controller.scrape_product_categories()

    # 2. Allgemeine Produktdetails zu jedem Produkt scrapen
    # controller aufrufen und alle Produkte scrapen
    controller.scrape_products(produkt_categories)
