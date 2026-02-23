from fastapi import FastAPI, APIRouter
from routes.blogs import router as blog_route


BOOKS = [
    {"title":"title1","author":"author-1","category":"science"},
    {"title":"title2","author":"author-2","category":"commerce"},
    {"title":"title3","author":"author-3","category":"IT"},
    {"title":"title4","author":"author-4","category":"Arts"},
    {"title":"title5","author":"author-5","category":"science"}
    ]



app = FastAPI()

app.include_router(blog_route)

@app.get("/")
async def root():
    return {"message":"This is our root router"}

@app.get("/books")
async def showBooks():
    return BOOKS

@app.get("/books/{book_title}")
async def book_by_title(book_title:str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
             return book
    
