"""Index for Employee.job

Revision ID: b90ca5e79443
Revises: 20c0eaf1085d
Create Date: 2021-01-29 23:08:47.577168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b90ca5e79443'
down_revision = '20c0eaf1085d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_employees2_job'), 'employees2', ['job'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employees2_job'), table_name='employees2')
    # ### end Alembic commands ###
