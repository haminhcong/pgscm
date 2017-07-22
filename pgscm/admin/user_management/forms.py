from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import Email, DataRequired, Length, Optional, Regexp, \
    EqualTo
from pgscm.utils import __


class CreateUserForm(FlaskForm):
    user_name = StringField(
        label=__('User Name'),
        validators=[
            DataRequired(),
            Length(5, 64),
            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                   __('Usernames must have only letters, '
                      'numbers, dots or underscores'))
        ]
    )
    email = StringField(
        label=__('Email'),
        validators=[Email(), DataRequired(), Length(1, 64)])
    password = PasswordField(
        label=__('Password of new user'),
        validators=[Length(5, 64), DataRequired()]
    )
    retype_password = PasswordField(
        label=__('Retype Password'),
        validators=[
            DataRequired(),
            EqualTo('password',message=__('Passwords must match.'))
        ]
    )
    role_id = SelectField(
        choices=[('', 'Select role for new user')],
        label=__('User Role'),
        validators=[
            DataRequired(message=__('Please select role for new user.')),
            # Length(64, 64)
        ]
    )
    region_id = SelectField(
        label=__('User Region'),
        choices=[('', __('Select region for new user'))],
        id='region-id',
        validators=[Optional(),]
    )
