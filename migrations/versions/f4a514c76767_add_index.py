"""empty message

Revision ID: f4a514c76767
Revises: 56502d362ab5
Create Date: 2017-07-16 16:12:17.155853

"""

# revision identifiers, used by Alembic.
revision = 'f4a514c76767'
down_revision = '56502d362ab5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_fullname'), 'user', ['fullname'], unique=True)
    op.drop_index('ix_users_email', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_email', 'user', ['email'], unique=1)
    op.drop_index(op.f('ix_user_fullname'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    # ### end Alembic commands ###
