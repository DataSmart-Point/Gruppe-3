from db import Product


def visualize_products(products: list[Product]) -> None:
    print("\nProdukte in der Datenbank:")
    for product in products:
        print(product)


def create_html_template(products: list[Product]) -> str:
    html = []

    for product in products:
        # füge tags zu einem HTML template hinzu
        availability_for_template = (
            "Auf Lager" if product.available else "Nicht auf Lager"
        )
        single_product_html = f"<div><h2>{product.name}</h2><p>{product.price}€</p><p>{product.short_description}</p><p>{availability_for_template}</p></div>"
        html.append(single_product_html)

    html_template = "".join(html)
    return html_template
