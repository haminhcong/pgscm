from flask import render_template
from .. import admin
from . import forms
from flask_security import roles_accepted
from pgscm.db.models import User


@admin.route('/vi/quan-tri/nguoi-dung', endpoint='users_vi')
@admin.route('/en/admin/users', endpoint='users_en')
@roles_accepted('national_admin', 'regional_admin')
def users_index():
    create_user_form = forms.CreateUserForm()
    system_users = User.query.all()
    return render_template(
        'admin/user_management/index.html',
        users=system_users,
        create_user_form=create_user_form
    )
