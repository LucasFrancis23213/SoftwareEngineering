import os
import sys
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, request, jsonify
from FileOperate.upload_file import file_uploader,UPLOAD_FOLDER
from werkzeug.utils import secure_filename
from Utilities.data_classes import Submission

from logger import logger
import json


from SqlOperation.session_manager import get_session
from main import app


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER    

@app.route('/upload', methods=['POST'])
async def upload_file():
    print("hello i am in")
    logger.info('activate upload file router')

    # 从 request.form 中读取 JSON 数据并解析
    if 'json' not in request.form:
        print("request body must include 'json' field")
        return jsonify({'error': "request body must include 'json' field"}), 400
    

    
    try:
        data = json.loads(request.form['json'])
        received_submission = Submission(
            studentID = data['studentID'],
            assignmentTopic = data['assignmentTopic'],
            commitTime = data['commitTime'],
            status = data['status'],
            commitContent = data['commitContent']
        )

        # 获取到session
        async with get_session() as session:
            session.add(received_submission)
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

        logger.info('File(s) uploaded successfully.')
        return jsonify({'message': 'File(s) uploaded successfully.'}), 200  # 添加成功响应
        
    except Exception as e:
        logger.error('in unpload_file_router, error:{e}')
        return jsonify({f'error': {e}}), 400

if __name__ == "__main__":
    app.run(debug=True)