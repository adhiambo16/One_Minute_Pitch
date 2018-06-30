"""Changing category database from string to integer

Revision ID: c0bb201f0566
Revises: eb88052e9657
Create Date: 2018-05-20 18:41:22.100214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0bb201f0566'
down_revision = 'eb88052e9657'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_pitches_pitch_category'), 'pitches', ['pitch_category'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pitches_pitch_category'), table_name='pitches')
    # ### end Alembic commands ###