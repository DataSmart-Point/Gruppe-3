from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from mvc import model, view

BASE_URL = "https://www.stihl.de/de/"


def scrape_product_categories() -> list[model.ProductCategory]:
    # 1. request auf die startseite
    full_url = urljoin(BASE_URL, "geraete-werkzeuge")
    response = requests.get(full_url)

    if response.status_code == 200:
        # 2. soup erstellen
        soup = BeautifulSoup(response.text, "html.parser")
        # 3. model aufrufen - extrahiere produkt kategorien
        product_categories = model.extract_product_categories(soup)
        # 4. return produkt kategorien, weitergabe an zweiten schritt: scrape_products
        return product_categories
    else:
        raise Exception("Request failed, URL does not exist!")


def scrape_products(product_categories: list[model.ProductCategory]) -> bool:
    for product_category in product_categories:
        # 1. request auf die dedizierte produktkategorie
        full_url = urljoin(BASE_URL, product_category.path)
        response = requests.get(full_url)

        if response.status_code == 200:
            # 2. soup erstellen
            soup = BeautifulSoup(response.text, "html.parser")
            # 3. model aufrufen - extrahiere produktdetails
            success = model.extract_product_details(soup)
            # 4. return an main: produkte erfolgreich in DB gespeichert
            if success:
                print(
                    "Daten wurden in DB gespeichert for folgende Kategorie:",
                    product_category.category,
                )
        else:
            print("No valid URL found for Product Category:", product_category.category)
            return False


def scrape_new_products():
    # 1. Alle Produktkategorien scrapen
    product_categories = scrape_product_categories()
    # 2. Allgemeine Produktdetails zu jedem Produkt scrapen
    scrape_products(product_categories=product_categories)


def retrieve_data() -> str:
    # 1. Geht ins Model und fragt daten an
    products = model.get_data()
    # 2. In View visualisieren
    html_template = view.create_html_template(products)
    return html_template
