from flask import Blueprint, render_template

page = Blueprint('страница', __name__, template_folder='templates', static_folder='static', static_url_path='web')

# @page.route('/', defaults={'path': ''})
# # @page.route('/<path:path>')
# def catch_all(path):
#     return render_template('index.html', base_url=request.base_url)


@page.route('/', methods=['GET'])
# @jwt_required()
def index():
    return render_template('index.html')