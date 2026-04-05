# 🚀 fastapi-qdrant-rag-starter

A minimal **Retrieval-Augmented Generation (RAG)** backend built with:

* ⚡ FastAPI (Async API layer)
* 🧠 OpenAI Embeddings (semantic understanding)
* 📦 Qdrant (vector database)
* 🤖 OpenAI Responses API (LLM answers)
* ⚡ Redis (caching layer)
* 🐳 Docker + Docker Compose
* 🔁 GitHub Actions CI/CD

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

### 5. 🚦 Rate Limiting (API Protection)

* Implemented using `slowapi`
* Prevents abuse and excessive requests
* Per-endpoint request limits

---

### 6. 📦 Vector Database (Qdrant)

* Lightweight and fast vector store
* Runs via Docker
* Supports cosine similarity search

---

### 7. ✨ OpenAI Integration

* **Embeddings API** → text → vectors
* **Responses API** → generate answers

---

### 8. 🔁 Retry + Resilience

* Retry logic for OpenAI calls
* Handles transient network failures
* Production-friendly design

---

### 9. 🐳 Dockerized Setup

* Containerized FastAPI app
* Docker Compose for:

  * Qdrant
  * Redis

---

### 10. 🔁 CI/CD Pipeline (GitHub Actions)

* Automatic Docker image build
* Push to DockerHub
* Triggered on every push to `main`

---

## 🏗️ Project Structure

```
fastapi-qdrant-rag-starter/
│
├── app/
│   ├── main.py              # FastAPI entrypoint (async + lifespan + rate limit)
│   ├── rag_service.py       # RAG pipeline
│   ├── embeddings.py        # OpenAI embeddings (async + retry)
│   ├── qdrant_client.py     # Qdrant connection
│   ├── cache.py             # Redis caching layer
│   └── config.py            # Config management
│
├── docker-compose.yml       # Qdrant + Redis
├── Dockerfile              # App container
├── .github/workflows/      # CI/CD pipeline
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
✔ Cached in Redis (optional)
✔ Rate limited

---

### ❓ Ask Question

```
GET /ask?query=What is FastAPI?
```

### Flow:

1. Check Redis cache
2. Query → embedding
3. Retrieve relevant docs (Qdrant)
4. Combine context + query
5. LLM generates answer
6. Cache response

---

## 🔄 Architecture Flow

```
User Query
   ↓
Rate Limiter
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
* API protection (rate limiting)
* CI/CD automation
* Clean service separation
* Easy to scale into microservices

---

## 👨‍💻 Author

Built by **Dhiraj** — Backend Engineer focused on:

* FastAPI ⚡
* System Design 🏗️
* GenAI + RAG 🤖

---
