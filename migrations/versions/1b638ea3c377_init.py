"""init

Revision ID: 1b638ea3c377
Revises: ddaaa6474ce1
Create Date: 2022-06-20 14:27:23.137466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b638ea3c377'
down_revision = 'ddaaa6474ce1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eo_DB', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age_31122022', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('age_date_31122022', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('age_31122022_calc_operation_status', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eo_DB', schema=None) as batch_op:
        batch_op.drop_column('age_31122022_calc_operation_status')
        batch_op.drop_column('age_date_31122022')
        batch_op.drop_column('age_31122022')

    # ### end Alembic commands ###
