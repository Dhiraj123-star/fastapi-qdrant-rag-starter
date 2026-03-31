# 🚀 fastapi-qdrant-rag-starter

A minimal **Retrieval-Augmented Generation (RAG)** backend built with:

* ⚡ FastAPI (API layer)
* 🧠 OpenAI Embeddings (semantic understanding)
* 📦 Qdrant (vector database)
* 🤖 OpenAI Responses API (LLM answers)

This project demonstrates how to build a **simple yet powerful semantic search + AI response system**.

---

## 🎯 Core Features

### 1. 🔍 Semantic Search (Vector Search)

* Converts text into embeddings using OpenAI
* Stores vectors in Qdrant
* Retrieves the most relevant documents based on similarity

---

### 2. 🧠 Retrieval-Augmented Generation (RAG)

* Combines:

  * Retrieved context (from Qdrant)
  * User query
* Sends both to the LLM for **context-aware answers**

---

### 3. 📦 Vector Database Integration (Qdrant)

* Lightweight, fast vector storage
* Runs locally via Docker
* Supports cosine similarity search

---

### 4. ✨ OpenAI Integration

* **Embeddings API** → convert text → vectors
* **Responses API** → generate answers from context

---

### 5. ⚡ FastAPI Microservice

* Simple REST endpoints
* Clean architecture (service layer separation)
* Easy to extend into production systems

---

## 🏗️ Project Structure

```
fastapi-qdrant-rag-starter/
│
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── rag_service.py       # Core RAG logic
│   ├── embeddings.py        # OpenAI embeddings
│   ├── qdrant_client.py     # Qdrant connection
│   └── config.py            # Environment config
│
├── docker-compose.yml       # Qdrant setup
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Start Qdrant (Vector DB)

```
docker-compose up -d
```

Qdrant will run on:

```
http://localhost:6333
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=http://localhost:6333
COLLECTION_NAME=documents
```

---

### 4️⃣ Run FastAPI

```
uvicorn app.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

---

## 🧪 API Usage

### ➕ Add Document

```
POST /add?text=FastAPI is a modern web framework
```

👉 Stores text as embedding in Qdrant

---

### ❓ Ask Question

```
GET /ask?query=What is FastAPI?
```

👉 Flow:

1. Convert query → embedding
2. Retrieve relevant documents
3. Send context + query → LLM
4. Return AI-generated answer

---

## 🔄 How It Works

```
User Query
   ↓
Embedding (OpenAI)
   ↓
Vector Search (Qdrant)
   ↓
Relevant Context
   ↓
LLM (Responses API)
   ↓
Final Answer
```

---

## 🚀 Use Cases

* AI-powered search engines
* Knowledge base assistants
* Internal documentation bots
* Chat with your data
* FAQ automation systems

---

## ⚡ Why This Project?

This is a **starter template** designed to:

* Teach core RAG concepts
* Provide clean architecture
* Be easily extendable into production

---

## 🔮 Next Improvements

* Async FastAPI support
* Streaming responses
* Metadata filtering
* Batch ingestion
* Authentication (JWT)
* Redis caching
* Full Dockerization

---

## 👨‍💻 Author

Built by **Dhiraj** — Backend Engineer focused on:

* FastAPI ⚡
* System Design 🏗️
* GenAI + RAG 🤖

---
