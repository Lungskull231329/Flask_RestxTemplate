import hashlib
import uuid

from flask import current_app

from .repo import save_info_file_repo, get_file_list_repo


def get_file_list():
    """

    """
    return get_file_list_repo()



class DataFile:

    def __init__(self, current_request):
        self.current_request = current_request
        if not self.current_request.files['file'].filename:
            raise ValueError
        self.file_size = self.current_request.form['file_size']
        self.mime_type = self.current_request.form['mime_type']
        self.file_name = self.current_request.files['file'].filename
        self.file_alias = str(uuid.uuid4())
        self.md5_hash = None

        q = 1

        self.save_file()


    def get_md5(self):
        """

        """
        with open('app/uploads/04b75cf4-db56-4887-9a1a-161efa19a0a3', 'rb') as f:
            contents = f.read()
            self.md5_hash = hashlib.md5(contents)

    def save_file(self):
        """

        """
        file = self.current_request.files['file']
        file.save(current_app.config.get('UPLOAD_FOLDER'), self.file_alias)
        self.get_md5()

        self.save_info_file(self.file_alias, self.file_size, self.mime_type, self.file_name, self.md5_hash)


    def save_info_file(self, file_alias, file_size, mime_type, file_name, md5_hash):

        result = save_info_file_repo(file_alias, file_size, mime_type, file_name, md5_hash)
