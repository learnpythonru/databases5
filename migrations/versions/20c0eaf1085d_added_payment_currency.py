"""Added Payment.currency

Revision ID: 20c0eaf1085d
Revises: 8dd1c069e980
Create Date: 2021-01-27 23:13:51.066504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20c0eaf1085d'
down_revision = '8dd1c069e980'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payments', sa.Column('currency', sa.String(), nullable=True))
    op.execute("UPDATE payments SET currency='RUB'")
    op.alter_column('payments', 'currency', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payments', 'currency')
    # ### end Alembic commands ###