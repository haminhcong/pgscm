from flask import render_template
from . import api
from flask_security import roles_accepted
from flask import jsonify
import datetime
from flask_login import current_user

# @api.route('/vi/chung-chi', endpoint='index_vi')
# @api.route('/', endpoint='index_en')
# @roles_accepted('national_admin', 'national_moderator', 'national_user')
# def index():
#     sample_certificate = Certificate(11, 'certificate smp',
#                                      datetime.date(2015, 8, 23),
#                                      100, "OK", "Group 1")
#     result_certificates = []
#     for i in range(1, 30):
#         result_certificates.append(sample_certificate)
#     return render_template('certificate/index.html',
#                            certificates=result_certificates)


# @api.route('/vi/chung-chi', endpoint='index_vi')
@api.route('/api/user/current_user_roles', endpoint='current_user_roles')
@roles_accepted('national_admin', 'national_moderator', 'national_user')
def current_user_roles():
    user_roles =[]
    for role in current_user.roles:
        user_roles.append(role.name)
    return jsonify(user_roles)
