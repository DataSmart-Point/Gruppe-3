from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select, text


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    short_description: str
    available: bool


engine = create_engine("sqlite:///./stihl-products.db")


def initialize_db():
    global engine
    SQLModel.metadata.create_all(engine)


def product_exists(session: Session, name: int) -> Product:
    # Wir schauen, ob es bereits einen Eintrag gibt
    query = select(Product).where(Product.name == name)
    result = session.exec(query).first()
    # Wir geben das Ergebnis zurück, damit wir dieses Updaten können, falls es existiert
    return result


def create_products(products: list[Product]):
    global engine
    if not engine:
        raise Exception("No Engine for DB found")

    # engine macht einen CREATE Befehl auf die DB
    with Session(engine) as session:
        for product in products:
            db_product = product_exists(session=session, name=product.name)
            if db_product:
                # Produkt exisitert bereits, ok dann werden wir ein Update durchführen, indem wir einfach die ID des Eintrags in der DB zum neuen Produkt zuweisen
                db_product.name = product.name
                db_product.price = product.price
                db_product.short_description = product.short_description
                db_product.available = product.available
                session.add(db_product)
            else:
                session.add(product)
        session.commit()


def read_data() -> list[Product]:
    global engine
    if not engine:
        raise Exception("No Engine for DB found")

    with Session(engine) as session:
        products = session.exec(select(Product)).all()
        return products
