from fastapi import APIRouter


BOOKS = [
    {"title":"title-1","author":"author-1","category":"science"},
    {"title":"title-2","author":"author-2","category":"commerce"},
    {"title":"title-3","author":"author-3","category":"IT"},
    {"title":"title-4","author":"author-4","category":"Arts"},
    {"title":"title-5","author":"author-5","category":"science"}
    ]


router = APIRouter()

@router.get("/books")
async def showBooks():
    return BOOKS