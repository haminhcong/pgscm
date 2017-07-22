from flask import render_template
from flask_security import roles_accepted
from pgscm.db.models import Region

from . import api
import datetime


# @api.route('/region', endpoint='index_en')
# @roles_accepted('national_admin', 'region_admin')
# def index():
#     sample_certificate = Certificate(11, 'certificate smp',
#                                      datetime.date(2015, 8, 23),
#                                      100, "OK", "Group 1")
#     result_certificates = []
#     for i in range(1, 30):
#         result_certificates.append(sample_certificate)
#     return render_template('certificate/index.html',
#                            certificates=result_certificates)