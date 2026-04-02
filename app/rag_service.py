import uuid
from qdrant_client.models import VectorParams, Distance, PointStruct
from app.qdrant_client import client
from app.embeddings import get_embedding
from app.config import COLLECTION_NAME
from openai import OpenAI
from app.config import OPENAI_API_KEY

openai_client = OpenAI(api_key=OPENAI_API_KEY)

def create_collection():
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=1536,
                distance=Distance.COSINE,
            ),
        )
        

def add_document(text:str):
    vector= get_embedding(text)

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

def search(query: str):
    query_vector = get_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3,
    )

    return [point.payload["text"] for point in results.points]

def generate_answer(query:str):
    context=search(query)

    prompt= f"""
    Answer the question based on context.
    Context: 
    {context}

    Question:
    {query}

    """

    response = openai_client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return  response.output_text