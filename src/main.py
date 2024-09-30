from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from logger import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from SqlOperation.db_config import config

Base = declarative_base()
Database_URL = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
engine = create_engine(url=Database_URL)
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
