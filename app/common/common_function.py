import os
from os.path import isfile, join

from flask import current_app


def get_list_file():
    """

    :return:
    """
    list_file = [{'name_file':
                      f, 'size_file': str(round(os.path.getsize(current_app.config.get('UPLOAD_FOLDER') + '/' + f) / (1024 * 1024), 2))}
                 for f in os.listdir(current_app.config.get('UPLOAD_FOLDER')) if isfile(join(current_app.config.get('UPLOAD_FOLDER'), f))]
    return list_file