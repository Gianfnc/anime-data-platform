from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importando nossos módulos
from app.core.database import get_db
from app.models.anime import Anime
from app.core.schemas import AnimeSchema

router = APIRouter()

@router.get("/animes", response_model=List[AnimeSchema], tags=["Animes"])
def get_all_animes(db: Session = Depends(get_db)):
    """
    Retorna uma lista de todos os animes no banco de dados.
    """
    animes = db.query(Anime).all()
    return animes

@router.get("/animes/{anime_id}", response_model=AnimeSchema, tags=["Animes"])
def get_anime_by_id(anime_id: int, db: Session = Depends(get_db)):
    """
    Retorna os detalhes de um anime específico pelo seu ID.
    """
    anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if anime is None:
        raise HTTPException(status_code=404, detail="Anime não encontrado")
    return anime