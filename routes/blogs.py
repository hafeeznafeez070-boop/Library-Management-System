from fastapi import APIRouter

blogs = [
    {"title":"blog-1","blog_content":"content-text-1","card_img":"cardImgURL-1","feature_img":"featureImgURL-1","tags":["tag1","tag2"]},
    {"title":"blog-2","blog_content":"content-text-2","card_img":"cardImgURL-2","feature_img":"featureImgURL-2","tags":["tag1","tag2"]},
    {"title":"blog-3","blog_content":"content-text-3","card_img":"cardImgURL-3","feature_img":"featureImgURL-3W","tags":["tag1","tag2"]}
    ]

router = APIRouter(prefix="/blogs",tags=["Blogs"])

@router.get("/{blog_title}")
async def get_blog_by_title(blog_title:str):
    for blog in blogs:
        if blog.get("title").casefold == blog_title.casefold():
            return blog
    




    
    