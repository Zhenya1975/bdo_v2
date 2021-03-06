"""init

Revision ID: 318183f18738
Revises: 35856df5297b
Create Date: 2022-06-21 08:26:38.053419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '318183f18738'
down_revision = '35856df5297b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eo_calendar_operation_status_DB', schema=None) as batch_op:
        batch_op.add_column(sa.Column('july_2022_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('july_2022_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('july_2022_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('august_2022_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('august_2022_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('august_2022_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('sep_2022_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('sep_2022_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('sep_2022_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('oct_2022_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('oct_2022_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('oct_2022_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('nov_2022_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('nov_2022_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('nov_2022_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('dec_2022_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('dec_2022_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('dec_2022_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2022_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2022_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2022_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2023_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2023_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2023_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2024_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2024_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2024_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2025_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2025_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2025_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2026_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2026_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2026_out', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2027_qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2027_in', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('year_2027_out', sa.Integer(), nullable=True))
        batch_op.drop_column('august_2022')
        batch_op.drop_column('july_2022')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eo_calendar_operation_status_DB', schema=None) as batch_op:
        batch_op.add_column(sa.Column('july_2022', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('august_2022', sa.INTEGER(), nullable=True))
        batch_op.drop_column('year_2027_out')
        batch_op.drop_column('year_2027_in')
        batch_op.drop_column('year_2027_qty')
        batch_op.drop_column('year_2026_out')
        batch_op.drop_column('year_2026_in')
        batch_op.drop_column('year_2026_qty')
        batch_op.drop_column('year_2025_out')
        batch_op.drop_column('year_2025_in')
        batch_op.drop_column('year_2025_qty')
        batch_op.drop_column('year_2024_out')
        batch_op.drop_column('year_2024_in')
        batch_op.drop_column('year_2024_qty')
        batch_op.drop_column('year_2023_out')
        batch_op.drop_column('year_2023_in')
        batch_op.drop_column('year_2023_qty')
        batch_op.drop_column('year_2022_out')
        batch_op.drop_column('year_2022_in')
        batch_op.drop_column('year_2022_qty')
        batch_op.drop_column('dec_2022_out')
        batch_op.drop_column('dec_2022_in')
        batch_op.drop_column('dec_2022_qty')
        batch_op.drop_column('nov_2022_out')
        batch_op.drop_column('nov_2022_in')
        batch_op.drop_column('nov_2022_qty')
        batch_op.drop_column('oct_2022_out')
        batch_op.drop_column('oct_2022_in')
        batch_op.drop_column('oct_2022_qty')
        batch_op.drop_column('sep_2022_out')
        batch_op.drop_column('sep_2022_in')
        batch_op.drop_column('sep_2022_qty')
        batch_op.drop_column('august_2022_out')
        batch_op.drop_column('august_2022_in')
        batch_op.drop_column('august_2022_qty')
        batch_op.drop_column('july_2022_out')
        batch_op.drop_column('july_2022_in')
        batch_op.drop_column('july_2022_qty')

    # ### end Alembic commands ###
