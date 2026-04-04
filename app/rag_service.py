import uuid
from qdrant_client.models import VectorParams, Distance, PointStruct
from app.qdrant_client import client
from app.embeddings import get_embedding
from app.config import COLLECTION_NAME,OPENAI_API_KEY
from openai import AsyncOpenAI
from app.cache import get_cache, set_cache

openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

def create_collection():
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=1536,
                distance=Distance.COSINE,
            ),
        )
        

async def add_document(text:str):
    vector= await get_embedding(text)

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={"text":text},
            )
        ],
    )

async def search(query: str):
    query_vector = await get_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3,
    )

    return [point.payload["text"] for point in results.points]

async def generate_answer(query:str):
    # check cache first
    cached = get_cache(query)
    if cached:
        return cached
    context=await search(query)

    prompt= f"""
    Answer the question based on context.
    Context: 
    {context}

    Question:
    {query}

    """

    response = await openai_client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    answer=  response.output_text

    # Store in cache
    set_cache(query, answer)
    
    return answer