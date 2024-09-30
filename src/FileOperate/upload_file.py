import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from logger import logger

# specify the root folder of storing file
UPLOAD_FOLDER = 'src/test'
ALLOWED_EXTENSION = {'png', 'jpg', 'jpeg', 'pdf', 'md', 'doc', 'docx'}

class file_uploader:
    
    def __init__(self, files:list[FileStorage], path:str) -> None:
        self.file_list = files 
        self.saved_path = path
        
    def allowed_file(self, file_name:str) -> bool:
        """
        examine if file uploaded have allowed file extension name
        Returns:
            bool: true means all files are valid, false means some files are not valid
        """
        if '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION:
            return True
        else:
            return False
        
    def create_folder_if_not_exists(self):
        if not os.path.exists(path=self.saved_path):
            os.makedirs(self.saved_path)
        
    def save_files_to_folder(self):
        """
        save files uploaded by student to his specific folder
        """
        try:
            for file in self.file_list:
                if file and self.allowed_file(file_name=file.filename):
                    file_name = secure_filename(file.filename)
                    file_path = os.path.join(self.saved_path, file_name)
                    file.save(file_path)
                    logger.info(f'{file.filename} has been save to {file_path}')
                else:
                    logger.warning(f'{file.filename} is not valid and is not saved')
        except Exception as e:
            logger.error(f'in upload_file, error : {e}')
        
    def activate(self):
        self.create_folder_if_not_exists()
        self.save_files_to_folder()
                    