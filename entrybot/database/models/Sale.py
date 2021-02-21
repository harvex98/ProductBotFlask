from sqlalchemy import Column, Integer, String, Float, Date
from entrybot.database import Base


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    productId = Column(Integer, foreign_key=True)
    salePrice = Column(Float)
    saleDate = Column(Date)
    salePlatform = Column(String(50))

    def __init__(self, productId, salePrice, saleDate, salePlatform):
        self.productId = productId
        self.salePrice = salePrice
        self.saleDate = saleDate
        self.salePlatform = salePlatform
    
    def __repr__(self):
        return '<Sale Id %r>' % (self.id)