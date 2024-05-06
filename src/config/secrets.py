import os
from dotenv import load_dotenv

def load_secrets() -> tuple:
    # Загрузка переменных окружения 
    load_dotenv()  
    
    api_key = os.getenv('BYBIT_API_KEY')
    api_secret = os.getenv('BYBIT_API_SECRET')
    return api_key, api_secret

