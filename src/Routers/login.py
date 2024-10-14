import os
import sys
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import request, jsonify

from logger import logger
from main import app
from Utilities.data_classes import Login
from LoginLogic.login_logic import LoginManager


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({'error': 'request body must be json'}), 400
    
    data = request.get_json()
    
    try:
        login_info = Login(
            userID = data['userID'],
            password = data['password']
        )   
        login_manager = LoginManager(login=login_info)
        login_valid, login_message = login_manager.is_password_valid()
        if not login_valid:
            return jsonify({'warning': f'login information incorrect {login_message}'}), 200
        
        
    except Exception as e:
        logger.error(f'in login.py, error is {str(e)}')
        return jsonify({'error': f'{str(e)}'}), 400
        
