# 🚀 CrewAI Multi-Agent Research System

A **production-ready AI agent system** built using **CrewAI, FastAPI, and Gemini**, capable of performing structured research using multiple collaborating agents.

---

## 🌍 Live Demo

https://crew-ai-agent.onrender.com/docs

---

## 🧠 Overview

This project implements a **multi-agent AI pipeline** where different agents collaborate to:

* Research a topic
* Critically evaluate it
* Simplify it for understanding
* Refine the final output

The system is exposed via a **FastAPI backend** and deployed on **Render**.

---

## ⚙️ Architecture

FastAPI → CrewAI → Agents → Tools → LLM (Gemini)

---

## 🤖 Agents

The system consists of four specialized agents:

* **Researcher** → Gathers detailed information
* **Critic** → Reviews and improves accuracy
* **Writer** → Simplifies the explanation
* **Reviewer** → Polishes final output

---

## 🛠️ Features

* ✅ Multi-agent AI system using CrewAI
* ✅ Tool-augmented reasoning with Tavily Search API
* ✅ Gemini LLM integration
* ✅ FastAPI backend with async endpoints
* ✅ LangSmith tracing support
* ✅ Production deployment on Render
* ✅ Environment-based configuration

---

## 📡 API Endpoint

### POST `/research`

#### Request:

```json
{
  "topic": "Artificial Intelligence"
}
```

#### Response:

```json
{
  "topic": "Artificial Intelligence",
  "result": "Detailed multi-agent generated output..."
}
```

---

## 🧪 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/crew-ai-agent.git
cd crew-ai-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Create `.env` file:

```env
GEMINI_API_KEY=your_key
TAVILY_API_KEY=your_key
LANGCHAIN_API_KEY=your_key
```

---

### 5. Run the server

```bash
uvicorn main:app --reload
```

---

## 🐳 Deployment (Render)

* Python 3.10 runtime
* Build Command:

```bash
pip install -r requirements.txt
```

* Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## 📁 Project Structure

```bash
.
├── main.py          # FastAPI entry point
├── pipeline.py      # CrewAI orchestration
├── agents.py        # Agent definitions
├── tools.py         # External tools (Tavily)
├── requirements.txt
├── runtime.txt
├── .env.example
└── README.md
```

---

## 🧠 Key Learnings

* Multi-agent orchestration using CrewAI
* Tool integration for real-time data
* Managing dependencies in cloud deployments
* Handling Python runtime compatibility issues
* Observability using LangSmith

---

## 🚀 Future Improvements

* Streaming responses
* Frontend (React UI)
* RAG integration (vector DB)
* User authentication
* Persistent memory

---

---

