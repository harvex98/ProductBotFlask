from entrybot.database.db import Base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    ownerId = Column(Integer, foreign_key=True)
    productName = Column(String(50)) #
    productSource = Column(String(50)) #
    dateBought = Column(Date) #
    priceBought = Column(Float) #


    def __init__(self, ownerId=None, productName=None, dateBought=None, priceBought=None, isSold=None, productSource=None):
        self.productName = productName
        self.dateBought = dateBought
        self.priceBought = priceBought
        self.isSold = isSold
        self.ownerId = ownerId
        self.productSource = productSource


    def __repr__(self):
        return '<Item %r>' % self.productName
