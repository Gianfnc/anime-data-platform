from pydantic import BaseModel, ConfigDict # <-- Adicione ConfigDict aqui
from typing import Optional

class AnimeSchema(BaseModel):
    id: int
    title: str
    score: Optional[float] = None
    genres: str
    synopsis: Optional[str] = None

    # Este é o novo estilo, mais moderno e limpo
    model_config = ConfigDict(from_attributes=True)