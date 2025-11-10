from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate
app = FastAPI()

# @app.get("/hello-world")
# def hello_world():
#     return {"message": "Hello world"}
text_posts = {1:{"title":"new post","content":"This is a new post"},
2:{"title":"another post","content":"second post"}}


@app.get("/posts")
def get_all_posts(limit: int =None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")
    return text_posts[id]

@app.post("/posts")
def create_post(post: PostCreate)-> PostCreate:
    new_post = {"title":post.title,"content":post.content}
    text_posts[max(text_posts.keys())+1] = new_post
    return new_post

