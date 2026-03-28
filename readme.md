# 🤖 AI Research Agent Pipeline

An intelligent multi-agent AI system built using CrewAI + Gemini + Tavily that performs deep research, critiques it, simplifies it, and delivers a polished beginner-friendly explanation.

---

## 🚀 Overview

This project implements an agentic workflow where multiple AI agents collaborate to:

1. Research a topic using real-time web search  
2. Critically evaluate the research quality  
3. Convert it into a simple explanation  
4. Review and polish the final output  

All powered by Gemini LLM and CrewAI orchestration.

---

## 🧩 Architecture

The system consists of 4 AI agents:

- Researcher → Gathers information using Tavily search  
- Critic → Validates and improves research quality  
- Writer → Simplifies the content for beginners  
- Reviewer → Polishes the final output  

---

## ⚙️ Tech Stack

- CrewAI → Multi-agent orchestration  
- Google Gemini (gemini-2.5-flash) → LLM  
- Tavily API → Real-time web search  
- LangSmith → Tracing and observability  
- Python → Core implementation  

---

## 📁 Project Structure

.
├── main.py
├── .env
├── requirements.txt
└── README.md

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

GEMINI_API_KEY=your_gemini_api_key  
TAVILY_API_KEY=your_tavily_api_key  
LANGCHAIN_API_KEY=your_langsmith_api_key  

---

## 🛠️ Installation

# Clone the repository
git clone https://github.com/your-username/research-agent.git

# Navigate to project
cd research-agent

# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

---

## ▶️ Usage

Run the project:

python main.py

You will be prompted:

Enter topic to research:

Example:

Enter topic to research: Artificial Intelligence

---

## 🔄 Workflow

1. User enters a topic  
2. Researcher uses search_tool (Tavily) to gather data  
3. Critic ensures completeness and correctness  
4. Writer simplifies the explanation  
5. Reviewer refines and delivers final output  

---

## 🧠 Features

- Real-time web search integration  
- Multi-agent collaboration  
- Self-correcting research pipeline  
- Beginner-friendly explanations  
- Observability via LangSmith tracing  

---

## 🔍 Example Output

Artificial Intelligence (AI) is a technology that allows machines to think and learn like humans.

Example:
Virtual assistants like Siri and Alexa use AI.

Benefits:
- Automation
- Efficiency

Challenges:
- Bias
- Job displacement

---

## 📌 Key Components

- Custom Tool (SearchTool) → Uses Tavily API for search  
- Agents → Defined using CrewAI  
- Tasks → Structured pipeline with dependencies  
- Crew Execution → Orchestrates full workflow  

---

## 🧪 Future Improvements

- Add memory to agents  
- Add UI (React / Next.js frontend)  
- Support multiple LLM providers  
- Store research history  
- Add citations and sources formatting  

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests!

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Author

Aryan Mehta  
Building toward becoming a Top 1% Software Engineer 🚀