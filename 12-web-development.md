# Web Development

This chapter covers web development in Python, from simple web servers to full-featured frameworks.

---

## HTTP Basics

### Understanding HTTP

```python
# HTTP (HyperText Transfer Protocol) is the foundation of web communication

# HTTP Methods:
# GET     - Retrieve data
# POST    - Submit data
# PUT     - Update data (full replacement)
# PATCH   - Update data (partial)
# DELETE  - Remove data

# HTTP Status Codes:
# 1xx - Informational
# 2xx - Success (200 OK, 201 Created, 204 No Content)
# 3xx - Redirection (301 Moved Permanently, 302 Found)
# 4xx - Client Error (400 Bad Request, 401 Unauthorized, 404 Not Found)
# 5xx - Server Error (500 Internal Server Error)
```

---

## The requests Library

### Making HTTP Requests

```bash
pip install requests
```

```python
import requests

# GET request
response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.headers)      # Response headers
print(response.text)         # Response body as string
print(response.json())       # Response body as JSON

# With parameters
params = {'q': 'python', 'page': 1}
response = requests.get('https://api.github.com/search/repositories', params=params)

# With headers
headers = {'Authorization': 'Bearer token123'}
response = requests.get('https://api.example.com/data', headers=headers)

# POST request
data = {'username': 'john', 'email': 'john@example.com'}
response = requests.post('https://api.example.com/users', json=data)

# Other methods
response = requests.put('https://api.example.com/users/1', json=data)
response = requests.patch('https://api.example.com/users/1', json={'email': 'new@example.com'})
response = requests.delete('https://api.example.com/users/1')
```

### Handling Responses

```python
import requests

response = requests.get('https://api.github.com/users/python')

# Check success
if response.ok:  # status_code < 400
    data = response.json()
    print(f"Name: {data['name']}")
    print(f"Followers: {data['followers']}")

# Raise exception on error
try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"HTTP Error: {e}")

# Timeouts
try:
    response = requests.get('https://api.example.com', timeout=5)
except requests.Timeout:
    print("Request timed out")
except requests.RequestException as e:
    print(f"Request failed: {e}")
```

### Sessions

```python
import requests

# Session maintains cookies and connection pooling
with requests.Session() as session:
    # Login
    session.post('https://example.com/login', data={'user': 'john', 'pass': 'secret'})
    
    # Subsequent requests include cookies
    response = session.get('https://example.com/dashboard')
    
    # Set default headers
    session.headers.update({'Authorization': 'Bearer token'})
```

---

## Flask Basics

### What is Flask?

Flask is a lightweight WSGI web application framework. It's designed to be simple and easy to use.

### Installation

```bash
pip install flask
```

### Hello World

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

```bash
# Run the application
python app.py
# or
flask run
```

### Routes and Methods

```python
from flask import Flask, request

app = Flask(__name__)

# Basic routes
@app.route('/')
def home():
    return '<h1>Home Page</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

# Dynamic routes
@app.route('/user/<username>')
def show_user(username):
    return f'<h1>User: {username}</h1>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'<h1>Post #{post_id}</h1>'

# Multiple HTTP methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f'Welcome, {username}!'
    return '''
        <form method="post">
            <input type="text" name="username">
            <button type="submit">Login</button>
        </form>
    '''
```

### Templates (Jinja2)

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

```html
<!-- templates/hello.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    
    {% if name == 'admin' %}
        <p>Welcome, administrator!</p>
    {% else %}
        <p>Welcome, user!</p>
    {% endif %}
    
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

### Request Data

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def handle_data():
    # JSON data
    json_data = request.json
    
    # Form data
    form_data = request.form
    
    # Query parameters
    query_params = request.args
    page = request.args.get('page', 1, type=int)
    
    # Headers
    auth_header = request.headers.get('Authorization')
    
    # Files
    if 'file' in request.files:
        file = request.files['file']
        file.save(f'uploads/{file.filename}')
    
    return jsonify({'status': 'success'})
```

### JSON API

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database
users = {
    1: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    2: {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
}

# Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

# Get single user
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        abort(404)
    return jsonify(users[user_id])

# Create user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    new_id = max(users.keys()) + 1
    users[new_id] = {'id': new_id, **data}
    return jsonify(users[new_id]), 201

# Update user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        abort(404)
    data = request.json
    users[user_id].update(data)
    return jsonify(users[user_id])

# Delete user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        abort(404)
    del users[user_id]
    return '', 204

# Error handler
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404
```

### Flask Project Structure

```
myapp/
├── app/
│   ├── __init__.py       # App factory
│   ├── routes.py         # Route definitions
│   ├── models.py         # Database models
│   ├── templates/        # HTML templates
│   │   ├── base.html
│   │   └── index.html
│   └── static/           # Static files
│       ├── css/
│       ├── js/
│       └── images/
├── config.py             # Configuration
├── requirements.txt      # Dependencies
└── run.py               # Entry point
```

```python
# app/__init__.py
from flask import Flask

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config_name)
    
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app
```

---

## Django Overview

### What is Django?

Django is a high-level Python web framework that encourages rapid development. It follows the "batteries included" philosophy.

### Installation

```bash
pip install django
```

### Creating a Project

```bash
# Create project
django-admin startproject myproject

# Create app
cd myproject
python manage.py startapp myapp

# Run development server
python manage.py runserver
```

### Project Structure

```
myproject/
├── manage.py              # Command-line utility
├── myproject/
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL configuration
│   ├── asgi.py           # ASGI entry point
│   └── wsgi.py           # WSGI entry point
└── myapp/
    ├── __init__.py
    ├── admin.py           # Admin site config
    ├── apps.py            # App configuration
    ├── migrations/        # Database migrations
    ├── models.py          # Database models
    ├── tests.py           # Tests
    ├── urls.py            # App URL patterns
    └── views.py           # View functions
```

### Views and URLs

```python
# myapp/views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def hello(request, name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")

def template_view(request):
    context = {'title': 'My Page', 'items': ['a', 'b', 'c']}
    return render(request, 'myapp/index.html', context)

def api_view(request):
    data = {'message': 'Hello, API!'}
    return JsonResponse(data)
```

```python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('template/', views.template_view, name='template'),
    path('api/', views.api_view, name='api'),
]
```

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

### Models (Database)

```python
# myapp/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title
```

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate
```

### Templates

```html
<!-- myapp/templates/myapp/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

```html
<!-- myapp/templates/myapp/index.html -->
{% extends 'myapp/base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
    <h1>{{ title }}</h1>
    
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% empty %}
        <li>No items found.</li>
    {% endfor %}
    </ul>
{% endblock %}
```

### Admin Interface

```python
# myapp/admin.py
from django.contrib import admin
from .models import User, Post

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_active']
    search_fields = ['name', 'email']
    list_filter = ['is_active', 'created_at']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_at']
    search_fields = ['title', 'content']
```

```bash
# Create superuser
python manage.py createsuperuser
```

---

## REST APIs with FastAPI

### What is FastAPI?

FastAPI is a modern, fast web framework for building APIs with Python 3.7+. It features automatic OpenAPI documentation and type checking.

### Installation

```bash
pip install fastapi uvicorn
```

### Hello World

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

```bash
# Run the server
uvicorn main:app --reload
```

### Request and Response Models

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

app = FastAPI()

# Request/Response models
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

# In-memory database
users_db = {}
user_counter = 0

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    global user_counter
    user_counter += 1
    user_data = {
        "id": user_counter,
        "name": user.name,
        "email": user.email,
        "created_at": datetime.now()
    }
    users_db[user_counter] = user_data
    return user_data

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.get("/users/", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 10):
    users = list(users_db.values())
    return users[skip : skip + limit]
```

### Path and Query Parameters

```python
from fastapi import FastAPI, Query, Path
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., title="The ID of the item", ge=1),
    q: Optional[str] = Query(None, min_length=3, max_length=50),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {"item_id": item_id, "q": q, "skip": skip, "limit": limit}
```

### Async Endpoints

```python
from fastapi import FastAPI
import asyncio
import httpx

app = FastAPI()

@app.get("/async-data")
async def get_async_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com")
        return response.json()

@app.get("/slow-operation")
async def slow_operation():
    await asyncio.sleep(2)
    return {"message": "Operation completed"}
```

### Middleware and CORS

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

### Dependency Injection

```python
from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

# Dependency function
def get_db():
    db = {"connection": "active"}
    try:
        yield db
    finally:
        db["connection"] = "closed"

# Authentication dependency
async def verify_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")
    token = authorization.split(" ")[1]
    if token != "secret-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/protected")
async def protected_route(token: str = Depends(verify_token)):
    return {"message": "Access granted", "token": token}

@app.get("/data")
def get_data(db: dict = Depends(get_db)):
    return {"db_status": db["connection"]}
```

---

## Web Scraping

### BeautifulSoup

```bash
pip install beautifulsoup4 requests
```

```python
import requests
from bs4 import BeautifulSoup

# Fetch and parse HTML
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements
title = soup.title.string
print(f"Title: {title}")

# Find by tag
all_links = soup.find_all('a')
for link in all_links:
    href = link.get('href')
    text = link.text
    print(f"{text}: {href}")

# Find by class
items = soup.find_all('div', class_='item')

# Find by ID
header = soup.find(id='header')

# CSS selectors
articles = soup.select('article.post h2')
nav_links = soup.select('nav > ul > li > a')

# Extract text
content = soup.get_text(separator=' ', strip=True)
```

### Scrapy (Overview)

```bash
pip install scrapy
```

```python
# myspider.py
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        
        # Follow pagination
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

```bash
# Run spider
scrapy runspider myspider.py -o quotes.json
```

---

## WebSockets

### Flask-SocketIO

```bash
pip install flask-socketio
```

```python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('message', {'data': 'Connected!'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('chat_message')
def handle_message(data):
    print(f'Message: {data}')
    emit('chat_message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
```

### FastAPI WebSockets

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

---

## Summary

| Framework | Type | Best For |
|-----------|------|----------|
| Flask | Micro-framework | Small apps, APIs, learning |
| Django | Full-stack | Large apps, CMS, admin panels |
| FastAPI | API framework | Modern APIs, async, microservices |

### Framework Comparison

| Feature | Flask | Django | FastAPI |
|---------|-------|--------|---------|
| Learning Curve | Low | Medium | Low |
| Performance | Good | Good | Excellent |
| Async Support | Limited | Django 3.1+ | Native |
| Admin Interface | No | Yes | No |
| ORM | No (SQLAlchemy) | Yes | No (SQLAlchemy) |
| Documentation | Good | Excellent | Excellent |
| Auto API Docs | No | No | Yes (OpenAPI) |

### Best Practices

1. **Use virtual environments** - Isolate project dependencies
2. **Structure projects properly** - Separate concerns (routes, models, templates)
3. **Handle errors gracefully** - Provide meaningful error messages
4. **Validate input data** - Never trust user input
5. **Use environment variables** - Keep secrets out of code
6. **Implement logging** - Track errors and debugging info
7. **Write tests** - Ensure code reliability

## Next Steps

Continue to [Testing](13-testing.md) to learn about writing tests for your Python applications.
