"""evaluated finish date

Revision ID: 3972d87653e3
Revises: c6028657badb
Create Date: 2022-06-17 12:41:55.618543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3972d87653e3'
down_revision = 'c6028657badb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eo_DB', schema=None) as batch_op:
        batch_op.add_column(sa.Column('evaluated_operation_finish_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eo_DB', schema=None) as batch_op:
        batch_op.drop_column('evaluated_operation_finish_date')

    # ### end Alembic commands ###