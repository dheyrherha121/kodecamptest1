from fastapi import FastAPI, HTTPException,status
from schema import BookIn

app = FastAPI()

fake_db = []

@app.get('/')
def index():
    return {'welcome to this page'}

@app.post('/', status_code=status.HTTP_200_OK)
def create_book(book:BookIn):
    new_book = fake_db.append(book)
    return {'your book has been added successfully'}

@app.get('/{id}', status_code=status.HTTP_200_OK)
def get_book_by_id(id:int):
    check = fake_db
    if id== check:
        return fake_db.dict()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='the book you want to get does not exist')
    

@app.put('/{id}', status_code=status.HTTP_200_OK)
def update(id:int, book:BookIn):
    check = fake_db[0]
    if id== check:
        check.update(book.dict(), synchronize_session=False)
        return {'successful'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='the book you want to get does not exist')
@app.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_book(id:int):
    check = fake_db[0]
    if id == check:
        check.delete( synchronize_session=False)
        return {'successful'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='the book you want to get does not exist')
