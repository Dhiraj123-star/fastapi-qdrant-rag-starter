from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.rag_service import create_collection,add_document,generate_answer

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic
    create_collection()
    print("✅ Qdrant collection ready!!")

    yield
    # shutdown logic
    print("🛑 Shutting down Qdrant collection...")

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message":"RAG API running !!"}

@app.post("/add")
async def add(text:str):
    await add_document(text)
    return {"status":"added"}

@app.get("/ask")
async def ask(query:str):
    answer = await generate_answer(query)
    return {"answer":answer}