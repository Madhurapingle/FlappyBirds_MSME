import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm(
    model: str = "llama-3.3-70b-versatile",
    temperature: float = 0.0,
    max_tokens: int = 256
):
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name=model,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=10
    )
