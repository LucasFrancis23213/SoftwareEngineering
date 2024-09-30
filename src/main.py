from flask import Flask, request, jsonify
from logger import logger
from sqlalchemy.ext.declarative import declarative_base
from SqlOperation.db_config import config

Base = declarative_base()
Database_URL = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
LOGGER_LOCATION = 'src/logfile.log'

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
