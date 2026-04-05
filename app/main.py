from fastapi import FastAPI,Request
from contextlib import asynccontextmanager
from app.rag_service import create_collection,add_document,generate_answer
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

limiter = Limiter(key_func=get_remote_address)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic
    create_collection()
    print("✅ Qdrant collection ready!!")

    yield
    # shutdown logic
    print("🛑 Shutting down Qdrant collection...")

app = FastAPI(lifespan=lifespan)

# Add middleware
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Custom handler
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request:Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Please try again later."}
    )

@app.get("/")
async def root():
    return {"message":"RAG API running !!"}

@app.post("/add")
@limiter.limit("10/minute")
async def add(request:Request, text:str):
    await add_document(text)
    return {"status":"Document added"}

@app.get("/ask")
@limiter.limit("5/minute")
async def ask(request:Request, query:str):
    answer = await generate_answer(query)
    return {"answer":answer}