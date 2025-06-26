from flask import Flask
import logging
from app.routes import register_routes
from app.bot import BasicBot
import os
from dotenv import load_dotenv
load_dotenv()
def create_app():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler() # To print the logs to console
        ]
    )
    app = Flask(__name__)
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("SECRET_KEY")
    
    if not api_key or not api_secret:
        raise KeyError("API_KEY or SECRET_KEY is missing in .env")

    bot = BasicBot(api_key, api_secret)
    register_routes(app, bot)
    return app