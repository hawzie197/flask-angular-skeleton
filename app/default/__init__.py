from flask import Blueprint
import os
static_folder = os.path.join(os.pardir, 'static/dist')
default = Blueprint('cast', __name__, static_folder=static_folder, static_url_path='')
from . import routes
