from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from starlette.responses import JSONResponse
from data_ingestion.ingestion_pipeline import DataIngestion  
from agents.workflow import GraphBuilder  
from models.model import *
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGSMITH_PROJECT")

app = FastAPI(title="Agentic Trading Bot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    try:
        ingestion = DataIngestion()
        ingestion.run_pipeline(files)
        return {"message": "Files successfully processed and stored."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    

@app.post("/query")
async def query_chatbot(request: QuestionRequest):
    try:
        graph_service = GraphBuilder()
        graph_service.build()
        graph = graph_service.get_graph()
        
        # req {"question": "your text"}
        messages={"messages": [request.question]}
        
        result = graph.invoke(messages)
        
       
        if isinstance(result, dict) and "messages" in result:
            final_output = result["messages"][-1].content  # Last AI response
        else:
            final_output = str(result)
        
        return {"answer": final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    

@app.get("/")
def read_root():
    return {"message": "Welcome to the Agentic Trading API"}