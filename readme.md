🧠 MSME Agent System

An Agentic Decision-Making Platform for MSMEs

📌 Overview

The MSME Agent System is an end-to-end agentic AI platform designed to help Micro, Small, and Medium Enterprises (MSMEs) automate operational decisions such as order handling, inventory checks, staff availability, and recovery planning.

Unlike simple chatbots, this system uses multiple specialized AI agents that:

perceive structured and unstructured inputs,

reason deterministically,

act safely on business data,

plan recovery steps when actions fail,

and learn from past outcomes to improve future decisions.

🚀 Key Features

✅ Structured + Free-Text Input Support

🧠 Deterministic Reasoning Agent

📦 Real-time Inventory & Staff Constraints

🧭 Recovery Planning for Failed Actions

🔁 Human-in-the-Loop Retry System

📊 Learning-Driven Confidence Adaptation

🧪 Interactive Web UI (Playground)

🌐 API-first Design (FastAPI)

🧩 Agent Architecture

The system is built using a multi-agent pipeline powered by LangGraph:

User Input
   ↓
Perception Agent
   ↓
Reasoning Agent  ←── Learning Feedback
   ↓
Action Agent
   ↓
Planning Agent
   ↓
Learning Agent

🔹 Agent Responsibilities
Agent	Responsibility
PerceptionAgent	Extracts intent & entities (rules + LLM fallback)
ReasoningAgent	Makes deterministic decisions with confidence
ActionAgent	Executes actions with safety checks
PlanningAgent	Generates recovery plans when actions fail
LearningAgent	Records outcomes & influences future confidence
🧠 Learning-Driven Intelligence

The system continuously learns from outcomes:

Tracks blocked, successful, and skipped actions

Computes failure rates per intent

Dynamically adjusts decision confidence

Influences planning and human-review thresholds

This ensures safer automation over time.

🖥️ Frontend Playground

An interactive UI allows you to:

Test structured forms (safe execution)

Try free-text inputs

View:

intent

decision

confidence bar

reasoning summary

recovery plans

execution logs

Retry blocked actions after reviewing plans

⚙️ Tech Stack

Backend: Python, FastAPI

Agents: LangGraph, LangChain

LLM Provider: Groq (LLama models)

Database: SQLite

Frontend: HTML, Tailwind CSS

Deployment: Render

📂 Project Structure
msme-agent-system/
│
├── agents/          # All AI agents
├── api/             # FastAPI server
├── graph/           # LangGraph workflow & state
├── tools/           # Business logic tools
├── frontend/        # Web UI
├── models/          # LLM configuration
├── config/          # Settings
├── main.py          # Local runner
├── requirements.txt
├── .gitignore
└── README.md

🛠️ Setup Instructions (Local)
1️⃣ Clone the repository
git clone https://github.com/Madhurapingle/FlappyBirds_MSME.git
cd msme-agent-system

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file (do NOT commit it):

GROQ_API_KEY=your_api_key_here

5️⃣ Run the server
uvicorn api.server:app --reload


Open:

API Docs → http://127.0.0.1:8000/docs

UI → http://127.0.0.1:8000

☁️ Deployment (Render)

Start Command

uvicorn api.server:app --host 0.0.0.0 --port 10000


Build Command

pip install -r requirements.txt


Environment Variables

GROQ_API_KEY

🏆 Why This Matters

This project demonstrates:

Explainable AI decision-making

Safe automation with human oversight

Real-world operational constraints

Adaptive intelligence without black-box behavior

It is designed to be practical, scalable, and production-ready.

📌 Future Enhancements

Persistent learning storage

Supplier auto-reorder integration

Multi-branch MSME support

Real-time dashboards

Role-based staff scheduling

👤 Authors

FlappyBirds