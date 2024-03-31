from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging


load_dotenv()
API_TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# print(API_TOKEN)

#Connect to OpenAI
openapi_api_key = os.getenv("OPENAI_API_KEY")

#print("OK")

# print(API_TOKEN)

#configure logging
logging.basicConfig(level=logging.INFO)

MODEL_NAME = "gpt-3.5-turbo"

#Initialize bot 
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)