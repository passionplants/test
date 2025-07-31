import dotenv
from langchain_groq import ChatGroq

def prepare_llm(llm_model_id ="llama-3.3-70b-versatile", 
                temperature=0, 
                max_tokens=2000):
    # llm model 
    dotenv.load_dotenv()

    # Use llm model from Groq 
    # Get an API here: https://console.groq.com/keys
    llm=ChatGroq(model_name=llm_model_id,
                temperature=temperature,
                max_tokens=max_tokens)
    return llm


