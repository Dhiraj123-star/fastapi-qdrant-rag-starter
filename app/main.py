from fastapi import FastAPI
from app.rag_service import create_collection,add_document,generate_answer

app = FastAPI()

@app.on_event("startup")
def start_up():
    create_collection()

@app.get("/")
def root():
    return {"message":"RAG API running !!"}

@app.post("/add")
def add(text:str):
    add_document(text)
    return {"status":"added"}

@app.get("/ask")
def ask(query:str):
    answer=generate_answer(query)
    return {"answer":answer}