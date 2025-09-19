from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Anime(Base):
    __tablename__ = "animes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    score = Column(Float)
    genres = Column(String) # Simplificando para uma string de gêneros separados por vírgula
    synopsis = Column(String, nullable=True)