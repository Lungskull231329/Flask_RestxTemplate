import uuid

from app.api.data.schemas import FileOutSchema
from app.models.models import Data
from app.session import session_scope
import random


def save_info_file_repo(file_alias, file_size, mime_type, file_name, md5_hash):

    with session_scope() as session:
        data = Data()

        data.id = str(uuid.uuid4())
        data.size = file_size
        data.expansion = mime_type
        data.md5 = md5_hash
        data.real_name = file_name
        data.alias_name = file_alias
        data.note = ''
        session.add(data)


def get_file_list_repo():
    with session_scope() as session:
        query = session.query(Data)
        query = query.all()
        result = FileOutSchema(many=True).dump(query)
    return result