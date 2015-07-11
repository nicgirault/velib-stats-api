"""add stationSnapshot table

Revision ID: a969324903
Revises: 142855bf6fe
Create Date: 2015-07-11 13:22:26.406414

"""

# revision identifiers, used by Alembic.
revision = 'a969324903'
down_revision = '142855bf6fe'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('station_snapshot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('contract_name', sa.String(length=120), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('bike_stands', sa.Integer(), nullable=False),
    sa.Column('available_bike_stands', sa.Integer(), nullable=False),
    sa.Column('available_bikes', sa.Integer(), nullable=False),
    sa.Column('last_update', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('auth_user')


def downgrade():
    op.create_table('auth_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_pkey')
    )
    op.drop_table('station_snapshot')
