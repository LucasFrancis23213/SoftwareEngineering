from flask import Flask, request, jsonify
from sqlalchemy.ext.declarative import declarative_base
from SqlOperation.db_config import config
from flask_cors import CORS  # 导入 CORS

import os
import sys
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


Base = declarative_base()
Database_URL = f"mysql+aiomysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
LOGGER_LOCATION = 'logfile.log'



app = Flask(__name__)
CORS(app)  # 启用全域 CORS，允许所有来源


if __name__ == "__main__":
    app.run(debug=True)
