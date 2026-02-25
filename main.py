from fastapi import FastAPI, Body
from pydantic import BaseModel


class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1,"CS","Roby","Cs 101 for everyone",4),
    Book(2,"Phy","Newton","nice book in universe",5),
    Book(3,"Chem","Rutherford","Basic industrial chemistry",3),
    Book(4,"Maths","Ibn-e-seena","D1 and D2",3),
    Book(5,"Astro","Evens","Get to know your Sky",5),
    Book(6,"Eng","Roby","learn to read and write",1)
]

class BookRequest(BaseModel):
    id:int
    title:str
    author:str
    description:str
    rating:int




app = FastAPI()


@app.get("/")
async def root():
    return {"message":"This is our root router"}

@app.get("/books")
async def showBooks():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    return BOOKS


