# 🚀 fastapi-qdrant-rag-starter

A minimal **Retrieval-Augmented Generation (RAG)** backend built with:

* ⚡ FastAPI (Async API layer)
* 🧠 OpenAI Embeddings (semantic understanding)
* 📦 Qdrant (vector database)
* 🤖 OpenAI Responses API (LLM answers)
* ⚡ Redis (caching layer)

This project demonstrates how to build a **simple, scalable, and production-ready semantic search + AI system**.

---

## 🎯 Core Features

### 1. 🔍 Semantic Search (Vector Search)

* Converts text into embeddings using OpenAI
* Stores vectors in Qdrant
* Retrieves most relevant documents using similarity search

---

### 2. 🧠 Retrieval-Augmented Generation (RAG)

* Combines:

  * Retrieved context (Qdrant)
  * User query
* Sends both to LLM → generates **context-aware answers**

---

### 3. ⚡ Fully Async FastAPI

* End-to-end async architecture
* Non-blocking API calls (OpenAI, DB)
* High performance & scalable

---

### 4. ⚡ Redis Caching (Performance Boost)

* Caches embeddings / responses
* Reduces redundant API calls
* Improves latency significantly

---

### 5. 📦 Vector Database (Qdrant)

* Lightweight and fast vector store
* Runs via Docker
* Supports cosine similarity search

---

### 6. ✨ OpenAI Integration

* **Embeddings API** → text → vectors
* **Responses API** → generate answers

---

### 7. 🔁 Retry + Resilience

* Retry logic for OpenAI calls
* Handles transient network failures
* Production-friendly design

---

## 🏗️ Project Structure

```
fastapi-qdrant-rag-starter/
│
├── app/
│   ├── main.py              # FastAPI entrypoint (async + lifespan)
│   ├── rag_service.py       # RAG pipeline
│   ├── embeddings.py        # OpenAI embeddings (async + retry)
│   ├── qdrant_client.py     # Qdrant connection
│   ├── cache.py             # Redis caching layer
│   └── config.py            # Config management
│
├── docker-compose.yml       # Qdrant + Redis setup
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Start Services (Qdrant + Redis)

```bash
docker-compose up -d
```

Services:

```
Qdrant → http://localhost:6333
Redis  → localhost:6379
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment

Create `.env`:

```
OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=http://localhost:6333
COLLECTION_NAME=documents
REDIS_HOST=localhost
REDIS_PORT=6379
```

---

### 4️⃣ Run FastAPI

```bash
uvicorn app.main:app --reload
```

API:

```
http://127.0.0.1:8000
```

---

## 🧪 API Usage

### ➕ Add Document

```
POST /add?text=FastAPI is a modern web framework
```

✔ Converts → embedding
✔ Stores in Qdrant
✔ Optionally cached in Redis

---

### ❓ Ask Question

```
GET /ask?query=What is FastAPI?
```

### Flow:

1. Query → embedding (cached if available)
2. Retrieve relevant docs (Qdrant)
3. Combine context + query
4. LLM generates answer
5. Response cached (optional)

---

## 🔄 Architecture Flow

```
User Query
   ↓
Redis Cache (check)
   ↓
Embedding (OpenAI)
   ↓
Vector Search (Qdrant)
   ↓
Relevant Context
   ↓
LLM (Responses API)
   ↓
Cache Result (Redis)
   ↓
Final Answer
```

---

## 🚀 Use Cases

* AI-powered search engines
* Chat with your data
* Knowledge base assistants
* Internal documentation bots
* FAQ automation

---

## ⚡ Why This Project?

This is a **production-ready starter template**:

* Async-first architecture
* Caching for performance
* Clean service separation
* Easy to scale into microservices

---

## 👨‍💻 Author

Built by **Dhiraj** — Backend Engineer focused on:

* FastAPI ⚡
* System Design 🏗️
* GenAI + RAG 🤖

---
