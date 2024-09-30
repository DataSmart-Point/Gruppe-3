from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    short_description: str
    available: bool


engine = None


def initialize_db():
    global engine
    engine = create_engine("sqlite:///./stihl-products.db")
    SQLModel.metadata.create_all(engine)


def create_products(products: list[Product]):
    global engine
    if not engine:
        raise Exception("No Engine for DB found")
    # engine macht einen CREATE Befehl auf die DB

    with Session(engine) as session:
        for product in products:
            session.add(product)
        session.commit()
