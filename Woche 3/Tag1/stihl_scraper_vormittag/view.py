from db import Product


def visualize_products(products: list[Product]) -> None:
    print("\nProdukte in der Datenbank:")
    for product in products:
        print(product)
