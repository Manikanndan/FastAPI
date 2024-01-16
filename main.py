from fastapi import FastAPI # import statement 
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  # creating instance of app

@app.get('/')
def index():
    return {'data': "Hello World!"}

# query parameter
# http://localhost:8000/blog?limit=50&published=false
@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data' : f'{limit} published blogs from the db'}
    else:
        return {'data' : f'{limit} blogs from the db'}

@app.get('/about')
def about():
    return {'data': 'About page'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : "all unpublished blogs"}

# path parameters
@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data' : id}


@app.get('/blogs/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data' : {'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data' : f"Blog is created with title as {blog.title} and body as {blog.body}"}