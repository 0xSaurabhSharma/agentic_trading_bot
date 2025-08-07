# 📈 Agentic Trading Bot

A full-stack, AI-powered trading assistant that integrates multiple APIs, LLMs, and real-time data sources to help users make informed market decisions. It features both a FastAPI backend and a Streamlit-based interactive UI.

---

## 🚀 Features

- 🤖 **LLM-Powered Agent Workflows** – Custom agent workflows for reasoning over market conditions.
- 🧠 **RAG (Retrieval-Augmented Generation)** – Combine knowledge from Pinecone, Polygon, and other APIs.
- 📊 **Real-Time Market Data** – Live data fetching from Polygon and Tavily.
- 🗣️ **LLM Integration** – Groq and Google Gemini AI-powered insights and decision support.
- 💻 **FastAPI Backend** – Robust, asynchronous REST API.
- 🌐 **Streamlit Frontend** – Minimal UI to interact with agents and visualize outputs.
- 📦 **Modular Structure** – Clean separation of concerns for ease of development and scaling.
- 🛠️ **Custom Toolkits** – Extendable tools to interact with external systems and perform complex logic.
- ⚠️ **Exception Handling** – Custom exception classes for robust error management.
- 🧪 **Jupyter Notebooks** – For experimentation and prototyping strategies.
- 🔐 **Secure API Keys Handling** – `.env` support for secure credentials.

---


## 🗂️ Project Structure

```txt
.
├── main.py                 # FastAPI app entrypoint
├── frontend.py             # Streamlit UI entrypoint
├── .env                    # Environment variables
├── config/                 # YAML-based configuration
├── agents/                 # Agent workflows and logic
├── data_ingestion/         # Data fetching and ingestion pipeline
├── exception/              # Custom error classes
├── logger/                 # Logging utilities
├── models/                 # Pydantic/BaseModel definitions
├── notebooks/              # Jupyter notebooks for experimentation
├── prompt_lib/             # Prompt templates for LLMs
├── static/                 # CSS styles for frontend
├── template/               # Jinja2 HTML templates
├── toolkit/                # Utility tools used by agents
├── utils/                  # Config & model loading helpers
├── fallback_data/          # Backup data if APIs fail
└── requirements.txt        # Python dependencies
````

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/agentic-trading-bot.git
cd agentic-trading-bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or using Pipenv:

```bash
pipenv install
```

### 4. Configure Environment

Create a `.env` file with the following:

```env
GOOGLE_API_KEY=your_key
GROQ_API_KEY=your_key
POLYGON_API_KEY=your_key
TAVILY_API_KEY=your_key
PINECONE_API_KEY=your_key
```

---

## 🏁 Running the App

### 🔧 Start FastAPI Backend

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 🎛️ Launch Streamlit UI

```bash
streamlit run frontend.py
```

---

## 📓 Notebooks

Check the `notebooks/` directory for experiment logs, debugging, and rapid iteration.

---

## 📬 API Docs

Once the FastAPI app is running, visit:

* Swagger: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`

---

## 📌 To-Do / Ideas

* [ ] Add authentication for Streamlit and FastAPI
* [ ] Backtest trading logic with historical data
* [ ] Deploy on cloud (GCP, AWS, or Railway)
* [ ] Containerize with Docker
* [ ] Schedule background agents using `APScheduler` or `Celery`
