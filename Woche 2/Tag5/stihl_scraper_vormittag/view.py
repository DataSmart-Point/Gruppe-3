from db import Product


def visualize_products(products: list[Product]) -> None:
    for product in products:
        print(product)
