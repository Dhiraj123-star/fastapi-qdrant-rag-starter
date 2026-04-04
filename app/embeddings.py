import asyncio
from openai import AsyncOpenAI
from app.config import OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY,timeout=10.0)

async def get_embedding(text:str):
    for _ in range(3):
        try:

            response = await client.embeddings.create(
                model="text-embedding-3-small",
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            await asyncio.sleep(1)
    raise Exception("OpenAI API failed after retries")