from flask import Blueprint

admin = Blueprint('admin', __name__)

from pgscm.admin.views import *  # noqa
from pgscm.admin.user_management.views import *  # noqa
