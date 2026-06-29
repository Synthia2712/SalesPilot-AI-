# 🚀 SalesPilot AI

An AI-powered autonomous sales intelligence platform that discovers companies, researches them, qualifies leads, generates personalized outreach, and stores results automatically.

---

# 🌟 Features

- 🤖 Multi-Agent AI Architecture
- 🔍 Company Discovery using Tavily Search
- 🌐 Website Content Extraction
- 🧠 AI Company Research
- 📊 Lead Scoring
- ✉️ Personalized Cold Email Generation
- ⚡ Parallel Processing
- 💾 SQLite Database Storage
- 📁 Excel Export
- 📜 Execution Logging
- 📚 Swagger API Documentation

---

# 🏗️ Architecture

```
                    User
                      │
                      ▼
                FastAPI API
                      │
                      ▼
              Execution Engine
                      │
          ┌───────────┴────────────┐
          ▼                        ▼
      Planner Agent          Tool Registry
                                   │
        ┌──────────────┬───────────────┬──────────────┬──────────────┐
        ▼              ▼               ▼              ▼
 Company Search    Research Agent   Lead Scoring   Outreach Agent
        │
        ▼
 Website Reader
        │
        ▼
     SQLite Database
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| FastAPI | REST API |
| LangChain | LLM Framework |
| LangGraph | Multi-Agent Workflow |
| OpenRouter | LLM Gateway |
| Google Gemini | Reasoning Model |
| Tavily | Web Search |
| BeautifulSoup | Website Parsing |
| Requests | HTTP Requests |
| SQLAlchemy | ORM |
| SQLite | Database |
| Pandas | Excel Export |
| Uvicorn | ASGI Server |

---

# 🤖 AI Agents

## Planner Agent

Converts the user's request into executable tasks.

Example:

```
User

↓

Find AI startups in Bangalore

↓

Tasks

Company Search

Research

Lead Scoring

Outreach
```

---

## Research Agent

Reads company websites and extracts:

- Industry
- Products
- Customers
- Opportunities
- Pain Points
- Business Summary

---

## Lead Scoring Agent

Qualifies each company.

Returns:

- Score
- Recommendation
- Reasons

---

## Outreach Agent

Generates personalized cold emails based on:

- Industry
- Products
- Pain Points
- Opportunities

---

# 📂 Project Structure

```
backend/

│
├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── graph/
│   ├── prompts/
│   ├── schemas/
│   ├── services/
│   ├── tools/
│   ├── main.py
│
├── requirements.txt
├── render.yaml
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SalesPilot-AI.git
```

Go into the project

```bash
cd backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
OPENROUTER_API_KEY=YOUR_KEY

OPENROUTER_MODEL=google/gemini-2.5-pro

TAVILY_API_KEY=YOUR_KEY
```

---

# ▶️ Run

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/planner/plan` | Generate execution plan |
| `/companies/search` | Search companies |
| `/research` | Research company |
| `/scoring` | Score lead |
| `/outreach` | Generate email |
| `/agent/run` | Execute complete AI workflow |
| `/history` | View saved companies |
| `/export` | Export results to Excel |

---

# 🚀 Example Workflow

```
User

↓

Find AI startups in Bangalore

↓

Planner

↓

Company Search

↓

Research

↓

Lead Scoring

↓

Outreach

↓

Database

↓

Excel Export
```

---

# 📈 Future Improvements

- React Dashboard
- JWT Authentication
- PostgreSQL
- Redis Caching
- Docker
- Kubernetes
- CRM Integrations
- LinkedIn Enrichment
- Email Sending
- Background Task Queue
- RAG Knowledge Base
- Multi-LLM Routing

---

# 👩‍💻 Author

**Antriksha Jain**

Built as an end-to-end AI Sales Intelligence Platform demonstrating:

- Multi-Agent Systems
- LLM Orchestration
- AI Workflow Automation
- FastAPI Development
- Prompt Engineering
- Database Integration
- Production API Design
