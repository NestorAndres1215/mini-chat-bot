from sqlalchemy import Column, Integer, String, DECIMAL, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String(50))
    monto = Column(DECIMAL(10, 2))
    fecha = Column(Date)