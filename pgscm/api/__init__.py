from flask import Blueprint

api = Blueprint('api', __name__)

from pgscm.api import user_views  # noqa
