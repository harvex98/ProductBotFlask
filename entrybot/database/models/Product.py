from entrybot.database.db import Base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    ownerId = Column(Integer, foreign_key=True)
    productName = Column(String(50))
    dateBought = Column(Date)
    priceBought = Column(Float)
    isSold = Column(Boolean)

    def __init__(self, productName=None, dateBought=None, priceBought=None, isSold=None, ownerId=None):
        self.productName = productName
        self.dateBought = dateBought
        self.priceBought = priceBought
        self.isSold = isSold
        self.ownerId = ownerId
    
    def __repr__(self):
        return '<Item %r>' % self.productName
