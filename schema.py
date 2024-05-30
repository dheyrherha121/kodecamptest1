from pydantic import BaseModel

class BookIn(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    genre: str