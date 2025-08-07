from dotenv import load_dotenv
import os 
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from utils.config_loaders import load_config
from langchain_groq import ChatGroq


class ModelLoader:
    """
    A utility class to load embedding models and LLM models.
    """
    
    def __init__(self):
        load_dotenv()
        self._validate_env()
        self.config = load_config()
    
    def _validate_env(self):
        """
        Validate necessary environment variables.
        """
        required_var = ["GOOGLE_API_KEY", "GROQ_API_KEY"]
        # self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        missing_var = [var for var in required_var if not os.getenv(var)]
        if missing_var:
            raise EnvironmentError(f"Missing environment variables: {missing_var}")
        
    
    def load_embeddings(self):
        """
        Load and return the embedding model.
        """
        print("Loading Embedding Model...")
        model_name = self.config["embedding_model"]["model_name"]
        return GoogleGenerativeAIEmbeddings(model=model_name)
    
    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("Loading LLM...")
        # model_name = self.config["llm"]["groq"]["model_name"]
        # llm = ChatGroq(model=model_name, api_key=self.groq_api_key)
        model_name = self.config["llm"]["google"]["model_name"]
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")
        print(llm.invoke("Hi"))
        return llm