from fastapi import FastAPI
from routes.books_routes import router as books_router

app = FastAPI()

app.include_router(books_router)