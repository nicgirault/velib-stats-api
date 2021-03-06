"""empty message

Revision ID: 40fd49c7dc7
Revises: 2fc2e0a7bdc
Create Date: 2015-07-11 16:39:31.393511

"""

# revision identifiers, used by Alembic.
revision = '40fd49c7dc7'
down_revision = '2fc2e0a7bdc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_station_snapshot_contract_name'), 'station_snapshot', ['contract_name'], unique=False)
    op.create_index(op.f('ix_station_snapshot_last_update'), 'station_snapshot', ['last_update'], unique=False)
    op.create_index(op.f('ix_station_snapshot_number'), 'station_snapshot', ['number'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_station_snapshot_number'), table_name='station_snapshot')
    op.drop_index(op.f('ix_station_snapshot_last_update'), table_name='station_snapshot')
    op.drop_index(op.f('ix_station_snapshot_contract_name'), table_name='station_snapshot')
    ### end Alembic commands ###
