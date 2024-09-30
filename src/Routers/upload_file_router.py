import os
import sys
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import request, jsonify
from werkzeug.utils import secure_filename
from FileOperate.upload_file import UPLOAD_FOLDER
from Utilities.data_classes import Submission

from main import app
from logger import logger
from FileOperate.upload_file import file_uploader
from SqlOperation.session_manager import get_session

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER    

@app.route('/upload', methods=['POST'])
def upload_file():
    logger.info('activate upload file router')
    if not request.is_json:
        return jsonify({'error': 'request body must be json'}), 400
    
    data = request.get_json()
    
    try:
        
        received_submission = Submission(
            studentID = data['studentID'],
            assignmentTopic = data['assignmentTopic'],
            commitTime = data['commitTime'],
            status = data['status'],
            commitContent = data['commitConten']
        )
        
        with get_session() as session:
            session.add(received_submission)
            session.commit()
            logger.info('uploaded file has been received at server side')
        
    except KeyError as e:
        logger.error(f'In upload_file_route, missing required field {str(e)}')
        return jsonify({'error': f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        logger.error(f'In upload_file_route, Failed to save submission {str(e)}')
        return jsonify({"error": f"Failed to save submission: {str(e)}"}), 500
    
    
    try:
        files = request.files.getlist('file')
        if len(files) == 0:
            logger.warning('no file content has been uploaded')
            return jsonify({'warning': 'no file content has been uploaded'}), 200
        user_folder = os.path.join(app.config['UPLOAD_FOLDER'], received_submission.studentID)
        upload_file = file_uploader(files=files,path=user_folder)
        upload_file.activate()
        
    except Exception as e:
        logger.error('in unpload_file_router, error:{e}')
        return jsonify({f'error': {e}}), 400