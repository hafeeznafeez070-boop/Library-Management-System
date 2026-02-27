from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, Field
from typing import Optional


class Book:
    id:Optional[int] = None 
    title:str = Field(min_length=3, max_length=25)
    author:str = Field(min_length=3,max_length=20)
    description:str = Field(min_length=2, max_length=100)
    rating:int = Field(gt=0,lt=6),
    publish_date:int = Field(gt=1999,lt=2030)

    def __init__(self,id,title,author,description,rating,publish_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date

BOOKS = [
    Book(1,"CS","Roby","Cs 101 for everyone",4,2026),
    Book(2,"Phy","Newton","nice book in universe",5,2027),
    Book(3,"Chem","Rutherford","Basic industrial chemistry",3,2026),
    Book(4,"Maths","Ibn-e-seena","D1 and D2",3,2023),
    Book(5,"Astro","Evens","Get to know your Sky",5,2022),
    Book(6,"Eng","Roby","learn to read and write",1,2009)
]

class BookRequest(BaseModel):
    id:int
    title:str
    author:str
    description:str
    rating:int
    publish_date:int

    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"CS",
                "author":"Sipn",
                "description":"A basic book on Cs",
                "rating":5,
                "publish_date":2000
            }
        }
    }




app = FastAPI()


@app.get("/")
async def root():
    return {"message":"This is our root router"}

@app.get("/books")
async def showBooks():
    return BOOKS


@app.get("/books/{book_id}")
async def book_by_id(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/")
async def books_by_rating(book_rating:int = Path(gt=0,lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return






@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(book_id(new_book))
    return BOOKS

@app.put("/books/update_book")
async def update_a_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
    return BOOKS
    


@app.delete("/books/{book_id}")
async def delete_a_book(book_id:int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break


@app.get("/books/publish/")
async def get_books_by_publish_date(publish_date:int = Path(gt=1999,lt=2030)):
    books_to_return = []
    for book in BOOKS:
        if book.publish_date == publish_date:
            print(book)
            books_to_return.append(book)
    return books_to_return


def book_id(book:Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    
