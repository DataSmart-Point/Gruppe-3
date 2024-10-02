from db import Product


def visualize_products(products: list[Product]) -> None:
    print("\nProdukte in der Datenbank:")
    for product in products:
        print(product)


def create_html_template(products: list[Product]) -> str:
    html = []

    for product in products:
        # füge tags zu einem HTML template hinzu
        pass
